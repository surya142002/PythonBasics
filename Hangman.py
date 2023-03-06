'''
This program will ask user to enter a word

They will then get 7 mistakes to guess the word

I am too lazy to draw out a hangman so I will use something easier
'''
def drawPicture(guesses):
    print()
    print("Imaginary Bullet", end =" ")
    for i in range(0,guesses):
        print("->", end =" ")
    for i in range(0, 7 - guesses):
        print("  ", end =" ")
    if guesses < 7:
        print("(@.@)")
        print("OH NO! Only " + str(7 - guesses) + " attempts remaining!!")
    else:
        print("(x.x)")
        print("OH NO! You died!!")
        quit()
    print()

def printString(listGuesses, secretWord):
    print()
    for letter in secretWord:
        if letter.lower() in listGuesses:
            print(letter.upper(), end =" ")
        else:
            print("-", end =" ")
    print()


guesses = 0
secretWord = input("Please enter the word you want to guess: ").lower()
print()
listGuesses = []

while guesses < 7:
    choice = input("Enter 1 to guess the word or Enter 2 to guess a letter: ")
    if int(choice) == 1:
        wordGuess = input("What is your guess?").lower()
        if wordGuess == secretWord:
            print("YOU WINN!!!!!")
        else:
            print("YOU LOSE!!!!! The word was " + secretWord)
        quit()
    else:
        letter = input("What is your " + str(guesses + 1) + " guess?").lower()
        listGuesses.append(letter)
        if letter in secretWord:
            print("Good guess!!")
            printString(listGuesses, secretWord)
        else:
            print("Bad Guess!!")
            guesses = guesses + 1
            drawPicture(guesses)
            printString(listGuesses, secretWord)
            print()








