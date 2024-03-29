---
layout: spec
title: Lab 8
sitemapOrder: 20
header-includes: |
    \usepackage{amsmath}
---

Lab 8
==========================
{: .primer-spec-toc-ignore }


## Task
In this lab, you will continue your exploration of (part of) the COMPAS dataset and get experience building a simple machine learning model using the package scikit-learn. This lab will explore one source of harm that can occur in the learning process: **overfitting**. You will then continue practice computing conditional probabilities and you will compute a conditional expectation value as well.

To get started, first download the simplified COMPAS dataset using `wget` and then create a file called `lab8.py` in the same folder as the downloaded dataset.
```terminal
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/compas-data-lab-8.csv
```
### Data - COMPAS Dataset (Simplified)
The original COMPAS dataset contains many features including demographic features, criminal history, and information about the current charge of defendants. In this lab, you will use a simplified version of this dataset contained in `compas-data-lab-8.csv` so that we can follow along part of the critical analysis [ProPublica did with this dataset](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing). Different from last week in Lab 7, there is another column added to define the training/testing split.

Following ProPublica's analysis, the `features` we consider and their corresponding numeric values are: 
* `sex`: Male: 0, Female: 1
* `age`: `age` < 25: 0, 25<= `age`<= 45: 1, `age` >45: 2 
* `race`: Caucasian: 0, African-American: 1, Asian: 2, Hispanic: 3, Native American 4, Other: 5
* `priors_count`: Number of prior offences to current charge. 
* `c_charge_degree`: Degree of current charge. Misdemeanor: 0, Felony: 1
* `two_year_recid`: Indicator variable for whether the defendent re-offended two years after current charge. No: 0, Yes: 1

Again, following ProPublica's analysis, the `target variable` we are trying to predict and its corresponding numeric values is:
* `score_text`: Whether the defendent was classified as Low or High/Medium risk with Northpointe's tool. Low: 0, High/Medium: 1

The training/testing split is defined by the last column in the dataset:
* `split`: One of `Train` and `Test` to indicate whether the row should be in the training or the testing set.

The `features` and `target variable` are coded as numeric values because the model we are using needs numeric values to make predictions.

### Representation and Loss - Logistic Regression Model and Cross Entropy Loss
We are again going to be using a Logistic Regression model to fit the data by minimizing the `cross entropy loss`. See Lab 7 or [here](https://en.wikipedia.org/wiki/Logistic_regression) for more details on the logistic regression model and [here](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression) for more details on the loss function.

### Optimization - Training the Logistic Regression Model
Now that we have introduced the model and loss function we will use, we can begin coding the training process. To get started, import `sklearn`. If you need to install `sklearn`, run `pip install scikit-learn` in your terminal.
```python
from sklearn import linear_model, metrics
```

Next, read in the data from `compas-data-lab-8.csv` however you'd like, but split the data into four `lists` as follows:
* `compas_train_features`: The features (the columns: `sex,age,race,priors_count,c_charge_degree,two_year_recid`) for all the rows that have `split == "Train"`.
* `compas_train_labels`: The corresponding label (the column `score_text`) for the above features for all the rows that have `split == Train `.
* `compas_test_features`: The features for all the rows that have `split == "Test"`.
* `compas_test_labels`: The corresponding label for the above features for all the rows that have `split == "Test"`.

Make sure to cast the values to `int`s as you read them in and populate the lists.

Recall that in Lab 7 we used a function from `sklearn` to split our data, but this time we have already manually split the data ourselves. These splits were chosen to give an example of what it means for a model to **overfit**. A model is said to be overfit to its training data when it performs well on the training data, but performs poorly on the testing data. We will again use **accuracy** as our measure of performance and we will see overfitting in the next section.

First, we need to train the logisitic regression model and recall from Lab 7 this is done as follows:
```python
logistic_regression_model = linear_model.LogisticRegression().fit(compas_train_features, compas_train_labels)
```

After that, we can use the trained model to make predictions on the test data.
```python
test_pred = logistic_regression_model.predict(compas_test_features)
```
We also want the predictions on the training data, so that we can compare the performance of the model on the training data and on the testing data.
```python
train_pred = logistic_regression_model.predict(compas_train_features)
```

### Evaluating the Model
We are going to use **accuracy** to evaluate our model for evidence of overfitting. 

Let `Y` be a random variable for the *actual* risk score for each defendant in `compas_test_features` (i.e., `compas_test_labels`) and let `Y'` be a random variable for the *predicted* score for each defendent in `compas_test_features` (i.e., `test_pred`). Further, let `n` be the number of examples in the testing set. Then, the **accuracy** of the model is defined as the number of examples out of the `n` examples where `Y==Y'` divided by `n`. We will again use the function `metrics.accuracy_score()` to get the accuracy of our model.

Compute the **accuracy** of the model on both the training and testing set and print out the result as follows:
```console
Train Accuracy of model: 0.8376353039134055
Test Accuracy of model: 0.587809293904647
```
As we can see, the *training accuracy* is much higher than that of the *testing accuracy* which indicates our model has **overfit** to the training data! This gives us evidence that the model has not learned a pattern in the training dataset that can be found in other distributions of data, and thus it may cause harm (through errors in prediction) if we tried to use this model on datasets beyond the training set.

### Computing Conditional Expectation 

We will use the **test set**  and **train set** to calculate *empirical* probabilities in this section to use in our expected value calculation. 

For this section, you will compute the expected value of `Y'` (i.e., the model prediction) *conditioned on each age category* for the *train set* and *test set* separately so that we can compare the conditional expected values among the different groups. Recall that conditional expected value is computed as the weighted sum of possible values of `Y'` (i.e., `0` or `1`) where the weights are the conditional probabilities. That is,
```math
E[Y' | \text{age_category} = a] = 0 * P(Y' = 0 | \text{age_category} = a) + 1 * P(Y' = 1 | \text{age_category} = a)
```

Print out the results of your calculation. Your output (combined with the accuracy calculation) should look as follows
```console
Train Accuracy of model: 0.8376353039134055
Test Accuracy of model: 0.587809293904647
Age Category: 0, Test Expected Y' Value: 0.017817371937639197, Train Expected Y' Value: 0
Age Category: 1, Test Expected Y' Value: 0.13410596026490065, Train Expected Y' Value: 0
Age Category: 2, Test Expected Y' Value: 0, Train Expected Y' Value: 0.1257285595337219
```

Turn in `lab8.py` to Gradescope when you're done.


