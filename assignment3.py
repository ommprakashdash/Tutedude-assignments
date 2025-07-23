def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example call
number = 5
print(f"The factorial of {number} is: {factorial(number)}")

import math

try:
    num = float(input("Enter a number: "))

    if num < 0:
        print("Square root and logarithm are not defined for negative numbers.")
    else:
        sqrt_val = math.sqrt(num)
        log_val = math.log(num)
        sine_val = math.sin(num)

        print(f"Square root of {num} is: {sqrt_val}")
        print(f"Natural logarithm of {num} is: {log_val}")
        print(f"Sine of {num} (in radians) is: {sine_val}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
    