"""Expense Tracker"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expense_record')


def get_expense_data():
    """This function gets the all the expenses data from the user."""
    exp_ls = []
    year = year_validation('Enter Year (Ex. 2022):', 2020, 2030, 4)
    exp_ls.append(year)
    month = months_and_weeks_validation('Enter Month (Ex. 1 - 12):', 1, 12)
    exp_ls.append(month)
    week_number = months_and_weeks_validation('Enter Week Number (Ex. 1 - 4):', 1, 4)
    exp_ls.append(week_number)
    food_exp = expenses_validation('Enter FOOD EXPENSES:', 1, None)
    exp_ls.append(food_exp)
    car = expenses_validation('Enter CAR EXPENSES:', 0, None)
    exp_ls.append(car)
    chidlcare = expenses_validation('Enter CHILDCARE EXPENSES:', 0, None)
    exp_ls.append(chidlcare)
    utilities = expenses_validation('Enter UTILITIES EXPENSES:', 0, None)
    exp_ls.append(utilities)
    mortgage = expenses_validation('Enter MORTGAGE EXPENSES:', 0, None)
    exp_ls.append(mortgage)
    shopping = expenses_validation('Enter SHOPPING EXPENSES:', 0, None)
    exp_ls.append(shopping)
    return exp_ls


def year_validation(msg, min=None, max=None, no_of_digits=None):
    """Years Entry validation"""
    try:
        number = int(input(msg))
        if no_of_digits:
            if len(str(number)) != no_of_digits:
                raise ValueError('Please enter values in 4 digits like 2020....')
        if min and number < min:
            raise ValueError("Year input range should be in the range of {2020 - 2030} ")
        if max and number > max:
            raise ValueError("Year input range should be in the range of {2020 - 2030} ")
        return number
    except ValueError as e:
        print(f'Invalid entry.. {e}. Please try again..\n')
    return year_validation(msg, min, max)


def months_and_weeks_validation(msg, min=None, max=None):
    """Month and Weeks Entry validation"""
    try:
        number = int(input(msg))
        if min and number < min:
            raise ValueError("Input should be greater than " + str(min))
        if max and number > max:
            raise ValueError("Input should be less than " + str(max))
        return number
    except ValueError as e:
        print(f'Invalid entry.. {e}. Please try again..\n')
    return months_and_weeks_validation(msg, min, max)


def expenses_validation(msg, min=None, max=None):
    """Month and Weeks Entry validation"""
    try:
        number = int(input(msg))
        if min and number < min:
            raise ValueError("Input should be greater than " + str(min))
        if max and number > max:
            raise ValueError("Input should be less than " + str(max))
        return number
    except ValueError as e:
        print(f'Invalid entry.. {e}. Please try again..\n')
    return expenses_validation(msg, min, max)

# def expenses_validation(msg, min=None):
#     """Month and Weeks Entry validation"""
#     try:
#         number = int(input(msg))
#         if min and number < min:
#             raise ValueError("Input should be greater than " + str(min))
#         return number
#     except ValueError as e:
#         print(f'Invalid entry.. {e}. Please try again..\n')
#     return expenses_validation(msg, min)


def update_worksheet(data1):
    """Update worksheets with data"""    
    print('Updating worksheet...\n')
    worksheet_to_update = SHEET.worksheet('EXPENSE')
    worksheet_to_update.append_row(data1)
    print('worksheet updated successfully.\n')
    return data1


def total_calculation(data):
    """Calculating expenses total"""
    dt = data[3:9]
    sum_of_expenses = sum(dt)
    return sum_of_expenses


def operation_selections(msg):
    try:
        selection = input(msg).upper()
        if(selection == 'A'):
            print("Please Enter the details of expenses & update it.")
            data = get_expense_data()
            total = total_calculation(data)
            data.append(total)
            update_worksheet(data)
        elif(selection == 'B'):
            print("B : View past entries")
            entries = SHEET.worksheet('EXPENSE').get_all_records()
            print(entries)
        elif(selection == 'C'):
            print("C : Exit")
            exit()
        else:
            raise ValueError("Invalid selection..")
            return selection
    except ValueError as e:
        print(f"{e} Please try again")
    return operation_selections(msg)
    

def main():
    """This will run all the functions"""
    print()
    print("Welcome to your Expense Tracker\n")
    print("Which operation would you like to do today:\n")
    opt_sel = operation_selections("A : Enter expense data & update, B : View past entries, C : Exit\n")
    print(opt_sel)


main()
