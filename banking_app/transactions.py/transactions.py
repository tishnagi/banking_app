from account import Account

def create_account():
    account_number = input("Enter account number: ")
    owner = input("Enter account owner name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    account = Account(account_number, owner, initial_deposit)
    print(f"Account created successfully for {owner}")
    return account

def deposit(account, amount):
    account.deposit(amount)
    print(f"{amount} deposited successfully. New balance: {account.get_balance()}")

def withdraw(account, amount):
    if account.withdraw(amount):
        print(f"{amount} withdrawn successfully. New balance: {account.get_balance()}")
    else:
        print("Insufficient funds.")

def check_balance(account):
    print(f"Account balance: {account.get_balance()}")
