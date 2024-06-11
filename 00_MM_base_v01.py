# functions go here

# Checks user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

    else:
        print("please enter yes or no")


# checks that user response is not blank
def not_blank(question):


    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# main routine starts here

# calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors 65+
    else:
        price = 6.5

    return price

# checks that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 2
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[0] or response == item:
                return item

        print("Error")


# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0
# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions")

if want_instructions == "yes":
    print("Instructions go here")

print()

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")


    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
            pass
    elif age < 12:
            print("Sorry you are too young for this movie")
            continue
    else:
            print("?? That looks like a typo, please try again. ")
            continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)

tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s " 
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
