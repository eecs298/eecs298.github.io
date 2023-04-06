---
layout: spec
title: EECS 298 Homework 3
subtitle: Due 11:59 PM EST on April 24.
sitemapOrder: 20
latex: true
---
Homework 3: To Predict and Serve
==========================
Due 11:59 PM EST on April 24.

## Submission
This homework will consist of a programming task and written responses. You will submit your work via Gradescope (linked from Canvas). On Gradescope, there are two assignments you will need to use to submit. Upload your written responses as a `.pdf` file to the `Homework 3: Written Responses` Gradescope assignment. It is required that you typeset your written responses in a document editor or a program like LaTeX.  Make sure to specify the location of each answer to each question.  In addition, upload your code as `hw3.py` to the `Homework 3: Code Submission` Gradescope assignment. The code that you upload to Gradescope will be graded using an autograder.  There will not be public test cases for this assignment.

Your code will be tested on private datasets in addition to the datasets you are given, and as such, your code should be properly generalizable to other, similar data. Your programming implementation will be graded on correctness as well as efficiency.  We encourage collaboration, but all work you submit must be your own.  All writing must be your own, and collaboration must not result in code or writing that is identifiably similar to other solutions.

## Introduction to Predictive Policing
Predictive policing refers to the use of data analysis and machine learning techniques to identify patterns and make predictions about future criminal activity. Typical stated goals of predictive policing include allocating police resources more effectively and efficiently, reducing crime rates, and improving public safety.  Predictive policing has seen increasingly widespread use in the US [[1]](#1) [[2]](#2).  Perhaps the predictive policing algorithm that has recieved the most media coverage is an algorithm called PredPol, developed by a private company (formerly called PredPol, now called Geolitica), claiming to help "to help protect one out of every 30 people in the United States" [[3]](#3).

PredPol is software developed by social scientists in collaboration with the Los Angeles Police Department (LAPD). It uses historical crime data to predict the probability of future crimes occurring in specific areas using a machine learning model based on earthquake prediction called Epidemic Type Aftershock-Sequences (ETAS) [[4]](#4). The algorithm divides a city into grid cells as small as 500x500 feet and assigns a risk score to each cell, indicating the risk of crime in that cell. The idea is to then use this information to increase the presence of officers to those cells that have the highest risk of crime. However, critics argue that flawed and systemically biased data that results in racially discriminatory predictions and policing, where the use of such algorithms can help produce the very same flawed data that then gets fed back into these systems.  This leads to a predictive policing system that reinforces patterns of over-policing, creating feedback loops that create a cycle of oppression [[2]](#2) [[5]](#5) [[6]](#6).

In this assignment, we will investigate these claims by using real arrest data from the city of Oakland, California from 2009 to 2011.  For cells, we will use census tracts, units of area that the US Census uses to collect population totals.  These are convenient to use because it breaks up the city of Oakland into reasonably sized pieces, and the US Census conveniently collects lots of demographic data on the people who live in each tract.  Using this data, we will investigate the racial distribution of the people arrested in this data and and the people who could be affected by the use of the PredPol algorithm on this data.  We will also investigate what happens when assigning additional police to a tract results in additional arrests, which then get fed back into the model.  We will loosely be following the original analysis of Lum and Isaac [[6]](#6).

### Arrest Data
Download the [Oakland arrest data here]({% link files/arrests.csv %}).

You are provided real data collected from the Oakland police department about arrests in the city in the form of `arrests.csv`. This dataset contains details on drug-related arrests in Oakland from 2009 to 2011. The columns include information such as the description of the incident and the location of the arrest. The most relevant columns will be `Date` (in YYMMDD format) and `Tract` (the census tract where the arrest took place).

### Demographic Data
Download the [demographic data here]({% link files/2010_Pop_Tract_County.csv %}).

You are also provided racial demographic data from the 2010 US Census for each tract in Oakland in `2010_Pop_Tract_County.csv`, which has a column for the tract and the number of people living in that tract from each racial category the US Census collects.  These racial categories are dictated by the US Census Bureau and are measured via people self reporting on the US Census.  The tract is stored in a slightly different format in this data than the arrest data.  Here the tracts look like either, for example, 4001 or 4035.01, whereas in the arrest data the same tracts are written 400100 and 403501.

### Drug Use Data
Download the [drug use data here]({% link files/2010_drug_use.csv %}).

Finally, you are provided with rates of drug use, broken down by demographic category.  This data is from the National Survey on Drug Use and Health (NSDUH), and lists the percentage of people belonging to each demographic category who respond to the survey that they participated in illicit drug use in the last month (among persons aged 12 or older).  The survey is from 2010.  This will serve as a proxy for the ground truth, given that an anonymous survey conducted using careful sampling techniques will undoubtedly be better than arrest data in measuring illicit drug use.

### hw3.py
Download the [starter file here]({% link files/hw3_starter.py %}).

First, you will have to load in the data.  We have provided a wrapper class to do so, creatively called `DataWrapper`, but you will have to provide the functionality of this class yourself.
You will then write the code for analyzing this data in a series of functions creatively called `q1` through `q7`.  You may (and should) add extra functions to help you with the other questions in the analysis section, but they will not be graded.  You can also add attributes or functions to `DataWrapper` to help with other questions in the analysis section, but the input to the DataWrapper constructor should not change.

The starter file has more details on what each function should do, but here is an overview of all of the functions that you will have to write yourself:

* `DataWrapper.__init__` : Constructs all of the attributes of the DataWrapper.
* `DataWrapper.build_tracts` : Constructs the tracts.
* `DataWrapper.process_demo_data` : Constructs the data structure for storing demographic data.
* `DataWrapper.process_arrests` : Constructs the data structure for storing arrest data.
        Hint: It will help to use a library to process the dates and convert them to timestamps, such as the [datetime library](https://docs.python.org/3/library/datetime.html).
* `DataWrapper.split_timestamps` : Splits the arrests data into a training set, for training the PredPol model, and a test set for evaluating the model.
* `q1`, `q2`, `q3`, `q5`, `q7` : Functions to generate the answers to five of the questions in the analysis section, see below for details.

There's also some functions provided that you should not change:

* `DataWrapper.generate_counterfactual` : Generates arrest data, given the tracts selected by PredPol at a given time step; see the analysis section for more on where we need to use this.
* `PredPol` : This class represents the PredPol model.  Has a function `train_model` to build the model from arrest data given by a `DataWrapper`, and a function `predict` to predict the expected number of
    crimes at a given time step for a given tract.  Note that PredPol, even after the model is finished training, also needs the timestamps of all previous arrests to make predictions.  (For those of you who have seen models 
    like SVM, just as SVM makes predictions based on the support vectors, this model makes predictions based on the timestamps).  Do not attempt to retrain the model with timestamps at test time, just feed
    new time stamps from the test set to the prediction function.

### Analysis

Answer each of the questions below as written responses, but in addition, some questions will require code to answer, as indicated by a (C).  There is a corresponding function you must use in the starter code.  These functions must output the answers to the corresponding questions for any input DataWrapper object.

For the sake of simplicity, this analysis will focus only on racial categories, and only four racial categories, each in our demographic data:  `Hispanic or Latino`, `White`, `Black or African American`, and `Asian`.  (The other categories all have relatively small numbers in Oakland.)  Answer each of the following questions using these four racial categories, and these should be the strings used to represent the four racial categories.

For specificity, we will use some notation.  We will use the random variable $$A$$ to denote which of the four racial categories a given person in Oakland belongs to, as measured empirically by our data.  We will use $$Y$$ to denote whether the Oakland resident has used illicit drugs in the last month ($$Y=1$$) or not ($$Y=0$$).

Before we dive into the impact of PredPol, let's start by looking at underlying demographics and drug use.

1. [2 pts.] (C) What is the proportion of each of the four racial categories in Oakland, i.e. what is $$P[A]$$?  (This is short-hand notation for asking for a tuple of four numbers, $$P[A=a]$$ for each of the four racial categories $$a$$.)

2. [2 pts.] (C) What is the probability that a person in each of the racial categories uses illicit drugs, i.e. what is $$P[Y=1\mid A]$$?

Now let's see how these numbers compare to the arrests made.  The problem is that, while we know where each arrest was made, we don't know from this data who was arrested.  So let's assume that whenever an arrest is made in tract r, a uniformly random person is arrested from r:  everyone is equally likely in that tract to get arrested.  Now we can calculate the following:

{:start="3"}
3. [3 pts.] (C) What is the expected number of times a person of each racial category was arrested in Oakland?  Hint: You can calculate the expected number of times a person of each racial category was arrested for each given arrest made (this number will be no more than 1) and then add up over all arrests, because for any random variables $$X$$ and $$Y$$, $$E[X+Y]=E[X]+E[Y]$$.

4. [2 pts.] What is the total expected number of times a person of each racial category was arrested as a percentage of all arrests?  Which racial group(s) were arrested in an outsized proportion to their overall proportion in the population? Which racial group(s) were arrested in an outsized proportion to their overall proportion in the population?  What about, instead of the overall proportion in the population, their estimated rates of using illicit drugs?

Now let's move to analyzing the outputs of the PredPol algorithm.  The PredPol algorithm outputs its belief for the expected number of crimes for any given tract and timestamp.  To turn this into a decision for each time step, we will send a heightened police to twenty different tracts per day.  We will choose the top twenty tracts with the highest expected number of crimes in that timestep.  To measure the potential for PredPol to be discriminatory, we will start with group fairness, as discussed in class, specifically demographic parity (aka independence).  There are two differences from the definition of demographic parity we used in class.  The first is that the task is not binary classification: the algorithm doesn't make a decision about a person only once, but rather once every day -- does a person face heightened police presence at timestamp t, or not (we assume that a person will always be subject to a heightened police presence in a given tract if they live there).  The other difference is that the sensitive attribute $$A$$ is not binary but rather quaternary, with four distinct values.  

To fix the first issue, we will make this a binary question by asking if a person will *ever* face a heightened police presence in their tract, a random variable we will call $$P$$.  Note $$P=1\{\sum_t P_t > 0\}$$.  And because $$A$$ is not binary, we will instead compute all four probabilities, and instead measure discrimination as the difference between the largest probability and the smallest probability.  That is:

{:start="5"}
5. [4 pts.] (C) Run PredPol on each day in the test set and compute the set of twenty tracts to send a heightened police presence to.  What is $$P[P=1\mid A]$$?  Make sure to input when generating a prediction with PredPol all timestamps of arrests made before the time step you are currently predicting for.  Hint: $$P[P\mid A] = \sum_r P[P,R=r\mid A]$$ and then use the definition of conditional probability to write $$P[P,R=r\mid A]$$ in terms of $$P[P\mid R=r,A]$$ and $$P[R=r\mid A]$$.  The first probability can be calculated from the arrest data and the second from the demographic data.

6. [2 pts.] How far away from demographic parity is PredPol?  Which groups faced an outsized police presence compared to their rates of illicit drug use?

However, running PredPol only on the existing data doesn't take into account that by assigning more police officers to a given tract, they are more likely to make more arrests than would have otherwise occurred by not using PredPol.  But PredPol uses those same arrests:  the more recent arrests in a given tract, the more crime PredPol thinks is going to be there. So could PredPol be creating a feedback loop where its initial choices are reinforced, leading to initial bias or discrimination getting reinforced?  This would be even worse than PredPol merely repeating the initial bias!

{:start="7"}
7. [4 pts.] (C) Repeat the same analysis, i.e. compute $$P[P=1\mid A]$$, except use as test-time input to PredPol the arrests that would have happened if police officers were assigned according to PredPol.  Because they were not the arrests that actually happened, but arrests that would have happened had the police acted according to PredPol, we call this a *counterfactual*.  In order to compute the desired probabilities, use the DataWrapper.generate_counterfactual function to generate these counterfactual arrests, and then input all arrests so far into PredPol.predict to generate the twenty top tracts for the next time step.

8. [3 pts.] Run the same analysis for both the original dataset in question 5 and the counterfactual dataset, this time keeping track of the top ten tracts that were chosen the most often.  How different were the top ten tracts chosen different between the two approaches?  Does this explain the differences, or lack there of, between the two different versions of $$P[P=1\mid A]$$?

Here's another way of understanding the difference between the original dataset and the counterfactual dataset.  Our concern is that on the counterfactual dataset, PredPol gets more and more confident of its choice because of a feedback loop between sending police to a location and PredPol's confidence that there is crime there.  For each dataset, let's split the tracts into two: the top ten tracts chosen by PredPol for that dataset, and every other tract.

{:start="9"}
9. [4 pts.] Run the same analysis again, but this time, for each of the two different approaches, keep track of the following for each time step: 
$$
\frac{\sum_{r \text{ a top tract}} P[P_t\mid R=r]}{\sum_{r \text{ not a top tract}} P[P_t\mid R=r]}.
$$  This is a sequence of odds ratios, representing how much more confident PredPol was on the top ten tracts for that dataset than all other tracts at each time step.  Plot these two sequences of odds ratios using matplotlib, and include it in the written write-up (make sure the plot is legible and the two sequences labeled).  What does this plot say about how counterfactuals affected how confident PredPol got over time?

### Reflection
Answer the following short-response questions. Your response should only be as long as necessary to answer the questions, but do make sure to briefly state why you are right for those questions that need it.

{:start="10"}
10. [2 pt.] What is PredPol trying to predict, and what does it actually predict?  That is, what is PredPol trying to measure, and what is its target variable?  For this question, assume that PredPol achieves very low error with respect to its target variable.  How it can fail to successfully predict what its trying to predict even with low error?

11. [3 pts.] How is the arrest dataset biased, and who is it biased towards?  Make sure to state what you mean by bias.  What changes, if any, would you make to the dataset to remove biases?  Use what you've learned in the analysis section to justify your response.

12. [3 pts.]  What is a feedback loop, and how can feedback loops contribute to worsen discrimination?  Can PredPol contribute to a feedback loop?  Use what you've learned in the analysis section to justify your response.

13. [3 pts.] Does PredPol exhibit racial discrimination?  Make sure to state what you mean by racial discrimination, using concepts discussed in class.  Use what you've learned in the analysis section to justify your response. 

14. [2 pt.] We had assumed that whenever an arrest is made in a given tract, a uniformly random person is arrested from that tract.  How might this assumption be tested?  If it's wrong, what consequences for our analysis might this incorrect assumption cause?

15. [3 pt.] How should predictive policing algorithms, such as PredPol, be governed?  What should we require out of them, and what mechanisms should we use to uncover failures in your requirements?  

16. [3 pt.] Do predictive policing algorithms such as PredPol have any ethical place in policing? Why or why not? Consider the input necessary for such a model as well as the potential effects that would be produced by a precinct using such a model to help make their policing decisions.


## References
<a id="1">[1]</a> 
Walter L. Perry, Brian McInnis, Carter C. Price, Susan C. Smith, and John S. Hollywood. Predictive Policing: The Role of Crime Forecasting in Law Enforcement Operations.  National Institute of Justice, 2013. <https://nij.ojp.gov/library/publications/predictive-policing-role-crime-forecasting-law-enforcement-operations>

<a id="2">[2]</a> 
Karen Hao.  Police across the US are training crime-predicting AIs on falsified data.  MIT Technology Review, 2019.  <https://www.technologyreview.com/2019/02/13/137444/predictive-policing-algorithms-ai-crime-dirty-data/>

<a id="3">[3]</a> 
Geolitica.  Website accessed April 2023.  <https://geolitica.com/company/>

<a id="4">[4]</a>
G. O. Mohler, M. B. Short, Sean Malinowski, Mark Johnson, G. E. Tita, Andrea L. Bertozzi, and P. J. Brantingham. Randomized Controlled Field Trials of Predictive
Policing.  Journal of the American Statistical Association, 2015. <https://doi.org/10.1080/01621459.2015.1077710>

<a id="5">[5]</a>
Rashida Richardson, Jason Schultz, and Kate Crawford. Dirty Data, Bad Predictions: How Civil Rights Violations Impact Police Data, Predictive Policing Systems, and Justice. 94 N.Y.U. L. Rev. Online, 2019. <https://www.nyulawreview.org/wp-content/uploads/2019/04/NYULawReview-94-Richardson_etal-FIN.pdf>

<a id="6">[6]</a>
Kristian Lum and William Isaac.  To predict and serve?  Significance, 2016. <https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.1740-9713.2016.00960.x>
