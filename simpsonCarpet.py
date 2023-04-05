# Semester 1 - Final Sprint Week - Simpson Carpet World Python Program
# Group 3 - Michael Bennett, Matt Davis, Evan Holloway, Kostiantyn Karzhanov, Daniel Shepelev, Michael Sheridan
# Last Modified - April 4th, 2023

# Import Statements
import datetime


# Functions
def option_one():
    pass


def option_two():
    pass


def option_three():
    pass


def option_four():
    pass


def option_five():
    pass


def option_six():
    pass


def option_seven():
    pass


def option_eight():
    pass




# Start of main function

# While true statement to continuously loop over main menu options until user selects option "9" to quit.



while True:
    print()
    print("   Simpson Carpet World")
    print("  Company Services System")
    print()
    print('1. Enter a New Employee.')
    print('2. Enter a New Customer.')
    print('3. Enter a New Inventory Item.')
    print('4. Record Customer Purchase.')
    print('5. Print Employee Listing.')
    print('6. Print Customers By Branch.')
    print('7. Print Orders By Customer,.')
    print('8. Print Recorder Listing.')
    print('9. Exit Menu')
    print()
    print()

    while True:
        try:
            choice = int(input("Please make a list selection: "))
        except:
            print("Please enter a valid number")
        else:
            if choice < 1 or choice > 9:
                print("Please enter a number from 1-9 to make a selection")
            else:
                break

    if choice == 1:
        print()
        print('First option')
        print("-------------")
        option_one()
    elif choice == 2:
        print()
        print('Second option')
        print("-------------")
        option_two()
    elif choice == 3:
        print()
        print('Third option')
        print("------------")
        option_three()
    elif choice == 4:
        print()
        print('Fourth option')
        print("-------------")
        option_four()
    elif choice == 5:
        print()
        print('Fifth option')
        print("-------------")
        option_five()
    elif choice == 6:
        print()
        print('Sixth option')
        print("-------------")
        option_six()
    elif choice == 7:
        print()
        print('Seventh option')
        print("--------------")
        option_seven()
    elif choice == 8:
        print()
        print('Eighth option')
        print("-------------")
        option_eight()
    elif choice == 9:
        exit()
