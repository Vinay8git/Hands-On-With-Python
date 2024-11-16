class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(Account Number: {self.account_number}, Balance: {self.balance})"

class Customer:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.bank_account = BankAccount(account_number, balance)  # Composition: Customer owns BankAccount

    def show_account(self):
        print(f"{self.name}'s Account: {self.bank_account}")

# Customer has a bank account, and they are tightly coupled
customer = Customer("John Doe", 123456, 5000)

# Display customer's account
customer.show_account()

# When the customer is deleted, the bank account is also deleted
del customer
# customer.show_account()
print("Object Does not exist")
# BankAccount cannot exist without Customer, so it's gone after deletion then
