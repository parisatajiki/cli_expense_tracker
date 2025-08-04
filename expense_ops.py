import datetime
from file_handler import read_json , write_json

def add_expense():
    expenses = read_json("expenses.json",[])
    new_expense = {
        "id" : len(expenses) + 1,
        "date" : str(datetime.datetime.now()),
        "description": input("Enter your descriptio of expense : "),
        "amount": input("Enter amount of expense : "),
        "category": input("Enter category of expense : "),
    }
    expenses.append(new_expense)

    write_json("expenses.json",expenses)



def update_expense():
    expenses = read_json("expenses.json",[])
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

    write_json("expenses.json",expenses)



def delete_expense():
    expenses = read_json("expenses.json",[])

    print("Which expense would you like to delete?")
    print(expenses)
    id = int(input("Please enter the ID of the task you wish to delete : "))
    found = False
    for expense in expenses:
        if expense["id"] == id:
            print(f"Current expense: {expense}")
            expenses.remove(expense)
            print("deleted.")
            found = True
    if found==False:
        print("Invalid id.")

    write_json("expenses.json",expenses)