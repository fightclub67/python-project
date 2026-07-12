
print("welcome to quiz game!")
score = 0
option = input("are you ready? ")
if option == "yes":
    print("the quiz has started!")

    choice = input("what does CPU stand for? ")
    if choice == "central processing unit":
        print("correct!")
        score += 1
    else:
        print("wrong!")

else:
    print("Goodbye!")

option2 = input("what does RAM stand for? ")

if option2 == "random access memory":
    print("correct!")
    score += 1

else:
    print("wrong!")

option3 = input("what keyword is used to create a loop in python? ")

if option3 == "while":
    print("correct!")
    score += 1

else:
    print("wrong!")

print("your score is: ", score)