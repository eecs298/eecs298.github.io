---
layout: spec
title: EECS 298 Homework 2
subtitle: Due 11:59 PM EST on Friday, February 23rd, 2024.
sitemapOrder: 20
---

Homework 2: Celebrity Linkage Attack
==========================
Due 11:59 PM EST on Friday, February 23rd, 2024.

Written Points: 23
Coding Points: 38
Total Points: 61

## Submission
This homework will consist of two sections, each with a programming task and written responses. You will submit your work via Gradescope (linked from Canvas). On Gradescope, there are two assignments you will need to use to submit. Upload your written responses as a `.pdf` file to the `Homework 2: Written Responses` Gradescope assignment. It is required that you typeset your written responses in a document editor or a program like LaTeX. In addition, upload your implementation in `HW2.py` to the `Homework 2: Code Submission` Gradescope assignment. The code that you upload to Gradescope will be graded using an autograder. This autograder will consist of public test cases, the results of which are visible upon each submission, and private test cases, the results of which will only be visible after the final deadline for the assignment. You can submit your code to the autograder as many times as you wish.  We encourage collaboration, but all work you submit must be your own.  All writing must be your own, and collaboration must not result in code or writing that is identifiably similar to other solutions.

Specifications where you must implement code will be highlighted in <span style="background-color: #3B67A8D4">Blue</span> for clarity.

## Introduction: The NYC Taxicab Database
The New York Freedom of Information Law (FOIL) grants the public the ability to access, upon request, records maintained by state government agencies. This includes the New York City Taxi and Limo Commission (NYC TLC), an agency which manages the city's taxi cabs. In 2013, a data analyst named Chris Whong submitted a FOIL request to the NYC TLC and was in turn provided with a database containing full records of every taxi ride given in New York City that year. Chris Whong then published this data in its entirety. Due to the public nature of the NYC taxi system, along with the poor de-anonymization of the database done by NYC officials, this database is ultimately highly vulnerable to a linkage attack.

Recall that a linkage attack requires a (seemingly innocuous) feature or features contained in two or more datasets, one dataset containing personally identifiable information (PII) and the other containing sensitive information.  For this assignment, you will perform a real linkage attack on this dataset by using public photos captured by paparazzi documenting celebrities in NYC taxi cabs since many of their pictures show the cab’s unique medallion number. In this case, the **taxi medallion number** and the **date of the picture/trip** will be used as the PII and the sensitive information we are trying to recover is each **celebrity's tip amount** for their taxi trip.


## Part 1: Executing Linkage Attacks

First, use the wget command to get the HW2.py starter code file and the two `csv` files used in this homework.

```
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/homeworks/HW2.py
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/trips.csv
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/celebrities.csv
```

For this assignment, you will be provided access to a lightly modified version in the interest of convenience of the original 2013 NYC TLC database in `trips.csv`. In addition, you will be provided with the `celebrities.csv` file containing information about another publicly available NYC TLC dataset with photographs of celebrities in taxi cabs.

Your task will be to perform a linkage attack using these two datasets. The NYC TLC dataset has tips, but no names of passengers, while the celebrity photographs we have names, but no tip amounts. The goal is to match celebrity information with trips in the taxi database. It is possible that not every celebrity in this dataset is boarding a taxi contained in the NYC dataset, and furthermore, there are many taxis in the NYC dataset for which we have no photographs. So, your implementation should not assume a strict one-to-one relationship between datasets. However, you may assume that a **medallion** and **date** match between the datasets is a correct match.

### `trips.csv`
The original NYC dataset consists of hundreds of thousands of lines. You will be given a shortened, modified version of this dataset with 1000 lines. Each row in this dataset represents one trip made by a NYC taxi. The columns of this dataset are as follows:

* `medallion`: The medallion number on the taxi cab. Hashed with MD5.
* `date`: The date of the trip. Follows `YYYY-MM-DD` format.
* `fare_amount`: The fare for the trip in USD.
* `tip_amount`: The tip, in USD, given to the driver by the passenger.
* `pickup_latitude`: The latitude of the starting location for the trip.
* `pickup_longitude`: The longitude of the starting location for the trip.
* `dropoff_latitude`: The latitude of the trip destination.
* `dropoff_longitude`: The longitude of the trip destination.

The medallion number is used to identify the taxi cab and appears on the license plate of the taxi, the side of the taxi, and atop the taxi. The medallion numbers in this dataset follow a specific format, and are composed of one number, followed by one (uppercase) letter, followed by two numbers, e.g.: `1A23`.

