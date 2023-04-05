import re
import datetime

valid_prov = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
# Read data from the file defaults.dat
f = open('defaults.dat', 'r')
employee_num = f.readline()
inventory_num = f.readline()
commission_rate = f.readline()
bonus_threshold = f.readline()
commission_bonus_amt = f.readline()
reorder_num = f.readline()
f.close()

def option_one():
    # User Validated Inputs
    # First name, mandatory input, alpha only, converted to Title-case
    employee_info = []
    while True:
        emp_f_name = input("First Name: ").title()
        if emp_f_name == "":
            print("First name cannot be empty, Please re-enter")
        elif not emp_f_name.isalpha():
            print("Please enter a valid name")
        else:
            break

    # Last name, mandatory input, alpha only, converted to Title-case
    while True:
        emp_l_name = input("Last Name: ").title()
        if emp_l_name == "":
            print("Last name cannot be empty, Please re-enter")
        elif not emp_l_name.isalpha():
            print("Please enter a valid name")
        else:
            break

    # Street Address, mandatory input, converted to Title-case
    while True:
        str_add = input("Street Address: ").title()
        if str_add == "":
            print("Street address cannot be empty, Please re-enter")
        else:
            break

    # City, mandatory input, converted to Title-case -------- need to make exception for '--------------
    while True:
        city = input("City: ").title()
        if city == "":
            print("City cannot be empty, Please re-enter")
        else:
            break

    # Province, mandatory input,converted to Upper-case, compared to valid list of provinces
    while True:
        prov = input("Province (XX): ").upper()

        if len(prov) != 2:
            print("Please re-enter province as (XX)")
        elif prov == "":
            print("Province field cannot be empty, Please re-enter")
        elif not prov in valid_prov:
            print("Please enter a valid province")
        else:
            break

    # Postal Code, mandatory input, must be valid format as X0X 0X0 ------ADD REPLACE STATEMENTS
    # The pattern below is used to compare against user input, this will be done using Regular Expressions
    # The pattern will accept a space or dash between postal code
    pattern = r"^[A-Z]\d[A-Z][ -]?\d[A-Z]\d$"

    while True:
        post_code = input("Postal Code: (e.g. A1A 1A1):   ").upper()
        if re.match(pattern, post_code):
            break
        else:
            print("Invalid postal code. Please re-enter")

    # Phone Number, mandatory input, 10 characters long
    while True:
        phone_num = input("Phone number (Without Spaces): ")
        phone_num = phone_num.replace("-", "")
        phone_num = phone_num.replace("/", "")
        if len(phone_num) != 10:
            print("Please format phone number as 10 digits without spaces")
        elif not phone_num.isdigit():
            print("Please enter a valid phone number")
        else:
            formatted_phone_num = phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
            break

    # Date hired, mandatory input, valid date
    while True:
        try:
            date_hired = input("Please enter date hired as dd-mm-yyyy: ")
            # date_hired = datetime.datetime.strftime(%d-%m-%Y)
            break
        except:
            print("You make fucking mistake in the date of hiring, common")

    employee_info.append((employee_num.strip(), emp_f_name, emp_l_name, str_add, city, prov, post_code, phone_num))

    f = open('employeeLog.dat', 'a')
    for data in employee_info:
        f.write(",".join(map(str, data)) + "\n")
    f.close()

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

while True:
    # Allow user to enter as many employees as needed, option to escape loop at end via input statement

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
