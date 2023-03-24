---
layout: spec
title: Lab 10
sitemapOrder: 20
---

Lab 10
==========================
{: .primer-spec-toc-ignore }


## Task
In this lab, you will continue your exploration of the scikit-learn diabetes dataset. Following your introduction to linear regression on this dataset in the previous lab, you will any bias in the predictive ability of a linear regression model towards people classified as a certain sex. Then, you will determine whether and how this bias might be easily reduced by removing parts of the dataset.

For this assignment, you will include a short write-up in addition to your code submission. Include this write-up as a comment on your Canvas submission or by submitting a `.txt` or `.docx` file along with your code submission for the lab.

### Review: training the model
As before, to get started, import `numpy` and `sklearn`. If you need to install `sklearn`, refer to the previous lab.
```python
import numpy as np
from sklearn import datasets, linear_model, model_selection, metrics
```

Next, load in the diabetes dataset and extract the features and the target.
```
# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Extract data
x = diabetes['data'] # Features
y = diabetes['target'] # Target (disease progression)
```

Recall that, in order to train the model, you must first fix the seed, split the data into train and test sets, then call the scikit-learn `LinearRegression` method.

```python
np.random.seed(298) # Set numpy seed
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y) # Split data
model = linear_model.LinearRegression().fit(x_train, y_train) # Train model
```

After that, we can use the trained model to make predictions on the test data.
```python
y_test_pred = model.predict(x_test)
```

Then, to determine the overall predictive ability of our model, we can calculate the mean squared error. A lower MSE indicates a better model.

This process can be done with the following scikit-learn library:
```python
metrics.mean_squared_error(y_test, y_test_pred)
```

### Identifying predictive bias
Compare the ability of the model to predict diabetes progression for people classified as male vs. for people classified as female. To do this, train the model as normal. Next, you will need to split the x and y test sets into those for people classified as male and female using your knowledge of Python dictionary and list comprehension. You may need to review earlier labs for a reminder on how the dataset is structured. In the dataset, negative values for the sex column indicate a person classified as female, and positive values indicate a person classified as male. Is there a disparity in test accuracy between the two? If so, why might this be? Report the difference in MSE for the two groups and discuss your results in your writeup.

One might imagine that a possible way to remove any biases for one sex or another would be to remove the sex feature entirely during training. Is this a good choice for removing bias in the dataset? Is it likely to work? Discuss this in your writeup by referring to previous discussions in lecture.

Next, give this method a try. Recall from the last lab that we can remove a given feature from the dataset as follows:
```python
feature_names = diabetes['feature_names']
index_of_feature = feature_names.index("sex")
x = np.delete(x, index_of_feature, 1)
```

Does disparity across sex improve just by removing the feature? Discuss the results in your writeup and identify why this may be the case.
