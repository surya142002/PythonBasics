'''
Objective is to guess a random number between 1 and 100

There are 5 attempts.

After each attempt, the user will know if their answer is either
- Correct
- Too High
- Too Low
- Incorrect: Out of Guesses!
'''

import random

target = random.randint(1, 100)
winner = False

print("You have 5 guesses to find the random number between 1 and 100!")

for i in range(1,6):
    guess = input("What is your " + str(i) + " guess? ")
    if int(guess) > target:
        print("Too High!")
    elif int(guess) < target:
        print("Too Low!")
    else:
        print("Correct!")
        winner = True
        break

print("The number was: " + str(target))

if winner:
    print("Good Guess You Win!!")
else:
    print("You Are Out Of Guesses! Better Luck Next Time!")

