import csv

class Bid:
    """
    A class to represent a single bid.

    Attributes:
        company: The name of the company resposible for this bid.
        keyword: The keyword this bid was placed for.
        price_of_bid: The amount submitted with the bid.
        price_to_pay: Initialized to None. This attribute is only
                      to be used in the case that this company is
                      selected as a winner or runner-up for this keyword.
    """

    def __init__(self, company: str, keyword: str, price_of_bid: float):
        pass


def auctionKeyword(bid_list: list):
    """
    Uses the generalized second-price auction system to generate
    the winner and runner-up for a certain keyword. The winner is
    the the one which made the highest bid and pays the price of 
    the second-highest bid. The runner-up is the one which made
    the second-highest bid and pays the price of the third-highest bid.

    Args:
        bid_list: A list containing all Bid objects for a certain keyword 

    Returns:
        A list containing two Bid objects, representing the winner and the 
        runner-up, in that order. These two Bid objects should each have their
        price_to_pay field updated with the price that company will pay.
    """

    pass

def processCSV(bids_filepath: str):
    """
    Uses the csv library to process a .csv file containing a series of bids
    made by multiple companies on multiple keywords. 

    Args:
        bids_filepath: the path the the spreadsheet to be processed.

    Returns:
        A dictionary. The keys of this dictionary are the keywords in the auction. The value
        associated with each keyword is a list of Bid objects associated with each bid placed
        on that keyword. Each Bid object has its price_to_pay field set to None, as no winners
        have yet been calculated. Returns None if no file is found at that location.s
    """

    pass


def secondPriceAuction(bids_filepath):
    """
    Organizes a second-price auction with the data in the spreadsheet at bids_filepath.
    Uses the processCSV function to process this spreadsheet into a Dict of Lists of Bids
    and uses the auctionKeyword function to execute this auction for each keyword in that dictionary.


    Args:
        bids_filepath: the path the the spreadsheet containing auction data.

    Returns:
        A dictionary. The keys of this dictionary are the keywords in the auction. The value
        associated with each keyword is a list of containing two Bid objects, the winner and
        the runner-up for that keyword, in that order. Each Bid object has its price_to_pay 
        field set to the price it will pay according to the auction.
        have yet been calculated.
    """

    pass
