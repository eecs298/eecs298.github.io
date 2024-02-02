---
layout: spec
title: Lab 2
sitemapOrder: 20
---

Lab 3
==========================
{: .primer-spec-toc-ignore }

## Task
We are going to be exploring the ethical idea of **utilitarianism** in this lab and specifically how changing the definition of your utility function can change the outcome of a decision. At a high level, the utility function is a measure of how much satisfaction an agent gets from a particular outcome.  

You and four of your friends are deciding where to eat dinner in Ann Arbor. You have narrowed down the list to three restaurants: Cafe Zola, Frita Batido's, and Tomokun. At this point, you each rank how much you want to go to each resaurant where `3` is your top choice and `1` is your bottom choice. These choices are stored in `friends.csv`. 

### `friends.csv`
Download the `friends.csv` file using the following command.
```
wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/friends.csv
```
This file contains four columns: `Person`, `CafeZola`, `Fritos`, `Tomokun`. The `Person` column contains an ID for each friend and the other columns contains that friend's ranking for the restaurant according to the scheme above.

### `lab3.py`
Create a file named `lab3.py` in the same folder as the `friends.csv` file. Your task will be to choose a restaurant for the group using two different definitions of utility. First, read in the `friends.csv` file using the `csv` package and create a `dict` object where the  `key` is the name ofeach restaurant and the `value` is a `list` of ranking values for that restaurant. Remember that `csv` reads in data as type `str`, so cast the ranking values to `int` when you read them in so that we can compute the utility later on.

Next, create a function named `choose_restaurant` that takes in the `dict` object you created above and a keyword argument `utility_function` which is a `str` that specifies which utility definition you should use in choosing a restaurant. The two definitions we will use are

- `utility_function="sum"`: Here, each friend gets utility equal to their ranking choice number for a restaurant choice. Then, the total utility for a restaurant choice is the sum of all the ranking values for that restaurant. Hint: use the built-in Python function `sum()`. 
- `utility_function="top_choice"`: Here, each friend gets utility of 1 if their top choice is picked and 0 otherwise. Then, the total utility for a restaurant choice is the total number of ranking values equal to `3` for that restaurant.
- For any other input to the keyword `utility_function`, return `Invalid utility function: utility_function`

Using this function, print out the top restaurant choice and utility value for each utility definition and the output you get when you pass in `utility_function="other"`. Your output should be formatted as below.

```output
Restaurant choice: XX, utility function: sum, value: XX
Restaurant choice: XX, utility function: top_choice, value: XX
Invalid utility function: other
```

## Tips

### Type casting
Python is a dynamically typed language, which means that the type of any variable will be determined during runtime. As such, you do not need to specify the type of a variable when you instantiate it. You still need to keep track of a variable's type, though, as certain operations or functions will still require certain types. To cast a variable, use the built-in functions:
```python
num = 123
num = str(num) # "123"
num = int(num) # 123
num = float(num) # 123.0
num = bool(num) # True
```

You can also the Python built-in functions `type` and `isinstance` to return the type of an object and determine if an object is of a certain type, respectively.

```python

num = 123
type(num) # <class 'int'>
num = str(num)
isinstance(num, int) # False
isinstance(num, str) # True
```

### String formating
When printing out values of variables in your Python program, it is helpful to use string formatting. If you put `f` before the `""` in a string definition, then you can include variable names inside `{}` in the string definition to include their values. See the example below.

```python

num = 298
string = "EECS"

formatted_string = f"Welcome to {string} {num}!"
print(formatted_string) # Welcome to EECS 298
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

Find the sum and length of a list using `sum()` and `len()`. 
```python
my_list = [1, 3, 5, 7, 9]
sum(my_list) # 25
len(my_list) # 5
```

### Conditionals
We can use conditionals statements similar to how you would in `C++`. Consider the following comparison examples. 

```C

if(condition1) {
    // Do stuff
}
else if(condition2 && condition3){
    // Do stuff
}
else{
    // Do stuff
}
```

is equivalent to:
```python
if condition1:
    # Do stuff
elif condition2 and condition3:
    # Do stuff
else:
    # Do stuff
```

### Iterables and loops
One python data type is the `Iterable`. This type is inherited by `list`s, `tuple`s, and many others. A type that inherits from the `Iterable` type can be used as an iterator in `for` loops. For example:

```python
my_list = [123, 456, 789]
for item in my_list:
  # Do stuff
```

The dict.keys() and dict.values() functions used in previous labs each return an object of the `Iterable` type. As such, they can be iterated through in `for` loops. You may have noticed that they are not actually lists, and thus cannot be used with list operators, unless explicitly cast to a list with `list(dict.keys())`.

You can use the `range(n)` function to create an `Iterable` over the natural numbers from `0` through `n-1`. With this you can construct `for` loops similar to those you would see in `C++`. For example:

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

You can also use two built-in functions `enumerate(Iterable)` and `zip(Iterable1,Iterable2,...)` to loop over an `Iterable` in a special way. See below.

```python

myList1 = ["a","b","c"]
myList2 = [1,2,3]

for i, l1 in enumerate(myList1):
    print("Index:",i, "Value:",l1) 

for l1,l2 in zip(myList1, myList2):
    print("Value 1:", l1, "Value 2:", l2)  
```
You would get the output
```output
Index: 0 Value: a
Index: 1 Value: b
Index: 2 Value: c
Value 1: a Value2: 1
Value 1: b Value2: 2
Value 1: c Value2: 3
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

### List comprehension
You can create new `list`s using `Iterable`s and `for` loops using something called list comprehension. See below for an example.
```python

myList = [1,2,3]

myNewList = [element*2 for element in myList] # [2,4,6]
``` 

You can also include conditionals in the list comprehension to include only certain elements or apply operations to only some of the elements in the original `Iterable`. Note the difference in position of the `if` statement depending on whether an `else` statement is included or not.

```python
myList = [1,2,3]

myNewList = [element if element == 2 else element**2 for element in myList] # [1,2,9]
myNewList2 = [element for element in myList if element == 2] # [2]
```
