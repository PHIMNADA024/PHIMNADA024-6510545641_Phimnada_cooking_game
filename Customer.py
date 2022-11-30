from time import strftime, localtime
import json


class Customer:
    """Create a customer name, the customer's birthday, and the price of the menu object that customers have to pay."""
    def __init__(self):
        self.__name = ""
        self.__birthday = (0, 0, 0)
        self.__pay = 0

# Make all attributes private.
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def pay(self, pay):
        self.__pay = pay

    def change_money(self, food_price):
        """Calculate discounts, customer changes, and menu prices that customers have to pay."""
        banknotes = [1000, 500, 100, 50, 20]
        coins = [10, 5, 2, 1]
        food_price_discount = food_price - self.discount(food_price)
        print(f"Price of the pizza: {food_price} Baht")
        print(f"Discount : {food_price - food_price_discount} Baht")
        print(f"Please pay {food_price_discount} Baht")
        cash = int(input("Input your money here : "))
        # If the amount that the customer enters is less than the price of the menu that the customer chooses,
        # the customer must enter money again until it is greater than or equal to the price of that menu.
        while cash < food_price_discount:
            print("Your money is not enough.")
            cash = int(input("Input your money here : "))
        print(f"Your change is {cash-food_price_discount} Baht.")
        print("Here is your change.")
        change = cash-food_price_discount
        # Calculate the change until the amount of change is equal to 0.
        while change != 0:
            for bank in banknotes:
                if change // bank >= 1:
                    print(f"You get {int(change // bank)} of {bank} Baht Banknote.")
                    change -= bank * (change // bank)
            for coin in coins:
                if change // coin >= 1:
                    print(f"You get {int(change // coin)} of {coin} Baht Coin.")
                    change -= coin * (change // coin)
        self.pay += food_price_discount
        self.write_file()

    def birthday_check(self):
        """Check if today matches the customer's birthday or month of birth. If yes, give the customer a discount."""
        if int(strftime("%m", localtime())) == self.birthday[1]:
            if int(strftime("%d", localtime())) == self.birthday[0]:
                return 0.5
            return 0.1
        return 0

    def discount(self, price):
        """Take the discount percentage to calculate the price that customers have to pay."""
        return self.birthday_check()*price

    def write_file(self):
        """Write information about the customer's name, date of birth, and food prices that customers have paid."""
        data = {
            self.name: {
                "birth_date": self.birthday[0],
                "birth_month": self.birthday[1],
                "birth_year": self.birthday[2],
                "total_pay": self.pay,
                "purchase": [self.pay]
            }
        }
        try:
            with open("customer.json", "r") as customer_file:
                customer_data = json.load(customer_file)
            if self.name in customer_data:
                customer_data[self.name]["total_pay"] += self.pay
                customer_data[self.name]["purchase"].append(self.pay)
            elif self.name not in customer_data:
                customer_data.update(data)
            with open("customer.json", "w") as customer_file:
                json.dump(customer_data, customer_file, indent=4)
        except FileNotFoundError:
            with open("customer.json", "w") as customer_file:
                json.dump(data, customer_file, indent=4)
