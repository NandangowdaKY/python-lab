"""Use built-in functions and the math module for calculations."""

import math

# Read a number and demonstrate common built-in and math functions.
number = float(input("Enter a number: "))

print("\nMathematical Calculator")
print(f"Absolute value: {abs(number)}")
print(f"Rounded value: {round(number)}")
print(f"Ceiling value: {math.ceil(number)}")
print(f"Floor value: {math.floor(number)}")
print(f"Square root of absolute value: {math.sqrt(abs(number))}")
print(f"Power (number squared): {math.pow(number, 2)}")
print(f"Sine: {math.sin(number)}")
print(f"Cosine: {math.cos(number)}")
print(f"Tangent: {math.tan(number)}")
