"""Check whether a number is prime or not prime."""

# Read a whole number from the keyboard.
number = int(input("Enter a positive integer: "))

if number < 2:
    is_prime = False
else:
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
