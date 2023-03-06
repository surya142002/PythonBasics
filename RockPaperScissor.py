'''
Rock Paper Scissor vs the computer

Randomly generated value
1 - rock
2 - paper
3 - scissor
'''
import random

def checkWinner(computer, person):
    valueDict = {1: "Rock", 2: "Paper", 3: "Scissor"}
    if computer == person:
        print("Tie Game Both Picked: " + str(valueDict[computer]))
    elif computer == 1 and person == 2:
        print("You Win! Computer picked " + str(valueDict[computer]))
    elif computer == 2 and person == 3:
        print("You Win! Computer picked " + str(valueDict[computer]))
    elif computer == 3 and person == 1:
        print("You Win! Computer picked " + str(valueDict[computer]))
    else:
        print("You Lose! Computer picked " + str(valueDict[computer]))


print("1 = Rock")
print("2 = Paper")
print("3 = Scissor")

computer = random.randint(1,3)
person = int(input("Please Enter Number of Choice: "))

checkWinner(computer, person)

