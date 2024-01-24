---
layout: spec
title: EECS 298 Homework 1
subtitle: Due 11:59 PM EST on Friday, February 2, 2022.
sitemapOrder: 20
---

Homework 1: Restaurant Recommendations
==========================
Due 11:59 PM EST on Friday, February 2, 2024.

Autograder points: 20

Written response points: 38

Total points: 58

## Submission
This homework will consist of a written section with reflection questions and a programming section in Python. You will submit your work via Gradescope (linked from Canvas). On Gradescope, there are two assignments you will need to use to submit. Part 1 is the coding part where you will write all your implementations in `HW1.py`. Part 2 is the written reflection part.  Upload your code for Part 1 as `HW1.py` to the `Homework 1: Code Submission` Gradescope assignment. The code that you upload to Gradescope for Part 1 will be graded using an autograder. Upload your written responses for the reflection questions in Part 2 as a `.pdf` file to the `Homework 1: Written Responses` Gradescope assignment. It is required that you typeset your written responses in a document editor or a program like LaTeX.

## Introduction
For this assignment, you are a software engineer for LivingLikeALocal, a software company that creates a restaurant recommendation website for travelers in cities across the United States. Your task is to design a database of local restaurants as well as implement a class to sort and search the database. Your goal as a designer is to provide the most amount of information to your customers so that they can go to highly recommended restaurants in an area.

Specifications where you must implement code will be highlighted in $\color{blue}\text{Blue}$ for clarity.

## Part 1: Creating the Database
In this section, you will create the restaurant database including data collection and code implementation. The first task will be to collect restaurant information and organize it in a `csv` file. Next, you will implement the `RestaurantDatabase` class in `HW1.py` which includes several functions related to searching, sorting, and outputting the data in the database. After, you will answer a few analysis questions.

First, use the `wget` command to get the `HW1.py` starter code file.
```console
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/homeworks/HW1.py
```

