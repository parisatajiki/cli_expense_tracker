from file_handler import read_json , write_json

def set_budget():
    budget = read_json("budget.json",0)
    budget = int(input("Enter budget to enable warning: "))
    print(f"Budget set to {budget}")
    write_json("budget.json",budget)


def show_summary():
    sum = 0
    expenses = read_json("expenses.json",[])
    for expense in expenses:
        sum += int(expense["amount"])
    print(f"your Summary {sum}")

    budget = read_json("budget.json",0)
    if budget != 0 :
        if sum > budget:
            print(f"Warning: Your expenses have exceeded the budget you set.\n your budget = {budget}\n your expenses = {sum}")
        elif sum == budget:
            print(" You have reached your budget limit. :) ")
        else:
            print(f"your budget = {budget}.\n You're under budget. Keep it up!")