### `celebrities.csv`
This dataset contains information about different celebrity trips as evidenced by paparazzi photos such as the following example pictures.

![Emma Roberts, 2013-12-20](image15.png) ![Jake Gyllenhaal, 2013-03-08](image12.png) ![Extra Image](image20.png)

Each row in the dataset represents one celebrity trip. The columns of this dataset are as follows:

* `name`: The name of the celebrity or celebrities in the picture.
* `medallion`: The medallion number of the taxi in the picture.
* `date`: The date the picture was taken. Follows `YYYY-MM-DD` format.

### Deanonymizing the Data
Before you can execute the linkage attack, you will first need to reverse the anonymization that NYC TLC attempted.  The `medallion` column in the trip dataset is hashed with a hash function called MD5. Hashing is the process of transforming one string of characters into another, often to make storage and access easier. Hashes are stable, since performing a given hash on the same string *will always produce the same output*.  MD5 is a type of hash that functions by taking any length string, and outputting a 32-character alphanumeric string.  While some hash functions can be used cryptographically to hide the input of the hash function, MD5 is not one of them.

The hashing of the `medallion` data with MD5 appears to be evidence that NYC officials intended to anonymize the medallion and license numbers. However, it turns out that each medallion gets hashed to a *unique* hash value. Therefore, we can use our knowledge of the hashing function to figure out the hashed version of the medallions seen in `celebrities.csv` to match celebrities to trips!

To encode a string using MD5, you can use the `md5` library as follows:

```python3
import md5

hashed_value = md5(my_value.encode()).hexdigest()
```

## HW2.py
First, you will <span style="background-color: #ADD8E6">implement several classes</span> to set up the taxi trip database with `trips.csv` as described below. Then, you will use the main branch of the file to perform a linkage attack with the `celebrities.csv` information. We will then explore trying to protect against this attack by coarsening the query allowed to the database as well as making the query function differentially private.

### Implementing the classes
* `Celebrity`: A class containing information from a single photo of a celebrity. Takes the name of the celebrity or celebrities in the photo, the taxi medallion in the photo, and the date the photo was taken. You will <span style="background-color: #ADD8E6">compute and store</span> the hashed `medallion` value with *all letters given in upper case* as an attribute. You will also <span style="background-color: #ADD8E6">overload the `print` function</span> so that you get the following output when printing a `Celebrity` object using Olivia Munn as an example:  
```
Celebrity Name: Olivia Munn, Medallion: 2E42, Photo Date: 2013-04-19\n
```

* `Trip`: A class containing all information for a given trip as given in `trips.csv`. You will <span style="background-color: #ADD8E6">overload the `print` function</span> so that you get the following output when printing a `Trip` object using an example `Trip` from `trips.csv`:
```
Hashed Medallion: BCF07D2F69DB29C27DA7CCF5DE6B4843, Trip Date: 2013-04-19, Fare Amount: 8, Tip Amount: 2.1, Pickup Location: ('40.757977','-73.978165'), Dropoff Location: ('40.751171','-73.989838')\n
```

