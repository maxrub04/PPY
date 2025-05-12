#Task_1
product_ids = [1, 2, 3, 4]
print("Memory address before modification:", id(product_ids))

product_ids.append(5)
product_ids.remove(5)
#2.Explain: Does the id() of product_ids change? Why or why not?
print("Memory address after modification:", id(product_ids)) #The address remains the same because lists in python are
#mutable and we do not create a new object with append and remove

product_ids_1 = product_ids[:]
#3.Modify the program to assign product_ids to a new list with the same values. Does
#the id() change now?
print("Memory address of the new list:", id(product_ids_1)) #Yes, the address is changed because we created the new object

#Task2
sq_loop = []
for i in range(1, 11):
    sq_loop.append(i ** 2)

sq_compr = [i ** 2 for i in range(1, 11)]

print("\nSquares with loop:", sq_loop)
print("Squares with comprehension:", sq_compr)

#Task3
#1.Why does it work even though tuples are immutable?
my_tuple = (1, [2, 3], (4, 5)) #mutability depends on the elements inside the tuple and list[2,3] is mutable
my_tuple[1].append(6)
print("\n",my_tuple)
my_tuple = (1, [2, 3], (4, 5))
#2.What happens?
#my_tuple[2].append(7)
#print(my_tuple) #AttributeError: 'tuple' object has no attribute 'append'

#3Create a new tuple where all elements are immutable and prove it cannot be changed.
immutable_tuple = (1, (2, 3), "max", 2.28) #all elements are immutable because commands below will raise an error
immutable_tuple[1] = (4, 5)
immutable_tuple[2] = " rub"
immutable_tuple[3] = 2.31

#Task4
students = {
    101: {'name': 'Alice', 'age': 20, 'grades': {'math': 88, 'science': 92, 'english': 85}},
    102: {'name': 'Bob', 'age': 22, 'grades': {'math': 90, 'science': 85, 'english': 80}},
    103: {'name': 'Charlie', 'age': 21, 'grades': {'math': 95, 'science': 89, 'english': 91}},
}
#Add a new student
students[104] = {'name': 'David','age': 23,'grades': {'math': 92, 'science': 87, 'english': 90}}
#Update Bob's English grade to 88
students[102]['grades']['english'] = 88

#Task5
a = 1000
b = 1000
print(a is b) # False
x = 10
y = 10
print(x is y) # True
#so for effiency python for small int(-5 to 256) for x=10 and y =10 reference the same memory location
#because of the fact that a and b is bigger than 256, thus  a and b have different addres
a = 256
b = 256
print(a is b) # True because a and b are within Python’s cached integer range

#Task 6
Name = input('Enter your name: ')
Age =int(input("Enter your year of birth: "))
Age=2025-Age
print(f"Hello, {Name}! You are {Age} years old.")