---
layout: spec
title: Lab 6
sitemapOrder: 20
---

Lab 6
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will be given a file called `lab6.py` which will have the implementation of a simple online shopping market and a simulated shopping session in the `__main__ ` branch. However, there are **two** errors in the implementation that you will have to debug to produce the correct output. One error will be related to a technical error that allows shoppers to spend more than they have and the other error is a violation of contextual integrity. In this context, we will assume that the *norms of appropriateness* are for shoppers to share their product preference with the store they buy something from and we will assume that the *norms of flow* are for stores to only advertise to shoppers who have *bought* something from *their* store before.

### lab6.py
Download the file`lab6.py` and the two `csv` files using `wget`.
```
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/labs/lab6.py
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/productsA.csv
$ wget https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/files/productsB.csv
```
The file `lab6.py` implements the `Shopper` class which represents an online shopper with a given budget and product preference looking to buy clothes from one of two clothing stores: `StoreA` and `StoreB`. `StoreA` and `StoreB` are two classes that inherit from the `Store` parent class. The `Store` parent class defines the basic store functionalities while the `StoreA` and `StoreB` child classes implement the specific advertising strategies of each store. Since this is a debugging exercise, it will be up to you to read through the code and comments in the code to figure out all the functionalities of the classes and how data is stored and transferred.

The two csv files, `productsA.csv` and `productsB.csv` contain the price of each product (`jeans`, `sweater`, and `t-shirt`) and the amount of each product in stock at `StoreA` and `StoreB`, respectively.

The `__main__` branch of `lab6.py` goes through a simulated shopping and advertising session. Run `python3 lab6.py` without modifying anything and inspect the outputs. You will notice that three of the shoppers end up with negative budgets! Further, you will notice that `StoreA` was able to successfully advertise to `shopper1`, `shopper3`, and `shopper4` even though those shoppers had not bought anything from `StoreA` yet, thus violating our assumed *norms of flow* in this context.  To be explicit, the errors you will need to correct are:
1. Do not allow a `Shopper` to add a product to their cart if the price of the new product exceeds their remaining budget and make sure to account for the total price in their current cart as well! 
2. Do not let any child classes of `Store` know the identities of active shoppers (those who have bought something) at other stores. Hint: See below for variable scopes in class inheritance.

To help with debugging this code, you will implement a **decorator** function as specfied below
* `_debug_advertised_shoppers(func)`: This function will create an inner function to print out the list of `Shopper`s that each store is advertising to before the store calls `advertise`. Note that this list of shoppers is stored in the `active_shoppers` variable. 
    * Implement the inner function which you can name anything you'd like.
    * Have the inner function accept `*args` as its parameter.
    * Print out the name of store you are displaying advertisees for: `print(f"Advertisees for {args[0].name}")`. Note that `args[0]` is `self` for class functions. 
    * Print out each shopper in `args[0].active_shoppers`
    * Call the passed in function with its arguments: `func(*args)`.
  * Return the inner function in the outer function
  * Decorate the `advertise` function of each child `Store`
  * See the Tips section below for examples of decorator functions if needed.

After you have corrected the two errors and implemented the decorator function, you should get the following correct output when you run `python3 lab6.py`
```output
Advertisees for StoreA
Advertisees for StoreB
Shopper 1, Remaining Budget: 63, Cart Contents: [('jeans', 33, 'StoreA')], Bought Items: [('jeans', 37, 'StoreB')]

Shopper 2, Remaining Budget: 0, Cart Contents: [], Bought Items: [('sweater', 50, 'StoreB')]

Shopper 3, Remaining Budget: 25, Cart Contents: [], Bought Items: [('t-shirt', 25, 'StoreB'), ('t-shirt', 25, 'StoreB')]

Shopper 3, Remaining Budget: 25, Cart Contents: [], Bought Items: [('t-shirt', 25, 'StoreB'), ('t-shirt', 25, 'StoreB')]

Shopper 4, Remaining Budget: 75, Cart Contents: [('t-shirt', 20, 'StoreA'), ('t-shirt', 20, 'StoreA'), ('t-shirt', 20, 'StoreA')], Bought Items: [('t-shirt', 25, 'StoreB')]

Store: StoreA, Profits: 93

Store: StoreB, Profits: 162

Shopper 1, Remaining Budget: 30, Cart Contents: [], Bought Items: [('jeans', 37, 'StoreB'), ('jeans', 33, 'StoreA')]

Shopper 2, Remaining Budget: 0, Cart Contents: [], Bought Items: [('sweater', 50, 'StoreB')]

Shopper 3, Remaining Budget: 25, Cart Contents: [], Bought Items: [('t-shirt', 25, 'StoreB'), ('t-shirt', 25, 'StoreB')]

Shopper 4, Remaining Budget: 15, Cart Contents: [], Bought Items: [('t-shirt', 25, 'StoreB'), ('t-shirt', 20, 'StoreA'), ('t-shirt', 20, 'StoreA'), ('t-shirt', 20, 'StoreA')]
```

