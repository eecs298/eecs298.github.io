---
layout: spec
title: Lab 5
sitemapOrder: 20
---

Lab 5
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will take the role of a Facebook web designer for the ad campaign creation page. Your task will be to write several Regular Expressions to be used for validation of user input. A Regular Expression, or RegEx, is a sequence of characters that forms a search pattern, which can be used to detect correct or incorrect formatting of a certain string. If the search pattern within RegEx does not find a match within a given input string, then that string can be considered not to satisfy that RegEx. RegEx is commonly used for purposes like this across the web. For this lab, you will use an existing RegEx library for Python to write RegEx patterns for various purposes within a Python program.

### lab5.py
Create a file titled `lab5.py`. In this file, you will write code to perform RegEx matching on various input strings. You can choose two of the following three categories to write your RegEx for:

* An expression to determine whether the user has entered a real name or not. Facebook infamously requires the use of real names for all accounts, going so far as to automatically check the "realness" of a name during account creation. Their policy on real names can be found [here](https://www.facebook.com/help/229715077154790), whereas more details on the controversy can be found [here](https://en.wikipedia.org/wiki/Facebook_real-name_policy_controversy). Much of this policy centers around checking that names don't contain the names of famous characters or words from the English dictionary, but checking against a dictionary isn't something that can be done with RegEx. Instead, try to think of your own conditions to determine whether a name might be valid, such as checking for numbers, unusual punctuation or capitalization, or an unusual number or arrangement of spaces. Your criteria to determine the realness of a name are up to you, and do not need to be based off of Facebook's actual policy.

* An expression to determine whether a Cost-Per-Click bid is formatted as an actual monetary amount. Again, your critera for this case are up to you -- think about ways that a monetary amount could be represented with both numbers and symbols, and write test cases that reflect them.

* An expression to determine whether a phone number is formatted correctly. The way you determine whether a phone number is real is up to you, and, like the other cases, can be as in-depth as you wish. Think of some correctly and incorrectly formatted phone numbers and write your expression accordingly.

For each of the two cases above that you choose, you will need to write a Regular Expression to determine whether a string fits your required format for that case. In addition, hardcode several test cases (simply assign test strings to variables in your code), as many as you find necessary, and test them against your Regular Expression with the `re` library, as shown below.

RegEx is very powerful and can be used to create arbitrarily complex expressions, but for the sake of this lab, you simply need to do your best within the allotted timeframe to create reasonable expressions -- try to think of as many test cases as you can, but if you can't get your expression to fit them all in time, that's alright, simply turn in what you have! This lab will be graded based off of your participation in the exercise, not the completeness of your implementation. 

After completing your implementation, write a short reflection on how the expressions you wrote might exclude certain individuals or result in social harm if put into place. You can copy-paste this reflection and include it as a comment in your Canvas submission.

### Getting started 
The `re` library in Python supports Regular Expression use and can be used as follows:

```python
test_case_1 = "The rain in Spain" # An example test case
regex = "^The.*Spain$" # An example expression

# The re.search function determines whether the expression finds a match.
# If there is one, it evaluates to True.
# If there is no match, it evaluates to False.
match = re.search(regex, input_str) 

if match:
  print("Input string is valid.")
if not match:
  print("Input string is invalid.)
```

To gain a feel for how to write a Regular Expression, check out these resources:

[https://www.w3schools.com/python/python_regex.asp](
https://www.w3schools.com/python/python_regex.asp)

[https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)

To write and test RegEx live and get feedback, check out the site below:

[https://regex101.com/r/cO8lqs/10](https://regex101.com/r/cO8lqs/10)
