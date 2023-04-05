import re
import datetime

valid_prov = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

while True:
# Allow user to enter as many employees as needed, option to escape loop at end via input statement

# User Validated Inputs
# First name, mandatory input, alpha only, converted to Title-case
    while True:
        emp_f_name = input("First Name:").title()
        if emp_f_name == "":
            print("First name cannot be empty, Please re-enter")
        elif not emp_f_name.isalpha():
            print("Please enter a valid name")
        else:
            break

# Last name, mandatory input, alpha only, converted to Title-case
    while True:
        emp_l_name = input("Last Name:").title()
        if emp_l_name == "":
            print("Last name cannot be empty, Please re-enter")
        elif not emp_l_name.isalpha():
            print("Please enter a valid name")
        else:
            break

# Street Address, mandatory input, converted to Title-case
    while True:
        str_add = input("Street Address:").title()
        if str_add == "":
            print("Street address cannot be empty, Please re-enter")
        else:
            break

# City, mandatory input, converted to Title-case -------- need to make exception for '--------------
    while True:
        city = input("City:").title()
        if city == "":
            print("City cannot be empty, Please re-enter")
        else:
            break

# Province, mandatory input,converted to Upper-case, compared to valid list of provinces
    while True:
        prov = input("Province (XX):").upper()
   
   
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
            date_hired = input("Please enter date hired as dd-mm-yyyy")
            # date_hired = datetime.datetime.strftime(%d-%m-%Y)