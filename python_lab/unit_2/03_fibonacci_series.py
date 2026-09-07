"""Display a Fibonacci series using a loop."""

# Read the number of terms to display.
terms = int(input("Enter the number of terms: "))

first_term = 0
second_term = 1
series = []

for _ in range(terms):
    series.append(first_term)
    first_term, second_term = second_term, first_term + second_term

print("Fibonacci series:", *series)
