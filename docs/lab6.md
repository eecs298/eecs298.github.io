---
layout: spec
title: Lab 6
sitemapOrder: 20
---

Lab 6
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you will be given three `.csv` databases, each containing the metadata for several posts from one of three social media sites -- Twitter, Facebook, and Reddit. Your task will be to use user IP addresses for each post to match user accounts between these three sites in order to track cross-site aggregate statistics for users. To this end, you will store post data by utilizing object polymorphism in Python: you will create a parent `Post` class and three child classes, `Tweet`, `FacebookPost`, and `RedditPost`. Download the databases [here](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/facebook.csv), [here](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/reddit.csv), and [here](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/twitter.csv).

### lab6.py
Create a file titled `lab6.py`.

In this file, create four classes: `Post`, `Tweet`, `FacebookPost`, and `RedditPost`.

#### Post
 The `Post` class should represent a generic social media post contain the following fields assigned on object creation:
 * A string field to contain the username of the user that made the post.
 * A string field to contain the user-written text within the post.
 * An integer field to track the number of likes on the post.
 * An integer field to track the number of comments on the post.

 This class should contain a constructor that handles arguments for these four fields. In addition, the class should be an integer field to track the total number of interactions on the post. This value should not be passed in as an argument in the constructor, but should instead be calculated and assigned within the constructor by calling a method called `_getTotalInteractions(self)`. This method should take no arguments and should return the total number of interactions on the post. For this generic `Post` class, this method should calculate total interactions by adding together the number of likes and comments on the post. In addition, you should override the `__str__` operator to return the post's text, and the `__len__` operator to return the length of the post's text.

#### Tweet
The `Tweet` class should inherit from the `Post` class and should take the user's username, the body of the tweet, the number of likes on the tweet, the number of retweets, and the number of replies. This class' constructor should call its parent class' constructor with its values for username, post text, likes and replies. It should also override its parent class' `_getTotalInteractions(self)` method to return the sum of likes, retweets, and replies.

#### FacebookPost
The `FacebookPost` class should inherit from the `Post` class and should take the name of the user, the body of the post, the number of reacts on the post, the number of shares, and the number of comments. This class' constructor should call its parent class' constructor with its values for username, post text, like_reacts (in place of likes) and comments, while assigning the other arguments to fields manually. It should also override its parent class' `_getTotalInteractions(self)` method to return the sum of number of comments, shares, and all reacts.

#### RedditPost
The `RedditPost` class should inherit from the `Post` class and should take the user's username, the title and body of the post, the number of upvotes and downvotes on the post, the number of rewards, and the number of comments. This class' constructor should call its parent class' constructor with username, post body, the difference between number of upvotes and downvotes (in place of likes) and comments, while assigning the other arguments to fields manually. It should also override its parent class' `_getTotalInteractions(self)` method to return the sum of number of comments, total upvotes, total downvotes, and all rewards. In addition, its `__str__` method should return the title, plus a newline, plus the body of the post, and the `__len__` operator should return just the length of the body of the post.

Read in the data from the three databases into a dictionary. The keys of these dictionaries should be the IP addresses of the user, and the value for each key should be a list of all that user's posts across all three platforms, with each post in the form of the respective class for that post. For each user, print out the following:

* All of the user's usernames across the different platforms
* The total number of interactions on all of the user's posts across all platforms
* The text of the user's post with the most interactions from any platform (using that post's `__str__` method)

In addition, call `dir(mypost)` on any post from the dataset and print the output. This list contains all methods contained within the object, most of which are inherited from the base `Object` class. Any of these methods can be overwritten as done in this lab. For example the `__iadd__` and `__imul__` methods change how the object responds to the + and * operators, and the `__del__` method, known as the deconstructor, handles behaviour for when all references to the object are deleted. Pick one of these and leave a comment with an idea for how one of these could be used in either this lab's context or another context.

## Tips
### Inheritance
A powerful feature of object-oriented programming is the ability to create a new class by extending an existing class. When extending a class, we call the original class the parent class and the new class the child class. All classes inherit from the base Python `Object` class.

Parent class:
```python
class MyParentClass:
  __init__(self, field1, field2): # Parent's constructor
    self.field1 = field1
    self.field2 = field2
    # Do stuff
```

Child class:
```python
  class MyChildClass(MyParentClass):
      __init__(self, otherfield1, otherfield2, otherfield3): # Child's constructor
        super.__init__(otherfield1, otherfield2) # Runs the code in the parent class' constructor
        self.otherfield3 = otherfield3
```

Note that in the code for the child class above, the value passed in for `otherfield1` will be assigned to `self.field1` in the `MyChildClass` object, not to `self.otherfield`.

### Overriding methods
Any method within a parent class can be overridden in a child of that class, as seen with the constructors in the classes above. When writing the constructor, you actually override the default constructor of the `Object` class, from which every class inherits. You can do the same with other methods belonging to parent classes, for example the `__str__` method, which is automatically called whenever an object is implicitly or explicitly converted to a string.
```python
class MyClass: # Implicitly inherits from Object class
  __init__(self, field1, field2):
    # Do stuff

  __str__(self)
    return field + field2 # Should return a reasonable string representation of the object
```
