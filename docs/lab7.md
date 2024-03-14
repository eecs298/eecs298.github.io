---
layout: spec
title: Lab 7
sitemapOrder: 20
header-includes: |
    \usepackage{amsmath}
---

Lab 7
==========================
{: .primer-spec-toc-ignore }


## Task
In this lab, you will explore (part of) the COMPAS dataset and get experience building a simple machine learning model using the package scikit-learn. This lab will walk you through the four stages of the machine learning pipeline discussed in lecture (Data, Representation, Loss, Optimization) and you will compute some probabilities with the model we create.

To get started, first download the simplified COMPAS dataset using `wget` and then create a file called `lab7.py` in the same folder as the downloaded dataset.
```terminal
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/compas-data-lab-7.csv
```
### Data - COMPAS Dataset (Simplified)
The original COMPAS dataset contains many features including demographic features, criminal history, and information about the current charge of defendants. In this lab, you will use a simplified version of this dataset contained in `compas-data-lab-7.csv` so that we can follow along part of the critical analysis [ProPublica did with this dataset](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing). We saw partially how Northpointe created their tool in lecture, so this lab shows another way to choose features on a dataset to perform an analysis. 

Following ProPublica's analysis, the `features` we consider and their corresponding numeric values are: 
* `sex`: Male: 0, Female: 1
* `age`: `age` < 25: 0, 25<= `age`<= 45: 1, `age` >45: 2 
* `race`: Caucasian: 0, African-American: 1, Asian: 2, Hispanic: 3, Native American 4, Other: 5
* `priors_count`: Number of prior offences to current charge. 
* `c_charge_degree`: Degree of current charge. Misdemeanor: 0, Felony: 1
* `two_year_recid`: Indicator variable for whether the defendent re-offended two years after current charge. No: 0, Yes: 1

Again, following ProPublica's analysis, the `target variable` we are trying to predict and its corresponding numeric values is:
* `score_text`: Whether the defendent was classified as Low or High/Medium risk with Northpointe's tool. Low: 0, High/Medium: 1

The `features` and `target variable` are coded as numeric values because the model we are using needs numeric values to make predictions (see below).

### Representation - Logistic Regression Model
The model we are using, following ProPublica's analysis, we are going to be using a Logistic Regression model to fit the data. A logistic regression model uses the given `features` to predict the binary `target variable` by fitting a logistic curve to the data (see lab slides). Thus, for a given set of inputs (a vector of `features`), the logisitic regression model outputs a score in `[0,1]` which represents the probability of target variable being equal to `1` (thus an output of `0` implies the `target variable` is `0` with probability `1`).

In our setting, we have a dataset of defendants with associated `features` and a `target variable` (describe above) that we will use to train the logisitic regression model to determine how inputs (`features`) are matched to an output (probability of `target variable` being 1).

