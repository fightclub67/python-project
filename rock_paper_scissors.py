score = 0
import random
choices = ["rock", "paper", "scissors"]
player = input("choose rock, paper or scissors: ")
computer = random.choice(choices)
print("player:", player)
print("computer:", computer)

if player == computer:
    print("draw!")

elif player == "rock" and computer == "scissors":
    print("player won!")
    score+= 1

elif player == "paper" and computer == "rock":
    print("player won!")
    score+= 1

elif player == "scissors" and computer == "paper":
    print("player won!")
    score+=1

else:
    print("computer won!")
print("your score is:", score)