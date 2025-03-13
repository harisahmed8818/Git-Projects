def is_palindrome(s):
    s = (s.lower())
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char 

    return new_s == new_s[::-1] 

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Raca a car"))
print(is_palindrome("madam"))
print(is_palindrome("Hello!"))