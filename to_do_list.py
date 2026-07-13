tasks = ['study python', 'go to gym', 'read book']
while True:
    print("\nA) Add task")
    print("B) View tasks")
    print("C) Remove task")
    print("D) Exit")
    option = input("choose an option: ")
    if option == "A":
        task = input("Enter a task: ")
        tasks.append(task)
        print(task)
    elif option == "B":
        print(tasks)
    elif option == "C":
        task2 = input("which task do you want to remove? ")
        tasks.remove(task2)
        print(tasks)
    elif option == "D":
        print("goodbye!")
        break