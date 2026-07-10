print("welcome to ATM!")
balance = 1000
while True:
    print("A) check balance")
    print("B) deposit")
    print("C) withdraw")
    print("D) exit")

    choice = input("choose: ")
    if choice == "A":
        print(balance)

    elif choice == "B":
        amount = int(input("enter deposit amount: "))
        balance += amount
        print(balance)

    elif choice == "C":
        amount2 = int(input("enter withdraw amount: "))
        if amount2 > balance:
            print("insufficient balance!")
        else:
            balance -= amount2
            print("new balance:", balance)

    elif choice == "D":
        print("goodbye!")
        break