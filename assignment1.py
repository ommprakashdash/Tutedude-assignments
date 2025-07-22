# Task 1: Basic Mathematical Operations

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying the results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:",division)

# Task 2: Personalized Greeting

# Taking input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Creating full name
full_name = first_name + " " + last_name

# Displaying greeting
print(f"\nHello, {full_name}! Welcome to the Python programming world.")