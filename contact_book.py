contacts = []
while True:
    print("you are welcome!")
    print("\nA) Add contact")
    print("\nB) View contact")
    print("\nC) Search contact")
    print("\nD) Delete contact")
    print("\nE) Exit")
    choice = input("choose an option: ")
    if choice == "A":
        Name = input("Enter a name: ")
        Phone = input("Enter a phone number: ")
        contact = {
            "Name": Name,
            "Phone": Phone
        }
        contacts.append(contact)
        print("Added!")
    elif choice == "B":
        for contact in contacts:
            print(f'Name:{contact["Name"]}')
            print(f'Phone:{contact["Phone"]}')
    elif choice == "C":
        Search_name = input("Enter a name to search: ")
        for contact in contacts:
            if contact["Name"] == Search_name:
                print(f'Name: {contact["Name"]}')
                print(f'Phone: {contact["Phone"]}')
    elif choice == "D":
        Delete_name = input("Enter a name to delete: ")
        for contact in contacts:
            if contact["Name"] == Delete_name:
                contacts.remove(contact)
                print("Deleted!")
                break
    elif choice == "E":
        print("Goodbye!")
        break