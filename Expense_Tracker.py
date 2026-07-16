while True:
    print("==== Expense Tracker ====")
    print("\nA) Add Expense")
    print("\nB) View Expenses")
    print("\nC) Delete All Expenses")
    print("\nD) Show Total")
    print("\nE) Exit")
    choice = input("choose an option: ")
    if choice == "A":
        Title = input("Enter the Title: ")
        amount = input("Enter amount: ")
        with open("expenses.txt", "a") as file:
            file.write(Title + " - " + amount + "\n")
    elif choice == "B":
        with open("expenses.txt", "r") as file:
            expenses = file.read()
            if not expenses:
                print("no epenses found!")
            else:
                print(expenses)
    elif choice == "C":
        with open("expenses.txt", "w") as file:
            pass
        print("All epenses deleted!")
    elif choice == "D":
        Total = 0

        with open("expenses.txt", "r") as file:
            for expense in file:
                parts = expense.split(" - ")
                number = int(parts[1])
                Total += number
                print(Total)
    elif choice == "E":
        print("Goodbye!")
        break