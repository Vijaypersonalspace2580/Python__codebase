import csv
import os
if not os.path.exists('user.csv'):
    open('user.csv', 'w').close()
if not os.path.exists('budget.csv'):
    open('budget.csv', 'w').close()
if not os.path.exists('expenses.csv'):
    open('expenses.csv', 'w').close()
def read_user():
    with open('user.csv', 'r') as check:
        reader = csv.reader(check)
        data={}
        for row in reader:
            if len(row)>0:
                data[row[0]]=row[1]
        return data
def read_budget():
    with open('budget.csv', 'r') as f:
        reader = csv.reader(f)
        data_budget={}
        for row in reader:
            if len(row)>0:
                data_budget[row[0]]=int(row[1])
        return data_budget
def read_expenses():
    data_expenses = {}
    with open('expenses.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row)>0:
                if row[0] in data_expenses:
                    if row[1] not in data_expenses[row[0]][0]:
                        data_expenses[row[0]][0][row[1]]=int(row[2])
                    else:
                        data_expenses[row[0]][0][row[1]]+=int(row[2])
                else:
                    data_expenses[row[0]] = [{}]
                    data_expenses[row[0]][0][row[1]]=int(row[2])
        return data_expenses
def budget_ask():
    choice = input("Are you want to add monthly budget?(yes/no):")
    if choice.lower() == "yes":
        monthly_budget(current_username)
def update_budget_file(data):
    with open('budget.csv', 'w') as budget:
        writer = csv.writer(budget,delimiter=',')
        for key, value in data.items():
            writer.writerow([key, value])
def login_account():
    users_data = read_user()
    user_name = input("Enter Username: ").lower()
    password = input("Enter Password: ")
    if user_name in users_data:
        if password == users_data[user_name]:
            print("Login Successfully")
            return user_name
        else:
            print("Invalid Password")
            ask()
            return None
    else:
        print("Username not found")
        ask()
        return None
def ask():
    try:
        choice = str(input("Are you want to create a new account?(yes/no):"))
        if choice.lower() == "yes":
            create_account()
    except ValueError:
        print("Enter a valid input")
def create_account():
    while True:
        users_data = read_user()
        user_name = input("Enter Username: ").lower()
        space=0
        for i in user_name:
            if i.isspace():
               space+=1
        if space==0:
            password = input("Enter Password: ")
            if user_name in users_data:
                print("Username already exists")
                print("Enter another username")
            else:
                with open('user.csv', 'a') as user:
                    writer = csv.writer(user,delimiter=',')
                    writer.writerow([user_name, password])
                    print("Account Created successfully")
                break
        else:
            print("Invalid Username")
            print("Username contains spaces")
def monthly_budget(user_name):
    while True:
        data = read_user()
        budget_read = read_budget()
        try:
            if user_name in data :
                if user_name not in budget_read:
                    budget = int(input("Enter Monthly Budget: "))
                    with open('budget.csv', 'a') as file:
                        writer = csv.writer(file,delimiter=',')
                        writer.writerow([user_name, budget])
                    break
                else:
                    print("You hava already set your monthly budget")
                    print("This is your monthly budget:",budget_read[user_name])
                    break
            else:
                print("Username not found")
                ask()
                break
        except ValueError:
            print("Enter a valid input")
def add_income(user_name):
    while True:
        budget = read_budget()
        try:
            if user_name in budget:
                income = int(input("Enter adding Income: "))
                if income>=0:
                    budget[user_name]=budget[user_name]+income
                    break
                else:
                    print('Enter a valid income')
            else:
                print("Username not found in Monthly Budget")
                budget_ask()
                break
        except ValueError:
            print("Enter a valid input")
    update_budget_file(budget)
def add_expense(user_name):
    while True:
        budget = read_budget()
        try:
            amount = int(input("Enter Amount: "))
            category=input("Enter category=").lower()
            if amount>0:
                if user_name in budget:
                    if amount <= budget[user_name]:
                        with open('expenses.csv', 'a') as expenses:
                            writer = csv.writer(expenses,delimiter=',')
                            writer.writerow([user_name,category,amount])
                            budget[user_name]-=amount
                            update_budget_file(budget)
                        break
                    else:
                        print("You spent more than your budget")
                        break
                else:
                    print("Username not found in monthly Budget")
                    budget_ask()
                    break
            else:
                print("Enter a valid amount")
        except ValueError:
            print("Enter a valid input")
def view_expenses(user_name):
    reading_expenses = read_expenses()
    budget=read_budget()
    if user_name in reading_expenses:
        print("Your expenses:")
        for category,amount in reading_expenses[user_name][0].items():
            print('Category:', category, '|Amount:', amount)
    elif user_name in budget and user_name not in reading_expenses:
        print("No expenses found")
    elif user_name not in budget:
        print("Username not found in Monthly Budget")
        budget_ask()
def view_budget(user_name):
    budget = read_budget()
    if user_name in budget:
        print("Your budget:")
        print("Username:", user_name,"|Amount:", budget[user_name])
    else:
        print("Username not found in Monthly Budget")
        budget_ask()
print("Welcome to Personal Finance & Budget Management System")
current_username=None
while True:
    try:
        print("1.Sign In")
        print("2. Create Account")
        print("3. Monthly Budget")
        print("4. Add Income")
        print("5. Add Expense")
        print("6. View Expenses")
        print("7. View Balance Budget")
        print("8.Save & Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            current_username=login_account()
        elif choice == 2:
            create_account()
        elif choice<1 or choice>8:
            print("select valid option")
        elif choice == 8:
            print("Saved successfully")
            break
        else:
            if current_username:
                if choice == 3:
                    monthly_budget(current_username)
                elif choice == 4:
                    add_income(current_username)
                elif choice == 5:
                    add_expense(current_username)
                elif choice == 6:
                    view_expenses(current_username)
                elif choice == 7:
                    view_budget(current_username)
            else:
                print("Please login your account")
                current_username=login_account()
    except ValueError:
        print("Enter a valid input")