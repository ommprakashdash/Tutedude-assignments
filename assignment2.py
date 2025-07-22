# Task 1: Check if a Number is Even or Odd

def check_even_odd():
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the function
check_even_odd()

# Task 2: Sum of Integers from 1 to 50 Using a Loop

def sum_1_to_50():
    total = 0
    for i in range(1, 51):
        total += i
    print(f"The sum of integers from 1 to 50 is: {total}")

# Call the function
sum_1_to_50()

