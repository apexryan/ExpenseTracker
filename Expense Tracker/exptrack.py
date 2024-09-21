from expense import Expense 
import calendar
import datetime

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = float(input("Enter your budget for this month : "))

    #expense = get_user_expense()

    #save_exp_to_file(expense, expense_file_path)

    summarize_expenses(expense_file_path,budget)
    pass

def get_user_expense():
    print(f"Receiving User Expense")
    expense_name=input("Enter expense name : ")
    expense_amount=float(input(f"Enter expense amount : "))
    print(f"Your expense is {expense_name}, ₹{expense_amount}")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Entertainment",
        "Others"
    ]

    while True:
        print(f"Select expense category from the following options : ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter category number {value_range} : ")) - 1

        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, amount=expense_amount, category=selected_category)
            return new_expense
        else:
            print(f"Invalid input. Please enter a number between {value_range}")


        break
    
def save_exp_to_file(expense: Expense, expense_file_path):
    print(f"Saving expenses : {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path,budget):
    print(f"Summarizing Expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
             amount_by_category[key] = expense.amount

    print("Expenses by Category")        
    for key, amount in amount_by_category.items():
        print(f"  {key}: ₹{amount:.2f}")

    total_spent = sum([expense.amount for expense in expenses])
    print(f"You've spent ₹{total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Your remaning budget is ₹{remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print("Remaning days in current month : ",remaining_days)

    daily_budget = remaining_budget / remaining_days
    print(purple(f"Budget Per Day : ₹{daily_budget:.2f}"))

def purple(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()