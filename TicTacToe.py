'''
Implement 2 player Tic Tac Toe Game

Player 1 and Player 2 Alternate taking turns

Player wins when they get 3 of their mark in a row
mark is either
- O
- X
'''
def checkWinner(options):
    # check vertical
    for i in range(0,4):
        if options[i] != " " and options[i] == options[i + 3] and options[i + 3] == options[i + 6]:
            print("GAME OVER PLAYER " + options[i] + " WINS!!")
            return True

    # check horizontal
    for i in range(0,7,3):
        if options[i] != " " and options[i] == options[i + 1] and options[i + 1] == options[i + 2]:
            print("GAME OVER PLAYER " + options[i] + " WINS!!")
            return True

    # check 2 diagonals
    if options[1] != " " and options[1] == options[5] and options[5] == options[9]:
        print("GAME OVER PLAYER " + options[1] + " WINS!!")
        return True
    if options[3] != " " and options[3] == options[5] and options[5] == options[7]:
        print("GAME OVER PLAYER " + options[3] + " WINS!!")
        return True

def createBoard(options):
    print("***** Board Layout *****")
    print(" 1 | 2 | 3 ")
    print("--- --- ---")
    print(" 4 | 5 | 6 ")
    print("--- --- ---")
    print(" 7 | 8 | 9 ")
    print()
    print("***** Current Board *****")
    print(" " + options[0] + " | " + options[1] + " | " + options[2] + " ")
    print("--- --- ---")
    print(" " + options[3] + " | " + options[4] + " | " + options[5] + " ")
    print("--- --- ---")
    print(" " + options[6] + " | " + options[7] + " | " + options[8] + " ")
    print("************************")

gameOver = False
player1 = True
options = [" ", " ", " ",
           " ", " ", " ",
           " ", " ", " "]

createBoard(options)
while not gameOver:
    if player1:
        choice = input("Please enter Choice Player 1 (You are X): ")
        if options[int(choice) - 1] != " ":
            print("Invalid Choice Try Again!")
            continue
        else:
            options[int(choice) - 1] = "X"
        player1 = False
    else:
        choice = input("Please enter Choice Player 2 (You are O): ")
        if options[int(choice) - 1] != " ":
            print("Invalid Choice Try Again!")
            continue
        else:
            options[int(choice) - 1] = "O"
        player1 = True
    createBoard(options)
    gameOver = checkWinner(options)
