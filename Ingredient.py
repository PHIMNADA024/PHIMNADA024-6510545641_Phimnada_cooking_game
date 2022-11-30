class Ingredient:
    def __init__(self, price=0, new_type=""):
        """Create an object for menu ingredient."""
        self.__price = price
        self.__type = new_type

# Make all attributes private.
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type):
        self.__type = new_type

    def food_price(self, piece):
        """Calculate the price of toppings per piece."""
        return self.price*piece

    def __eq__(self, other):
        return self.type == other.type