Formally, if $$X$$ is a vector of input `features` (i.e., one defendant), then the logistic regression model learns parameters for the probability function $$p(X) =\frac{1}{1+e^(-\beta_0+\beta_1 X)}$$ where $$\beta_0$$ is the `intercept` of the model and $`\beta_1`$ is the `rate parameter`. Therefore, the `prediction`, $$\hat{Y}$$, for an input $$X$$ is given as $$\hat{Y} =  1$$ if $$p(X) \ge 0.5$$ and $$\hat{Y} =0$$ if $$p(X) <0.5$$. See [here](https://en.wikipedia.org/wiki/Logistic_regression) for more details on the logistic regression model. 

### Loss - Fitting the Logistic Curve
The loss function associated with the logisitic regression model is called `cross entropy loss` and you can read more about the details [here](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression). However, for the purposes of this lab assignment, you only need to know that minimizing this loss function suffices to find parameters $\beta_0, \beta_1$ that best fit the logistic regression model given in the previous section.

### Optimization - Training the Logistic Regression Model
Now that we have introduced the model and loss function we will use, we can begin coding the training process. To get started, import `numpy` and `sklearn`. If you need to install `sklearn`, run `pip install scikit-learn` in your terminal. Set the random seed here as well to ensure stability of training results.
```python
import numpy as np
from sklearn import linear_model, model_selection, metrics

np.random.seed(298298) # sets the random seed for stability of outputs
```

Next, read in the data from `compas-data-lab-7.csv`however you'd like, but make sure to create a list of `features` called `compas_features` and a list of `target variable` labels called `compas_labels`. That is,`compas_features` is a `list` of `lists` of `features`(all but the last column in the dataset) of each defendant  and `compas_labels` is a `list` of `target variables` (the last column in the dataset). Make sure to cast the values to `int`s as you read them in and populate the lists.

For example, looking at the first couple rows of `compas-data-lab-7.csv`, you want each variable to look as follows
```console
compas_features = [[0,2,5,0,1,0], [0,1,1,0,1,1],[0,0,1,4,1,1], ...]
compas_labels = [0,0,0, ...]
```

Next, it is common practice to split the available data into separate sets for training and testing the model. The primary reason for doing this is to evaluate the performance of the model on unseen data. When we train a machine learning model, we use a portion of the available data to fit the model to the underlying patterns in the data. The goal is to find a model that can accurately predict the target variable for new, unseen data. However, if we use all of the available data for training, we have no way of knowing how well the model will generalize to new data. By splitting the data into training and testing sets, we can use the training data to fit the model and the testing data to evaluate its performance.

You can use the following scikit-learn function to arbitrarily split the data into train and test sets:
```python
x_train, x_test, y_train, y_test = model_selection.train_test_split(compas_features, compas_labels)
```

When training our logistic regression model, we will let the model learn the target values (`y_train`) from the defendants in the training set (`x_train`). Then, once trained, we will give it the defendants in the test set (`x_test`) and ask it to predict the `score_text` for each.

We can use scikit-learn to train a logisitic regression model in the following way 
```python
logistic_regression_model = linear_model.LogisticRegression().fit(x_train, y_train)
```

After that, we can use the trained model to make predictions on the test data.
```python
y_test_pred = logistic_regression_model.predict(x_test)
```

### Evaluating the Model
We are going to use **accuracy** and **true positive rate** to evaluate our model and gain practice in computing probabilities from model outputs. We will use the **test set** to evaluate our model and specifically calculate *empirical* probabilities in this section.

#### Accuracy
Let $Y$ be a random variable for the actual risk score for each defendant in `x_test` (i.e., `y_test`) and let $\hat{Y}$ be a random variable for the predicted score for each defendent in `x_test` (i.e., `y_test_pred`). Further, let $n$ be the number of examples in `x_test`. Then, the **accuracy** of the model is defined as $\sum^n_{i=1} \mathbb{I}[Y_i = \hat{Y}_i]$ where $\mathbb{I}$ is the indicator function and $Y_i, \hat{Y}_i$ are the risk score and predicted risk score for the $i$th defendant, respectively. To get practice using functions in `sklearn`, we will use the function `metrics.accuracy_score(y_test, y_test_pred)` to get the accuracy of our model.

Compute the **accuracy** of the model and print out the result as follows
```console
Accuracy of model: 0.7524303305249513
```

#### True Positive Rate
The `positive` outcome of a machine learning model can be interpreted in many ways, but we will say that the `positive` outcome corresponds to `score_text` label of `1`. Using this definition, the true positive rate of a model is the probability that $\hat{Y}=1$ given that $Y = 1$. This is a conditional probability which we would write as $P(\hat{Y} = 1 | Y=1)$. 

For this section, you will compute the true positive rate *for each race* so that we can compare the rates among the different groups. Let $A$ be a random variable to represent the race of each defendant. Then, will compute $P(\hat{Y} = 1 | Y=1, A=a)$ for $a \in \{0,1,2,3,4,5\}$ (since there are 6 possible race categories -- see Data section). Print out the results of your calculation. Thus, your output (combined with the accuracy calculation) should look as follows
```console
Accuracy of model: 0.7524303305249513
Race Category: 0, TPR: 0.6144578313253012
Race Category: 1, TPR: 0.7244444444444444
Race Category: 2, TPR: 0.6
Race Category: 3, TPR: 0.6521739130434783
Race Category: 4, TPR: 0.0
Race Category: 5, TPR: 0.42105263157894735
```

Turn in `lab7.py` to Gradescope when you're done.



