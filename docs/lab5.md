---
layout: spec
title: Lab 4
sitemapOrder: 20
---

Lab 5
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will work with a dataset of product sales at a clothing store to report the average price of each product over different time periods.

### lab5.py
First download the dataset you will use for this lab, `sales.csv`:
```
wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/sales.csv
```

Next, create a file named `lab5.py` in the same folder as `sales.csv`. In this file, first `import` `csv` and `datetime` using the following code. The `from` keyword is used to import a specific `function` from a package, both named `datetime` in this case.
```python3
import csv
from datetime import datetime
```

There are three types of products in `sales.csv`: `"t-shirt"`, `"jeans"`, and `"sweater"` and each line in the `csv` represents a sale of one of the products and the corresponding `date` and `price` of the purchase. When you read in the data, you will create a `dictionary` where each key is one of the products and the value is a list of purchases associated with that product. The purchases will be stored as `tuple`s in the format of `(date, price)` where `date` is a string in the format of `YYYY-MM-DD` and `price` is a `float`.

You will implement one function `get_average_price(start_date: str, end_date: str, product_list: list[tuple])` that you will use to calculate the average price for a list of products in the `__main__` branch.

* `get_average_price`: Calculates the average price of a list of products within the given date range.
    * Arguments
        - `start_date`: A `string` for the start of the date range to calculate the average in. In `YYYY-MM-DD` format.
        - `end_date`: A `string` for the end of the date range to calculate the average in. In `YYYY-MM-DD` format.
        - `product_list`: A `list` of product `tuple`s formatted as `(date, price)`.
    * Returns
        - The average price of products purchased between the `start_date` and `end_date` (inclusive).
    * Hint
        - Use `datetime.strptime(date_string,"%Y-%m-%d")` to create a `datetime` object out of a date given as a `string` so that you can check if a date is in the given range with `<=` and `>=` operators.
* `__main__`: Perform the following tasks in the `__main__` branch.
    * Read in the `csv` data and store it in a `dictionary` described above.
    * Print out the result of three queries to `get_average_price`
        - Get the average price of `jeans` in December 2023.
        - Get the average price of `sweater`s in January 2024.
        - Get the average price of `t-shirt`s in December 2023 thru January 2024.
    * Try to use `**kwargs` to pass in the different queries to `get_average_price`!
    * The output of running `python3 lab5.py` should be
    ```output
    Average price of jeans in December: 42.37428571428571
    Average price of sweaters in January: 53.193333333333335
    Average price of tshirts in December and January: 30.718888888888884
    ```

Submit `lab5.py` to Gradescope when you're done.

## Tips

### Tuples
`tuple`s are a powerful datatype akin to a more efficient `list`, with the difference being that `tuple`s are immutable and hashable. Since `tuple`s are hashable, they, unlike `list`s, can be used as keys to a `dictionary`. Read more about `tuple`s [here](https://www.py4e.com/html3/10-tuples).

To create a Tuple:
```python3
my_tuple = (123, "ABC")
my_tuple_2 = ("Hello", "World", 298, True)

my_tuple[0] # 123

# Tuples are immutable, so you cannot change its values or
# add values once created, e.g. my_tuple[0] = 456 does not work
```

### *args and **kwargs
The `*args` and `**kwargs` operators can be used to unpack `list`s and `dict`s, respectively, and are typically used to define functions with variable length inputs and pass values into functions. See the examples below.

```python3

def variable_length_args_function(*args):
    for arg in args: # args is a tuple of values
        # Do stuff with args

def variable_length_kwargs_function(**kwargs):
    for key,value in kwargs.items(): # kwargs is a dictionary of key/values
        # Do stuff with key,values

def my_func(input1: str, input2: int, input3: bool):
    print(input1, input2, input3)

# Using *args operator
message = ["EECS",298,True]
my_func(*message) # prints out: EECS 298 True

# Using **kwargs operator
message = {"input1": "EECS", "input2":298, "input3":True}
my_func(**message) # prints out: EECS 298 True
```

### `datetime.strptime` Function
`datetime` is a package that has functions related to handling dates in python. The `datetime.strptime(date_string, format)` function takes as input a date given as a `string` and the format of the date (e.g., `YYYY-MM-DD` and you can find all the format codes [here](https://docs.python.org/3/library/datetime.html#format-codes)) and outputs the date as a `datetime` object such that you can make meaningful comparisons to other `datetime` objects.

```python3
from datetime import datetime

date1_string = "2023-12-01"
date2_string = "2024-01-15"
date3_string = "2024-02-16"

date1 = datetime.strptime(date1_string, format="%Y-%m-%d")
date2 = datetime.strptime(date2_string, format="%Y-%m-%d")
date3 = datetime.strptime(date3_string, format="%Y-%m-%d")

print(date1 <= date2) # True
print(date3 - date2) # datetime.timedelta(days=32)
```