* `TaxiTripsDatabase`: This class is used to store and query information from `trips.csv`. The constructor is implemented for you and sets the `self.trips_list` attribute to the return value of `_read_trips_data`.

    * `_read_trips_data`: <span style="background-color: #ADD8E6"> Implement this function</span> to read in the data from `trips.csv` from the location given as `file_path`. The `_` at the start of this function is commonly used to indicate it is a function only intended to be used within the class.
        * Arguments
            - `file_path`: File path to `trips.csv`
        * Returns
            - Return a `list` of `Trip` objects to store into `self.trips_list`.

    * `query_trips`: <span style="background-color: #ADD8E6"> Implement this function</span> to return a `list` of `Trip` objects that have the same attribute values as the attributes names passed into the function.
        * Arguments
            - `attribute_list`: A `list` of `Trip` attribute names to use to query the database
            - `attribute_matching_values`: A `list` of values (one for each attribute name given in attribute_list) to match in the database
        * Returns
            - a `list` of `Trip`s with matching given attributes
        * Error Handling
            - `raise` an `AttributeError` if any attribute name in `attribute_list` is not one of the `Trip` class attributes: `"md5_medallion", "date", "fare_amount", "tip_amount", "pickup_location", "dropoff_location"`.
        * Example Output
            - For example, `query_trips(["date", "tip_amount"], ["2013-02-09", 1.50])` should return a list of `Trip` objects that have `date ==  "2013-02-09"` and `tip_amount==1.50`.

    * `query_mean_tip`: <span style="background-color: #ADD8E6">Implement this function</span> to calculates and returns the mean tip in `self.trips_list` between the given dates . Additonally, do not include `Trip`s in the mean calculation that have the same hashed medallion as the optional argument `filtered_medallion`. Finally, if the optional argument `epsilon` is not `None`, you will implement <span style="background-color: #ADD8E6"> implement `epsilon`-Differential Privacy</span> as specified in a later section, for now you can ignore this optional argument.
        * Arguments
            - `start_date`: The start date for the average, in YYYY-MM-DD format.
            - `end_date`: The end date (inclusive) for the average, in YYYY-MM-DD format.
            - `filtered_medallion`: MD5 hashed medallion to not include in mean tip calculation. Default empty string.
            - `epsilon`: Specifies the differential privacy level if not None. Default None.
        * Returns
            - Two values separated by a comma: 1. A float denoting the average tip within the timeframe, 2. the number of tips used in the mean calculation. For example: `return mean_tip, number_of_tips`. Make sure to properly unpack the
            return values when calling the function. For example: `mean_tip, num_tips = query_mean_tip(*args)`.
        * Error Handling
            - If no `Trip`s are found within the given timeframe, `raise ValueError`.
        * Hint: Refer to [datetime.strptime(string, format)](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) for how to create a `datetime` object out of a given `string` formatted in the given `format`. The `format` you will use is `%Y-%m-%d`. This will allow you to compare dates using the `<=` and `>=` operators.


### Linkage Attack: `perform_linkage_attack`

You are now going to attempt a *linkage attack* by implementing `perform_linkage_attack`. Your goal with this attack is to gather a `list` of `tuple`s of linked `Trip`s and `Celebrity`s so that you can figure out how much each `Celebrity` tipped on their trip. Hint: recall what our PII is in this setting to determine with attributes should be passed to `query_trips` to link a `Celebrity` to a `Trip`!

* `perform_linkage_attack`: <span style="background-color: #ADD8E6"> Implement this function</span> to return a `list` of `(Trip, Celebrity)` `tuple`s (in that order) to link a `Celebrity` to a `Trip`.
    * Arguments
        - `celebrity_list`: A list of `Celebrity` objects to link
        - `taxi_trip_databse`: An instance of a `TaxiTripsDatabase` to query data from
    * Returns
        - A `list` of linked `(Trip, Celebrity)` `tuple`s.

Use the `"__main__"` branch of the Python program to read in `celebrities.csv` and use this function as you wish to answer the questions.

1. [2 pts.] Report the celebrity who tipped the highest amount, along with the amount they tipped.

2. [2 pts.] Considering the data available in `trips.csv` (i.e., the column categories), name **one** thing an attacker could learn about the celebrity and describe how it might violate their sense of privacy.

### Difference Attack: `perform_difference_attack`

For this part, you are now **only allowed** access to `trips.csv` using `query_mean_tip`. Since you can only get mean tip values for a given date range, you will have to perform a *difference attack* by implementing `perform_difference_attack` to recover the tip information for a single `Celebrity`. Recall that a difference attack is performed when you figure out information about an individual when querying a value with and without filtering them out of the query. Hint: You can filter out a given celebrity in a mean tip calculation using the `filtered_medallion` optional argument in `query_mean_tip`.

Your goal with this attack is to try to reconstruct the tip values for each `Celebrity` you linked in the above section using queries to `query_mean_tip` for each `Celebrity`. Hint: You should only need two queries for each `Celebrity`.

* `perform_difference_attack`:<span style="background-color: #ADD8E6"> Implement this function</span> to return the calculated tip value of the given celebrity using only two calls to `query_mean_tip`.
    * Arguments
        - `celebrity`: A Celebrity to guess the tip_amount for
        - `taxi_trip_databse`: An instance of a TaxiTripsDatabase to query data from
        - `epsilon`: Specifies the differential privacy level if not None. Default None. Pass this argument into `query_mean_tip`
    * Returns
        - The calculated tip amount for the given celebrity


Again, use the `"__main__"` branch of the Python program to read in `celebrities.csv` and use this function as you wish to answer the questions. Use your results from the linkage attack section to verify you calculated the correct `tip_amount` for each celebrity! Note: it is okay if your calculated tips are slightly different (within 0.005) to the true tip values as this may happen with rounding errors.

