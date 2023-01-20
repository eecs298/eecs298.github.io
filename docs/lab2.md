---
layout: spec
title: Lab 2
sitemapOrder: 20
---

Lab 2
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will play the role of an IT intern at MyHealth, a large new hospital in Ann Arbor. The company recently hired and is currently onboarding ten prestigious surgeons from out-of-state, and you have been asked to write a Python program to automate generating the new doctors' employee information.

For each doctor, you will need to generate a random 6-digit personal identification number (PID), as well as a company email. Each company email should adhere to the following format: first 4 digits of first name + first 4 digits of last name + last 2 digits of PID + @myhealth.org.

### doctors.txt
Create a file titled `doctors.txt`, containing the full names of ten doctors at the hospital, with one full name per line. Write these names yourself, but keep them appropriately realistic -- we will come back to these details in a future lecture.

### lab2.py
Create a file titled `lab2.py`. In this file, perform the following:

* Define a `Doctor` class with fields for name, PID, and email address.
* Define a `generateEmail` function which, given a name and PID, returns an email address as outlined above.
* Load and read `doctors.txt` using the method from last week's lab. Create a `Doctor` object for each name in the file, with the PID for each doctor randomly generated and the email address generated using the `generateEmail` function. Add these `Doctor` objects to a list.
* Iterate through this list, printing out the name, PID, and email of each doctor, as follows:

```
FirstName LastName, PID: 123456, email: FirsLast56@myhealth.org
...
```

Turn in `doctors.txt` and `lab2.py`.

## Tips
### Random integers
Generate a random integer as follows:
```
from random import randint

n = randint(a, b) # a ≤ n ≤ b
```

### Type casting
Python is a dynamically typed language, which means that the type of any variable will be determined during runtime. As such, you do not need to specify the type of a variable when you instantiate it. You still need to keep track of a variable's type, though, as certain operations or functions will still require certain types. To cast a variable, use the built-in functions:
```
num = 123
num = str(num) # "123"
num = int(num) # 123
num = float(num) # 123.0
```

### Lists
Python lists are the most common data structure used, and function like souped-up C arrays. Note that they support items of different types.
```
mylist = []

mylist.append(123)
mylist.append("abc")

print(mylist[0]) # 123
```

### String slicing
Python string syntax provides powerful tools to index and "slice" strings. See below:
```
s = "abcdef"

print(s[0]) # The first char: "a"
print(s[-1]) # The last char: "f"

print(s[1:3]) # From the 2nd char to the fourth char (non-inclusive): "bc"
print(s[2:]) # From the 3rd char to the end: "cdef"
print(s[:-2]) # From the beginning to the second-to-last char (non-inclusive), "abcd"
```

### String splitting
The `split()` function can be used to split a string into substrings. These substrings will be put into a list and split based on a given delimiter string. If none is given, the default delimiter is the space character.
```
tokens = "abc def".split() # tokens = ["abc", "def"]
```

### Defining a function
You can define a function in Python as follows:
```
def my_func(arg1, arg2):
  return arg1 + arg2
```

### Defining a class
Python is an object-oriented language. Create and instantiate a class as follows. The `__init__` function is called automatically whenever an object of that class is instantiated. You can get and set internal variables by referencing them explicitly, as shown below.  Note that functions of a class always include `self` in their signature, but this is never included when calling the function (it's passed in automatically).
```
class Test:
  def __init__(self, arg1, arg2):
    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = self.arg1 + self.arg2

  def test_func(self):
    return self.arg1 + self.arg2 == self.arg3

test_obj = Test(arg1, arg2)
num = test_obj.arg3
test_obj.arg1 = 0
test_obj.test_func() #this returns a Boolean
```

### Main branch
Python can be used purely as a scripting language, but if any functions or classes are defined, you'll need to define the main branch as follows. The body of this branch is what will run when you execute your program.
```
if __name__ == "__main__":
```

If you run into any issues, please ask questions.
