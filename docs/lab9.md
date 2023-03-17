---
layout: spec
title: Lab 9
sitemapOrder: 20
---

Lab 9
==========================
{: .primer-spec-toc-ignore }


## Task
In this lab, you will continue your exploration of the scikit-learn diabetes dataset. Following your exploratory data analysis of the dataset in the previous lab in which you established qualitative correlation between the features and the target, in this lab you will train a linear regression model to quantitatively predict disease progression using the features in the dataset.

For this assignment, you will include a short write-up in addition to your code submission. Include this write-up as a comment on your Canvas submission or by submitting a `.txt` or `.docx` file along with your code submission for the lab.

### Intro to Multiple Linear Regression
Linear regression is a machine learning method used to make predictions on a target using one or more features. In its simplest form, linear regression involves fitting a straight line to the data using the following equation:

y = mx + b

Here, y is the value of the target, x is the value of the feature, and m and b are the coefficients trained by the linear regression model. Given a set of examples x and matching targets y, the model iteratively changes the values of m and b until the value of the function for each feature x is as close as possible to the value of that feature's label, y. Linear regression is used for problems where the target is a continuous value, as is the case for our diabetes dataset. If our target was instead a discrete value, such as either 1, for a positive diabetes test, or 0, for a negative test, we would want to use a classification algorithm rather than a regression algorithm.

Multiple linear regression is an extension of simple linear regression for when there is more than one feature. As such, the line trained by the model depends on the values for all n features x<sub>n</sub>:

y = m<sub>1</sub>x<sub>1</sub> + m<sub>2</sub>x<sub>2</sub> + ... + m<sub>n</sub>x<sub>n</sub> + b

Here, the model gets all of the features (in this case, each of the readings for a single patient), and iteratively updates all of the m<sub>n</sub> values at once in order to get the value of the function as close to the target y for that patient as it can. Once the model has updated these coefficients for every patient (a process referred to as training), we can then make predictions on other patients not included in training in order to test the model. To make a prediction, the linear regression model simply plugs in all of the features x<sub>n</sub> into the line function with the trained coefficients and calculates the y value, which becomes the prediction made by the model.

To get started, import `numpy` and `sklearn`. If you need to install `sklearn`, refer to the previous lab.
```python
import numpy as np
from sklearn import datasets, linear_model, model_selection, metrics
```

Next, as in the previous lab, load in the diabetes dataset and extract the features and the target.
```
# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Extract data
x = diabetes['data'] # Features
y = diabetes['target'] # Target (disease progression)
```

### Splitting Data into Train and Test Sets
It is common practice to split the available data into separate sets for training and testing the model. The primary reason for doing this is to evaluate the performance of the model on unseen data. When we train a machine learning model, we use a portion of the available data to fit the model to the underlying patterns in the data. The goal is to find a model that can accurately predict the target variable for new, unseen data. However, if we use all of the available data for training, we have no way of knowing how well the model will generalize to new data. By splitting the data into training and testing sets, we can use the training data to fit the model and the testing data to evaluate its performance.

You can use the following scikit-learn function to arbitrarily split the data into train and test sets:
```python
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y)
```

When training our linear regression model, we will let the model learn the target values (`y_train`) from the patients in the training set (`x_train`). Then, once trained, we will give it the patients in the test set (`x_test`) and ask it to predict the disease progression values for each. We will then compare those predictions to the actual disease progression values for those patients (`y_test`). `y_test` is also known as the ground truth.

### Making Predictions with Linear Regression
```python
np.random.seed(298) # Set numpy seed
```

Next, we can use a pre-made scikit-learn function to train the linear regression model using the training data.
```python
model = linear_model.LinearRegression().fit(x_train, y_train) # Perform linear regression
```

To see the coefficients trained by the model, reference the following field:
```python
print(model.coef_)
```

After that, we can use the trained model to make predictions on the test data.
```python
y_test_pred = model.predict(x_test)
```

Take a look at these predictions and compare them to the ground truth. Each index `i` in `y_test_pred` corresponds to the same patient as in `y_test[i]`.

### Visualizing Predictions
We can use the libraries from last week's lab to visualize the predictions made by our linear regression model. Here, you will create a density graph, which compares the distributions of the target variable between the predicted values and the ground truth.

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

```python
sns.kdeplot(y_test,  label="Ground Truth") # Graph actual values
sns.kdeplot(y_test_pred,  label="Predicted Values") # Graph predicted values
```

What does the density graph show? What does it indicate about the predictions made by our linear regression model? Write down your answers to these questions in your writeup.

```python
# Show density graph
plt.title('Density of Prediction vs. Actual Progression')
plt.xlabel('Progression')
plt.ylabel('Density')
plt.show()
```

### Measuring Predictions with Mean Square Error
It is useful to quantitatively measure the quality of our model's predictions. To this end, we use a metric called mean squared error (MSE). The motivation behind using MSE is to quantify the difference between the predicted values and the actual values, known as the error. The lower the MSE, the better the model is at predicting the value of the target variable. As such, we can use it to compare different models to determine their relative performance.

In addition, MSE is often used as the loss function in the training process of a linear regression model. The goal of the training process is to find the coefficients of the regression equation that minimize the MSE. Broadly speaking, machine learning models work by continuously minimizing the value of loss functions in order increase their ability to correctly predict target values. Linear regression trains its line of best fit by iteratively finding the best coefficients to minimize the mean squared error for the training data.

Mean squared error is calculated as follows:
* Calculate the error for each prediction by finding the difference between that prediction and the ground truth.
* Square each error value.
* Find the mean of these squared values.

This process can be done with the following scikit-learn library:
```python
metrics.mean_squared_error(y_test, y_test_pred)
```

If you would like a short challenge, try to code the MSE function using the steps shown above!

Print out the MSE of your linear regression model and note it for the following step.

### Making Predictions without Certain Features
Now that we have a way to quantitatively measure our linear regression model's ability to predict disease progression given our set of features, let's see how our model's predictive ability changes if we remove certain features from our dataset.

We can remove a given feature from the dataset as follows:
```python
feature_names = diabetes['feature_names']
index_of_feature = feature_names.index("bmi")
x_without_feature = np.delete(x, index_of_feature, 1)
```

Using your work from last week's lab, choose a few features that had the highest and lowest correlation to disease progression. Remove one of these features from the dataset and perform linear regression on the altered dataset. How does the MSE of the model change? Repeat this experiment by changing the single feature that you remove. How does removing features with high correlation to the target change the MSE as compared to removing those with low correlation to the target? Why is this? Write down your answers to these questions in your writeup, including the MSE for each.
