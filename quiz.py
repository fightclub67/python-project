print("welcome to quiz game!")
option = input("are you ready? ")
score = 0
if option == "yes":
    print("the game has started!")

else:
    print("the game is over!")

choice = input("what is the capital of france?\nA) London\nB) Paris\nC) Berlin\nyour answer: ")

if choice == "A":
    print("wrong!")

elif choice == "B":
    print("correct!")
    score += 1
else:
    print("wrong!")

choice2 = input("how long ago was America discovered?\nA) 250 years\nB) 150 yaers\nC) 200 years\nyour answer: ")

if choice2 == "A":
    print("correct!")
    score += 1

elif choice2 == "B":
    print("wrong!")

else:
    print("wrong!")

choice3 = input("which country was winner of 2018 world cup?\nA) Brazil\nB) Germany\nC) France\nyour answer: ")

if choice3 == "A":
    print("wrong!")

elif choice3 == "B":
    print("wrong!")

else:
    print("correct!")
    score += 1

print("your score is:", score)