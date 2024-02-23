import csv

def _debug_advertised_shoppers(func):
    # TODO implement this decorator as specified.
    pass 


class Shopper:
    """A class to represent an online shopper looking for one type of product"""
    def __init__(self, id, budget, product_preference):
        self.ID = id
        self.budget = budget # how much they have to spend
        self.product_preference = product_preference # the product they are looking for 
        self.cart = [] # stores tuples of (product, price, store.name)
        self.bought_items = [] # stores tuples of (product, price, store.name)
    
    def __str__(self):
        return f"Shopper {self.ID}, Remaining Budget: {self.budget}, Cart Contents: {self.cart}, Bought Items: {self.bought_items}\n"

    def add_to_cart(self, product, store):
        current_cart_price = sum([item[1] for item in self.cart]) # how much user has currently spent in cart

        if store.inventory[product][0] <= self.budget - current_cart_price:
            self.cart.append((product, store.inventory[product][0], store.name))
        
    def checkout(self, store):
        items_to_buy = [item for item in self.cart if item[2] == store.name] # collect items for given store
        for item in items_to_buy:
            sale_made = store.make_sale(self, item[0]) # check store inventory
            if not sale_made:
                # remove from cart
                self.cart.remove(item)
                raise ValueError("Store ran out of this product!")
            else:
                # buy item
                self.bought_items.append(item)
                self.budget -= item[1]
                # remove from cart
                self.cart.remove(item)

    def receive_advertisement(self, product, price, store):
        if product == self.product_preference and price < self.budget:
            self.cart.append((product, price, store.name)) # add to cart 

class Store:
    """Parent class of all clothing stores in an area"""
    active_shoppers = [] # keep track of who is shopping at the store

    def __init__(self, products_file_path, name):
        self.inventory = self._stock_store(products_file_path)
        self.profits = 0
        self.name = name
    
    def __str__(self):
        return f"Store: {self.name}, Profits: {self.profits}\n"
    
    def _stock_store(self, products_file_path):
        with open(products_file_path, "r") as csv_file:
            dict_reader = csv.DictReader(csv_file)
            inventory = {}
            for row in dict_reader:
                inventory[row["product"]] = (int(row["price"]), int(row["amount"])) # tuple of price and amount of product in stock
        
        return inventory

    def make_sale(self, shopper, product):
        if self.inventory[product][1] > 0:
            self.profits += self.inventory[product][0] # add price to profits
            self.inventory[product] = (self.inventory[product][0], self.inventory[product][1] - 1) # decrease inventory
            self.active_shoppers.append(shopper) # add this shopper to the active_shoppers list
            return True # indicate the sale was made
        else:
            return False # indicate the sale could not be made


class StoreA(Store):
    """A class to represent Store A selling clothes"""
    def __init__(self, products_file_path, name):
        super().__init__(products_file_path, name) # call parent's contructor


    def advertise(self):
        """Advertising strategy for StoreA"""
        for shopper in self.active_shoppers:
            product = shopper.product_preference
            if self.inventory[product][1] > 0: # make sure store has the inventory of the shopper's preference
                shopper.receive_advertisement(product, self.inventory[product][0],self)



class StoreB(Store):
    """A class to represent Store B selling clothes"""
    def __init__(self, products_file_path, name):
        super().__init__(products_file_path, name) # call parent's contructor
    
    
    def advertise(self):
        """Advertising strategy for StoreB"""
        for shopper in self.active_shoppers:
            for item in shopper.bought_items:
                if item[2] == self.name and self.profits < 100: # only advertise if shopper has shopped here before and profits are low
                    product = shopper.product_preference
                    if self.inventory[product][1] > 0: # make sure store has the inventory of the shopper's preference
                        shopper.receive_advertisement(product, self.inventory[product][0],self)
                    break
                
                


if __name__ == "__main__":

    # initialize stores and shoppers
    storeA = StoreA("productsA.csv", "StoreA")
    storeB = StoreB("productsB.csv", "StoreB")

    shopper1 = Shopper(1, 100, "jeans")
    shopper2 = Shopper(2, 50, "sweater")
    shopper3 = Shopper(3, 75, "t-shirt")
    shopper4 = Shopper(4, 100, "t-shirt")

    # shopping happens
    shopper1.add_to_cart("jeans", storeA)
    shopper1.add_to_cart("jeans", storeB)
    shopper2.add_to_cart("sweater", storeB)
    shopper3.add_to_cart("t-shirt", storeB)
    shopper3.add_to_cart("t-shirt", storeB)
    shopper4.add_to_cart("t-shirt", storeA)
    shopper4.add_to_cart("t-shirt", storeA)
    shopper4.add_to_cart("t-shirt", storeA)
    shopper4.add_to_cart("t-shirt", storeB)

    # checkout at store B
    shopper1.checkout(storeB)
    shopper2.checkout(storeB)
    shopper3.checkout(storeB)
    shopper4.checkout(storeB)

    # advertising
    storeA.advertise()
    storeB.advertise()

    # checkout at store A
    shopper1.checkout(storeA)
    shopper2.checkout(storeA)
    shopper3.checkout(storeA)
    shopper4.checkout(storeA)

    # print information
    print(storeA)
    print(storeB)
    print(shopper1)
    print(shopper2)
    print(shopper3)
    print(shopper4)

