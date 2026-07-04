import random 
number = random.randint(1, 100)
print(number)
print("welcome to guess number game")
choice = int(input("choose a number between 1 and 100: "))
attempts = 1
while choice != number:
    if choice < number:
        print("too low")

    elif choice > number:
        print("too high")
    choice = int(input("false, guess again: "))
    attempts += 1
print("congratulations")
print(f"you guessed the number in {attempts} attempts!")