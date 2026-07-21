while True:
    print("\nA) Add Room")
    print("\nB) View Room")
    print("\nC) Search Room")
    print("\nD) Book Room")
    print("\nE) Cancel Reservation")
    print("\nF) Delete Room")
    print("\nG) Exit")
    choice = input("Enter your choice: ").upper()
    if choice == "A":
        Room_number = input("Enter room number: ")
        Room_type = input("Enter room type: ")
        Room_price = int(input("Enter room price: "))
        with open("rooms.txt", "a") as file:
            file.write(f"{Room_number} , {Room_type} , {Room_price} Available \n")
            print("Room added successfully!")
    elif choice == "B":
        with open("rooms.txt", "r") as file:
            for line in file:
                print(line.strip())
    elif choice == "C":
        Room_number = input("Enter room number: ")
        with open("rooms.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if Room_number in line:
                    print("Room found!")
                    print(line)
                    break
                else:
                    print("Room not found!")
    elif choice == "D":
        Room_number = input("Enter room number: ")
        with open("rooms.txt", "r") as file:
            lines = file.readlines()
            update_lines = []
            for line in lines:
                if Room_number in line:
                    line = line.replace("Available", "Booked")
                    update_lines.append(line)

                    with open("rooms.txt", "w") as file:
                        file.writelines(update_lines)
                        print("Room booked successfully!")
    elif choice == "E":
        Room_number = input("Enter room number: ")
        with open("rooms.txt", "r") as file:
            lines = file.readlines()
            update_lines = []
            for line in lines:
                if Room_number in line and "Booked" in line:
                    line = line.replace("Booked", "Available")
                    update_lines.append(line)

                    with open("rooms.txt", "w") as file:
                        file.writelines(update_lines)
                        print("Reservation cancelled")
    elif choice == "F":
        print("i am in F")
        Room_number = input("Enter room number: ")

        with open("rooms.txt", "r") as file:
            lines = file.readlines()

        update_lines = []

        for line in lines:
            print(line)
            if Room_number.strip() not in line:
                update_lines.append(line)

        with open("rooms.txt", "w") as file:
            file.writelines(update_lines)

        print("Room deleted successfully!")
        
    elif choice == "G":
        print("Have a nice day!")
        break