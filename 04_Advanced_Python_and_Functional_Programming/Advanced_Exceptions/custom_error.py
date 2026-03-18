# nomal Error Raised
# raise ValueError("This is a value error")

def withdraw_money(balance, amount):
    if amount > balance:
        # we can raise an error here to indicate that the withdrawal cannot be processed due to
        # insufficient funds
        raise ValueError("Insufficient funds") 
    print(f"Withdrew {amount}. Remaining balance: {balance - amount}")

withdraw_money(5000, 1000)



# Custom Exceptions
# We can create our own custom exceptions by defining a new class that inherits
# from the built-in Exception class. This allows us to provide more specific error
# messages and handle different types of errors in a more organized way.

class InsufficientFundsError(Exception):
    pass

def withdraw_money(balance, amount):
    if amount > balance:
        # we can raise an error here to indicate that the withdrawal cannot beprocessed due to 
        raise InsufficientFundsError("Insufficient funds")
    print(f"Withdrew {amount}. Remaining balance: {balance - amount}")

withdraw_money(5000, 10000)
