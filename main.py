from Pizza import Pizza
from Hamburger import Hamburger
from Customer import Customer
import json
from time import strftime, localtime

customer = Customer()
print("What’s your name?")
customer.name = input("Name : ")
print("What’s your birthday? (DD/MM/YYYY)")
birthday = input("Birthday : ")
# To see if you entered your birthday accurately or not.
try:
    with open("customer.json", "r") as customer_file:
        customer_data = json.load(customer_file)
    try:
        while int(birthday.split("/")[2]) >= int(strftime("%Y", localtime())) or int(birthday.split("/")[1]) > 12 or \
                int(birthday.split("/")[0]) > 31 or \
                int(birthday.split("/")[0]) != customer_data[customer.name]["birth_date"] \
                or int(birthday.split("/")[1]) != customer_data[customer.name]["birth_month"] or \
                int(birthday.split("/")[2]) != customer_data[customer.name]["birth_year"]:
            print("Invalid Input.")
            birthday = input("Birthday : ")
            if int(birthday.split("/")[0]) == customer_data[customer.name]["birth_date"] \
                    and int(birthday.split("/")[1]) == \
                    customer_data[customer.name]["birth_month"] \
                    and int(birthday.split("/")[2]) == customer_data[customer.name]["birth_year"]:
                print(f"Welcome Back {customer.name}!!")
                break
    except KeyError:
        while int(birthday.split("/")[2]) >= int(strftime("%Y", localtime())) or int(birthday.split("/")[1]) > 12 or \
                int(birthday.split("/")[0]) > 31:
            print("Invalid Input.")
            birthday = input("Birthday : ")
        print(f"Hello {customer.name}!!")
except FileNotFoundError:
    pass
# Separate birthdays as days, months, or years.
customer.birthday = (int(birthday.split("/")[0]), int(birthday.split("/")[1]),  int(birthday.split("/")[2]))
if customer.birthday_check() == 0.5:
    print("Oh!Happy birthday^^")
elif customer.birthday_check() == 0.9:
    print("Oh!Happy birth month^^")
print("---------------------------")
print("1.Pizza")
print("2.Hamburger")
choice = input("What do you want to eat?: ")
# Check if you choose pizza or a hamburger.
while choice != "1" and choice != "2":
    print("Please choose the valid menu")
    choice = input("What do you want to eat?: ")
if choice == "1":
    """Show the pizza making screen."""
    print("You choose pizza.")
    print("It’s cooking time!!")
    print("---------------------------")
    pizza = Pizza()
    pizza.pizza_screen()
    customer.change_money(pizza.price)
    pizza.write_file_pizza()
elif choice == "2":
    """Show the hamburger making screen."""
    print("You choose hamburger.")
    print("It’s cooking time!!")
    print("---------------------------")
    hamburger = Hamburger()
    hamburger.burger_screen()
    customer.change_money(hamburger.price)
    hamburger.write_file_burger()
