"""Perform scientific calculations with two numbers."""

import math

# Read the two numbers used in the calculations.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("\nScientific Calculator")
print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")

if second_number != 0:
    print(f"Division: {first_number / second_number}")
else:
    print("Division: Cannot divide by zero")

print(f"Power: {first_number ** second_number}")
print(f"Square root of first number: {math.sqrt(abs(first_number))}")
print(f"Square root of second number: {math.sqrt(abs(second_number))}")
print(f"Sine of first number: {math.sin(first_number)}")
print(f"Cosine of first number: {math.cos(first_number)}")
