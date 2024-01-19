---
layout: spec
title: Lab 1
sitemapOrder: 20
---

Lab 1: Getting started with Python
==========================
{: .primer-spec-toc-ignore }

This lab is intended to provide a starting point for the Python development within this course, and is designed to be approachable from any experience level. Please feel free to ask questions as you progress through the lab.

## Setup
First, check out the Setup Tutorial section on the homepage of this site. If you are new to navigation with the command line, visit the [windows setup](setup_wsl.html) or [macOS setup](setup_macos.html), then review the [command line tutorial](setup_cli.html).

If you do not have an IDE set up for Python, I recommend you [set up VS Code](setup_vscode.html). If you are on Windows and/or plan to develop on multiple machines during this course (such as on both a laptop and a desktop), it may be most convenient for you to set up [remote development](setup_remote.html) on one of the U-M Linux servers. This will save you needing to perform setup on multiple machines.

Next, view the [python tutorial](setup_python.html) for steps on how to install python and setup a virtual environment for the course.

## Coding
Once you have completed the setup tutorials, navigate to your folder for the course and create a file named `lab1.py`.

From the terminal, ensure you are in the folder containing `lab1.py` and use the `wget` command to download the text file we'll use for I/O in today's lab:

```console
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/numbers.txt
```

Take a look at the file you downloaded. Our goal today will be to read the values from this file in Python, then use the `numpy` library to find the average of those values. We will create a `MeanCalculator` class with the appropriate functions to do the calculations. To continue, open `lab1.py` with your editor of choice.

First, import the `numpy` library. We can optionally rename this library for ease of use within the scope of this program with the `as` keyword.

```python
import numpy as np
```

Next, create the outline for our `MeanCalculator` class. We will need a constructor, a function to read in the numbers file, and a function to calculate and return the integer mean.

```python
class MeanCalculator:

    def __init__(self):
        pass

    def read_numbers(self, filename):
        pass

    def calculate_integer_mean(self):
        pass
```
We will first write the constructor function `__init__`. The only attribute we will need is a `list` to hold the numbers we read in from the file. We will call it `self.numbers` and initiate it as an empty `list`. Python `list`s are dynamically allocated, so we do not need to specify the size.

It is good practice to add `docstring comments` on all of your functions and classes. All starter code in homeworks and labs will have the same documentation style as seen in this lab. The documentation for the constructor function `__init__` will always describe the class it constructs and the other documentation comments will describe the purpose of the function they describe. After these short descriptions, `__init__` will include a list of `Attributes` of the class while all other functions will include a list of `Arguments` passed into the function (besides `self`), a list of which `Attributes` are `Modified`, and what the function `Returns`.

```python
def __init__(self):
    """The MeanCalculator class calculates the integer mean on a list of numbers.

    Attributes:
      self.numbers (List): a list to store numbers on which to calculate the mean.
    """
    self.numbers = []
```

Next, we will write the `read_numbers` function that reads numbers from the specified `filename`. To read from our text file, we can use the built-in Python `open` function. We can loop through the object `f` and get one line (everything before the `\n` character) at a time as follows. Python is a dynamically typed language, so although we do not specify it, these lines will come to us as `str` (string) objects. When we use `numpy` to take the mean of these numbers, it accepts a `list` of `int`s, so we can cast each line to an `int` before adding it to our list with `append`. After we finish, we `close` our text file to indicate to the system that we are done reading from it.

```python
def read_numbers(self, filename):
    """Function to read in a number file. Adds numbers from files to
    self.numbers cast as integers
    
    Arguments:
      filename (String): filename of .txt file to read numbers from
    Modifies:
      self.numbers
    Returns:
      None
    """
    
    f = open(filename, "r", encoding="utf-8")

    for line in f:
      num = int(line)
      self.numbers.append(num)

    f.close()
```
Finally, we will write the `calculate_integer_mean` function that calculates the mean of the given numbers and casts the result to an integer. We can compute the mean of our list by calling `numpy`'s `np.mean` function and return the result as an `int`.

```python
def calculate_integer_mean(self):
    """Calculates and returns mean of numbers in self.numbers cast as an integer.

    Arguments:
      None
    Modifies:
      None
    Returns:
      Integer mean of self.numbers
    """
    mean = int(np.mean(self.numbers))

    return mean
```

Now that we have implemented our full class, we can move to the `__main__` branch of our Python file to use the class. The body of this branch is what will run when you execute your program. To write code in this branch, we specify the following conditional.
```python
if __name__ == "__main__":
```

Here, we first need to construct an instance of our `MeanCalculator` class.
```python
if __name__ == "__main__":

    calculator = MeanCalculator()
```

Next, we can use the `read_numbers` member function to read from the `numbers.txt` file. Make sure your `numbers.txt` file is in the same directory as your `lab1.py`.

```python
if __name__ == "__main__":

    calculator = MeanCalculator()

    calculator.read_numbers("numbers.txt")

```

 We can then check out our list of numbers by printing out the contents as follows. Note that Python class variables are `public` by default, much like `structs` in C++!

```python
if __name__ == "__main__":

    calculator = MeanCalculator()

    calculator.read_numbers("numbers.txt")

    print("Contents:", calculator.numbers)
```

And, finally, we can compute the mean of our list by calling the `calculate_integer_mean` function as follows:

```python
if __name__ == "__main__":

    calculator = MeanCalculator()

    calculator.read_numbers("numbers.txt")

    print("Contents:", calculator.numbers)

    print("Welcome to EECS", calculator.calculate_integer_mean())
```


Run your file and check the output:
```console
$ python3 lab1.py
```

Next, turn in `lab1.py` on Gradescope. Once you pass the autograder, you are done with the lab!
