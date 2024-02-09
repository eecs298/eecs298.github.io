---
layout: spec
title: Lab 4
sitemapOrder: 20
---

Lab 4
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will take the role of a professor processing final grades for a course. You will write a program to take student names and grades via user input, then calculate information about the grading curve and the students' letter grades. In this lab, you will recieve an introduction to the Tuple data structure as well as Python input validation. You will also have practice implementing the randomized response mechanism to protect the students' grade privacy.

### lab4.py
First, download the files `grades.csv`, `input.txt`, `input_bad_key.txt`, and starter code `lab4.py` using the `wget` command:
```
wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/grades.csv
wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/input.txt
wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/input_bad_key.txt
wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/labs/lab4.py
```
In `grades.csv`, you will see grade and student ID information for 40 students. Information about each column is given in the constructor of the `SemesterGrade` class.

You will implement functions in two classes in `lab4.py`, `SemeseterGrade` and `StudentGrades`, as follows: 

* `SemesterGrade`: This class will hold the information for one student's semester grades. The constructor is implemented for you.
  * `calculate_semester_grade()`: Implement this function to calculate the weighted sum (using the given weights in the constructor) of the assignments. The weighted sum will be a number between 0 and 100 and is the numerical semester grade for the student. Use this number to return their letter grade  using the following scale:
  ```
  90%  <=  A   <=  100%
  80%  <=  B   <  90%
  70%  <=  C   <  80%
  60%  <=  D   <  70%
  0%  <=  F   <  60%
  ```

* `StudentGrades`: This class will hold all the grade information in the attribute `student_grades` as well as a function for querying student grade data.
  * `_read_student_grades(grades_file_path: str)`: Implement this function to read in the data from `grades.csv` and add it to the `student_grades` dictionary where the each key is a student ID and the corresponding value is a `SemesterGrade` object.
  * `query_student_grade_rr(student_id: str)`: Implement this function to return the semester grade of the given `student_id` while applying the randomized response differential privacy mechanism. 
      * First, you will perform **error handling** by raising two `Exception`s: (1) If `student_id == "Done"` (case sensitive), `raise` `Exception("End of queries.")` and (2) if `student_id` is not in the `self.student_grades` keys, `raise` `Exception("Student ID not found.")`. 
      * Next, you will implement **randomized response** to return the semester grade of the given `student_id`. Use `np.random.uniform()` to generate a random value and if that value is `>=0.5`, return the true student semester grade using `calculate_semester_grade()`. Otherwise, generate another random value and return the following letter grades for each range of the random value
      ``` 
      0.8 <= random_value <= 1 return "A"
      0.6 <= random_value < 0.8 return "B"
      0.4 <= random_value < 0.6 return "C"
      0.2 <= random_value < 0.4 return "D"
      0 <= random_value < 0.2 return "F"
      ```


In the main branch, you will first create a `StudentGrades` object and pass in the file path to `grades.csv`. Then, create a `while True` loop where you read in `student_id` inputs from the console with the following prompt (Hint: use the `input` function):
```console
Enter a student ID to return a semester grade:
> 
```
After reading in a `student_id`, call `query_student_grade_rr(student_id)` and print out the following output
```
Student ID: XXXXXX, Semester Grade: X
```
Wrap your code in a `try` block and `except Exception as e` and print out `e` and `break` the loop if an exception is rasied in `query_student_grade_rr(student_id)`. See the tips below for an example of handling exception in `try`/`except` blocks. 

### Example output
When running `lab4.py` on `input.txt` you should expect the following output:
```console
$ python3 lab4.py < input.txt
Enter a student ID to return a semester grade:
Student ID: 543584, Semester Grade: C
Enter a student ID to return a semester grade:
Student ID: 263174, Semester Grade: B
Enter a student ID to return a semester grade:
Student ID: 908486, Semester Grade: C
Enter a student ID to return a semester grade:
Student ID: 591245, Semester Grade: F
Enter a student ID to return a semester grade:
End of queries.
```

When running `lab4.py` on `input_bad_key.txt` you should expect the following output:
```console
$ python3 lab4.py < input_bad_key.txt
Enter a student ID to return a semester grade:
Student ID: 723068, Semester Grade: B
Enter a student ID to return a semester grade:
Student ID: 212583, Semester Grade: B
Enter a student ID to return a semester grade:
Student ID: 108978, Semester Grade: B
Enter a student ID to return a semester grade:
Student ID: 263174, Semester Grade: F
Enter a student ID to return a semester grade:
Student ID not found.
```

Turn in `lab4.py` to the Gradescope assignment when you're done.



## Tips

### Input
To prompt the user for console input, use the `input()` function. The program will pause until the user hits the return key in the console, and then the function will return the user's input as a string.


### Error handling and Exceptions
Especially when dealing with user input, one might wish to handle potential errors arising in code. Since Python is a dynamically typed language, one example of such a case is handling when one's code attempts to cast a variable to a type that it cannot be cast to. You can handle these situations with `try` and `except` blocks as shown:

```python

def a_function(arg1: str):

    if not isinstance(arg1, str):
        raise Exception("arg1 should be of type str")
    else:
      print(arg1)
if __name__ == "__main__":
    try:
        string = "ABC"

        a_function(string)  

    except Exception as e: # This code gets executed when an Exception is raised
        print(e) # Output: arg1 should be of type str
```

### `np.random.uniform()`
When using `numpy` functions, we first need to import `numpy` as follows
```python
import numpy as np
```
Recall that the `as` keyword lets us rename the import to use in our program.

We will use the `numpy` function `random.uniform()` to sample a point from the range `[0,1)` uniformly at random. We can then use that value to simulate probabalistic events like, say, a fair coin flip.

```python
import numpy as np

coin_toss = np.random.uniform() # generates a random float between 0 and 1

if coin_toss >= 0.5: # This happens 50% of the time 
    print("Heads")
else: # This happens 50% of the time
    print("Tails")
```
