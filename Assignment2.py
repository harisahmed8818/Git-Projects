import math 

# Taking input from user 
n = int(input("Enter a number: "))
     
    # Checking if the number is negative
if n < 0:
    print("Factorial does not exist for negative numbers.")

else:
    # Using math.factorial() to calculate factorial
    print(f"The factorial of {n} is {math.factorial(n)}.")    