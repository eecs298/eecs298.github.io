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
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/numbers.txt
```

Take a look at the file you downloaded. Our goal today will be to read the values from this file in Python, then use the `numpy` library to find the average of those values. To continue, open `lab1.py` with your editor of choice.

First, import the `numpy` library. We can optionally rename this library for ease of use within the scope of this program with the `as` keyword.

```
import numpy as np
```

To import our text file, we can use the built-in `open` function.

```
f = open("numbers.txt", "r")
```

Next, create an empty Python `list`. Python `list`s are dynamically allocated, so we do not need to specify the size.

```
numbers = []
```

We can loop through each line in our file as follows. Python is a dynamically typed language, so although we do not specify it, these lines will come to us as `String` objects. When we use `numpy` to take the mean of these numbers, it will want a `list` of `int`s, so we can cast each line to an `int` before adding it to our list with `append`.

```
for line in f:
    num = int(line)
    numbers.append(num)
```

We can then check out our list of numbers by printing out the contents as follows:

```
print("Contents:", numbers)
```

And, finally, we can compute the mean of our list by calling `numpy`'s `np.mean` function on our list and casting that result to an `int`, then printing the result:
```
mean = int(np.mean(numbers))
print("Welcome to EECS", mean)
```

Run your file and check the output:
```console
$ python3 lab1.py
```

Next, rerun the file and use the `>` operator to pipe the output into a new file called `results.txt`.
```console
$ python3 lab1.py > results.txt
```

To mark your completion of the lab, turn in `results.txt` on Canvas.
