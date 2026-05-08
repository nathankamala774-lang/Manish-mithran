class InsufficientFundsError(Exception): pass
class AccountNotFoundError(Exception): pass
accounts = {}
def create_account(acc_no, balance=0):
    accounts[acc_no] = balance
    print(f"Account {acc_no} created with ₹{balance}")

def deposit(acc_no, amount):
    if acc_no not in accounts:
        raise AccountNotFoundError("Account not found")
    accounts[acc_no] += amount
    print(f"Deposited ₹{amount} to {acc_no}")
def withdraw(acc_no, amount):
    if acc_no not in accounts:
        raise AccountNotFoundError("Account not found")
    if accounts[acc_no] < amount:
        raise InsufficientFundsError("Not enough balance")
    accounts[acc_no] -= amount
    print(f"Withdrew ₹{amount} from {acc_no}")

def transfer(src, dst, amount):
    withdraw(src, amount)
    deposit(dst, amount)
    print(f"Transferred ₹{amount} from {src} to {dst}")

def get_balance(acc_no):
    if acc_no not in accounts:
        raise AccountNotFoundError("Account not found")
    return accounts[acc_no]
create_account("A1", 5000)
create_account("B1", 3000)

deposit("A1", 2000)
withdraw("B1", 1000)
transfer("A1", "B1", 1500)

print("A1 Balance:", get_balance("A1"))
print("B1 Balance:", get_balance("B1"))
