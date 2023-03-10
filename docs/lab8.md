---
layout: spec
title: Lab 8
sitemapOrder: 20
---

Lab 8
==========================
{: .primer-spec-toc-ignore }


## Task
In this lab, you will engage in some exploratory data analysis on a public dataset hosted by scikit-learn, known as the diabetes dataset. This dataset tracks demographic and medical information of patients with diabetes, along with a measure of progression of the disease over time. Ten baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements were obtained for each of n = 442 diabetes patients, as well as the response of interest, a quantitative measure of disease progression one year after baseline. The data consists of ten features: `age`, `sex`, body mass index (`bmi`), average blood pressure (`bp`), six blood serum measurements (`s1`-`s6`), as well as the target variable (`target`), a quantitative measure of disease progression one year after baseline. These datapoints were each obtained for 442 diabetes patients. In this lab, you will explore the predictive ability of each of these ten features with regards to the target. Predictive ability refers to the strength of the correlation between a given feature and the target variable, or in other words, the degree to which these datapoints for a given individual allow us to predict how much the disease will progress for that individual.

For this assignment, you will include a short write-up in addition to your code submission. Include this write-up as a comment on your Canvas submission or by submitting a `.txt` or `.docx` file along with your code submission for the lab.

First, you will need the scikit-learn Python library. To install this library via pip, load up your virtual environment and run the following:

```console
pip3 install scikit-learn
```

To use `scikit-learn` to download the diabetes dataset, run the following:

```python
from sklearn import datasets

diabetes = datasets.load_diabetes()
```

This dataset will be given to you in a form similar to a Python dictionary. View the keys of this dataset by running:

```python
print(list(diabetes))
```

A description of these keys is as follows:

* `data`: The values for the ten features for each of the 442 recorded patients. Formatted as a 442 x 10 array
* `target`: The target data, a quantitative measure of diabetes disease progression one year after baseline
* `DESCR`: Description of the dataset
* `feature_names`: Names of the ten features

Next, read the description of the dataset by running:
```python
print(diabetes['DESCR'])
```

Verify the number and names of the features in your dataset by running:
```python
print(len(diabetes['feature_names']))
print(diabetes['feature_names'])
```

Below is a more in-depth description of each of the six blood serum measurement features:

* s1: cholesterol level
* s2: low-density lipoprotein level
* s3: high-density lipoprotein level
* s4: ratio of total cholesterol and high-density lipoprotein level
* s5: triglyceride level
* s6: blood sugar level

You can take a look at the raw data itself by running the following. Recall that the data is presented as a 442 x 10 array where each row represents one of the 442 diabetes patients, and each column representes value of one of the ten features for a given patient.
```python
print(diabetes['data'])
```

View the first 25 lines of the target variable by running the following. Recall that the target value does not have a unit, but is a comparative measure of diabetes progression one year after the features for that patient were measured. The higher the value of the target variable, the more the disease progressed over the course of that one year.
```python
print(diabetes['target'][:25])
```
{:start="1"}
1. Next, write a few lines of code to output the minimum and maximum values for the target variable across all 442 patients. Include these two values in your write-up.

2. Using the information gathered so far, along with your previous knowledge of diabetes as a disease, which of these features do you think would make the best predictor of disease progression? List the top two or three features you can think of, along with a short summary of your reasoning, in your write-up.

Next, use `matplotlib` to construct a scatterplot of each feature against the target. For each value of `N` from 0 through 9, use the following method:

```python
import matplotlib.pyplot as plt

plt.scatter(diabetes['data'].T[N], diabetes['target'])
plt.show()
# Or matplotlib.pyplot.savefig(filepath)
```

Make sure to also label your axes using the feature list for your own convenience. 

Then, answer the following:
{:start="3"}
3. Judging by these scatter plots, which features seem to be the best predictors of disease progression? How can you tell from the scatterplot?

Next, we can use the `seaborn` library to compute a heatmap showing correlations between these variables. A heatmap is a 2D grid with the list of variables on each axis, where each cell denotes the strength of the correlation between those variables.

First, we'll need to install the `pandas` and `seaborn` libraries:
```console
pip3 install pandas seaborn
```

Next, use `pandas` to prepare the dataset for the creation of the heatmap. We add in the `target` column to the main dataset so we can compare each feature's correlation with disease progression.
```python
import pandas as pd

df1 = pd.DataFrame(diabetes["data"], columns = diabetes['feature_names']) # The ten features
df2 = pd.DataFrame(diabetes["target"], columns = ["progression"]) # The target variable (progression)

df = pd.merge(df1, df2, left_index=True, right_index=True) # Merge in the target column
corr = df.corr() # Generate the correlation matrix
```

Then, use the `seaborn` library to generate the heatmap and display it with `matplotlib`.
```python
import seaborn as sns

ax_heatmap = sns.heatmap(corr, vmax=1, vmin=0, cmap="rocket_r") # Generate the heatmap
plt.show() # Display the heatmap using matplotlib
```

Observing this heatmap, answer the following:
{:start="4"}
4. Which features correlate most disease progression? Does this fit your hypothesis?

5. Which different features correlate most with eath other? Explain this correlation using your knowledge of the dataset and your real-world knowledge of diabetes.

Once you are complete, turn `lab8.py`, along with your write-up, to Canvas.
