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

        try:

            choice = int(input("enter your choice: "))

            if choice == 1:
                title = input("enter expense title: ")
                amount = input("enter expense amount: ")
                category = input("enter expense category: ")

                expense = addExpense(title, amount, category)
                print("Expense added successfully!")
                print("Expense ID:", expense["id"])

                return expense

            elif choice == 2:
                expenses = getAllExpenses()

                if not expenses:
                    print("No expenses found!")

                else:
                    for e in expenses:
                        print(f"""
                        ID: {e["id"]}
                        Title: {e["title"]}
                        Amount: {e["amount"]}
                        Category: {e["category"]}
                        Date: {e["date"]}
                        """)

            elif choice == 3:
            
                expenseID = input("enter expense id: ")
                title = input("Enter new title: ")
                amount = input("Enter new amount: ")
                category = input("Enter new category: ")

                expense = updateExpense(expenseID, title, amount, category)

                print("Expense updated successfully!")

            elif choice == 4:
                expenseID = input("enter expense id: ")
                deleteExpense(expenseID)

                print("Expense deleted successfully!")

            elif choice == 5:
                expenseID = input("enter expense id: ")
                expense = serachExpense(expenseID)

                print(f"""
                ID: {expense["id"]}
                Title: {expense["title"]}
                Amount: {expense["amount"]}
                Category: {expense["category"]}
                Date: {expense["date"]}
                """)

            elif choice == 6:
                total = totalExpenses()
                print(f"Total Expense: {total}")

            elif choice == 7:
                print("Categories:")
                for category in CATEGORIES:
                    print(f"- {category}")

            elif choice == 8:
                filePath = exportToCSV()
                print(f"Expenses exported successfully to {filePath}")

            elif choice == 0:
                print("Exiting...")
                break

        except Exception as e:
            print(e)

startApp()   