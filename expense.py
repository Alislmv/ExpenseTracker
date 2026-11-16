import uuid
from datetime import date
from storeage import *
from validation import *
from exceptions import expensesNotFound


def addExpense(title, amount, category):
    expenses = loadExpenses()

    expense = {
        "id": str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmount(amount),
        "category": validateCategory(category),
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    saveExpenses(expenses)

    return expense


def getAllExpenses():
    return loadExpenses()


def serachExpense(expenseID):
    expenses = loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            return e
        
    expensesNotFound()


def updateExpense(expenseID, title, amount, category):
    expenses = loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            e["title"] == validateTitle(title)
            e["amount"] == validateAmount(amount)
            e["category"] == validateCategory(category)

            saveExpenses(expenses)

            return e

    expensesNotFound()


def deleteExpense(expenseID):
    expenses = loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            expenses.remove(e)

            saveExpenses(expenses)

            return True

    expensesNotFound()