---
layout: spec
title: Lab 2
sitemapOrder: 20
---

Lab 3
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will assume the role of a course instructor. The semester has just concluded, and you wish to analyze student performance in your most recent course. You have access to a spreadsheet containing information on student grades for each assignment and exam. Your task is to write a Python script to process this spreadsheet and calculate statistics of interest relating to the students' grades.

Your course consisted of four homework assignments and two exams, each out of 100 points. The lowest homework grade for each student is dropped, and thus ignored in calculating their grade.

### grades.csv
For this lab, you will be processing information contained within `grades.csv`. Download this file with the following command:

```console
wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/grades.csv
```

Each row in the spreadsheet represents one student. There are seven columns: `Student ID`, `HW 1`, `HW 2`, `HW 3`, `Midterm`, `HW 4`, and `Final exam`. The `Student ID` column contains a 6-digit ID number, whereas each other column contains a score out of 100 for that particular assignment.

### lab3.py
Create a file titled `lab3.py`. In this file, read in `grades.csv`. You will need to report the following:

* The average final exam grade
* The average overall grade
* The IDs of the two students who got the highest overall grades in the course, along with their grades

Round each result to two decimal places. Remember to drop each student's lowest homework score when computing the overall grade for that student. Report your results as follows:

```console
Final exam average: XX.XX%
Overall average: XX.XX%
Highest grade: ID 123456, XX.XX%
Next highest grade: ID 456789, XX.XX%
```

Verify your output and turn in `lab3.py`.

## Tips
### Reading a csv
Read in a csv with the `csv` library:

```python
import csv

with open ('myfile.csv') as f:
  reader = csv.DictReader(f)
  for row in reader: # Iterates through each row in the spreadsheet

    # The row will be stored as a dict object.
    # Access the cells in this row by indexing the dict by column name.
    col1_value = row["Col1"] 
    col2_value = row["Col2"]
```

### Python dictionaries
The `dict` object in Python is a built-in data structure second only to `list` in ubiquity.  A dictionary can be thought of as a generalization of a list that is indexable by any object, rather than only an integer.More formally, dictionaries contain key/value pairs. Indexing a dictionary by its key returns the matching value. See usage below:

```python
my_dict = dict() 

# Add a key/value pair by indexing with any object and assigning a value
my_dict["Key 1"] = 10.0
my_dict["The next key"] = "Its value"
my_dict[15] = 0.0

my_dict.keys() # ["Key 1", "The next key", 15]
my_dict["Key 1"] # 10
my_dict # {"Key 1": 10, "The next key": "Its value", 15: 0.0}
```

### List operations
Find the minimum or maximum value in a list with the `min()` and `max()` functions.

```python
my_list = [4, 7, -2, 1, 3, 10]

min(my_list) # -2
max(my_list) # 10
```

Remove an item with a given value from a list with `list.remove()`.

```python
my_list = [10, 11, 12, 13]

my_list.remove(12)

my_list # [10, 11, 13]
```

Find the mean of a list using `numpy.mean()`
```python
import numpy

my_list = [1, 3, 5, 7, 9]
numpy.mean(my_list) # 5.0
```

### Rounding output
Convert a float into a string with a given number of decimal places with the `round()` function.

```python
num = 12.3456789

# Round to one decimal place
print(round(num, 3)) # 12.3

# Round to three decimal places
print(round(num, 3)) # 12.346
```