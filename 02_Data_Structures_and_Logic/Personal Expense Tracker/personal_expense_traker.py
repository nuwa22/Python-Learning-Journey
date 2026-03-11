import datetime
def add_expense():
    item = input("Enter the expense item: ")
    description = input("Enter the expense description: ")
    amount = float(input("Enter the expense amount: "))
    date = datetime.datetime.now().strftime("%Y.%m.%d %H.%M")
    line = f"{date} | {item} | {description} | LKR:{amount:.2f}\n"
    file = open("expenses.txt", "a")
    file.write(line)
    file.close()
    print("Expense added successfully.")
def view_expense():
    print("Your expenses")
    try:
        file = open("expenses.txt", "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("No Expenses Yet")
    finally:
        print("Thank You..!")


def main_menu():
    while True:
        try:
            user_input = int(input("Enter Number 1,2 or 3:"))
            if user_input == 1:
                add_expense()
            elif user_input == 2:
                view_expense()
            else:
                break
        except ValueError:
            print("Invalid Input. Please Enter 1,2 or 3")

main_menu()