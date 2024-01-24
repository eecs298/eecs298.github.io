"""
EECS 298 Social Consequences of Computing WN 2024 Homework 1

Implementing the database of local restaurants for the company LivingLikeALocal.
"""


import numpy as np
import csv

class Restaurant: 
    def __init__(self, name, address, telephone, website, rating, price, keyword, category_choice):
        """An object to hold all the information about a business.

        Attributes:
            name (str): the name of the restaurant
            address (str): the address of the restaurant
            telephone (str): the telephone number of the restaurant
            website (str): the website associated with the restaurant
            rating (str): the numerical rating of the restaurant out of 5 stars
            price (str): the relative price of the restaurant in terms of number of dollar signs displayed
            keyword (str): a key word (or two) describing the restaurant
            category_choice (str): category of your choosing
        """
        # TODO: set the attributes of this class based on the inputs
        pass
    
    def __str__(self):
        """Overloading the __str__ function to print Restaurant objects.

        Argurments:
            None
        Modifies:
            None
        Returns:
            A str displaying all the restaurant information
        """
        # TODO: create and return a string displaying the Restaurant information in the format specified in the spec
        pass



class RestaurantDatabase:


    def __init__(self):
        """A database to hold information about local restaurants.

        Attributes:
            self.restaurants (list): holds the list of Restaurant objects in the database
        """
        self.restaurants = []

    def read_data(self, file):
        """Reads in data from file to add to self.restaurants.

        Arguments:
            file (str): a CSV file with column names corresponding to the Restaurant attributes
        Modifies:
            self.restaurants
        Returns:
            None
        """
        # TODO: read from the given CSV file and store the restaurant information in self.restaurants
        pass

    def sort_database(self, attribute_name, reverse=False, k=0):
        """Sorts the database based on the given attribute_name and optionally returns the top k results. 

        Arguments:
            attribute_name (str): the name of the attribute from the Restaurant class
            reverse (bool): if True, reverses the order of the sort
            k (int): if greater than 0, return the top k restaurants after sorting otherwise return an empty list
        Modifies:
            None
        Returns:
            A (potentially empty) sorted list of Restaurant objects based on k
        """
        # TODO: sort the restaurants where attribute_name is not None and return the top k
        pass

    def sort_by_keyword(self):
        """Sorts the database into a dictionary where the keys of the dictionary 
        are the 'keyword' attribute and the values are a list of Restaurant objects with that 'keyword'.

        Arguments:
            None
        Modifies:
            None
        Returns:
            a sorted dict object
        """

        restaurants_keyword_sorted = {} # create empty dictionary

        # TODO: add restaurants from self.restaurants to the dictionary where attribute name is not None

        return restaurants_keyword_sorted


    def search_database(self, attribute_name, search_query):
        """Searches the database for the given search_query in the attribute_name category and returns matching restaurants.

        Arguments:
            attribute_name (str): the name of the attribute from the Restaurant class
            search_query (str): a query to search the attribute with.
        Modifies:
            None
        Returns:
            A list of matching Restaurant objects or an empty list for no matches
        """

        # TODO: search through self.restaurants for search_query and return matching restaurants
        pass


if __name__ == "__main__":

    # TODO: Use this space for analyzing output
    pass
