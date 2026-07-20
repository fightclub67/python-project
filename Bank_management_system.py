while True:
    print("\n=== Bank Management System ===")
    print("A) Create Account")
    print("B) Deposit Money")
    print("C) Withdraw Money")
    print("D) View Accounts")
    print("E) Search Account")
    print("F) Exit")

    choice = input("Enter your choice: ").upper()

    # Exit
    if choice == "F":
        print("Goodbye!")
        break

    # Create Account
    elif choice == "A":
        account_name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")
        balance = 0

        with open("accounts.txt", "a") as file:
            file.write(account_name + "," + account_number + "," + str(balance) + "\n")

        print("Account created successfully!")


    # Deposit Money
    elif choice == "B":
        account_number = input("Enter account number: ")
        amount = int(input("Enter deposit amount: "))

        with open("accounts.txt", "r") as file:
            accounts = file.readlines()

        found = False

        with open("accounts.txt", "w") as file:
            for account in accounts:
                data = account.strip().split(",")

                if data[1] == account_number:
                    balance = int(data[2])
                    balance += amount

                    file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")
                    print("Deposit successful!")
                    found = True

                else:
                    file.write(account)

        if not found:
            print("Account not found!")


    # Withdraw Money
    elif choice == "C":
        account_number = input("Enter account number: ")
        amount = int(input("Enter withdrawal amount: "))

        with open("accounts.txt", "r") as file:
            accounts = file.readlines()

        found = False

        with open("accounts.txt", "w") as file:
            for account in accounts:
                data = account.strip().split(",")

                if data[1] == account_number:
                    balance = int(data[2])

                    if amount <= balance:
                        balance -= amount
                        print("Withdrawal successful!")
                    else:
                        print("Not enough balance!")

                    file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")
                    found = True

                else:
                    file.write(account)

        if not found:
            print("Account not found!")


    # View Accounts
    elif choice == "D":
        with open("accounts.txt", "r") as file:
            accounts = file.readlines()

            if len(accounts) == 0:
                print("No accounts found!")

            else:
                for account in accounts:
                    print(account.strip())


    # Search Account
    elif choice == "E":
        account_number = input("What are you looking for?: ")

        with open("accounts.txt", "r") as file:
            accounts = file.readlines()

        found = False

        for account in accounts:
            data = account.strip().split(",")

            if data[1] == account_number:
                print("Account found:")
                print(account.strip())
                found = True
                break

        if not found:
            print("Not found!")


    else:
        print("Invalid choice!")