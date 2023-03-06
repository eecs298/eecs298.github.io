---
layout: spec
title: EECS 298 Homework 2
subtitle: Due 11:59 PM EST on Friday, March 17, 2022.
sitemapOrder: 20
---

Homework 2: Celebrity Linkage Attack
==========================
Due 11:59 PM EST on Friday, March 17, 2022.

## Submission
This homework will consist of two sections, each with a programming task and written responses. You will submit your work via Gradescope (linked from Canvas). On Gradescope, there are two assignments you will need to use to submit. Upload your written responses as a `.pdf` file to the `Homework 2: Written Responses` Gradescope assignment. It is required that you typeset your written responses in a document editor or a program like LaTeX. In addition, upload your code for both parts as `hw2.py` to the `Homework 2: Code Submission` Gradescope assignment. The code that you upload to Gradescope will be graded using an autograder. This autograder will consist of public test cases, the results of which are visible upon each submission, and private test cases, the results of which will only be visible after the final deadline for the assignment. Your code will be tested on private datasets in addition to the datasets you are given, and as such, your code should be properly generalizable to other, similar data. Your programming implementation will be graded on correctness as well as efficiency. You can submit your code to the autograder as many times as you wish.  We encourage collaboration, but all work you submit must be your own.  All writing must be your own, and collaboration must not result in code or writing that is identifiably similar to other solutions.

## Introduction: The NYC Taxicab Database
The New York Freedom of Information Law (FOIL) grants the public the ability to access, upon request, records maintained by state government agencies. This includes the New York City Taxi and Limo Commission (NYC TLC), an agency which manages the city's taxi cabs. In 2013, a data analyst named Chris Whong submitted a FOIL request to the NYC TLC and was in turn provided with a database containing full records of every taxi ride given in New York City that year. Chris Whong then published this data in its entirety. Due to the public nature of the NYC taxi system, along with the poor de-anonymization of the database done by NYC officials, this database is ultimately highly vulnerable to a linkage attack.

Recall that a linkage attack requires a (seemingly innocuous) feature or features contained in two or more datasets, one dataset containing PII like a person's name, and the other containing sensitive information.  For this assignment, you will perform a real linkage attack on this dataset by using public photos captured by paparazzi documenting celebrities in NYC taxi cabs. Paparazzi photographers in New York City frequently capture celebrities entering or exiting yellow taxi cabs, and many of their pictures show the cab’s unique medallion number. The number is prominently displayed on the car’s exterior in lit letters on top, in black paint on the side, and on both license plates. With this information in both datasets, it is possible to assign a name (and face) to a trip in this dataset (the PII), matching a celebrity with the trip's pickup and drop-off locations, the amount of the fare, and the tip each celebrity paid their driver (the sensitive information). 

On top of this, NYC TLC also publicly publishes up-to-date information about all licensed taxi drivers in the city. By combining this information with the trip database, we can identify the real name of the person who drove each celebrity, as well as the daily patterns, tips earned, and locations frequented by each driver.

## Part 1: Executing the Linkage Attack
For this assignment, you will be provided access to a version of the original 2013 NYC TLC database lightly modified in the interest of convenience. The structure of this database, however has been kept fully intact. In addition, you will be provided with another publicly available NYC TLC dataset containing identifying information about each taxi driver in the database, as well as photographs of celebrities in taxi cabs and the dates these photos were taken. Your task will be to perform a linkage attack using these three datasets. The NYC TLC dataset contains readily accecible data on tips and locations, but no names of passengers or drivers, while the celebrity photographs contain the celebrities themselves along with taxi medallion numbers, and the driver dataset allows you to identify the real name of the driver for each trip. Your goal is to match celebrity photographs with trips in the taxi database, aggregating information on celebrity tipping habits (the tips in our dataset have been modified from the original for convenience and privacy). Following this, you will implement a differential privacy technique to test out a method for privatizing this data.

### Trip Data
[Download trips.csv here.](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/trips.csv)

The original NYC dataset consists of hundreds of thousands of lines. You will be given a shortened, modified version of this dataset with 1,000 lines. Each row in this dataset represents one trip made by a NYC taxi. The columns of this dataset are as follows:

* `medallion`: The medallion number on the taxi cab. Hashed with MD5.
* `hack_license`: The hack license number of the taxi driver. Hashed with MD5.
* `date`: The date of the trip. Follows `YYYY-MM-DD` format.
* `payment_type`: The payment method used by the passenger. `CSH` for cash and `CRD` for credit card.
* `fare_amount`: The fare for the trip in USD.
* `tip_amount`: The tip, in USD, given to the driver by the passenger.
* `pickup_location`: The full latitude and longitude, in that order, of the starting location for the trip.
* `dropoff_location`: The full latitude and longitude, in that order, of the trip destination.

