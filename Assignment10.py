def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned_s = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage
print(is_palindrome("madam"))           # Output: True
print(is_palindrome("nurses run"))      # Output: True
print(is_palindrome("Hello"))           # Output: False
