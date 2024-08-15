import time

# Welcome message
print("<---Welcome to Charman Pizzaria--->")

# functions go here
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")

# main routine goes here
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    print("Instructions go here")
time.sleep(1)  # Pause for a moment after displaying instructions, if any

# Function to check pizza type
def num_checker(question, low, high):
    while True:
        error = f"Enter a valid option between {low} and {high}"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)

# Function to check for yes or no input
def string_checker(question, valid_ans):
    while True:
        error = f"Enter a valid option from {valid_ans}"
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)
        print()

# Function to check string is not empty
def not_blank(question):
    error = "Enter a name"
    while True:
        user_name = input(question)
        if user_name != '':
            return user_name
        else:
            print(error)

# Variables
yes_no = ["yes", "no"]
deliv_option = ["delivery", "pick up"]
pizza_size_option = ["large", "medium", "small"]
drink_size_option = ["330ml", "750ml", "1.5L"]

pizza_order = []
pizza_order_size = []
drink_order = []
drink_order_size = []

print()
delivery = string_checker("Is this order for delivery or pick up? ", deliv_option)

if delivery == "delivery":
    print("There is a $6 surcharge for delivery")
    name = not_blank("Enter your name: ")
    phone_num = num_checker("Enter your phone number: ", 0, 9999999999)
    address = not_blank("Enter your address: ")
else:
    name = not_blank("Enter your name: ")
    phone_num = num_checker("Enter your phone number: ", 0, 9999999999)

print()
want_menu = string_checker(f"Hello {name}, would you like the menu? ", yes_no)


if want_menu == "yes":
    print('''\n
|------------MENU------------|  
----------------------------------------|                        
Gourmet:                         Num id |
Lamb Kebab                          1   |
Crispy BBQ Pork Belly               2   | 
Chicken Bacon & Aoli                3   |
Smokehouse Meat lover               4   |
Peri-Peri Chicken                   5   |
The Lot                             6   |
----------------------------------------|                                    
Traditional:                            |
Philly Cheese steak                 7   |
Supreme                             8   |
Double Bacon Cheeseburger           9   |
Butter Chicken                      10  |
BBQ Meat lovers                     11  |
Chicken Supreme                     12  |
----------------------------------------|
Value:                                  |
Cheesy Garlic Pizza                 13  |
Pepperoni                           14  |
Ham Cheese                          15  |
Simply Cheese                       16  |
Hawaiian                            17  |
Mega Pepperoni                      18  |
----------------------------------------|
Small | Medium | Large |
 $9   |   $12  |  $16  |
------|--------|-------|
''')

keep_going = "yes"

while keep_going == "yes":
    pizza_num_id = num_checker("Enter the pizza number: ", 1, 18)
    pizza_order.append(pizza_num_id)
    size = string_checker("What Size | Small | Medium | Large |: ", pizza_size_option)
    pizza_order_size.append(size)
    print(f"Great! You have selected a {size} pizza with ID {pizza_num_id}")
    print()
    keep_going = string_checker("Do you want to order another pizza? ", yes_no)

print(f"You have ordered the following pizzas: {pizza_order} sizes: {pizza_order_size}")

# Would you like the drink menu question
want_drink_menu = string_checker(f"Hello {name}, would you like the drink menu? ", yes_no)

if want_drink_menu == "yes":
    print('''\n
|-------Drink Menu-------|
Num id | Drink           |
1      | Lift            |
2      | Fanta           |
3      | Coke            |
4      | L & P           |
5      | Sprite          |
|------------------------|
Sizes: 330ml , 750ml, 1.5L
''')

    keep_going = "yes"

    while keep_going == "yes":
        drink_num_id = num_checker("Enter the drink number: ", 1, 5)
        drink_order.append(drink_num_id)
        drink_size = string_checker("What size | 330ml | 750ml | 1.5L |: ", drink_size_option)
        drink_order_size.append(drink_size)
        print(f"Great! You have selected a {drink_size} drink with ID {drink_num_id}")
        print()
        keep_going = string_checker("Do you want to order another drink? ", yes_no)

print(f"You have ordered the following drinks: {drink_order} sizes: {drink_order_size}")
# loading bar

time.sleep(2)
print("               ⣠⣤⣶⣶⣦⣄⣀")
time.sleep(2)
print("⠀            ⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀")
time.sleep(2)
print("⠀    ⠀       ⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀")
time.sleep(2)
print("      ⠀   ⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀")
time.sleep(2)
print("⠀ ⠀       ⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀")
time.sleep(2)
print(" ⠀     ⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇")
time.sleep(2)
print("⠀⠀    ⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇")
time.sleep(2)
print("⠀⠀   ⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀")
time.sleep(2)
print("⠀  ⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀")
time.sleep(2)
print(" ⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀")
time.sleep(2)
print(" ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀")
time.sleep(2)
print(" ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀")
time.sleep(2)
print(" ⠈⠓⠾⠇⠀⠀⠀⠀")