The medallion number is used to identify the taxi cab and appears on the license plate of the taxi, the side of the taxi, and atop the taxi. The medallion number follows a specific format, and is composed of one number, followed by one letter, followed by two numbers, e.g.: `1A23`.

A hack license is a form of identification and licensure for taxi drivers in NYC. The number on each driver's hack license is 7 numerical digits long, e.g. `1234567`.

### Celebrity Data
[Access the celebrity photos here.](https://eecs298.github.io/celebs.html)

You are given access to 27 photos of celebrities spotted in taxis around NYC. The each photo comes with the name of the celebrity in the photo and with the date the photo was taken (in `YYYY-MM-DD` format).  As in many such problems, the data is not in the most convenient format -- in order to conduct the linkage attack, you will need to transcribe the medallion number contained in each photo.  

As such, you will need to create your own dataset (stored as a `.csv` file, see HW1 for an example of a `.csv`) containing the information in these photos. This dataset should contain the name of the celebrity in each photo, along with the medallion number present in the photo and the date the photo was taken. The structure for this dataset is ultimately up to you, as this file will not be graded, and is only for your own use in this assignment. You will need to manually identify and transcribe the medallion numbers from each photo into this database. Just as you would if you were performing a linkage attack in the wild, you'll need to pull out your thinking cap for this part! Pay close attention to the format, font, and possible locations of these medallion numbers. If you cannot identify these medallions yourself due to visual impairment, please reach out to a member of the course staff, and we will help you out.

It is possible that not every celebrity in this dataset is boarding a taxi contained in the NYC dataset, and furthermore, there are many taxis in the NYC dataset for which we have no photographs. Your implementation should reflect that, as with real-world data, one cannot necessarily assume a strict one-to-one relationship between datasets.

### Driver Data
[Download drivers.csv here.](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/drivers.csv)

The City of New York currently hosts publicly accessible databases listing all current licensed taxi drivers, along with their hack license number. With this information, you will be able to identify not only the passengers in select trips, but the names of the drivers themselves as well. Each row represents a registered NYC taxi driver, and the columns are as follows:

* `hack_license`: The hack license number of the taxi driver.
* `name`: The name of the driver, formatted as `Lastname, Firstname`.

Every hack license in the trip dataset matches to a driver in this dataset, but not every driver here can be found in the trip dataset.

### Deanonymizing the Data
Before you can execute the linkage attack, you will first need to reverse the anonymization that NYC TLC attempted.  The `medallion` and `hack_license` columns in the trip dataset are hashed with a hash function called MD5. Hashing is the process of transforming one string of characters into another, often to make storage and access easier. Hashes are stable, since performing a given hash on the same string will always produce the same output.  MD5 is a type of hash that functions by taking any length string, and outputting a 32-character alphanumeric string.  While some hash functions can be used cryptographically to hide the input of the hash function, MD5 is not one of them.

Take a look at the `medallion` and `hack_license` columns in the data. We can observe that the hash is not simply random, since the same alphanumeric string is sometimes repeated multiple times throughout each of the two columns. Since the MD5 hash is stable, the same medallion or license number will always be represented by the same alphanumeric string. The hashing of this data with MD5 appears to be evidence that NYC officials intended to anonymize the medallion and license numbers, but it doesn't work well here because we know the format of the medallion and hack licenses. There are only a few hundred thousand possible medallion or hack liscense numbers, and as such, we can brute force reversing the hash function by simply testing the hashed version of every possible medallion and license number against each value in these columns.

One possible way to do this is to construct a table of all precomputed values for both the medallion and the hack license number, called a `rainbow table`. When denonymizing a single value, you'll then look up the number in the table which, when hashed, is equal to that value.  You are given the `HackLicenseDecoder` and `MedallionDecoder` classes for this purpose. The structure for these classes is entirely up to you, but in the interest of efficiency, ensure that you are not recomputing the entire table for each new value you deanonymize.

To encode a string using MD5, you can use the `md5` library as follows:

```python3
import md5

hashed_value = md5(my_value.encode()).hexdigest()
```

### hw2.py
[Download the starter file here.](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/hw2.py)

First, create your own `.csv` file to contain the relevant information in the celebrity images and load that file in by implementing the `process_celebrities` function. You will also load in the driver data by implementing `process_drivers`. Next, implement the `linkage_attack` method to link this data and output a list of fully deanonymized trips. Finally, implement a function to return information about the average tip amount in the database. To help you with your implementation, you are given a detailed starter file, described below.

* `Celebrity`: A class containing information from a single photo of a celebrity. Takes the name of the celebrity in the photo, the taxi medallion in the photo, and the date the photo was taken. The `medallion` value can be either hashed or unhashed at this stage, your choice. The name of the celebrity should be stored as `Firstname Lastname`, and the date should be in `YYYY-MM-DD` format.

* `Driver`: A class containing information about a taxi driver from the NYC taxi drivers dataset. Takes the name of the driver and the hack license number of the driver. The `hack_license` value can be either hashed or unhashed  at this stage, your choice. The name of the celebrity should be stored as `Firstname Lastname` (note that you will need to convert this, as the database you are given stores these as `Lastname, Firstname`), and the date should be in `YYYY-MM-DD` format.

* `process_celebrities`: A function to process your `.csv` containing identifying celebrity information. Outputs a list with a `Celebrity` object for each row in the given `.csv`.

* `process_drivers`: A function to process the given `.csv` containing identifying taxi driver information. Outputs a list with a `Driver` object for each row in the given `.csv`.

* `Trip`: A class containing deanonymized information for a given trip. Includes unhashed medallion and hack license numbers, as well as the name of the driver. To get the name of the driver, pass in a `Driver` object, then pull out the driver's name and store it as a field. Note that `fare_amount` and `tip_amount` each need to be stored as a `float`, and that the two location fields should each be a `Tuple` containing two strings, with the latitude followed by the longitude.

* `CelebrityTrip`: A class containing deanonymized information for a given trip in which the passenger is known from a celebrity photograph. Includes unhashed medallion and hack license numbers, as well as the name of both the passenger and driver. To get the name of the passenger, pass in a `Celebrity` object, then pull out the celebrity's name and store it as a field. This class inherits from the `Trip` class, so be sure to make use of the `super()` method in your constructor. This class is only to be used for trips which match a celebrity photgraph.

* `MedallionDecoder`: An optional class for you to implement to help with decoding medallion numbers hashed with MD5. The structure of this class is up to you. If you choose to make a table of all possible medallion numbers, it is most efficient to only calculate this table once and then store it as a field.

* `HackLicenseDecoder`: An optional class for you to implement to help with decoding hack license numbers hashed with MD5. The structure of this class is up to you. If you choose to make a table of all possible hack license numbers, it is most efficient to only calculate this table once and then store it as a field.

* `linkage_attack`: Takes the outputs of the `process_celebrities` and `process_drivers` functions. Returns a list of `Trip` objects for each row in the dataset for each taxi trip you have successfully linked. When a given trip corresponds to a celebrity photo, use a `CelebrityTrip` object instead of a `Trip` object.

* `get_mean_tip`: Given the output of the `linkage_attack` method and a range of dates (in `YYYY-MM-DD` format), this function returns the average tip across all trips in the database occurring during that date range. Has an optional flag to exclude trips paid for in cash with `$0` given as tip from the calculation, since many of such entries are likely the result of a data collection error. You can use the `datetime` library to help with calculations involving dates; [refer here for documentation](https://docs.python.org/3/library/datetime.html).

* `get_mean_tip_dp`: A differentially private version of the above method. Detailed further in Part 2.

### Analysis
Use your code to give answers to the following questions. Include a short response when relevant.

1. [1 pt.] Report the celebrity who tipped the highest amount, along with the amount they tipped (if you have information on more than one trip made by that celebrity, take the average of all tips that celebrity made.) What is the average tip (including outliers) across all celebrities you have successfully linked?

2. [1 pt.] Use your implementation of the `get_mean_tip` method (including outliers) to find the average tip for all rides in the NYC database (not just those with celebrities). Do the same for all trips occurring between July 1st and August 1st, 2013. Report those values here. Is the average tip from the celebrities higher or lower than the year average?

3. [1 pts.] As it turns out, the full NYC database misreports tip amounts for many rides paid with cash as $0, leading some outlets to incorrectly report that some celebrities commonly tipped $0. This is a result of a data collection error, as tips made in cash are not reported in the dataset. What percentage of the passengers in this database paid with cash? Compare the average mean tip for the year including these outliers to the mean tip when these outliers are discluded.


### Reflection
Answer the following short-response questions. Your response should only be as long as necessary to answer the questions, but do make sure to briefly state why you are right for those questions that need it.

{:start="3"}
3. [3 pts.] The information in this database, both alone and in aggregate, can reveal other information besides the tip amount. Find a trip for which you have revealed the names of the celebrity and driver. Use a map service (e.g. Google Maps) to identify a NYC address at the latitude and longitude listed with this trip. Report this information and, not unlike a member of the paparazzi, speculate what the purpose of this trip may have been.  Then, identify and describe a way that this dataset could be used to uncover information not previously in the public domain.  What would the potential harms of this be?

4. [3 pts.] Think back to the issue of the misreporting of cash tips from question 3. How did trust play a role in this mistake, and what is the role of surveillance and technology in encouraging this trust? What might be the consequences of trusting data too much?

5. [3 pts.] Describe the social context of the NYC TLC taxi data, according to the principles of contextual integrity.  What norms of appropriateness and flow/information should apply to this data?

6. [3 pts.] Does this linkage attack constitute a breach of privacy, and if so, how, and under which conception(s) of privacy?  Include at least three conceptions of privacy.  Justify your answer.

7. [2 pts.] Do these celebrity images constitute a form of surveillance? Describe how it does or does not meet criteria for surveillance, as discussed in class.  Justify your answer.

8. [2 pts.] Does the NYC TLC dataset constitute a form of surveillance? Describe how it does or does not meet the criteria for surveillance, as discussed in class. Justify your answer.

9. [3 pts.] Why did the linkage attack succeed here? Is there a way to maintain the benefits of having this data while preventing the linkage attack?  If so, how?  Justify your answer.

10. [3 pts.] Consider how you would have handled the situation. How should this release have been handled differently by the NYC Taxi and Limousine Commission? How should public be given access to this data? Is your approach in line with Freedom of Information Law? (You may refer to the [text of the law](https://opengovernment.ny.gov/freedom-information-law)). If it is not, how should the law be changed to accommodate private data release?


## Part 2: Applying Differential Privacy
Refer to the `get_mean_tip` method you wrote for the previous section. Consider an alternative approach in which NYC hosts a live-updating version of this database online, and rather than letting users interact directly with the database, allows users to probe the database with queries similar to the one you created in this function. This approach would still introduce privacy issues, however, because if one knows the exact time that an individual took a taxi ride, one could query for the average tip directly before and directly after their trip to find the exact tip that individual left.  So you will implement a differentially private mechanism to prevent this difference attack.  You will implement the so-called Laplace mechanism, which adds noise to the result of the query, making any difference in the output caused by the inclusion of one individual much harder to detect.  In this section, your task will be to write a differentially private implementation of the `get_mean_tip` method using the Laplace mechanism and reflect on the results.

The tip amount column in this database is a continuous value rather than a discrete value, and as such, we won't be able to use the randomized response mechanism discussed in class.  Instead, we can return the mean tip, plus a random value drawn from a distribution ([the Laplace distribution](https://en.wikipedia.org/wiki/Laplace_distribution), in this case).  The Laplace distribution (like many other distributions, e.g. the Gaussian distribution) is parameterized by a variance, which for this distribution is called the scale parameter `b`, which is always a positive number. We want to add more variance (larger `b`) when epsilon is smaller or the amount the output of the query can change when one person's data changes is larger.  This latter amount is called the sensitivity of the query. In our case, the most the mean can change is the range of the tips (we'll assume the range is between 0 and the highest tip between the start and end dates), divided by the number of tips.  Then you can implement the Laplace mechanism for calculating the noised mean:

* Calculate the sensitivity. The sensitivity is given by the ratio of the range and the size of the data.
* Calculate the scale. The scale is found by dividing the sensitivity by epsilon.
* Use the numpy function `random.laplace` [method](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.laplace.html#numpy.random.Generator.laplace) to sample a value from this distribution.
* Add this value to the original mean, yielding the noised version to the query.

The outline of the `get_mean_tip_dp` method is given to you in the starter file for this assignment. This function should accept the following arguments:

* `linkage_attack_results`: the results of the `linkage_attack` method.
* `start_date`: the lower-bound date for the search. Follows `YYYY-MM-DD` format.
* `end_date`: the upper-bound date for the search. This bound is inclusive, so this date is included in the search. Follows `YYYY-MM-DD` format.
* `ignore_outliers`: if `True`, this method does not factor in cash trips with a tip of zero. This argument is optional. The default value is `False`.
* `epsilon`: the epsilon value for the Laplace distribution. This argument is optional. The default value should be `0.1`.

Your function should return a noised version of the query from your original `get_mean_tip` method. Your implementation will be tested for accuracy and to ensure that it is differentially private.

### Reflection
Answer the following short-response questions:

{:start="11"}
11. [1 pt.] What effect would increasing or lowering epsilon have on the privacy and accuracy of the results?

12. [2 pts.] What problems with the original release does this differentially private implementation solve? What problems with the original release does it not solve?

13. [3 pts.] To what degree does this differentially private solution satisfy contextual integrity, and how so?  What's the difference between differential privacy and contextual integrity?  Justify your answer.
