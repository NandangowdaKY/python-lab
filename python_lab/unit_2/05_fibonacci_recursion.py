"""Display a Fibonacci series using recursion."""


def fibonacci(term_number):
    """Return the Fibonacci value at the requested zero-based position."""
    if term_number <= 1:
        return term_number
    return fibonacci(term_number - 1) + fibonacci(term_number - 2)


# Read the number of terms and print each value recursively calculated.
terms = int(input("Enter the number of terms: "))
series = [fibonacci(index) for index in range(terms)]

print("Fibonacci series:", *series)
