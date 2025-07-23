def get_student_marks():
    student_marks = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "Diana": 92
    }

    name = input("Enter the student's name: ")

    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        print("Student not found in the record.")

def demonstrate_list_slicing():
    numbers = list(range(1, 11))  # List from 1 to 10
    first_five = numbers[:5]
    reversed_five = first_five[::-1]

    print(f"First five elements: {first_five}")
    print(f"Reversed list: {reversed_five}")

if __name__ == "__main__":
    get_student_marks()
    demonstrate_list_slicing()
