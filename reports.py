from file_handler import read_json
import csv


def list_expenses():
    expenses = read_json("expenses.json",[])
    print("list of all expenses : ")
    for expense in expenses:
        print(f"{expense}\n")


def monthly_summary():
    expenses = read_json("expenses.json",[])
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



def filter_with_cat():
    expenses = read_json("expenses.json",[])
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



def export_to_csv():
    expenses = read_json("expenses.json",[])

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