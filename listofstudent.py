def display_menu():
    print("\n--- Student List Manager ---")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Display student list")
    print("4. Exit")


def add_student(students):
    name = input("Enter the student's name to add: ").strip()
    if name:
        students.append(name)
        print(f"{name} has been added to the list.")
    else:
        print("Invalid input. Please enter a valid name.")


def remove_student(students):
    if students:
        name = input("Enter the student's name to remove: ").strip()
        if name in students:
            students.remove(name)
            print(f"{name} has been removed from the list.")
        else:
            print(f"{name} is not in the list.")
    else:
        print("The student list is empty. There's nothing to remove.")


def display_students(students):
    if students:
        print("\n--- Student List ---")
        for index, student in enumerate(students, start=1):
            print(f"{index}. {student}")
    else:
        print("The student list is currently empty.")


def main():
    students = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            remove_student(students)
        elif choice == "3":
            display_students(students)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "_main_":
    main()