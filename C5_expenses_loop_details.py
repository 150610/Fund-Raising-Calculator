# functions go here
def num_check(question, num_type = "float"):
    """Checks that response is a float/integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."

    else:
        error = "Please enter an integer that is more 0."


    while True:
        try:

            if num_type =="float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def not_blank(question):
    """Checks that a user response in not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")

def get_expenses(exp_type):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_items = []

    # expenses dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        # checks users enter at least one variable expense
        if (exp_type =="variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("Oops - you have not entered anything. "
                  "You need at least one item. ")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    # return all items for noe so we can check loop
    return all_items


# main routine

# print("Getting Variable Costs...")
# variable_expenses =get_expenses("variable")
# num_variable = len(variable_expenses)
# print(f"You entered {num_variable} items")
# print()

print("Getting Fixed Costs...")
fixed_expenses =get_expenses("fixed")
num_variable = len(fixed_expenses)
print(f"You entered {num_variable} items")
print()