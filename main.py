from expense import *
from reports import *
from validation import CATEGORIES


def showMenu():
    print("=" * 40)
    print("          EXPENSE TRACKER        ")
    print("=" * 40)
    print()

    print("""

    1. Add expense
    2. Show All Expenses
    3. Edit Expense
    4. Delete Expense
    5. Search Expense
    6. Show Total Expense
    7. Show Categories
    8. Export To CSV

    0. Exit

    """)
    print("=" * 40)

def startApp():
    while True:
        showMenu()

        choice = int(input("enter your choice: "))

        try:
            if choice == 1:
                title = input("enter expense title: ")
                amount = input("enter expense amount: ")
                category = input("enter expense category: ")

                expense = addExpense(title, amount, category)
                print("Expense added successfully!")
                print("Expense ID:", expense["id"])

        except:
            pass

startApp()   