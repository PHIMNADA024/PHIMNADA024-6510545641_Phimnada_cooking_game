from turtle import Turtle, Screen
from Ingredient import Ingredient
import json


class Hamburger:
    def __init__(self):
        """Create attributes for hamburger details and a dictionary to store toppings."""
        self.__size = 0
        self.__bun = ""
        self.__meat = ""
        self.__sauce = ""
        self.__topping = {}
        self.__price = 0

# Make all attributes private.
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def bun(self):
        return self.__bun

    @bun.setter
    def bun(self, bun):
        self.__bun = bun

    @property
    def meat(self):
        return self.__meat

    @meat.setter
    def meat(self, meat):
        self.__meat = meat

    @property
    def sauce(self):
        return self.__sauce

    @sauce.setter
    def sauce(self, sauce):
        self.__sauce = sauce

    @property
    def topping(self):
        return self.__topping

    @topping.setter
    def topping(self, topping):
        self.__topping = topping

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def burger_size(self):
        """Check out what size of hamburger the customer chooses."""
        print("1.mini(3 ounce)")
        print("2.standard(4 ounce)")
        print("3.big(5 ounce)")
        choice = input("Please choose the size of your hamburger: ")
        while choice != "1" and choice != "2" and choice != "3":
            print("Please choose the valid size")
            choice = input("Please choose the size of your hamburger: ")
        if choice == "1":
            print("You choose mini(3 ounce) size.")
            self.size = 3
        elif choice == "2":
            print("You choose standard(4 ounce) size.")
            self.size = 4
        elif choice == "3":
            print("You choose 3.big(5 ounce) size.")
            self.size = 5

    def burger_bun(self):
        """Check what kind of hamburger bun the customer chooses."""
        print("1.classic bun")
        print("2.charcoal bun")
        choice = input("Please choose your preferred hamburger bun type: ")
        while choice != "1" and choice != "2":
            print("Please choose the valid bun")
            choice = input("Please choose your preferred hamburger bun type: ")
        if choice == "1":
            print("You choose classic bun.")
            self.bun = "classic_bun"
        elif choice == "2":
            print("You choose charcoal bun.")
            self.bun = "charcoal_bun"

    def burger_meat(self):
        """Check what kind of meat the customer chooses for the hamburger."""
        print("1.pork")
        print("2.beef")
        print("3.shrimp")
        print("4.fish")
        print("5.chicken")
        choice = input("Please choose the meat you want to add to the hamburger: ")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("Please choose the valid meat")
            choice = input("Please choose the meat you want to add to the hamburger: ")
        if choice == "1":
            print("You choose pork burger.")
            self.meat = "pork"
        elif choice == "2":
            print("You choose beef burger.")
            self.meat = "beef"
        elif choice == "3":
            print("You choose shrimp burger.")
            self.meat = "shrimp"
        elif choice == "4":
            print("You choose fish burger.")
            self.meat = "fish"
        elif choice == "5":
            self.meat = "chicken"

    def burger_sauce(self):
        """Check out the pizza sauce that the customer chooses."""
        print("1.tomato sauce")
        print("2.mayonnaise sauce")
        print("3.mustard sauce")
        choice = input("Please choose the sauce of your hamburger: ")
        while choice != "1" and choice != "2" and choice != "3":
            print("Please choose the valid sauce")
            choice = input("Please choose the sauce of your hamburger: ")
        if choice == "1":
            print("You choose tomato sauce.")
            self.sauce = "tomato_sauce"
        elif choice == "2":
            print("You choose mayonnaise sauce.")
            self.sauce = "mayonnaise"
        elif choice == "3":
            print("You choose mustard sauce.")
            self.sauce = "mustard"

    def burger_topping(self):
        """Check the hamburger toppings chosen by the customer."""
        print("1.cheese")
        print("2.pickle")
        print("3.tomato")
        print("4.lettuce")
        print("5.onion")
        print("6.bacon")
        choice = input("Please choose the ingredients(enter q to quit): ")
        position = 3
        # Iterate over selecting toppings until choice equals "q".
        while choice != "q" or choice != "Q":
            topping = Turtle(visible=False)
            topping.hideturtle()
            topping.penup()
            topping.speed(0)
            topping.setx(-(self.size * 30))
            topping.sety(-(self.size * position))
            topping.pendown()
            if choice == "1":
                print("Cheese is added.")
                # Add toppings to the dictionary to calculate hamburger prices.
                self.topping[len(self.topping)] = Ingredient(10, "Cheese")
                topping.color("#E9A423")
                position -= 5
            elif choice == "2":
                print("Pickle is added.")
                # Add toppings to the dictionary to calculate hamburger prices.
                self.topping[len(self.topping)] = Ingredient(2, "Pickle")
                topping.color("#8B7E2F")
                position -= 5
            elif choice == "3":
                print("Tomato is added.")
                # Add toppings to the dictionary to calculate hamburger prices.
                self.topping[len(self.topping)] = Ingredient(3, "Tomato")
                topping.color("#CF2027")
                position -= 5
            elif choice == "4":
                print("Lettuce is added.")
                # Add toppings to the dictionary to calculate hamburger prices.
                self.topping[len(self.topping)] = Ingredient(3, "Lettuce")
                topping.color("#B5C541")
                position -= 5
            elif choice == "5":
                print("Onion is added.")
                # Add toppings to the dictionary to calculate hamburger prices.
                self.topping[len(self.topping)] = Ingredient(2, "Onnion")
                topping.color("#E6D2D8")
                position -= 5
            elif choice == "6":
                print("Bacon is added.")
                # Add toppings to the dictionary to calculate hamburger prices.
                self.topping[len(self.topping)] = Ingredient(10, "Bacon")
                topping.color("#410600")
                position -= 5
            elif choice == "q" or choice == "Q":
                break
            else:
                # If choosing something that is not a choice, the customer must select again.
                print("Please choose the valid ingredients")
            # Let the turtle draw the toppings that the customer chooses.
            topping.forward(self.size * 60)
            topping.begin_fill()
            topping.right(90)
            topping.forward(self.size * 5)
            topping.right(90)
            topping.forward(self.size * 60)
            topping.right(90)
            topping.forward(self.size * 5)
            topping.end_fill()
            choice = input("Please choose the ingredients(enter q to quit): ")
        return position

    def burger_price(self):
        """Calculate the price of the hamburger selected by the customer."""
        total_price = 0
        if self.size == 3:
            total_price += 50
        elif self.size == 4:
            total_price += 70
        elif self.size == 5:
            total_price += 90
        if self.bun == "classic_bun":
            total_price += 10
        elif self.bun == "charcoal_bun":
            total_price += 20
        if self.meat == "pork":
            total_price += 20
        elif self.meat == "beef":
            total_price += 30
        elif self.meat == "shrimp":
            total_price += 25
        elif self.meat == "fish":
            total_price += 20
        elif self.meat == "chicken":
            total_price += 15
        # Let the for loop calculate the price of the pizza topping from the Ingredient class.
        for topping in self.topping.values():
            total_price += topping.food_price(self.size)
        self.price = total_price

    def burger_screen(self):
        """Create turtle graphics of hamburger."""
        screen = Screen()
        screen.setup(800, 600)
        screen.bgpic("Table.gif")
        screen.update()
        self.burger_size()
        print("---------------------------")
        self.burger_bun()
        burger_base = Turtle(visible=False)
        burger_base.hideturtle()
        burger_base.penup()
        burger_base.speed(0)
        burger_base.setx(-(self.size * 25))
        burger_base.sety(-(self.size * 20))
        burger_base.pendown()
        # Check what hamburger bun base the customer chooses and let the turtle draw it.
        if self.bun == "classic_bun":
            burger_base.color("#D6852C")
        elif self.bun == "charcoal_bun":
            burger_base.color("#161C20")
        burger_base.forward(self.size * 50)
        burger_base.begin_fill()
        burger_base.right(90)
        burger_base.forward(self.size * 10)
        burger_base.right(90)
        burger_base.forward(self.size * 50)
        burger_base.right(90)
        burger_base.forward(self.size * 10)
        burger_base.end_fill()
        print("---------------------------")
        self.burger_meat()
        meat = Turtle(visible=False)
        meat.hideturtle()
        meat.penup()
        meat.speed(0)
        meat.setx(-(self.size * 30))
        meat.sety(-(self.size * 20)+(self.size * 10))
        meat.pendown()
        # Check what meat the customer chooses and let the turtle draw it.
        if self.meat == "pork":
            meat.color("#792B1C")
        elif self.meat == "beef":
            meat.color("#593729")
        elif self.meat == "shrimp":
            meat.color("#EE851C")
        elif self.meat == "fish":
            meat.color("#F3B535")
        elif self.meat == "chicken":
            meat.color("#DCA009")
        meat.forward(self.size * 60)
        meat.begin_fill()
        meat.right(90)
        meat.forward(self.size * 10)
        meat.right(90)
        meat.forward(self.size * 60)
        meat.right(90)
        meat.forward(self.size * 10)
        meat.end_fill()
        print("---------------------------")
        self.burger_sauce()
        sauce = Turtle(visible=False)
        sauce.hideturtle()
        sauce.penup()
        sauce.speed(0)
        sauce.setx(-(self.size * 27.5))
        sauce.sety(-(self.size * 7))
        sauce.pendown()
        # Check what sauce the customer chooses and let the turtle draw it.
        if self.sauce == "tomato_sauce":
            sauce.color("#B52A04")
        elif self.sauce == "mayonnaise":
            sauce.color("#F9F5E5")
        elif self.sauce == "mustard":
            sauce.color("#F2AF22")
        sauce.forward(self.size * 55)
        sauce.begin_fill()
        sauce.right(90)
        sauce.forward(self.size * 3)
        sauce.right(90)
        sauce.forward(self.size * 55)
        sauce.right(90)
        sauce.forward(self.size * 3)
        sauce.end_fill()
        print("---------------------------")
        position = self.burger_topping()
        burger = Turtle(visible=False)
        burger.left(90)
        burger.hideturtle()
        burger.penup()
        burger.speed(0)
        burger.setx(self.size * 25)
        burger.sety(-(self.size * (position+4.8)))
        burger.pendown()
        burger.begin_fill()
        # Check what hamburger bun the customer chooses and let the turtle draw it.
        if self.bun == "classic_bun":
            burger.color("#D6852C")
        elif self.bun == "charcoal_bun":
            burger.color("#161C20")
        burger.circle(self.size * 25, 180)
        burger.end_fill()
        print("Your hamburger is done!!")
        print("---------------------------")
        self.burger_price()

    def write_file_burger(self):
        """Write down the size, bun, meat, sauce, toppings and price of the hamburger that the customer chooses."""
        toppings = [topping.type for topping in self.topping.values()]
        try:
            with open("burger.json", "r") as burger_file:
                burger_data = json.load(burger_file)
            data = {
                len(burger_data) + 1: {
                    "size": self.size,
                    "bun": self.bun,
                    "meat": self.meat,
                    "sauce": self.sauce,
                    "topping": toppings,
                    "price": self.price
                }
            }
            burger_data.update(data)
            with open("burger.json", "w") as burger_file:
                json.dump(burger_data, burger_file, indent=4)
        except FileNotFoundError:
            data = {
                1: {
                    "size": self.size,
                    "bun": self.bun,
                    "meat": self.meat,
                    "sauce": self.sauce,
                    "topping": toppings,
                    "price": self.price
                }
            }
            with open("burger.json", "w") as burger_file:
                json.dump(data, burger_file, indent=4)
