"""Inventory Management System (Boolean, If-Else,
Dictionary)"""

inventory = {
"Laptop": 5,
"Mouse": 10,
"Keyboard": 8,
"Headphones": 3,
}
def print_inventory():
    print("\nList of items in inventory:")
    for item, quantity in inventory.items():
         print(f"- {item}: {quantity}")

def management_system(choice, amount):

            quantity = inventory.get(choice, 0)
            #print(quantity)
            if quantity >= amount:
                print(f"You have requested {amount} {choice}.")
                inventory[choice] -= amount
            else:
                print(f"Sorry, we do not have enough {choice} in stock.")

while True:
    print_inventory()
    choice = input("\nEnter the name of the item you would like to request  (or type 'stop' to exit): ").strip()
    if choice not in inventory:
        print("Error: Item not found. Please try again.")
        continue
    if choice.lower() == 'stop':
        break
    amount = int(input(f"Enter the amount of the item:").strip())
    if amount <= 0 :
        print("Error: Please enter a positive number.")
        continue
    management_system(choice, amount)