### Applying Differential Privacy (DP)
Refer to the `query_mean_tip` function you wrote for the previous section. Since we can recover `Celebrity` tip information with a difference attack, you will implement a differentially private algorithm to attempt to prevent the attack. You will implement the Laplace algorithm, which adds noise to the result of the query, making any difference in the output caused by the inclusion of one individual much harder to detect.  Specifically, your task will be to return an `epsilon`-DP response if the  `epsilon` argument is not `None` in the `query_mean_tip` function using the Laplace algorithm.

The tip amount column in this database is a continuous value rather than a discrete value, and as such, we won't be able to use the randomized response algorithm discussed in class.  Instead, we can return the mean tip, plus a random value drawn from a distribution ([the Laplace distribution](https://en.wikipedia.org/wiki/Laplace_distribution), in this case).  The Laplace distribution (like many other distributions, e.g. the Gaussian distribution) is parameterized by a variance, which for this distribution is called the scale parameter `b`, which is always a positive number. We want to add more variance (larger `b`) when epsilon is smaller or the amount the output of the query can change when one person's data changes is larger.  This latter amount is called the sensitivity of the query.  In our case, the most the mean can change is the range of the tips (you can assume the largest tip is $11 and the smallest is $0), divided by the number of tips that are used in the mean calculation.  Then you can implement the Laplace algorithm for calculating the noised mean:

* Calculate the `sensitivity` as described above.
* Calculate the `scale`. The `scale` is found by dividing the `sensitivity` by `epsilon`.
* Use the numpy `random.laplace` [function](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.laplace.html#numpy.random.Generator.laplace) to sample a value from this distribution to add noise to the output of the query.
* If the added noise makes the average tip value *negative*, output 0 instead.

3. [1 pt.] First, we will check the accuracy of our noised queries. Query the mean tip for the month of January in 2013 (i.e., `start_date="2013-01-01"` and `end_date="2013-01-31"`) without DP and with `epsilon=0.8`. Are the returned outputs close (within $0.50)?

4. [2 pts.] Set `epsilon=0.8` and use `perform_difference_attack` in the previous section and use the same calculation to try to guess each celebrity's tip amount. Report the tip guess for Judd Apatow and whether it is close to his actual tip value (within $0.50).  

5. [2 pts.] Repeat the above with `epsilon=0.1`, `epsilon=1`, and `epsilon=15`. Were you able to calculate a tip guess for Judd Apatow that is within $0.50 of his actual tip value for any of these values? If so, which one(s)? Use your results to order the `epsilon` values from **most** to **least** accurate in terms of how close the calculated tip value was to the true tip value.

## Part 2: Written Reflection Questions

Answer the following short-response questions. In your responses, we are looking for an effort to apply concepts from lectures and readings to answer each of these questions. Make sure to briefly justify each answer.

6. [4 pts.] Give 3 differences between k-anonymity and differential privacy in terms of the properties described in lecture. Which one is better at preventing difference attacks?

7. [2 pts.] Using the conception of privacy as restricted access to hidden information, describe whether this case study constitutes a violation of privacy. Why or why not?

8. Given that we were able to perform the linkage attack due to the poor anonymization of the taxi medallions, one reaction might be to *remove the taxi medallion information altogether* from the released data. However, the [FOIL](https://opengovernment.ny.gov/system/files/documents/2023/11/foil-law-text-11032023.pdf) act is intended to provide transparency of government data to the public, so one should be careful in removing publically available information.<br><br>
    a. [2 pts.] Describe **one possible benefit** to the community (NYC residents taking the taxis) for publically releasing some version of the taxi medallion information (anonymized or not). <br><br>
    b. [2 pts.] Describe **one possible way** the linkage attack could still be performed even if the taxi medallion information was removed.

9. In this question, we will examine contextual integrity in this setting of the NYC TLC dataset and celebrity photographs. <br><br>
    a. [2 pts.] Describe the sociotechnical context for this setting: the sender and recipient, the subject, information, and relationship under which information is transmitted.<br><br>
    b. [3 pts.] Describe a setting with a similar sociotechnical context **that is not this one** (it should not involve the NYC TLC dataset).  Make sure to point out why the context is similar.  Then describe the *norms of appropriateness* and the *norms of flow* for that other context.<br><br>
    c. [3 pts.] Describe how norms of appropriatness and norms of flow are violated in **this** setting by using the previous two parts to this question.  Conclude by stating whether contextual integrity holds in this setting.
