"""Calculate the factorial of a number using a loop."""

# Read a non-negative integer from the keyboard.
number = int(input("Enter a non-negative integer: "))

factorial = 1
for value in range(1, number + 1):
    factorial *= value

print(f"Factorial of {number} is {factorial}.")
