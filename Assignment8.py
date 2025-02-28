def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

def print_inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

def print_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

def print_diamond(n):
    for i in range(1, n + 1, 2):
        print(' ' * ((n - i) // 2) + '*' * i)
    for i in range(n - 2, 0, -2):
        print(' ' * ((n - i) // 2) + '*' * i)

# User input
n = int(input("Enter the number of rows: "))
print("Choose a pattern: ")
print("1. Right-Angled Triangle")
print("2. Inverted Triangle")
print("3. Pyramid")
print("4. Diamond")
choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print_triangle(n)
elif choice == 2:
    print_inverted_triangle(n)
elif choice == 3:
    print_pyramid(n)
elif choice == 4:
    if n % 2 == 0:
        print("For a proper diamond, enter an odd number of rows.")
    else:
        print_diamond(n)
else:
    print("Invalid choice! Please select a number between 1 and 4.")
