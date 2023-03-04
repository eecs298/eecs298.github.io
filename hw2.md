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
This homework will consist of two sections, each with a programming task and written responses. You will submit your work via Gradescope (linked from Canvas). On Gradescope, there are two assignments you will need to use to submit. Upload your written responses as a `.pdf` file to the `Homework 2: Written Responses` Gradescope assignment. It is required that you typeset your written responses in a document editor or a program like LaTeX. In addition, upload your code for both parts as `hw2.py` to the `Homework 2: Code Submission` Gradescope assignment. The code that you upload to Gradescope will be graded using an autograder. This autograder will consist of public test cases, the results of which are visible upon each submission, and private test cases, the results of which will only be visible after the final deadline for the assignment. Your code will be tested private datasets in addition to the datasets you are given, and as such, your code should be properly generalizable to other, similar data. Your programming implementation will be graded on correctness as well as efficiency. You can submit your code to the autograder as many times as you wish. You are free to work as a group on this assignment, but you must write your responses and code individually.

## Introduction: The NYC Taxicab Database
The New York Freedom of Information Law (FOIL) grants any member of the public the ability to access, upon request, any records maintained by state governmental agencies. One such state agency is the  New York City Taxi and Limo Commission (NYC TLC), which manages all public taxis within the metropolitan area. In 2013, Data analyst Chris Whong submitted a FOIL request to the NYC TLC and was in turn provided with a database containing full records of every taxi ride given in New York City that year. Chris Whong then published this data in its entirety. Due to the public nature of the NYC taxi system, along with the poor de-anonymization of the database done by NYC officials, this database is ultimately highly vulnerable to a linkage attack with wide-reaching implications.

For this assignment, you will perform a real linkage attack on this dataset by using public photos captured by paparazzi documenting celebrities boarding NYC taxi cabs.

## Part 1: Creating a linkage attack

A linkage attack is an attempt to re-identify individuals in an anonymized dataset by identifying overlaps with publicly available information.

For this assignment, you will be provided access to a lightly modified version of the original 2013 NYC TLC database as is was provided to Chris Whong. In addition, you will be provided with another publicly available NYC TLC dataset which  with photographs taken by NYC paparazzi of celebrities boarding taxi cabs and the dates these photos were taken. Your task will be to perform a linkage attack using these datasets to match celebrity photographs with trips in the taxi database, aggregating information on celebrity tipping habits. Following this, you will use a differential privacy technique to propose a method for re-privatizing this data.

City officials had attempted to anonymize certain identifying details associated with every ride -- namely the medallion number, an alphanumeric code assigned to each taxi cab in operation, and the hack license number, which is assigned to drivers authorized to operate a yellow taxi. They did so, however, by running both sets of numbers through a notoriously weak cryptographic algorithm known as MD5.

Hashing is the process of transforming one string of characters into another. Hashes are stable, in the sense that performing a given hash on the same string twice will always produce the same output. A hash is designed to be easy to compute in one direction, but difficult to compute in the other direction. MD5 works by taking any input, like a string of text, and outputting a 32-character alphanumeric string. An MD5 hash is reversible in the case where the original strings follow a specific format, such as with New York City medallion numbers. In this case, it is possible to reverse the hash via brute force by hashing every possible input with MD5 and finding the match with the hashed data point in question.

New York City medallion numbers follow one of three very particular formats:
 * One number, one letter, two numbers. For example: 5X55
 * Two letters, three numbers. For example: XX555
 * Three letters, three numbers. For example: XXX555

As such, it is possible to deanonymize all medallion numbers in this dataset. Without information on which passengers took which taxis at which times, however, the other data in the dataset has little application. As such, we introduce our celebrity photo database. Paparazzi photographers in New York City frequently capture celebrities entering or exiting yellow taxi cabs, and that many of their pictures depicted the cab’s unique medallion number. The number is prominently displayed on the car’s exterior: In lit letters on top, in black paint on the side, and on both license plates. With this information, it is possible to assign a name and face to a trip in this dataset, matching a celebrity with the trip's pickup and drop-off locations, the amount of the fare, and the tip each celebrity paid their driver.

