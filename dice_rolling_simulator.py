import random
print("welcome to Dice rolling simulator!")
while True:
    option = input("roll the dice? (yes/no): ")
    if option == "no":
        print("thanks for playing!")
        break
    elif option == "yes":
        dice = random.randint(1, 6)
        print("your rolled:", dice)
    else:
        print("invalid option!")