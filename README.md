# EXPENSE TRACKER APP 

* Expense Tracker is an python terminal application running in the CI mock terminal with Heroku.
* This facilates the user to setup monhtly budgets, store expenses data, view previous data entries.

![Responsive Screen](/assets/responsiveScreens.jpg)

# HOW IT WORKS
## Welcome Screen

* Welcome screen with selction options for the user to select which type os operation to perform.
* User can type the character provided with the message to navigate for the operation type.

![Welcome Screen](/assets/mainPage.jpg)

## Budget Window

* User can set the budget by entering Year, Month & Budget Amount.
* It also updates the provided data to the dedicated Google sheet.
* After the operation suucessfully executes there is a message for to continue or leave the program.
* If answered Yes it takes you back to the Welcome screen to perform another operation.

![Budget Window](/assets/budgetWdw.jpg)

## Expenses Window

* User can set the budget by entering Year, Month & Week Number and expenses catatgies like Food , Car , Childcare, Utilities, Mortage, Shopping.
* It also updates the provided data to the dedicated Google sheet.
* After the operation suucessfully executes there is a message for to continue or leave the program.
* If answered Yes it takes you back to the Welcome screen to perform another operation.

![Expenses Window](/assets/expensesWdw1.jpg)
![Expenses Window](/assets/expensesWdw2.jpg)

## View Previous Entries

* User can also view all the data entries performed previous through the app dispalyed as lists.

![View Previous Entries](/assets/viewEntries.jpg)

## Exit Window

* User can exit the app which is navigated by a message to press the 'Run Program' button in the app.

![Exit Window](/assets/exit.jpg)

# DATA MODEL

* Its a relational flow data model which explains how the app is working.
![DATA MODEL](/assets/dataModel.jpg)

# TESTING
## Validator Testing
* Passed the code through a PEP8 linter and confirmed no problems.
![PEP8](/assets/pep8Result.jpg)
Inavlid inputs validation check done with no errors.

# DEPLOYMENT
* Project was deployed using Heroku.
* New app craeted and named.
* Set config vars with PORT & CREDS details.
* Deplyment method connected to GitHub
* Automatic Deplyment set for each push updates.
*  Manually deplyment done for Heroku link.

![App Link](https://expense-tracker-4321.herokuapp.com/)

# Credits

* CI deplyment terminal.
* Love sandwiches project for coding ideas.
* Stack Overflow for various syntax logics.



