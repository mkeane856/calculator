#Here I define functions for each of my operations

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "cannot divide by zero"
    return x / y

#Here I display a menu to the user

print("select operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("Enter choice (1/2/3/4): ")

if choice not in ['1', '2', '3', '4']:
    print("Invalid choice")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == '1':
        result = add(num1, num2)
        operation = '+'
elif choice == '2':
    result = subtract(num1, num2)
    operation = '-'
elif choice == '3':
    result = multiply(num1, num2)
    operation = '*'
else:
    result = divide(num1, num2)
    operation = '/'
print(f"{num1} {operation} {num2} = {result}")