### Collecting Restaurant Data
To get started, you will choose any city in the **United States** to collect restaurant information from. Once you have a city in mind, you can use [Yelp](https://www.yelp.com/) and [Google Maps](https://www.google.com/maps) to look up **5 restaurants** in that city. You will collect the following information to include in the `csv` file:
1. Restaurant name
2. Restaurant address
3. Restaurant telephone
4. Restaurant website
5. A rating out of 5 stars
6. The relative price in the terms of the number of dollar signs shown
7. A keyword describing the restaurant (bar, pizza place, etc.)
8. 1 other categories of your choosing based on the information available on Yelp and Google Maps

If you cannot find one of the above categories for one of your restaurants, use the tag `None` to indicate the information was not available. We will use this later to replace the value with the built-in Python keyword `None` which represents a null value. Keep in mind that since you have control over the restaurants you choose for the database, you should try to limit your use of the tag (i.e., by choosing restaurants with most of the categories filled in).   

After collecting the restaurants, you will format the information into a `csv` file. To begin, create a file named `restaurants.csv` in the same folder as `HW1.py`. First, you will add the header line with the names of all the categories as follows:
```
Restaurant name,Restaurant address,Restaurant telephone,Restaurant website,Rating,Relative price,Keyword,YOUR_CATEGORY
```
Then, add all your restaurant information to this file and make sure to separate each restaurant by a new line. See below for an example of adding Cafe Zola in Ann Arbor to `restaurants.csv`:
```
Restaurant name,Restaurant address,Restaurant telephone,Restaurant website,Rating,Relative price,Keyword,YOUR_CATEGORY
Cafe Zola,"112 W Washington St Ann Arbor, MI 48104",+17347692020,http://www.cafezola.com/,3.8,2,Eclectic restaurant,YOUR_CATEGORY_INFO
```
Remember that `csv` stands for "Comma-separated values", so any value that has commas must be given in quotes so the information is read in properly. See the address value in the example above for an example of this. You will use the Python `csv` package to read in the file in your database which you can read more about [here](https://docs.python.org/3/library/csv.html). Keep in mind that `csv` files read in data as `str`s and we will work with all numeric data as if they are `str`s for ease of searching and sorting. However, we do not want the missing categories to affect our searching and sorting, so you will change any attribute value that is `"None"` to the Python  keyword `None`.

### Implementing the Database in `HW1.py`
Now it is time to implement the restaurant database. In `HW1.py` you will see two class outlines `Restaurant` and `RestaurantDatabase`. The `Restaurant` class will define our restaurant objects and give us a way to access the different information categories for each restaurant. In the constructor `__init__` function of `Restaurant`, you will see a list of input variables that corresponds to the list of categories of restaurant information above. $\color{blue}\text{Create and assign attributes}$ for this class for each of the input variables. Recall that all attributes in Python are `Public` by default, so there is no need to add any `get` or `set` functions to this class! Instead, we access attributes as follows
```python
restaurant = Restaurant(name, address, telephone, website, rating, price, keyword, category_choice)
print(restaurant.name) # accessing and printing the restaurant name
```
We will eventually want to be able to easily see the information in a `Restaurant` object, so we are going to overload the `__str__(self)` function in the `Restaurant` class. Python automatically calls the built-in function `__str__(self)` when you use the `print()` function and `__str__(self)` returns a `str` to be printed out. So, we can change the implementation of the `__str__(self)` function in the `Restaurant` class to get Python to display what we want when you use the `print()` function on a `Restaurant` object.

- $\color{blue}\text{Implement the function}$ `__str__(self)` to return a `str` that displays the following information when you use the `print()` function on a `Restaurant` object where each attribute value below (in all caps) should be the value of the attribute for that specific `Restaurant` object. Note that there is a single space before and after each value (except before `website` and after `telephone` and `keyword`) and there should be newline characters `\n` at the end of each line.
```
Name: NAME_VALUE Address: ADDRESS_VALUE Telephone: TELEPHONE_VALUE\n
Website: WEBSITE_VALUE Rating: RATING_VALUE Price: PRICE_VALUE Keyword: KEYWORD_VALUE\n
```
An example output for Cafe Zola is given below
```
Name: Cafe Zola Address: 112 W Washington St Ann Arbor, MI 48104 Telephone: +17347692020
Website: http://www.cafezola.com/ Rating: 3.8 Price: 2 Keyword: Eclectic restaurant
```

Next, the `RestaurantDatabase` class will be used to read and store the restaurant information as well as sort and search through the information. The descriptions and implementation instructions of each function in the class are given below. Look for the `# TODO` comment in `HW1.py` for where to add your implementations and remember to remove the `pass` keyword during your implementation.

- `__init__(self)`: Constructor for the `RestaurantDatabase` class. This class has one `attribute` called `self.restaurants` to hold all the `Restaurant` objects and is initialized as an empty list here.

- `read_data(self, file)`: $\color{blue}\text{Implement this function}$ to read in data from a `csv` file named `file` and create and add `Restaurant` objects to `self.restaurant`. Refer to the [csv package documentation](https://docs.python.org/3/library/csv.html) for how to use the function `csv.reader()`. As stated above, you will have to check if any of the attribute values are `"None"` (a `str`) and pass in the Python `None` keyword to the `Restaurant` constructor instead.

- `sort_database(self, attribute_name, reverse=False, k=0)`: $\color{blue}\text{Implement this function}$ to sort `self.restaurants` based on the given `attribute_name`. First, create a list of `Restaurant` objects that **do not** have the Python keyword `None` as the value for the given `attribute_name`. Then, use the default sorting of the built-in Python `sorted()` function on this list of filtered `Restaurant` objects. Use the optional argument `reverse` boolean argument in the `sorted()` function to determine if this default sorting is reversed or not. Refer to [Python sorting documentation](https://docs.python.org/3/howto/sorting.html) for how to use the `sorted()` function. Use the optional argument `k` to return the top `k` `Restaurant` objects in a `list` after sorting. Hint: use [getattr()](https://docs.python.org/3/library/functions.html#getattr) to access an attribute of a class when `attribute_name` is given as a `str`.

- `sort_by_keyword(self)`: $\color{blue}\text{Implement this function}$ to create and return a `dict` object where the `key` is the `keyword` attribute of the `Restaurant` class and the `value` is a list of `Restaurant`s that have a given `keyword`. Do not include any `Restaurant` objects where the `keyword` is the Python keyword `None`.

- `search_database(self, attribute_name, search_query)`: $\color{blue}\text{Implement this function}$ to search for the given `search_query` in the given `attribute_name` of the list of restaurants and return a `list` of matching `Restaurant`s. Use the Python keyword `in` to check if the `search_query` exists in the attribute of each `Restaurant`. As such, partial `str` matches are enough for the `Restaurant` to be in the returned `list`. We assume searches are **not** case sensitive, so make sure to match the case between the search query and the database information for an accurate search. Hint: use the [lower()](https://www.w3schools.com/python/ref_string_lower.asp) function for `str`s and remember to skip any `Restaurant` objects where the value of the `attribute_name` is the Python keyword `None`.

### Expanding the Scope of LivingLikeALocal
Your company has started to gain some attention from investors in **Japan**! Naturally, your company is excited to expand operations to this new country and has asked you to test the existing database to see if it can be deployed as-is as soon as possible for maximum profits.

Similar to above, you will choose any city in **Japan** and look for 5 restaurants on [Yelp](https://www.yelp.com/) and [Google Maps](https://www.google.com/maps) again and add the information to another `csv` file named `restaurants_japan.csv`.

### Analyzing Code Output
Recall that scripting code will execute in the `__main__` branch of a Python file, so any code you write to view the output of your program will be under the conditional
```python
if __name__ == "__main__":
```
Remember the importance of whitespace in Python and make sure all code in this section follows the indent of the `# TODO` comment.

A few of the reflection questions below will be based on the output of your code and you may use your class implementation however you'd like here to answer these questions.


## Part 2: Written Reflection Questions
For this section, write a short paragraph response to each question. The purpose of this part is to reflect on the design process in this homework as a whole and the consequences the decisions made throughout this assignment could have when implemented. In your responses, we are looking for an effort to apply concepts from lectures and readings to answer each of these questions.  Make sure to briefly justify each answer.


1. [6 pts] Suppose four users in the American city you chose are looking for the top `k=2` restaurants sorted by `name`, `price` (low to high), `rating` (high to low), and your `category_choice`, respectively. Name **two design decisions** that could change the output of at least one of these recommendations if those design decisions had been made differently. In your answer, consider design decisions made by either us, the homework designers, or you in choosing the additional category, creating the `csv` file, and implementing the code. Cite **specific examples from your dataset** for each design decision you named and explain why the outputs would change.

2. [3 pts] Report the city you chose in the United States and the city you chose in Japan. Name **two things** that were different about the process of finding 5 restaurants in a Japanese city compared to finding 5 restaurants in an American city. For example, why it was easy or difficult to parse the information you needed for your database in both cases. Name **one assumption** in the categories given to you for the database (or the one you chose) that might make it more difficult to collect data in contexts beyond the United States. If you encountered no difficulties at all, try to imagine a country/city/context where you might run into difficulties and report on that instead.

3. [3 pts] An American tourist visiting the Japanese city you chose used your recommendation function and went to the first restaurant recommended when sorting by `rating`. They loved the restaurant and wanted to send a handwritten letter to the owners to personally thank them for the experience. The tourist knows that the Japanese addressing system is different than in the United States, but they forget how it works. However, they had such success with your recommendation that they trust your algorithm to return the address in the correct order it would go on a letter. You may assume the following ordering for the [Japanese addressing system](https://en.wikipedia.org/wiki/Japanese_addressing_system#Address_order).<br> <br>Report the `address` output of your implementation for the restaurant recommendation described above using the output from the overloaded `__str__(self)` function. Does your implementation of `search_database` return the address in the correct order? (Note: your answer does not need to be yes here!) Briefly explain why or why not. Describe **one benefit** for reporting address information as the user would understand it in *their* local context and **one benefit** for reporting address information as it is understood in *the restaurant's* local context.

4. [6 pts] Using the concepts from the Friedman and Nissenbaum reading, describe **three examples** of **preexisting bias** in this restaurant recommendation system.

5. [6 pts] Using the concepts from the Friedman and Nissenbaum reading, describe **three examples** of **technical bias** in this restaurant recommendation system.

6. [6 pts] Using the concepts from the Friedman and Nissenbaum reading, describe **three examples** of **emergent bias** in this restaurant recommendation system.

7. [4 pts] Suppose LivingLikeALocal becomes very popular in a certain city such that hundreds of people (tourists and locals!) a day use the website to decide where to eat. Give **two potential consequences** on the local restaurants of deploying the website in this popular city compared to a city of the same size where only a few people use the website.

8. [4 pts] Using concepts and specific terms from the Winner reading, name **one way** the website technology might influence the communities it is deployed in and **one way** the community use might affect future development of the website technology.

9. [OPTIONAL FEEDBACK] As this class is a work in progress, what difficulties did you encounter while doing this assignment and how can we make the next homework assignment better? Thank you!
