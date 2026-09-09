students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter student course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n===== Student Details =====")

            for i, student in enumerate(students):
                print("\nStudent", i)
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])

    elif choice == "3":
        print("Thank you! Program exited.")
        break

    else:
        print("Invalid choice! Please try again.")