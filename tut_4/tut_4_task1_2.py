#taks_2_ATM_Withdrawal_System_(Boolean,If-Else)
accounts={
    "Alice":{"balance":1000.0},
    "Bob":{"balance":1500.0},
"Max":{"balance":2000.0}
}

def withdraw(name, amount):
    if amount > 0 and amount % 10 == 0:
        if amount <= accounts[name]["balance"]:
            accounts[name]["balance"] -= amount
            print(f"{amount} withdrawn from the bank account {name}. Current balance: {accounts[name]['balance']}.")
        else:
            print("There is a luck of funds on the account.")
    else:
        print("Invalid amount. Please enter a positive amount that is a multiple of 10.")

while True:
    print("\nSelect operation:")
    print("1. Withdraw")
    print("2. Exit")
    choice = input("Enter the number of the operation (1-2): ")
    if choice == "2":
        break
    name = input("Enter the name of the account: ")
    if name not in accounts:
        print("Error: Invalid account name. Please enter a valid account name.")
        continue
    amount = float(input("Enter the amount to withdraw: "))
    withdraw(name, amount)