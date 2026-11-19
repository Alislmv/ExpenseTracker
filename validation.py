from exceptions import *

CATEGORIES = [
    "Food",
    "Shopping",
    "Education",
    "Health",
    "Entertainment",
    "Other"
]

def validateTitle(title):
    title = title.strip()

    if not title:
        invalidExpense("Title cannot be emty")

    return title

def validateAmount(amount):
    try:
        amount = float(amount)

    except ValueError:
        invalidExpense("Amount must be number")

    if amount <= 0:
        invalidExpense("Amount must be greather than 0!")

    return amount

def validateCategory(category):
    category = category
    
    if category not in CATEGORIES:
        invalidExpense("Invalid category!")

    return category

