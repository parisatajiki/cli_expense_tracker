import json
import csv
import os
import datetime


expenses = []
budget = 0


#json file
if not os.path.exists("expenses.json"):
    with open("expenses.json","w") as f :
        json.dump(expenses,f,indent=4)

if not os.path.exists("budget.json"):
    with open("budget.json","w") as f :
        json.dump(budget,f,indent=4)


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
        json.dump(expenses,f,indent=4)



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
        json.dump(expenses,f,indent=4)




def delete_expense():
    with open("expenses.json","r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []

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

    with open("expenses.json","w") as f :
        json.dump(expenses,f,indent=4)




def show_summary():
    sum = 0
    with open("expenses.json","r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []
    for expense in expenses:
        sum += int(expense["amount"])

    print(f"your Summary {sum}")


    with open("budget.json","r") as f:
        try:
            budget = json.load(f)
        except json.JSONDecodeError:
            budget = 0

    if budget != 0 :
        if sum > budget:
            print(f"Warning: Your expenses have exceeded the budget you set.\n your budget = {budget}\n your expenses = {sum}")
        elif sum == budget:
            print(" You have reached your budget limit. :) ")
        else:
            print(f"your budget = {budget}.\n You're under budget. Keep it up!")





def monthly_summary():
    with open("expenses.json","r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []
    this_month = set()
    for expense in expenses:
        this_month.add(expense["date"][5:7])
    print(f"month : {this_month}")
    num = input("Enter your month do you see summary : ").strip().lower()
    summary = []
    n = False
    for expense in expenses:
        if num == expense["date"][5:7]:
            summary.append(expense)
            n = True
    if n == False:
        print("Invalid number.")
    else:
        print(f"your monthy summary :\n {summary} ")
            

    


def export_to_csv():
    with open("expenses.json","r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []

    with open("expenses.csv", "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['id','date','description','amount','category'])

        for expense in expenses:
            writer.writerow([
                expense['id'],
                expense['date'],
                expense['description'],
                expense['amount'],
                expense['category']
                ])
        file.close()


        

def filter_with_cat():
    with open("expenses.json","r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []

    this_cat = set()
    for expense in expenses:
        this_cat.add(expense["category"])
    print(f"Choose from these categories : {this_cat}")
    cat = input("Enter category : ").strip().lower()
    expense_cat = []
    found = False
    for expense in expenses:
        if expense["category"]== cat:
            expense_cat.append(expense)
            found = True
    if found == False:
        print("Invalid category.")
    else:
        print(f'expense with {cat} = {expense_cat}')





def set_budget():
    with open("budget.json","r") as f:
        try:
            budget = json.load(f)
        except json.JSONDecodeError:
            budget = 0

    budget = int(input("Enter budget to enable warning: "))
    print(f"Budget set to {budget}")

    with open("budget.json","w") as f:
        json.dump(budget,f,indent=4)







while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Set budget to enable warning")
    print("6. Show summary and warning for budget usage ")
    print("7. Show Monthly Summary")
    print("8. Export to CSV")
    print("9. Filter with category")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        set_budget()
    elif choice == "6":
        show_summary()
    elif choice == "7":
        monthly_summary()
    elif choice == "8":
        export_to_csv()
    elif choice == "9":
        filter_with_cat()
    elif choice == "0":
        break
    else:
        print("Invalid choice (Enter number between 0 - 8 ).")
