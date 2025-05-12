import math
#Problem_1
sales_data = {
    'Product A': [100, 200, 300],
    'Product B': [150, 250, 350],
    'Product C': [50, 70, 90]
}


def calculate_sales(sales_data):
    total_sales_per_product={}
    for product, sales in sales_data.items():
        total_sales_per_product[product]=sum(sales)
    max_sales_product=max(total_sales_per_product,key=total_sales_per_product.get)
    max_sales_value=total_sales_per_product[max_sales_product]

    return total_sales_per_product,max_sales_product,max_sales_value

totals,top_product,top_sales=calculate_sales(sales_data)
print("Total Sales:",totals)
print("Product with max sales:",top_product,"with -",top_sales,"sales")




#Problem_2

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

add = a+b
sub = a-b
mul = a*b
div = a/b
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

a = int(a)
b = int(b)
print(f"a: {type(a)}")
print(f"b: {type(b)}")

a = float(a)
b = float(b)
print(f"a: {type(a)}")
print(f"b: {type(b)}")

absolute = abs(a-b)
print(f"Absolute difference: {absolute}")

def even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

print(f"A is :{even_odd(a)}")
print(f"B is :{even_odd(b)}")

#Problem_3
def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
def primes_in_range(x, y):
    primes = [num for num in range(x, y + 1) if is_prime(num)]
    return primes

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
print(primes_in_range(x, y))
print(f"Sum of primes in range: {sum(primes_in_range(x, y))}")
print(f"Avg of primes in range: {sum(primes_in_range(x, y))/len(primes_in_range(x, y))}")

#Problem_4
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Power (x^y)")
        print("7. Exit")

        try:
            choice = int(input("Enter the number of the operation (1-7): "))
        except ValueError:
            print("Error: Please enter a valid number!")
            continue

        if choice == 7:
            print("Exiting the program")
            break

        if choice not in range(1, 7):
            print("Error: Please choose a valid operation (1-6)!")
            continue

        if choice == 5:
            try:
                num = float(input("Enter a number to calculate the square root: "))
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number!")
                else:
                    result = math.sqrt(num)
                    print(f"The square root of {num} is {result}")
            except ValueError:
                print("Error: Please enter a valid number!")
            continue

        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Error: Please enter a valid number!")
            continue

        if choice != 5:
            try:
                if choice != 6:
                    num2 = float(input("Enter the second number: "))
                else:
                    num2 = float(input("Enter the power: "))
            except ValueError:
                print("Error: Please enter a valid number!")
                continue

        try:
            if choice == 1:
                print(f"Result:{num1 + num2}")
            elif choice == 2:
                print(f"Result:{num1 - num2}")
            elif choice == 3:
                print(f"Result:{num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    print(f"Result: {num1 / num2}")
            elif choice == 6:
                print(f"Result:{math.pow(num1, num2)}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


calculator()
