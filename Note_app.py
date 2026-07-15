while True:
    print("you are welcome!")
    print("\nA) Add note")
    print("\nB) View notes")
    print("\nC) Delete all notes")
    print("\nD) Exit")
    choice = input("choose an option: ")
    if choice == "A":
        Note = input("Enter your note: ")
        with open("notes.text", "a") as file:
            file.write(Note + "\n")
    elif choice == "B":
        with open("notes.text", "r") as file:
            notes = file.read()
            if not notes:
                print("No notes found!")
            else:
                print(notes)
    elif choice == "C":
        with open("notes.text", "w") as file:
            pass
        print("All notes deleted!")
    elif choice == "D":
        print("Goodbye!")
        exit()
    else:
        print("invalid choice!")