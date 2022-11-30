from Ingredient import Ingredient
from turtle import Turtle, Screen
import json
import random


class Pizza:
    def __init__(self):
        """Create attributes for pizza details and a dictionary to store toppings."""
        self.__size = 0
        self.__flour = ""
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
    def flour(self):
        return self.__flour

    @flour.setter
    def flour(self, flour):
        self.__flour = flour

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

    def pizza_size(self):
        """Check out what size of pizza the customer chooses."""
        print("1.small(6 inches)")
        print("2.medium(8 inches)")
        print("3.large(12 inches)")
        choice = input("Please choose the size of your pizza: ")
        while choice != "1" and choice != "2" and choice != "3":
            print("Please choose the valid size")
            choice = input("Please choose the size of your pizza: ")
        if choice == "1":
            print("You choose small(6 inches) size.")
            self.size = 6
        elif choice == "2":
            print("You choose medium(8 inches) size.")
            self.size = 8
        elif choice == "3":
            print("You choose large(12 inches) size.")
            self.size = 12

    def pizza_flour(self):
        """Check out the pizza dough that the customer chooses."""
        print("1.thin and crispy")
        print("2.thick")
        choice = input("Please choose the flour of your pizza: ")
        while choice != "1" and choice != "2":
            print("Please choose the valid flour")
            choice = input("Please choose the flour of your pizza: ")
        if choice == "1":
            print("You choose thin and crispy flour.")
            self.flour = "thin_and_crispy"
        elif choice == "2":
            print("You choose thick flour.")
            self.flour = "thick"

    def pizza_sauce(self):
        """Check out the pizza sauce that the customer chooses."""
        print("1.tomato sauce")
        print("2.thousand island sauce")
        choice = input("Please choose the sauce of your pizza: ")
        while choice != "1" and choice != "2":
            print("Please choose the valid sauce")
            choice = input("Please choose the sauce of your pizza: ")
        if choice == "1":
            print("You choose tomato sauce.")
            self.sauce = "tomato"
        elif choice == "2":
            print("You choose thousand island sauce.")
            self.sauce = "thousand_island"

    def pizza_topping(self):
        """Check the pizza toppings chosen by the customer."""
        print("1.mushroom")
        print("2.crab stick")
        print("3.bell pepper")
        print("4.shrimp")
        print("5.pepperoni")
        print("6.bacon")
        choice = input("Please choose the ingredients(enter q to quit): ")
        # Iterate over selecting toppings until choice equals "q".
        while choice.lower() != "q":
            if choice == "1":
                if Ingredient(3, "Mushroom") in self.topping.values():
                    print("Mushrooms are already added.")
                else:
                    print("Mushroom is added.")
                    # Add toppings to the dictionary to calculate pizza prices.
                    self.topping[len(self.topping)] = Ingredient(3, "Mushroom")
                    direction = 0
                    # Create a turtle (mushroom) according to the specified degree.
                    for _ in range(self.size):
                        mushroom = Turtle(visible=False)
                        mushroom.hideturtle()
                        mushroom.penup()
                        mushroom.shape("circle")
                        mushroom.color("#F9EEC9")
                        mushroom.shapesize(1.5)
                        mushroom.showturtle()
                        mushroom.left(direction)
                        mushroom.forward(self.size*15)
                        direction += 360/self.size
            elif choice == "2":
                if Ingredient(2, "Crab stick") in self.topping.values():
                    print("Crab sticks are already added.")
                else:
                    print("Crab stick is added.")
                    # Add toppings to the dictionary to calculate pizza prices.
                    self.topping[len(self.topping)] = Ingredient(2, "Crab stick")
                    crab_stick_color = ["#E0115F", "#FFFFFF"]
                    direction = (360/self.size)*1.5
                    # Create a turtle (crab stick) according to the specified degree.
                    for _ in range(self.size):
                        crab_stick = Turtle(visible=False)
                        crab_stick.hideturtle()
                        crab_stick.penup()
                        crab_stick.shape("square")
                        crab_stick.color(random.choice(crab_stick_color))
                        crab_stick.shapesize(0.5)
                        crab_stick.showturtle()
                        crab_stick.left(direction)
                        crab_stick.forward(self.size * 15)
                        direction += 360 / self.size
            elif choice == "3":
                if Ingredient(4, "Bell pepper") in self.topping.values():
                    print("Bell peppers are already added.")
                else:
                    print("Bell pepper is added.")
                    # Add toppings to the dictionary to calculate pizza prices.
                    self.topping[len(self.topping)] = Ingredient(4, "Bell pepper")
                    bell_pepper_color = ["#FF0000", "#F6BD26", "#5DA21A"]
                    direction = 0
                    # Create a turtle (bell pepper) according to the specified degree.
                    for _ in range(self.size):
                        bell_pepper = Turtle(visible=False)
                        bell_pepper.penup()
                        bell_pepper.hideturtle()
                        bell_pepper.color(random.choice(bell_pepper_color))
                        bell_pepper.pensize(5)
                        bell_pepper.speed(0)
                        bell_pepper.left(direction)
                        bell_pepper.forward(self.size * 11)
                        bell_pepper.pendown()
                        bell_pepper.circle(13)
                        direction += 360 / self.size
            elif choice == "4":
                if Ingredient(10, "Shrimp") in self.topping.values():
                    print("Shrimps are already added.")
                else:
                    print("Shrimp is added.")
                    # Add toppings to the dictionary to calculate pizza prices.
                    self.topping[len(self.topping)] = Ingredient(10, "Shrimp")
                    direction = 0
                    # Create a turtle (shrimp) according to the specified degree.
                    for _ in range(self.size):
                        shrimp = Turtle(visible=False)
                        shrimp.penup()
                        shrimp.hideturtle()
                        shrimp.color("#FF8B3D")
                        shrimp.pensize(10)
                        shrimp.speed(0)
                        shrimp.left(direction)
                        shrimp.forward(self.size * 7)
                        shrimp.pendown()
                        shrimp.circle(10, 180)
                        direction += 360 / self.size
            elif choice == "5":
                if Ingredient(6, "Pepperoni") in self.topping.values():
                    print("Pepperonis are already added.")
                else:
                    print("Pepperoni is added.")
                    # Add toppings to the dictionary to calculate pizza prices.
                    self.topping[len(self.topping)] = Ingredient(6, "Pepperoni")
                    direction = (360/self.size)*1.7
                    # Create a turtle (pepperoni) according to the specified degree.
                    for _ in range(self.size):
                        pepperoni = Turtle(visible=False)
                        pepperoni.hideturtle()
                        pepperoni.penup()
                        pepperoni.shape("circle")
                        pepperoni.color("#FF2C2C")
                        pepperoni.shapesize(1.5)
                        pepperoni.showturtle()
                        pepperoni.left(direction)
                        pepperoni.forward(self.size * 11)
                        direction += 360 / self.size
            elif choice == "6":
                if Ingredient(8, "Bacon") in self.topping.values():
                    print("Bacon are already added.")
                else:
                    print("Bacon is added.")
                    # Add toppings to the dictionary to calculate pizza prices.
                    self.topping[len(self.topping)] = Ingredient(8, "Bacon")
                    direction = 20
                    # Create a turtle (mushroom) according to the specified degree.
                    for _ in range(self.size):
                        bacon = Turtle(visible=False)
                        bacon.hideturtle()
                        bacon.penup()
                        bacon.shape("square")
                        bacon.color("#410600")
                        bacon.shapesize(0.5)
                        bacon.showturtle()
                        bacon.left(direction)
                        bacon.forward(self.size * 3)
                        direction += 360 / self.size
            elif choice == "q" or choice == "Q":
                break
            else:
                # If choosing something that is not a choice, the customer must select again.
                print("Please choose the valid ingredients")
            choice = input("Please choose the ingredients(enter q to quit): ")

    def pizza_price(self):
        """Calculate the price of the pizza selected by the customer."""
        total_price = 0
        if self.size == 6:
            total_price += 100
        elif self.size == 8:
            total_price += 200
        elif self.size == 12:
            total_price += 300
        if self.flour == "thin_and_crispy":
            total_price += 50
        elif self.flour == "thick":
            total_price += 100
        # Let the for loop calculate the price of the pizza topping from the Ingredient class.
        for topping in self.topping.values():
            total_price += topping.food_price(self.size)
        self.price = total_price

    def pizza_screen(self):
        """Create turtle graphics of pizza."""
        screen = Screen()
        screen.setup(800, 600)
        screen.bgpic("Table.gif")
        screen.update()
        self.pizza_size()
        print("---------------------------")
        pizza = Turtle(visible=False)
        pizza.hideturtle()
        pizza.penup()
        pizza.speed(0)
        pizza.color("#F5AA42")
        pizza.pensize(self.size + 6)
        pizza.sety(-(self.size * 20))
        pizza.pendown()
        pizza.begin_fill()
        pizza.fillcolor("#FACD8E")
        pizza.circle(self.size * 20)
        pizza.end_fill()
        self.pizza_flour()
        print("---------------------------")
        self.pizza_sauce()
        print("---------------------------")
        sauce = Turtle(visible=False)
        sauce.penup()
        # Check what sauce the customer chooses and let the turtle draw it.
        if self.sauce == "tomato":
            sauce.color("#B52A04")
        elif self.sauce == "thousand_island":
            sauce.color("#FB8B23")
        sauce.hideturtle()
        sauce.pensize(self.size + 6)
        sauce.sety(-(self.size * 17))
        sauce.pendown()
        sauce.begin_fill()
        sauce.circle(self.size * 17)
        sauce.end_fill()
        self.pizza_topping()
        print("Your pizza is done!!")
        print("---------------------------")
        self.pizza_price()

    def write_file_pizza(self):
        """Write down the size, dough, sauce, toppings and price of the pizza that the customer chooses."""
        toppings = [topping.type for topping in self.topping.values()]
        try:
            with open("pizza.json", "r") as pizza_file:
                pizza_data = json.load(pizza_file)
            data = {
                len(pizza_data)+1: {
                    "size": self.size,
                    "flour": self.flour,
                    "sauce": self.sauce,
                    "topping": toppings,
                    "price": self.price
                }
            }
            pizza_data.update(data)
            with open("pizza.json", "w") as pizza_file:
                json.dump(pizza_data, pizza_file, indent=4)
        except FileNotFoundError:
            data = {
                1: {
                    "size": self.size,
                    "flour": self.flour,
                    "sauce": self.sauce,
                    "topping": toppings,
                    "price": self.price
                }
            }
            with open("pizza.json", "w") as pizza_file:
                json.dump(data, pizza_file, indent=4)
