# Taking input from the user
text = input("Enter a string: ")

# Checking if the string is equal to its reverse
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")