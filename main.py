import json
import os

from budget import set_budget , show_summary
from expense_ops import add_expense , delete_expense , update_expense
from file_handler import read_json , write_json
from reports import list_expenses, filter_with_cat, monthly_summary , export_to_csv


expenses = []
budget = 0
#json file
if not os.path.exists("expenses.json"):
    with open("expenses.json","w") as f :
        json.dump(expenses,f,indent=4)

if not os.path.exists("budget.json"):
    with open("budget.json","w") as f :
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