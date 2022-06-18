"""Expense Tracker App"""
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
    year = validate_year_data('Enter Year (Ex. 2022):\n', 2022, 2022, 4)
    exp_ls.append(year)
    month = int_validation('Enter Month (Ex. 1 - 12):\n', 1, 12)
    exp_ls.append(month)
    week_number = int_validation(
        'Enter Week Number (Ex. 1 - 4):\n', 1, 4)
    exp_ls.append(week_number)
    food_exp = int_validation('Enter FOOD EXPENSES:\n', 0, None)
    exp_ls.append(food_exp)
    car = int_validation('Enter CAR EXPENSES:\n', 0, None)
    exp_ls.append(car)
    chidlcare = int_validation('Enter CHILDCARE EXPENSES:\n', 0, None)
    exp_ls.append(chidlcare)
    utilities = int_validation('Enter UTILITIES EXPENSES:\n', 0, None)
    exp_ls.append(utilities)
    mortgage = int_validation('Enter MORTGAGE EXPENSES:\n', 0, None)
    exp_ls.append(mortgage)
    shopping = int_validation('Enter SHOPPING EXPENSES:\n', 0, None)
    exp_ls.append(shopping)
    return exp_ls


def validate_year_data(msg, _min=None, _max=None, no_of_digits=None):
    """Years Entry validation"""
    try:
        number = int(input(msg))
        if no_of_digits is not None:
            if len(str(number)) != no_of_digits:
                raise ValueError(
                    "Please enter values in 4 digits like 2022...."
                    )
        if _min is not None and number < _min:
            raise ValueError(
                "Year input range should be 2022 "
                )
        if _max is not None and number > _max:
            raise ValueError(
                "Year input range should be 2022 "
                )
        return number
    except ValueError as error_msg:
        print(f'Invalid entry.. {error_msg}. Please try again..\n')
    return validate_year_data(msg, _min, _max)


def int_validation(msg, _min=None, _max=None):
    """Integer validation"""
    try:
        number = int(input(msg))
        if _min is not None and number < _min:
            raise ValueError("Input should be greater than " + str(min))
        if _max is not None and number > _max:
            raise ValueError("Input should be less than " + str(max))
        return number
    except ValueError as error_msg:
        print(f'Invalid entry.. {error_msg}. Please try again..\n')
    return int_validation(msg, _min, _max)


def update_worksheet(data1):
    """Update worksheets with data"""
    print('Updating worksheet...\n')
    worksheet_to_update = SHEET.worksheet('EXPENSE')
    worksheet_to_update.append_row(data1)
    print('worksheet updated successfully.\n')
    return data1


def total_calculation(data):
    """Calculating expenses total"""
    exp_dt = data[3:9]
    sum_of_expenses = sum(exp_dt)
    return sum_of_expenses


def program_continue(msg):
    """Program continue function after each operation"""
    try:
        answer = input(msg).upper()
        if answer == 'Y':
            main()
        elif answer == 'N':
            exit()
            print("Press 'Run Program' button to Refresh the page.")
        else:
            raise ValueError("Invalid selection..")
    except ValueError as err_msg:
        print(f"{err_msg} Please try again")
        program_continue(msg)
        return


def operation_selections(msg):
    """Operation selection function"""
    try:
        selection = input(msg).upper()
        if selection == 'A':
            budget_list = budget_page()
            budget_page_update(budget_list)
        elif selection == 'B':
            print("Please Enter the details of expenses & update it.")
            data = get_expense_data()
            total = total_calculation(data)
            data.append(total)
            update_worksheet(data)
        elif selection == 'C':
            print("C : View past entries\n")
            entries = SHEET.worksheet('EXPENSE').get_all_records()
            entry = []
            for i in entries:
                entry.append(i)
            for j in entry:
                print(j)
        elif selection == 'D':
            print("Press 'Run Program' button to Refresh the page.")
            exit()
        else:
            raise ValueError("Invalid selection..")
    except ValueError as err_msg:
        print(f"{err_msg} Please try again")
        operation_selections(msg)
        return


def budget_page():
    """Gets data for the Budget worksheet."""
    yr_mnth = []
    print('Set a monthly budget amount for yourself.')
    year = validate_year_data(
        'Enter Current Year (Ex. 2022):\n', 2022, 2022, 4
        )
    yr_mnth.append(year)
    month = int_validation('Enter Month (Ex. 1 - 12):\n', 1, 12)
    yr_mnth.append(month)
    budget = input("Please set a budget amount:\n")
    yr_mnth.append(budget)
    return yr_mnth


def budget_page_update(data):
    """Budget worksheet update"""
    print("Updating Budget Page...")
    budget_worksheet_update = SHEET.worksheet('BUDGET')
    budget_worksheet_update.append_row(data)
    print("Budget Update Successful")
    return data


def expense_budget_difference():
    """Expenses & Budget difference"""
    # bdgt = SHEET.worksheet('BUDGET')
    exp = SHEET.worksheet('EXPENSE')
    # budget_amount = bdgt.row_values(-1)
    # exp_total = exp.row_values(-1)
    # difference = budget_amount - exp_total
    print(exp)
    return exp


def main():
    """This will run all the functions"""
    print("### 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝙴𝚇𝙿𝙴𝙽𝚂𝙴 𝚃𝚁𝙰𝙲𝙺𝙴𝚁 𝙰𝙿𝙿 !!! ###\n")
    print("SELECT THE FUNCTION YOU WOULD LIKE TO DO TODAY:\n")
    operation_selections(
        "A : Set Monthly Budget and update it to Google Sheet.\n" +
        "B : Enter expense data & update it to a google sheet.\n" +
        "C : View past entries\n" + "D : Exit\n")
    program_continue("Do you wish to continue. Answer (Y / N)- \n")


main()