Turn in `lab6.py` to Gradescope when you have this output.

## Tips
### Inheritance
A powerful feature of object-oriented programming is the ability to create a new class by extending an existing class. When extending a class, we call the original class the parent class and the new class the child class. All classes inherit from the base Python `Object` class. Note some differences in variable scope: Any variable defined outside the scope of the class functions (like `attribute1` in the example below) can be accessed and modified by every instance of `MyParentClass` and any class that inherits from it. All attributes defined in the scope of `__init__` can only be accessed and modified by specific instances of `MyParentClass` or specific instances of any class that inherits from it.

Parent class:
```python
class MyParentClass:
  
  attribute1 = 298 # instances of MyParentClass and any child classes have access to this variable! 
  
  def __init__(self, field1, field2): # Parent's constructor
    self.field1 = field1
    self.field2 = field2
    # Do stuff
```

Child class:
```python
  class MyChildClass(MyParentClass):
      def __init__(self, otherfield1, otherfield2, otherfield3): # Child's constructor
        super().__init__(otherfield1, otherfield2) # Runs the code in the parent class' constructor
        self.otherfield3 = otherfield3
```

Note that in the code for the child class above, the value passed in for `otherfield1` will be assigned to `self.field1` in the `MyChildClass` object. Further, the constructor for the parent class will not be automatically called, so you need to call `super().__init__` to invoke the parent's constructor.

### Inner Functions
An inner function is one that is defined within the scope of another function. This means a function can define and implement another function within its scope and return a function. See below for an example.
```python

def my_function(*args): # recall *args lets you pass in a variable number of arguments
    def my_inner_function(): 
        for arg in args: # the inner function is able to access the variables from the outer function!
          print(arg)
    return my_inner_function

returned_function = my_function("hello", "world", "EECS", 298) # my_function returns a function
returned_function() # call the returned function
```
The output is 
```
hello
world
EECS
298
```

### Decorators
A common use case of inner functions is in the definition of decorator functions. Decorator functions take a `function` as input and return another `function` that defines behavior before and/or after the decorated function is called. To decorate a function, you use the `@` symbol and the decorator function name above the function to decorate. See below for an example.

```python

def a_decorator(func):
    def decorator_behavior(*args): # *args captures all the arguments that could be passed into func
        print(args[0]) # print the first argument passed into func
        func(*args) # call func with its arguments
        print("Function complete") # runs after func finishes
    return decorator_behavior

@a_decorator
def decorated_function(val1: int, val2: int):
    print(val1 + val2)

decorated_function(-3,12)
```
The output is 
```
-3 
9
Function complete
```

Decorators can be used in many ways and one common use is for debugging. Below gives an example of how a decorator could be used to help debug our above example class implementation.

```python

def debug_attributes(func):
    def print_out_attribute_1(*args):
        print(args[0].attribute1) # args[0] is self in class functions!
        func(*args) # call the function
    return print_out_attribute_1

class MyParentClass:

  attribute1 = 298 # instances of MyParentClass and any child classes have access to this variable! 
  
  def __init__(self, field1, field2): # Parent's constructor
    self.field1 = field1
    self.field2 = field2
    # Do stuff

class MyChildClass1(MyParentClass):
      def __init__(self, otherfield1, otherfield2, otherfield3): # Child's constructor
        super().__init__(otherfield1, otherfield2) # Runs the code in the parent class' constructor
        self.otherfield3 = otherfield3

      @debug_attributes
      def child_function(self):
          print(f"My Attribute: {self.otherfield3}")
          addition = self.attribute1 + self.field1
          print(f"Adding Parent attributes: {addition}")

class MyChildClass2(MyParentClass):
      def __init__(self, otherfield1, otherfield2, otherfield3, otherfield4): # Child's constructor
        super().__init__(otherfield1, otherfield2) # Runs the code in the parent class' constructor
        self.otherfield3 = otherfield3
        self.otherfield4 = otherfield4

      @debug_attributes
      def child_function(self):
          print(f"My Attributes: {self.otherfield3}, {self.otherfield4}")
          subtraction = self.attribute1 - self.field1
          print(f"Subtracting Parent attributes: {subtraction}")
```
Now to see how the decorator works, we can call `child_function`:
```python

child1 = MyChildClass1(1,2,3)
child2 = MyChildClass2(1,2,3,4)

child1.child_function()
child2.child_function()
```
We get the following output:
```
298
My Attribute: 3
Adding Parent attributes: 299
298
My Attributes: 3, 4
Subtracting Parent attributes: 297
```
