# Create a dictionary where:
# Keys = student names
# Values = marks (integer)
# Write a menu-based program where user presses a key (’ A , ‘B , ‘C , ‘D ) depending on the operation they want to perform on the dictionary:
# - Add a student
# - Update marks
# - Search for a student
# - Display all students and marks
# - Exit

info = {}

while True:
    print("\n----- MENU -----")
    print("A : Add a student")
    print("B : Update marks")
    print("C : Search for a student")
    print("D : Display all students")
    print("E : Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        info[name] = marks
        print("Student added successfully!")

    elif choice == "B":
        name = input("Enter student name to update: ")
        if name in info:
            marks = int(input("Enter new marks: "))
            info[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    elif choice == "C":
        name = input("Enter student name to search: ")
        if name in info:
            print(f"{name} : {info[name]}")
        else:
            print("Student not found!")

    elif choice == "D":
        if len(info) == 0:
            print("No records available.")
        else:
            print("\n--- Student Records ---")
            for name, marks in info.items():
                print(f"{name} : {marks}")

    elif choice == "E":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter A/B/C/D/E")
