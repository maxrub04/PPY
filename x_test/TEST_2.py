import re

def is_valid_code(code):
    pattern = r"^PRD-\d{4}$"
    return bool(re.match(pattern, code))


class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email

class Customer(User):
    pass

class Order:
    def __init__(self):
        self.orders = []

    def add_customer_order(self, customer, items):
        self.orders.append((customer, items))

    def summary(self):
        print("Report:")
        for customer, items in self.orders:
            items_count = len(items)
            items_list = ', '.join(items)
            print(f"- {customer.name} order {items_count} items: {items_list}")

# === Demonstration ===
# Create customers
customer1 = Customer("Alice", "alice@example.com")
customer2 = Customer("Bob", "bob@example.com")

# Create Order system
order_system = Order()

# Add customer orders
order_system.add_customer_order(customer1, ["Laptop", "Mouse"])
order_system.add_customer_order(customer2, ["Smartphone", "Charger", "Headphones"])

# Display summary
order_system.summary()