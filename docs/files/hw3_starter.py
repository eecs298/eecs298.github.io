import itertools
import numpy as np
from typing import Optional

import matplotlib.pyplot as plt


class DataWrapper:
    """
    A wrapper that contains all of the data that we need, including the census tracts, the demographic data for each tract, and the arrest data for each tract.
    All attributes should be constructed in the initializer.

    Inputs:
    arrests_path: The file location of the arrest data.
    demo_path: The file location of the demographic data.
    training_percentage: The percentage of days, starting with the first day in the arrest data and ending with the last day, that will be used for training a predictive model.

    Attributes:
    rng: The source of randomness generate_counterfactual uses.  DO NOT change this, as it will allow for easier debugging and make consistent grading possible.
    arrests_path: The file location of the arrest data.
    demo_path: The file location of the demographic data.
    training_percentage: The percentage of days, starting with the first day in the arrest data and ending with the last day, that will be used for training a predictive model.
    tracts:  The list of tracts in the arrest data.  Each tract should be stored as a string.  Construct this with build_tracts().
    demographics: Stores the demographic data for each tract.  Construct this with process_demo_data().
    num_days:  Total number of days in the arrest data (including the first and last day).
    timestamps: Stores the timestamps of all arrests in the arrest data.  Timestamps represent the number of days since the first arrest, stored as integers, 
        with 0 as the day of the first arrest.  Construct this with process_arrests().

    """
    def __init__(self, arrests_path: str, demo_path: str, training_percentage:float = 2/3):
        #Do not modify this line
        self.rng = np.random.default_rng(seed=0)

    def generate_counterfactual(self, tract_choices: list, t: int):
        """
        Generates arrests at a given time if the police have a heightened presence in the tracts tract_choices at timestamp t.
        This uses real data, but the arrests outputted are synthetic, because in reality the police did not necessarily have a heightened presence in those tracts.
        Do not modify this function.

        Returns:
        Outputs a dictionary, whose keys are the tracts in tract_choices, and the values are the number of arrests made in that tract at time t 
        if there would be heightened police presence there.
        Note the outputs are not deterministic.
        """
        num_crimes = {}
        for tract in tract_choices:
            prior_expected_crimes = len(self.timestamps[tract])/self.num_days
            t_count = self.timestamps[tract].count(t)
            extra = self.rng.poisson(prior_expected_crimes*2)
            num_crimes[tract] = t_count + extra
        return num_crimes

    def build_tracts(self):
        """
        Constructs self.tracts.
        
        Returns:
        A list of all tracts in the arrest data.  Each tract should be a string, and no tract in the output should be repeated.
        """
        pass

    def process_demo_data(self):
        """
        Constructs self.demographics, which stores the number of people in each demographic category in each tract.

        Returns:
        A dict, or dictionary-like object.  You must return an object demographics where either
        demographics[tract][category] or demographics.loc[tract, category] returns the number of people in that category in that tract (this flexibility allows you to use Pandas' DataFrame 
        or other formats as well), for all categories, stored as strings, in the list ["Total population", "Hispanic or Latino", "White", "Black or African American", "Asian"].
        """
        pass

    def process_arrests(self):
        """
        Constructs self.timestamps.

        Returns:
        A dictionary, whose keys are tracts from self.tracts, and values are the list of timestamps of arrests made in that tract.  Timestamps must be represented as the number of days since the 
        first arrest, stored as integers, with 0 as the day of the first arrest.  Each list of timestamps must be sorted from earliest timestamp to latest.
        Note there may be more than one arrest in a tract on a given day.
        """
        pass
    
    def split_timestamps(self):
        """
        Split self.timestamps into training data and testing data.

        Returns:
        A tuple, the training data and then the testing data.  Both the training data and the testing data should be in the same format
        as self.timestamps.  The training data should consist of only timestamps in the first self.training_percentage of days in self.timesteps,
        and the testing data should countain the rest of the timestamps.  (I.e. if the training data should consist of the first 2/3 of 6 total days, timestamp 3 should
        be the last timestamp included in the training data, and it would remain the last timestamp if there were 7 total days instead.)

        """
        pass


