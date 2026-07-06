while True:
    print("\n===== calculator =====")
    print("1. Addition (+)")
    print("2. subtraction (-)")
    print("3. moltiplication (*)")
    print("4. power (**)")
    print("5. modulus (%)")
    print("6. floor division (//)")
    print("7. division (/)")
    print("8. Exist")

    choice = input("choose an option: ")

    if choice == "8":
        print("goodbye!")
        break

    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number"))

    if choice == "1":
        print("result:", num1 + num2)
        
    elif choice == "2":
        print("result:", num1 - num2)

    elif choice == "3":
        print("result:", num1 * num2)

    elif choice == "4":
        print("result:", num1 ** num2)

    elif choice == "5":
        print("result:", num1 % num2)

    elif choice == "6":
        print("reuslt:", num1 // num2)

    elif choice == "7":
        if num2 == 0:
            print("cant divide by zero!")
        else:
            print("result:", num1 / num2)
else:
    print("invalid choice!")