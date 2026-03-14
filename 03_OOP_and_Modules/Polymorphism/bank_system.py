class BankAccount:
    def get_interest(self):
        return 0

class SavingsAccount(BankAccount):
    def get_interest(self):
        return 0.05

class FixedDeposit(BankAccount):
    def get_interest(self):
        return 0.12

normal_account = BankAccount()
savings_account = SavingsAccount()
fixed_account = FixedDeposit()

print("Normal Account Interest:", normal_account.get_interest(), "%")
print("Savings Account Interest:", savings_account.get_interest(), "%")
print("Fixed Deposit Interest:", fixed_account.get_interest(), "%")