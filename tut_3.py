#task_1
def generate_sales_report():

    sales_data = []

    while True:
        user_input = input(
            "Enter the name, quantity and price of the product(enter 'done' to stop): ").strip()

        if user_input.lower() == 'done':
            break

        try:
            product_name, price, quantity = user_input.split()
            price = float(price)
            quantity = int(quantity)

            sales_data.append({
                "product_name": product_name,
                "price": price,
                "quantity": quantity
            })
        except ValueError:
            print("error: invalid input. Please enter the data in the correct format:")
            continue

    revenue_report = {}
    for transaction in sales_data:
        product = transaction["product_name"]
        revenue = transaction["price"] * transaction["quantity"]

        if product in revenue_report:
            revenue_report[product] += revenue
        else:
            revenue_report[product] = revenue

    print("\nTotal revenue by product:")
    for product, total_revenue in revenue_report.items():
        print(f"{product}: ${total_revenue:.2f}")

#generate_sales_report()

#task_2
def employee_salary_adjustment():
    employee_data = []

    while True:
        user_input = input(
            "Enter the employee's details (Name, Salary, Perfomance) or 'done' to finish: ").strip()

        if user_input.lower() == 'done':
            break

        try:
            name, salary, performance = user_input.split()
            salary = float(salary)
            performance = float(performance)

            employee_data.append({
                "name": name,
                "salary": salary,
                "performance": performance
            })

        except ValueError:
            print("Error: Invalid input. Please enter the data in the correct format:")
            continue

    for employee in employee_data:
        if employee["performance"] >= 4.5:
            employee["salary"] *= 1.10
        elif 3.0 <= employee["performance"] <= 4.4:
            employee["salary"] *= 1.05

    print("\nUpdated employee information, including adjusted salary, after applying corrections:")
    for employee in employee_data:
        print(f"Name: {employee['name']}, Salary: {employee['salary']:.2f}, Perfomance: {employee['performance']}")

#employee_salary_adjustment()

#task_3
def process_customer_orders():
    stock = {
        "meat": 50,
        "bread": 40,
        "banana": 30,
        "cheese": 20,
        "eggs": 10
    }

    print("Current stock:")
    for product_name, quantity in stock.items():
        print(f"{product_name}: {quantity} ")

    customer_orders = []

    while True:
        user_input = input("Enter customer orders ('Item Quantity'). Enter 'done' to stop: ").strip()

        if user_input.lower() == 'done':
            break

        try:
            product_name, quantity = user_input.split()
            quantity = int(quantity)
            customer_orders.append({"product_name": product_name.lower(), "quantity": quantity})
        except ValueError:
            print("Error: Invalid input. Please enter the data in the correct format:")
            continue

    print("\nResults:")
    for order in customer_orders:
        product_name = order["product_name"]
        quantity = order["quantity"]

        if product_name in stock and stock[product_name] >= quantity:
            print(f"Oder: {quantity} of '{product_name}' approved.")
            stock[product_name] -= quantity
        else:
            print(f"Oder {quantity} of '{product_name}' rejected")

    print("\nUpdated stock:")
    for product_name, quantity in stock.items():
        print(f"{product_name}: {quantity}")

#process_customer_orders()

#task_4
def fibonacci_sequence():
    n = int(input("Enter the number of terms in the sequence: "))
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        temp = a + b
        a = b
        b = temp
    print(f"fibonacci({n}) → {fib_sequence}")

#fibonacci_sequence()

#task_5
def enter_right_password():
    correct_password = "helloworld"
    remaining_attempts = 3
    while remaining_attempts > 0:
        password = input("Enter your password: ")
        if password == correct_password:
            print("Access granted!")
            return
        remaining_attempts -= 1
        print(f"Wrong password! {remaining_attempts} attempts left.") if remaining_attempts > 0 else print(
            "Access denied!")
#enter_right_password()






