---
layout: spec
title: Lab 2
sitemapOrder: 20
---

Lab 2
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will play the role of an IT intern at MyHealth, a large new hospital in Ann Arbor. The company recently hired and is currently onboarding five prestigious surgeons from out-of-state, and you have been asked to write a Python program to automate generating the new doctors' employee information.

For each doctor, you will need to create their company email. Each company email should adhere to the following format: first letter of first name + last name + PID + @myhealth.org.

### doctors.csv
The `doctors.csv` file contains a `FirstName`, `LastName`, `Department`, and `PID` of five doctors. Using the `wget` command, download the `doctors.csv` file.
```console
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/doctors.csv
```

### lab2.py
Create a file titled `lab2.py`. In this file, perform the following:

* `import` the `csv` package at the top of the file.
* Define a `Doctor` class with attributes for first name, last name, department, PID, and email address. The first name, last name, department, and PID are passed in as arguments to the `__init__()` constructor and you will set the email address yourself according to the specifications above.
* Override the less than operator, which has the function header `__lt__(self, other)`, to compare the PID of two `Doctor` objects.
* Override the greater than operator, which has the function header `__gt__(self, other)`, to compare the PID of two `Doctor` objects.

* In the `__main__` branch, load and read `doctors.csv` using the `open` built-in Python function and the function `reader()` from the `csv` package. Create a `Doctor` object for each doctor in the file. Add these `Doctor` objects to a `list`.
* Use the Python function `sorted()` to sort the `list` from low to high `PID`.
* Create a `dict` and add the doctors to the dictionary using department as the key and a `list` of emails of doctors in the department in order of low to high PID as the value. Hint: use the ordering from the sorted list above!
* Print out the key/value pairs from the `dict` as follows:

```console
Department1:[email1, email2]
...
```

Turn in `lab2.py` on Gradescope.

## Tips

### Lists
Python lists are the most common data structure used, and function like souped-up C arrays. Note that they support items of different types.
```python
mylist = []

mylist.append(123)
mylist.append("abc")
mylist.append(456)
mylist.append("def")

print(mylist[0]) # 123
print(mylist[:2]) # [123,"abc"]
```

### Python dictionaries
The `dict` object in Python is a built-in data structure. A dictionary can be thought of as a generalization of a list that is indexable by any object, rather than only an `int`. More formally, dictionaries contain key/value pairs. Indexing a dictionary by its key returns the matching value. See usage below:
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

### String slicing
Python string syntax provides powerful tools to index and "slice" strings. See below:
```python
s = "abcdef"

print(s[0]) # The first char: "a"
print(s[-1]) # The last char: "f"

print(s[1:3]) # From the 2nd char to the fourth char (non-inclusive): "bc"
print(s[2:]) # From the 3rd char to the end: "cdef"
print(s[:-2]) # From the beginning to the second-to-last char (non-inclusive), "abcd"
```

### CSV `reader()` function
The `reader()` function in the `csv` package is used to read in information from a `csv` file. The `reader()` function returns an iterable where each element in the iterable is the next line of the `csv` file represented as a list of `str`s when you split the line by commas. For example, suppose you have a file called `file.csv` that contains two lines of information
```
1,2,3
a,b,c
```
Then, you can use the `reader()` function as follows. Note that all information (including numbers!) is read in as `str`s.
```python
import csv

with open("file.csv","r") as file: # The 'with' keyword defines the scope where "file.csv" is open and automatically closes it out of scope.
    data = csv.reader(file)
    for row in data: # for loop in Python -- 'data' is an iterable and 'row' is a holder variable for each element in 'data'
        print(row) # first prints ["1","2","3"] then prints ["a","b","c"]
```


### Python `sorted()` function
The Python `sorted()` function takes an iterable (like a `list`) as input and returns a sorted version of the iterable. There are two optional keyword arguments. (1) `key` is a function that is run on each element of the iterable before comparisons are made between elements to sort the iterable. You can use the Python keyword `lambda` to write a simple function that takes as input a single argument representing the element in the iterable and returns to the `sorted()` function an new element to sort by. (2) `reverse` is default `False` and indicates whether the order of the sorted elements should be reversed or not at the end. The default sorting is `A-Za-z` for `str`s and low to high for `int`s.

```python

myList = [5,4,1,7,9]
print(sorted(myList)) # [1,4,5,7,9]
print(sorted(myList, reverse=True)) # [9,7,5,4,1]

myList2 = [(1,"banana"),(2,"apple")]
print(sorted(myList, key = lambda element: element[0])) # [(1,"banana"),(2,"apple")], sorting according to the first element of each tuple
print(sorted(myList, key = lambda element: element[1])) # [(2,"apple"),(1,"banana")], sorting according to the second element of each tuple
```



### Overriding functions
Any method within a parent class can be overridden in a child of that class. When writing the constructor, you actually override the default constructor of the `Object` class, from which every class inherits. You can do the same with other methods belonging to parent classes, for example the ` __le__(self, other)` method, which is automatically called whenever two objects from the same class are compared by `<=`.
```python

class MyClass:

    def __init__(self, attribute_1, attribute_2):
        self.att1 = attribute_1
        self.att2 = attribute_2

    def __le__(self, other):
        return self.att1 <= other.att1

if __name__ == "__main__":
    obj1 = MyClass(1,6)
    obj2 = MyClass(5,2)

    print(obj1<=obj2) # prints True

```
