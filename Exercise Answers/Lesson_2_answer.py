"""
Lesson 2: Floats and Types - Calculator Solution
"""

# Printing a welcome message
print("Welcome to the simple calculator!")

# Getting the first number
first_number = float(input("Enter the first number: "))

# Asking for the operation
operation = input("Choose an operation (+, -, *, /): ")

# Getting the second number
second_number = float(input("Enter the second number: "))

# Performing the calculation
if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    try:
        result = first_number / second_number
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = "undefined"
else:
    print("Invalid operation selected.")
    result = "undefined"

# Displaying the result
if result != "undefined":
    print(f"Result: {first_number} {operation} {second_number} = {result}")
