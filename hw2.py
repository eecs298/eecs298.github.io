import csv
import datetime
import numpy as np
from hashlib import md5
from typing import Tuple, List


class Celebrity:
    """
    Contains information represented in one photo of a celebrity.

    Attributes:
    celeb_name: The name of the celebrity in the photo, in Firstname Lastname format.
    medallion: The taxi cab identification number in the photo. This can be stored as either hashed or unhashed.
    photo_date: The date the photo was taken, as a string, in YYYY-MM-DD format.
    """

    def __init__(self, celeb_name: str, medallion: str, photo_date: str):
        pass


class Driver:
    """
    Contains information about one taxi driver.

    Attributes:
    driver_name: The name of the driver, in Firstname Lastname format.
    hack_license: The driver's hack license number. This can be stored as either hashed or unhashed.
    """

    def __init__(self, driver_name: str, hack_license: str):
        pass


class Trip:
    """
    Contains deanonymized information about one taxi trip, with the driver identified.

    Attributes:
    driver_name: The name of the taxi driver, in Firstname Lastname format. Take this field from the Driver object passed in.
    medallion: The unhashed medallion number of the taxi. 
    hack_license: The unhashed hack license number of the taxi driver. 
    date: The date of the trip, as a string, in YYYY-MM-DD format.
    payment_type: The payment method used. Must be either CRD (for credit card) or CSH (for cash).
    fare_amount: The fare paid for the trip. Must be stored as a float. 
    tip_amount: The tip paid for the trip. Must be stored as a float. 
    pickup_location: A Tuple of the pickup latitude and longitude (each stored as a string), in that order.
    dropoff_location: A Tuple of the dropoff latitude and longitude (each stored as a string), in that order.
    """

    def __init__(self, driver: Driver, medallion: str, hack_license: str, date: str, payment_type: str,
                 fare_amount: float, tip_amount: float, pickup_location: Tuple[str, str], dropoff_location: Tuple[str, str]):
        pass


class CelebrityTrip(Trip):
    """
    Contains deanonymized information about one taxi trip, with both the driver and passenger identified.
    Inherits from the Trip class. Handle assignment of parent attributes with the super() method.

    Attributes:
    passenger_name: The name of the passenger, in Firstname Lastname format. Take this field from the Celebrity object passed in.
    driver_name: The name of the taxi driver, in Firstname Lastname format. Take this field from the Driver object passed in.
    medallion: The unhashed medallion number of the taxi. 
    hack_license: The unhashed hack license number of the taxi driver. 
    date: The date of the trip, as a string, in YYYY-MM-DD format.
    payment_type: The payment method used. Must be either CRD (for credit card) or CSH (for cash).
    fare_amount: The fare paid for the trip. Must be stored as a float. 
    tip_amount: The tip paid for the trip. Must be stored as a float. 
    pickup_location: A Tuple of the pickup latitude and longitude (each stored as a string), in that order.
    dropoff_location: A Tuple of the dropoff latitude and longitude (each stored as a string), in that order.
    """

    def __init__(self, celebrity: Celebrity, driver: Driver, medallion: str, hack_license: str, date: str, payment_type: str,
                 fare_amount: float, tip_amount: float, pickup_location: Tuple[str, str], dropoff_location: Tuple[str, str]):
        pass


class MedallionDecoder:
    """
    A class to handle MD5 encoding/decoding of medallion numbers. The use of this class is optional and its structure is up to you. 
    """
    
    pass


class HackLicenseDecoder:
    """
    A class to handle MD5 encoding/decoding of hack license numbers. The use of this class is optional and its structure is up to you. 
    """

    pass


def process_celebrities(celebrity_csv_path: str):
    """
    Given a database of transcribed celebrity photos, returns a sorted list of Celebrity objects.

    Attributes:
    celebrity_csv_path: The location of the celebrity sighting database you created. This database can be structured however you like.

    Returns:
    A list of Celebrity objects, one for each row in the database. Must be sorted alphabetically by celebrity name,
    using the earliest date as the tiebreaker.
    """

    pass


def process_drivers(driver_csv_path: str):
    """
    Given a database of driver information, returns a sorted list of Driver objects.

    Attributes:
    driver_csv_path: The location of the NYC taxi driver database.

    Returns:
    A list of Driver objects, one for each row in the database. Must be sorted alphabetically by last name, followed by first name.
    """

    pass


def linkage_attack(trip_csv_path: str, celebrity_list: List[Celebrity], diver_list: List[Driver]):
    """
    Performs a linkage attack on the NYC taxi dataset using information on passengers and drivers.

    Attributes:
    travel_csv_path: The location of the NYC trip database.
    celebrity_list: A list of Celebrity objects.
    diver_list: A list of Driver objects.

    Returns:
    A list of Trip and CelebrityTrip objects containing deanonymized information from the trip database, one for each row. 
    Only rows which correspond to a trip taken by a celebrity should be represented by a CelebrityTrip object.
    """

    pass


def get_mean_tip(linkage_attack_results: List[Trip], start_date: str, end_date: str, ignore_outliers: bool = False):
    """
    Calculates the mean tip between the given dates.

    Attributes:
    linkage_attack_results: The output of the linkage_attack method.
    start_date: The start date for the average, in YYYY-MM-DD format.
    end_date: The end date (inclusive) for the average, in YYYY-MM-DD format.
    ignore_outliers: If True, this method does not factor in cash trips with a tip of zero. This arg is optional and defaults to False.

    Returns:
    A float denoting the average tip within the timeframe, with outliers factored into the average only if desired.
    """

    pass


def get_mean_tip_dp(linkage_attack_results: List[Trip], start_date: str, end_date: str, ignore_outliers: bool = False, epsilon: float = 0.1):
    """
    Calculates a noised version (via the Laplace mechanism) of the mean tip between the given dates.

    Attributes:
    linkage_attack_results: The output of the linkage_attack method.
    start_date: The start date for the average, in YYYY-MM-DD format.
    end_date: The end date (inclusive) for the average, in YYYY-MM-DD format.
    ignore_outliers: If True, this method does not factor in cash trips with a tip of zero. This arg is optional and defaults to False.
    epsilon: The epsilon value for the Laplace distribution. This arg is optional and defaults to 0.1.

    Returns:
    A noised float denoting the average tip within the timeframe, with outliers factored into the average only if desired.
    """

    pass
