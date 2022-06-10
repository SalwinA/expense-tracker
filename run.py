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
    year = input('Enter Year (Ex. 2022):')
    # validate_year_data(year)
    exp_ls.append(year)
    month = input('Enter Month (Ex. 1 - 12):')
    exp_ls.append(month)
    week_number = input('Enter Week Number (Ex. 1 - 4):')
    exp_ls.append(week_number)
    food_exp = input('Enter FOOD EXPENSES:')
    exp_ls.append(food_exp)
    car = input('Enter CAR EXPENSES:')
    exp_ls.append(car)
    chidlcare = input('Enter CHILDCARE EXPENSES:')
    exp_ls.append(chidlcare)
    utilities = input('Enter UTILITIES EXPENSES:')
    exp_ls.append(utilities)
    mortgage = input('Enter MORTGAGE EXPENSES:')
    exp_ls.append(mortgage)
    shopping = input('Enter SHOPPING EXPENSES:')
    exp_ls.append(shopping)
    ls = [int(i) for i in exp_ls]
    return ls

# def validate_year_data(values):
#     """Year Input Validation"""
#     try:
#         if(len(values) != 4):
#             raise ValueError('Please enter integer values.')
#     except ValueError as e:
#         print(f'Error{e}')


data = get_expense_data()
print(data)


def update_worksheet(data1):
    """Update worksheets with data"""    
    print('Updating worksheet...\n')
    worksheet_to_update = SHEET.worksheet('EXPENSE')
    worksheet_to_update.append_row(data1)
    print('worksheet updated successfully.\n')


update_worksheet(data)
