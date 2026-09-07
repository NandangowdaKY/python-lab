"""Generate a random four-digit or six-digit OTP."""

import random

# Let the user choose the OTP length.
length = int(input("Enter OTP length (4 or 6): "))

if length not in (4, 6):
    print("Please choose either 4 or 6 digits.")
else:
    lower_bound = 10 ** (length - 1)
    upper_bound = (10 ** length) - 1
    otp = random.randint(lower_bound, upper_bound)
    print(f"Your OTP is: {otp}")