Your task will be to reverse the hashes within the NYC database to link these photos of celebrities to taxi trips in the database, thereby fully deanonymizing those trips. Create a method to link this data and output a list of fully deanonymized trips using these databases. In addition, implement a function to return the average tip amount in the database, as well as a function to return the top ten celebrity tippers using your linked data.

Note that the data given to you in this assignment is closely based on real-world data, but has been altered in the interest of convenience and privacy.

### Trip Data
The original NYC dataset consists of hundreds of thousands of lines. You will be given a shortened version of this dataset with 1000 lines, with some data edited for convenience and privacy. Each row in this dataset represents one trip made by a NYC taxi. The columns of this dataset are are follows:

* `medallion`: The medallion number on the taxi cab. Hashed with MD5.
* `hack_license`: The hack license number of the taxi driver. Hashed with MD5.
* `date`: The date of the trip. Follows YYYY-MM-DD format.
* `payment_type`: The payment method used by the passenger. `CSH` for cash and `CRD` for credit card.
* `fare_amount`: The fare for the trip in USD.
* `tip_amount`: The tip, in USD, given to the driver by the passenger.
* `pickup_location`: The full latitude and longitude, in that order, of the starting location for the trip.
* `dropoff_location`: The full latitude and longitude, in that order, of the trip destination.

The medallion number is used to identify the taxi cab and appears on the license plate of the taxi, the side of the taxi, and atop the taxi. The medallion number follows a specific format, and is composed of one number, followed by one letter, followed by two numbers, e.g.: `1A23`.

A hack license is a form of identification and licensure for taxi drivers in NYC. The number on each driver's hack license is 7 numerical digits long, e.g. `1234567`.

### Celebrity Data
You are given a `.zip` file containing several dozen photos of celebrities spotted in taxis around NYC. The filename of each photo lists the name of the celebrity or celebrities in the photo, along with the date the photo was taken (in `YYYY-MM-DD` format).

As part of your task, you will need to create your own dataset (stored as a `.csv` file) containing the information in these photos. This dataset should contain the name of the celebrity (or celebrities) in each photo, along with the medallion number present in the photo and the date the photo was taken. The structure for this dataset is ultimately up to you, as this file will not be graded, and is only for your own use in this assignment. You will need to manually identify and transcribe the medallion numbers from each photo into this database. If you cannot identify these medallions yourself due to visual impairment, please reach out to a member of the course staff, and we can provide you with a list of the medallion numbers in each photo.

### Driver Data
The City of New York currently hosts publicly accessible databases listing all current licensed taxi drivers, along with their hack license number. With this information, you will be able to identify not only the passengers in select trips, but the names of the drivers themselves as well. Each row represents a registered NYC taxi driver, and the columns are as follows:

* `hack_license`: The hack license number of the taxi driver.
* `name`: The name of the driver.


### hw2.py
You are given a starter file off of which you should base your implementation.

* `Celebrity`:

* `Driver`:

* `Trip`:

* `HackLicenseDecoder`:

* `MedallionDecoder`:

* `process_drivers`:

* `process_drivers`:

* `linkToTravelCSV`:

* `get_mean_tip`: Given the path to the trip database and a range of dates, this function returns the average tip across all trips in the database occurring during that date range.

### Reflection

Answer the following short-response questions:

1. Report, in descending order, the five celebrities who tipped the highest amount, along with the amount each celebrity tipped. For cases in which you have information on more than one trip made by a given celebrity, take the average of all tips that celebrity made.

2. Use your implementation of the `get_mean_tip` method to find the average tip for all rides in the NYC database (not just those with celebrities). Do the same for all trips occurring between July 1st and August 1st, 2013. Report those values here.

3. Why is the release of this data socially relevant, and what are the social harms introduced by this linkage attack?

