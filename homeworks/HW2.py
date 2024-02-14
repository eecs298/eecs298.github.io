import csv
from datetime import datetime
import numpy as np
from hashlib import md5

np.random.seed(298298) # For stability of outputs in the autograder, DO NOT CHANGE.

class Celebrity:

    def __init__(self, celeb_name: str, medallion: str, photo_date: str):
        """Contains information represented in one photo of a celebrity.

        Attributes:
            celeb_name: The name of the celebrity in the photo, in Firstname Lastname format.
            medallion: The taxi cab identification number in the photo.
            photo_date: The date the photo was taken, as a string, in YYYY-MM-DD format.
        """
        self.celeb_name = celeb_name
        self.medallion = medallion
        self.md5_medallion = # TODO: compute the md5 hash of the medallion
        self.photo_date = photo_date

    def __str__(self):
        """Overload the print function.

        Arguments:
            None
        Modifies:
            None
        Returns:
            A string formatted as given in the spec
        """
        # TODO
        pass


class Trip:

    def __init__(self, md5_medallion: str, date: str,fare_amount: float, tip_amount: float,
                 pickup_location: tuple[str, str], dropoff_location: tuple[str, str]):
        """Contains anonymized information about one taxi trip.

        Attributes:
            md5_medallion: The md5 hashed medallion number of the taxi.
            date: The date of the trip, as a string, in YYYY-MM-DD format.
            fare_amount: The fare paid for the trip. Must be stored as a float.
            tip_amount: The tip paid for the trip. Must be stored as a float.
            pickup_location: A Tuple of the pickup latitude and longitude (each stored as a string), in that order.
            dropoff_location: A Tuple of the dropoff latitude and longitude (each stored as a string), in that order.
        """
        self.md5_medallion = md5_medallion
        self.date = date
        self.fare_amount = fare_amount
        self.tip_amount = tip_amount
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location

    def __str__(self):
        """Overload the print function.

        Arguments:
            None
        Modifies:
            None
        Returns:
            A string formatted as given in the spec.
        """
        # TODO
        pass

class TaxiTripsDatabase:

    def __init__(self, trips_file_path: str):
        """This class is used to store and query information from trips.csv.

        Attributes:
            trips_file_path: File path to trips.csv
        """
        self.trips_list = self._read_trips_data(trips_file_path)


    def _read_trips_data(self, file_path: str):
        """Local function to read in trips.csv.

        Arguments:
            file_path: File path to trips.csv
        Modifies:
            None
        Returns:
            A list of Trip objects to fill self.trips_list with
        """
        # TODO
        pass

    def query_trips(self, attribute_list: list[str], attribute_matching_values: list):
        """Returns a list of trips that match all the given arguments except those passed in as None.

        Arguments:
            attribute_list: A list of Trip attribute names to use to query the database. Raise AttributeError if any attribute not in the Trips class is provided.
            attribute_matching_values: A list of values (one for each attribute name given in attribute_list) to match in the database.
        Modifies:
            None
        Returns:
            a list of Trips with matching given attributes
        """
        # TODO
        pass

    def query_mean_tip(self, start_date: str, end_date: str, filtered_medallion: str = "", epsilon: float = None):
        """Calculates the mean tip between the given dates for Trips not with filtered_medallion and subject to epsilon-DP if epsilon is not None.

        Arguments:
            start_date: The start date for the average, in YYYY-MM-DD format.
            end_date: The end date (inclusive) for the average, in YYYY-MM-DD format.
            filtered_medallion: Md5 hashed medallion to not include in mean tip calculation. Default empty string.
            epsilon: Specifies the differential privacy level if not None. Default None.
        Modifies:
            None
        Returns:
            2 values separated by a comma: 1. A float denoting the (possibly noised) mean tip within the timeframe, 2. the number of tips used in the mean calculation.
        """
        # TODO
        pass

def perform_linkage_attack(celebrity_list: list[Celebrity], taxi_trip_database: TaxiTripsDatabase):
    """A function to perform the linkage attack using taxi_trip_database.query_trips.

    Arguments:
        celebrity_list: A list of Celebrity objects to link
        taxi_trip_databse: An instance of a TaxiTripsDatabase to query data from
    Returns:
        A list of tuple(Trip, Celebrity) reprsenting the linked celebrities to trips.
    """
    # TODO
    pass

def perform_difference_attack(celebrity: Celebrity, taxi_trip_database: TaxiTripsDatabase, epsilon = None):
    """A funcion to perform the difference attack using taxi_trip_database.query_mean_tip only. Hint: You need only call query_mean_tip twice!

    Arguments:
        celebrity: A Celebrity to guess the tip_amount for
        taxi_trip_databse: An instance of a TaxiTripsDatabase to query data from
        epsilon: Specifies the differential privacy level if not None. Default None.
    Returns:
        A tip amount guess for the given Celebrity
    """
    # TODO
    pass

if __name__ == "__main__":

    # File paths
    celebrity_csv_path = "celebrities.csv"
    trips_csv_path = "trips.csv"

    # TODO - use this space to answer the written questions and test your implementations
