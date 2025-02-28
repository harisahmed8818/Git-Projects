def calculate_statistics(grades):
    if not grades:
        print("No grades entered!")
        return

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print("\n--- Grade Statistics ---")
    print(f"Average Grade: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")

# Get user input
num_students = int(input("Enter the number of students: "))

if num_students <= 0:
    print("Invalid number of students!")
else:
    grades = []
    for i in range(num_students):
        grade = float(input(f"Enter grade for student {i + 1}: "))
        grades.append(grade)  # Dynamically storing grades

    calculate_statistics(grades)
