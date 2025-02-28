def factorial(n: int) -> int:
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
print(factorial(7))  # Output: 5040
