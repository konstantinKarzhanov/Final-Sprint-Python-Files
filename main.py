# Semester 1 - Final Sprint Week - Simpson Carpet World Python Program
# Group 3 - Michael Bennett, Matt Davis, Evan Holloway, Kostiantyn Karzhanov, Daniel Shepelev, Michael Sheridan
# Last Modified - April 4th, 2023

# Import Statements
import re
import datetime

# Lists for validation and receipts 
valid_prov = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
branch_list = ["St. John's", "Mt. Pearl", "Carbonear", "Northern Bay"]

# Read data from the file defaults.dat
f = open('defaults.dat', 'r')
EMP_NUM = int(f.readline().strip())
INV_NUM = int(f.readline())
COMMISSION_RATE = float(f.readline())
BONUS_THRESHOLD = int(f.readline())
COMMISSION_BONUS_AMT = int(f.readline())
REORDER_NUM = int(f.readline())
CUSTOMER_NUM = int(f.readline())
ORDER_NUM = int(f.readline())
HST_RATE = float(f.readline())
f.close()


def option_one():
    global EMP_NUM
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

    # City, mandatory input, converted to Title-case
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

    # Postal Code, mandatory input, must be valid format as X0X 0X0
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
            phone_num = phone_num[:3] + "-" + phone_num[3:6] + "-" + phone_num[6:]
            break

    # Date hired, mandatory input, valid date
    while True:
        try:
            date_hired = input("Please enter date hired as dd-mm-yyyy: ")
            date_hired = datetime.datetime.strptime(date_hired, "%d-%m-%Y")
        except:
            print("Please enter a valid date: ")
        else:
            date_hired = datetime.datetime.strftime(date_hired, "%d-%m-%Y")
            break

    # Employee Branch Number, mandatory input
    while True:
        try:
            emp_branch_num = int(input("Please enter branch number (0-3): "))
        except:
            print("Please enter valid number")
        else:
            if emp_branch_num < 0 or emp_branch_num > 3:
                print("Please enter a valid branch number")
            else:
                break

    # Employee title, mandatory input, checked via regular expressions, Alpha only 20 character max size.
    pattern =r"^[a-zA-Z ]{0,20}$"
    while True:
        emp_title = input("Employee Title: "). title()
        if re.match(pattern, emp_title):
            break
        else:
            print("Invalid Title, Please re-enter")

    # Employee Salary, mandatory input
    while True:
        try:
            emp_salary = int(input("Employee Salary: "))
        except:
            print("Please enter a valid number")
        else:
            if emp_salary < 13000:
                print("This salary is below minimum wage, please re-enter")
            elif emp_salary > 100000:
                print("This salary is above the highest paid person at Sampson's Carpet, Please re-enter")
            else:
                break
    
    # Employee Skills, mandatory input, alpha only
    while True:
        emp_skills = input("Enter employee skill: ").title()
        if not emp_skills.isalpha():
            print("Please enter valid skill")
        else:
            break

    # Birthdate, mandatory input, valid date
    while True:
        try:
            birthdate = input("Please enter birthdate as dd-mm-yyyy: ")
            birthdate = datetime.datetime.strptime(birthdate, "%d-%m-%Y")
        except:
            print("Please enter a valid date: ")
        else:
            birthdate = datetime.datetime.strftime(birthdate, "%d-%m-%Y")
            break
    
    # Add all info to employee info list
    employee_info.append((EMP_NUM, emp_f_name, emp_l_name, str_add, city, prov, post_code, phone_num, date_hired, emp_branch_num, emp_title, emp_salary, emp_skills, birthdate))

    # Append info to Employee Log data file
    f = open('employeeLog.dat', 'a')
    for data in employee_info:
        f.write(",".join(map(str, data)) + "\n")
    f.close()

    # Updating defaults file to new Employee Number
    EMP_NUM += 1
    f = open("defaults.dat", 'w')
    f.write("{}\n".format(str(EMP_NUM)))
    f.write("{}\n".format(str(INV_NUM)))
    f.write("{}\n".format(str(COMMISSION_RATE)))
    f.write("{}\n".format(str(BONUS_THRESHOLD)))
    f.write("{}\n".format(str(COMMISSION_BONUS_AMT)))
    f.write("{}\n".format(str(REORDER_NUM)))
    f.write("{}\n".format(str(CUSTOMER_NUM)))
    f.write("{}\n".format(str(ORDER_NUM)))
    f.close


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
