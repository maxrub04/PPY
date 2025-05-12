#task_1_Bank_Account_Management_System_with_Transactions
accounts={
    "Alice":{"balance":1000.0,"history":[]},
    "Bob":{"balance":1500.0,"history":[]},
"Max":{"balance":2000.0,"history":[]}
}

def deposit(name, amount):
    if amount > 0:
        accounts[name]["balance"] += amount
        accounts[name]["history"].append(("Deposit", amount))
        print(f"{amount} deposited on the bank account {name}. Current balance: {accounts[name]['balance']}.")
    else:
        print("Amount should be positive.")

def withdraw_1(name, amount):
    if 0 < amount <= accounts[name]["balance"]:
        accounts[name]["balance"] -= amount
        accounts[name]["history"].append(("Withdraw", amount))
        print(f"{amount} withdrawn from the bank account {name}. Current balance: {accounts[name]['balance']}.")
    else:
        print("There is a luck of funds on the account.")

def check_balance(name):
    print(f"The balance of the account {name} is {accounts[name]['balance']}.")

def print_history(name):
    print(f"Transaction history for account {name}:")
    for operation, amount in accounts[name]["history"]:
        print(f"{operation}: {amount}")

while True:
    print("\nSelect operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    print("5. Print transaction history")
    choice = input("Enter the number of the operation (1-5): ")

    if choice == "4":
        break

    name = input("Enter the name of the account: ")
    if name not in accounts:
        print("Error: Invalid account name. Please enter a valid account name.")
        continue

    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        deposit(name, amount)
    if choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        withdraw_1(name, amount)
    if choice == "3":
        check_balance(name)
    if choice == "5":
        print_history(name)
    elif choice not in ["1", "2", "3", "4", "5"]:
        print("Error: Invalid choice. Please enter a valid number.")


