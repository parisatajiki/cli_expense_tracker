import json
import csv
import os
import datetime


expenses = []

#json file
if not os.path.exists("expenses.json"):
    with open("expenses.json","w") as f :
        json.dump(expenses,f)



def add_expense():
    with open("expenses.json","r") as f :
        try :
            expenses = json.load(f)
        except json.JSONDecodeError :
            expenses = []

    new_expense = {
        "id" : len(expenses) + 1,
        "date" : str(datetime.datetime.now()),
        "description": input("Enter your descriptio of expense : "),
        "amount": input("Enter amount of expense : "),
        "category": input("Enter category of expense : "),
    }
    expenses.append(new_expense)

    with open("expenses.json","w") as f :
        json.dump(expenses,f)



def list_expenses():
    with open("expenses.json","r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []

    print("list of all expenses : ")
    for expense in expenses:
        print(f"{expense}\n")


def update_expense():
    with open("expenses.json","r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []
    print("Which expense would you like to update?")
    print(expenses)
    id = int(input("Please enter the ID of the task you wish to update : "))
    found_expense = False
    for expense in expenses :
        if expense["id"] == id :
            print(f"Current expense: {expense}")
            new_description = input("Enter new description (if you dont have update press enter key ) : ")
            new_amount = input("Enter new amount (if you dont have update press enter key ) : ")
            new_category = input("Enter new category (if you dont have update press enter key ) : ")
            if new_description != "":
                expense["description"] = new_description
            if new_amount != "":
                expense["amount"] = new_amount
            if new_category != "":
                expense["category"] = new_category   
            print(f"Task updated: {expense}")
            found_expense = True                  
    if found_expense == False:
        print("Invalid id.")

    with open("expenses.json","w") as f :
        json.dump(expenses,f)







while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Show Summary")
    print("6. Show Monthly Summary")
    print("7. Export to CSV")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        pass
        # delete_expense()
    elif choice == "5":
        pass
        # show_summary()
    elif choice == "6":
        pass
        # monthly_summary()
    elif choice == "7":
        pass
        # export_to_csv()
    elif choice == "0":
        break
    else:
        print("Invalid choice (Enter number between 0 - 8 ).")
