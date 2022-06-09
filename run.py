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
    while True:
        food_exp = input('Enter FOOD EXPENSES:')
        if (validate_values(food_exp)):
            print(f'Data provided is {food_exp}')
    print('Valid data')

get_expense_data()


def validate_values(values):
    """Validating expense values to be integers"""
    try:
        [int(value) for value in values]
        raise ValueError(
            f'Enter whole number / integer only.'
        )
    except ValueError as e:
        print(f'Invalid data {e}. Please try again..\n')
        return False
    return True