4. The information in this database, both alone and in aggregate, can be very revealing with regards to the lives of the deanonymized individuals associated with each trip. Find a trip for which you know the name of both the passenger and the driver. Use Google Maps to identify the NYC addresses associated with the latitudes and longitudes listed with this trip. List this information and, like a member of the paparazzi, speculate what the purpose of this trip may have been.

5. Why did the linkage attack succeed here? How could it have been prevented?

6. How do the celebrity images and NYC dataset each uniquely represent a breach of privacy? What does privacy mean in each case?

7. Do these celebrity images constitute a form of surveillance? Describe how they does or does not meet the criteria for surveillance. If you deem that they are surveillance, describe what kind of surveillance they are.

8. Is the data surveillance in the NYC database a form of surveillance? Describe how it does or does not meet the criteria for surveillance. If you deem that it is surveillance, describe what kind of surveillance it is.

9. As it turns out, the full NYC database misreports tip amounts for many rides paid with cash as $0, leading some outlets to incorrectly report that certain celebrities commonly tipped $0. What are the potential harms when a trusted organization releases incomplete information such as this?

10. Identify and describe another way that this dataset could be used to uncover information not previously in the public domain. What might the harms of this be?

11. What should have been released by the NYC Taxi and Limousine Commission? How should the public be able to access it? Is this in line with Freedom of Information Law? If not, how should the law be changed to accommodate private data release?


## Part 2: Applying Differential Privacy
Refer to the `get_mean_tip` method you wrote for the previous section. Consider an alternative approach in which NYC hosts a live-updating version of this database online, and rather than letting users interact directly with the database, allows users to probe the database with queries similar to the one you created in this function. This approach would still introduce some privacy flaws, however, because if one knows the exact time that an individual took a taxi ride, one could query for the average tip directly before and directly after their trip to find the exact tip that individual left. A differentially private implementation of this query, on the other hand, would guarantee the protection of all individuals in the data. Laplace mechanism is robust enough to effectively ensure that the noise obfuscates any actual difference in the data. One differentially private approach is to use the Laplace mechanism to add noise to the result of this query, thereby making difference caused by the inclusion of one individual less pronounced. As such, the Laplace mechanism is robust enough to effectively ensure that the noise obfuscates any actual difference in the data. In this section, your task will be to write a differentially private implementation of the `get_mean_tip` method using the Laplace mechanism and reflect on the results.

The tip amount column in this database represents a continuous datapoint rather than a discrete datapoint, and as such, a slightly modified approach to the Laplace mechanism should be used. To return a Laplace smoothed mean for continuous data, you will need the portion of the data over which  (in this case, the tips between two given dates), along with an epsilon value. The procedure for calculating the noised result is as follows:

* Calculate the sensitivity. The sensitivity is given by the ratio of the range and the size of the data.
* Calculate the scale. The scale is found by dividing the sensitivity by epsilon.
* Use the Numpy `random.laplace` method to construct a Laplace distribution with these values.
* Sample a value from this distribution and add it to the original mean, yielding the noised version to the query.

The outline of the `get_dp_mean_tip` method is given to you in the starter file for this assignment. This function should accept the following arguments:

* `trip_csv_path`: the filepath to the NYC trip database.
* `start_date`: the lower-bound date for the search. Follows YYYY-MM-DD format.
* `end_date`: the upper-bound date (inclusive) for the search. Follows YYYY-MM-DD format.
* `epsilon`: the epsilon value for the Laplace distribution. The default value should be 0.1.

Your function should return a noised version of the query from your original `get_mean_tip` method. Your implementation will be tested for accuracy and to ensure that it is differentially private.

### Reflection

Answer the following short-response questions:

12. What effect would increasing or lowering epsilon have on the privacy and interpretability of the results?

13. What problems with the original release does this differentially private implementation solve? What problems with the original release does it not solve?

14. Not all values in this dataset are as easy to query in a differentially private way as those involving dollar amounts. What might be some of the challenges or roadblocks associated with implementing a differentially private solution to queries involving location (with latitude and longitude)? What strategies could be used to overcome these challenges?
