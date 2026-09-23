def yes_no (question):
    """Checks that users answer yes/y or no/n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"

def instructions():
    """"Instructions"""

    print(make_statement("Instructions", "ℹ️"))

    print('''
This program will ask you for...
   - The name of the product you are selling
   - How many items you plan on selling
   - The costs for each component of the product 
     (variable expenses)
   - Whether or not you have fixed expenses (if you have
     fixed expenses, it will ask you what they are)
   - How much money you want to make (ie: your profit goal)
      
It will also ask you how much the recommended sales price should 
be rounded to.

The program outputs an itemised list of all the variable and fixed 
expenses (which includes the subtotals for these expenses).

Finally it will tell you how much you should sell each item for 
to reach your profit goal. 

The data will also be written to a text file which has the same
name as your product and today's date.     
      ''')


print(make_statement("Fund Raising Calculator","💸"))

want_instructions = yes_no("Do you want to read the instructions: ")
if want_instructions == "yes":
    instructions()