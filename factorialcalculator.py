def factorial(n):

    #Base case: factorial of 0 or 1 is 1 

    if n == 0 or n == 1:
     return 1
    else:    
     return n*factorial(n - 1)

    #Recursive Formula: n! = n * (n-1)!

num = int(input("Enter a positive integer:"))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")    
