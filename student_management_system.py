while True:
    print("\nA) Add student")
    print("\nB) View student")
    print("\nC) Search student")
    print("\nD) Edit student")
    print("\nE) delete student")
    print("\nF) Exit")
    choice = input("choose an option: ")
    if choice == "A":
        name = input("Enter student name: ")
        age = input("how old is the student?: ")
        grade = input("what is the student grades?: ")
        with open("students.txt", "a") as file:
            file.write(f"{name} - {age} - {grade}\n")
    elif choice == "B":
        with open("students.txt", "r") as file:
            students = file.read()
            if not students:
                print("No students found!")
            else:
                print(students)
    elif choice == "C":
        search_name = input("Enter student name: ")
        with open("students.txt", "r") as file:
            students = file.read()
            if search_name in students:
                print(search_name)
            else:
                print("not found!")
    elif choice == "D":
        edit_name = input("Enter student name to rdit: ")
        with open("students.txt", "r") as file:
            students = file.read()
            students = students.splitlines()
            new_age = input("Enter new age: ")
            new_grade = input("Enter new grade: ")
            for i in range(len(students)):
                if edit_name in students[i]:
                    students[i] = f"{edit_name} - {new_age} - {new_grade}"
            with open("students.txt", "w") as file:
                for student in students:
                    file.write(student + "\n")
    elif choice == "E":
        delete_name = input("Enter student name to delete: ")
        with open("students.txt", "r") as file:
            students = file.read().splitlines()
            new_students = []
            for student in students:
                if delete_name not in student:
                    new_students.append(student)
                    with open("students.txt", "w") as file:
                        for student in new_students:
                            file.write(student + "\n")
    elif choice == "F":
        print("Goodbye!")
        break