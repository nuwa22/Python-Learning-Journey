class BankAccount:
    def __init__(self, name, money):
        self.name = name
        self.__balance = money

    def show_balance(self):
        print("Balance is:", self.__balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit Success!") 

my_account = BankAccount("Suresh", 1000)

print(my_account.name)

my_account.show_balance()

my_account.deposit(500)

my_account.show_balance()

# print(my_account.__balance)
# this is error because __balance is private and cannot be accessed directly from outside the class.