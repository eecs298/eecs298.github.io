---
layout: spec
title: Lab 4
sitemapOrder: 20
---

Lab 4
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will continue your role as a professor processing final grades for a course. You will write a program to take student names and grades via user input, then calculate information about the grading curve and the students' letter grades. In this lab, you will recieve an introduction to the Tuple data structure as well as Python input validation. You will also build your intuition for iterators and loops.

### lab4.py
Create a file titled `lab4.py`.

In this file, create a loop to gather student names and grades via console user input. First, ask the user for the number of students in the course. Then, for each student in the course, prompt the user to enter the student's first and last name in the format `Firstname Lastname` on one line, then the student's grade percentage as a number (with any number of decimals) on another line. If the user does not properly capitalize the student's name, capitalize the first letter of the first/last names for them. If the user types `END` instead of the full name for any student, then the entire input loop should end early. The input loop should look something like this:

```console
Enter the course size:
> 10

Enter student 1 name:
> John Doe

Enter student 1 grade percentage:
> 89.99

Enter student 2 name:
```

And so on. Store each student's name as a Tuple of the form (Lastname, Firstname). Create a dictionary with these tuples as keys and the matching scores as values. You can debug and test this input loop with whatever input you like, but you will need to consider any edge cases and handle input validation accordingly. For example, you will need to ensure that the user-entered name for each student contains only one first name and one last name (so that the full name is hence only two words long), unless the user types `END` to end the input loop early. You will also need to ensure that the amount entered for the grade percentage on every line is a valid number and between 0 and 100.

Next, you will need to calculate the curve for the course. To do so, you can find the percentage-point difference between the highest grade in the course and a full 100%, then add that difference to each student's score. For example, if the highest grade in the course is 89.5%, then the curve will be 10.5%. (and each student will recieve 10.5% added to their grade.)

Next, create a function will the following signature:
```python
def calculateLetterGrades(score, curve):
```

This function should take one student's score as input, as well as the curve you calculated for the course. This function should then calculate their letter grade from both before and after the curve is applied, and return both letter grades as a Tuple. The letter grades should be assigned as follows:

```
97%  <=  A+ <= 100%
93%  <=  A   <  97%
90%  <=  A-  <  93%
87%  <=  B+  <  90%
83%  <=  B   <  87%
80%  <=  B-  <  83%
77%  <=  C+  <  80%
73%  <=  C   <  77%
70%  <=  C-  <  73%
67%  <=  D+  <  70%
63%  <=  D   <  67%
60%  <=  D-  <  63%
 0%  <=  F   <  60%
```

For example, if the student's final grade is 87.5% and the curve is 3.0%, then the function call `calculateLetterGrades(87.5, 3.0)` should return the following Tuple: `("B+", "A-")`.

Next, iterate through the students in the course alphabetically (first by last name, then first name if any last names are the same) and print their full name, followed by their letter grade before the curve, then their letter grade after the curve. Finally, print the number of students in the course, followed by the number of students whose letter grade was changed by the curve. Your input should look like the following:

```console
Firstname1 Lastname1: A -> A+
Firstname2 Lastname2: B+ -> B+
Firstname3 Lastname3: F -> D-

...

Number of students in the course: 15
Number of students with grades changed from curve: 11
```

## Tips
### Tuples
Tuples are a powerful datatype akin to a more efficient List, with the difference being that Tuples are immutable and hashable. Since Tuples are hashable, they, unlike Lists, can be used as keys to a dictionary. Read more about Tuples [here](https://www.py4e.com/html3/10-tuples).

To create a Tuple:
```python
my_tuple = (val1, val2)
my_tuple_2 = (val3, val4, val5, val6)

my_tuple[0] # val1

# Tuples are immutable, so you cannot change its values or
# add values once created, e.g. with my_tuple[0] = val7
```

Tuples can be used to make a function return multiple values:
```python
myFunc():
  # Do stuff
  return val1, val2, val3


tuple_result = myFunc() # assign the result to a tuple
result1, result2, result3 = myFunc() # assign the result to different variables
```

Tuples, unlike lists, are comparable using inequality operators. First, the first item in the Tuples are compared. If these are equal, then the next items in the Tuples are compared, and so on.
```python
(3,5) < (4,5) # True
(3,5) < (3,4) # False

("Apple", "Banana") < ("Apple", "Pear") # True, since Banana comes before Pear in the dictionary
```

The `dict.items()` function returns an Iterable of Tuples of each key-value pair:
```python
my_dict.items() # [(key1, value1), (key2, value2), (key3, value3), (key4, value4)]
```

### Iterables and loops
One python data type is the `Iterable`. This type is inherited by Lists, Tuples, and many others. A type that inherits from the `Iterable` type can be used as an iterator in `for` loops. For example:

```python
my_list = [123, 456, 789]
for item in my_list:
  # Do stuff
```

The dict.keys() and dict.values() functions used in previous labs each return an object of the `Iterable` type. As such, they can be iterated through in `for` loops. You may have noticed that they are not actually lists, and thus cannot be used with list operators, unless explicitly cast to a list with `list(dict.keys())`.

You can use the range(n) function to create an `Iterable` over the natural numbers from `0` through `n-1`. With this you can construct `for` loops similar to those you would see in `C` languages. For example:

```C
for(int i = 0; i < n; i++){
  // Do stuff
}
```

is equivalent to:

```
for i in range(n):
  # Do stuff
```

Another loop type `while`. This loop will continue as long as the conditional in the loop header evaluates to `True`.

```python
while my_boolean: # Will continue as long as my_boolean is True
  # Do stuff
```

Other tools you can use while constructing loops are the `continue` and `break` keywords. In a `for` or `while` loop, the `continue` keyword will skip to the next pass through the loop, starting at the top of the loop. The `break` keyword will end the entire loop early.

```python
for thing in other_thing:
  # Do stuff
  if certain_condition:
    continue # Skips to the next thing in other_thing
  else if other_condition:
    break # Ends the entire loop and moves on

  # Do other stuff -- this code will only run if neither continue or break are called.
```

### Input
To prompt the user for console input, use the `input()` function. The program will pause until the user hits the return key in the console, and then the function will return the user's input as a string.

### Error handling
Especially when dealing with user input, one might wish to handle potential errors arising in code. Since Python is a dynamically typed language, one example of such a case is handling when one's code attempts to cast a variable to a type that it cannot be cast to. You can handle these situations with `try` and `except` blocks as shown:

```python
try:
  val = "ABC"
  int_val = int(val) # This line will throw a ValueError exception.

except ValueError: # Handle the ValueError exception explicitly
  # Do stuff

except: # Handle all other exceptions
  # Do stuff
```
