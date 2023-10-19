def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

while True:
    print("Options:")
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for power")
    print("Enter 6 to quit")

    operation = input("Enter the operation number: ")

    if operation == '6':
        break

    if operation in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print("Addition Result: " + str(add(num1, num2)))
        elif operation == '2':
            print("subtraction Result: " + str(subtract(num1, num2)))
        elif operation == '3':
            print("Multiplication Result: " + str(multiply(num1, num2)))
        elif operation == '4':
            result = divide(num1, num2)
            if result == "Cannot divide by zero":
                print(result)
            else:
                print("Division Result: " + str(result))
        elif operation == '5':
            print("Exponential Result: " + str(power(num1, num2)))
    else:
        print("Invalid input , Please enter a valid operation number.")