class PredPol:
    """
    Represents the PredPol model (you will not need to modify anything in this class).  Uses data from a DataWrapper to
    train and make predictions.  Use its function predict() to make predictions with it.

    Inputs:
    datawrapper:  The DataWrapper that stores the data it will use.
    max_EM_steps: The number of epochs it uses to train.  You should use the default value to conduct analysis, but you can
        change this number for help in speeding up debugging.
    train:  If this Boolean flag is set, will automatically train during initialization.   Otherwise, train_model() will train the model.

    Attributes:
    datawrapper:  The DataWrapper that stores the data it will use.
    theta, omega, mu: The parameters that define the model.
    max_EM_steps:  The number of epochs it uses to train.  Decreasing this number will speed up training.
    train_timestamps:  The timestamps it uses to train the model, which is constructed from self.datawrapper.split_timestamps().
    """
    def __init__(self, datawrapper: DataWrapper, max_EM_steps: int = 20, train:bool = True):
        self.datawrapper = datawrapper

        self.theta, self.omega = None, None
        self.mu = None

        self.max_EM_steps = max_EM_steps

        training_ts, _ = self.datawrapper.split_timestamps()
        self.train_timestamps = training_ts

        assert all([len(l)>0 for l in self.train_timestamps.values()]), "There's a tract with no crime"


        if train:
            self.train_model()

    def train_model(self):
        """
        Trains the model and sets the class attributes self.theta, self.omega, and self.mu using an expectation maximization (EM) algorithm.
        """
        tracts = self.datawrapper.tracts
        train_length = int(self.datawrapper.num_days*self.datawrapper.training_percentage)
        num_timestamps = len(list(itertools.chain(*self.train_timestamps.values())))

        #EM algorithm
        #initializing guesses for all parameters, assumes that few of the events are aftershocks
        mu0 = {tract:len(self.train_timestamps[tract])/(train_length) for tract in tracts}
        theta0, omega0 = 0.1, 0.1
        def forward0(tract, t):
            kernels = [omega0*np.exp(-omega0*(t-t_n)) for t_n in self.train_timestamps[tract] if t_n < t]
            return mu0[tract] + theta0*sum(kernels)

        for i in range(self.max_EM_steps):
            #E-step
            predictions = {tract:{t:forward0(tract,t) for t in set(self.train_timestamps[tract])} for tract in tracts}
            #pj_n[n] is a list of p^j_n, the probability that the jth timestamp for tract n is not an aftershock
            pj_n = {tract: [mu0[tract]/predictions[tract][t] for t in ts] for tract, ts in self.train_timestamps.items()}

            #pij_n[n] is a list of p^{i,j}_n, the probability that the jth timestamp is an aftershock of the ith timestamp in tract n
            pij_n = []
            for tract in tracts:
                ts = self.train_timestamps[tract]
                pij = []
                for t1, t2 in itertools.combinations(ts,2):
                    #Note: if two time stamps happen at the same time, their prob. of causing each other is 0
                    if t2 > t1:
                        pij.append(theta0*omega0*np.exp(-omega0*(t2-t1))/predictions[tract][t2])
                    else:
                        pij.append(0)
                pij_n.append(pij)

            #M-step
            for tract in tracts:
                mu0[tract] = sum(pj_n[tract])/train_length

            total_aftershock_prob = sum(itertools.chain(*pij_n))
            theta0 = total_aftershock_prob/num_timestamps

            accum_weighted_aftershock_prob = 0
            for idx,tract in enumerate(tracts):
                ts = sorted(list(set(self.train_timestamps[tract])))
                accum_weighted_aftershock_prob += sum([pij_n[idx][i]*(t2-t1) for i,(t1, t2) in enumerate(itertools.combinations(ts,2))])
                
            omega0 = total_aftershock_prob/accum_weighted_aftershock_prob
            avg_mu0 = sum(mu0.values())/len(mu0.values())
            print(f'Epoch {i+1}/{self.max_EM_steps}, Parameter values-- Average mu: {avg_mu0:.6f}, Theta: {theta0:.6f}, Omega: {omega0:.6f}')

        #Update final parameters of the model
        self.mu, self.theta, self.omega = mu0, theta0, omega0
        

    def predict(self, tract:str, t:int, timestamps:Optional[dict] = None):
        """
        Given a trained model, predicts the expected number of arrests at a given tract and timestep t.
        This prediction takes as input a collection of timestamps, the timestamps of all events prior to t.
        The default is to use the training timestamps, otherwise it needs to be inputted (this flexibility
        allows us to investigate counterfactuals).

        Output: The expected number of arrests at time t at the given tract, as a float.
        """
        if timestamps == None:
            timestamps = self.train_timestamps
        kernels = [self.omega*np.exp(-self.omega*(t-t_n)) for t_n in timestamps[tract] if t_n < t]
        return self.mu[tract] + self.theta*sum(kernels)


def q1(dw:DataWrapper):
    """
    The proportion of each of the four racial categories.

    Output: A dict whose keys are the racial categories, as strings specified in the instructions, and whose values are the proportions, as floats.
    """
    pass

def q2(dw:DataWrapper):
    """
    The probability that a person in each of the racial categories uses illicit drug, i.e. P[Y=1|A].

    Output: A dict whose keys are the racial categories and whose values are the probabilities, as floats.
    """
    pass

def q3(dw:DataWrapper):
    """
    The expected number of times a person of each racial category was arrested.

    Outputs: A dict whose keys are the racial categories and the values are the expected number of times people in that category were arrested, as floats.
    """
    pass

def q5(dw:DataWrapper):
    """
    The probability that a person of each racial category will ever face a heightened police presence in their tract, i.e. P[P=1|A],
    when running PredPol on the test data.

    Outputs: A dict whose keys are the racial categories and the values are the above probabilities, as floats.
    """
    pass


def q7(dw:DataWrapper):
    """
    The probability that a person of each racial category will ever face a heightened police presence in their tract, i.e. P[P=1|A],
    when running PredPol on the counterfactual test data (see instructions for details).

    Outputs: A dict whose keys are the racial categories and the values are the above probabilities, as floats.
    """
    pass