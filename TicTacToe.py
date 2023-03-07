'''
Implement 2 player Tic Tac Toe Game

Player 1 and Player 2 Alternate taking turns

Player wins when they get 3 of their mark in a row
mark is either
- O
- X
'''


def createBoard():
    print("***** Board Layout *****")
    print(" 1 | 2 | 3 ")
    print("--- --- ---")
    print(" 4 | 5 | 6 ")
    print("--- --- ---")
    print(" 7 | 8 | 9 ")
    print()
    print("***** Current Board *****")
    # TODO: Update Board


gameOver = False
player1 = True
options = ["", "", "",
           "", "", "",
           "", "", ""]

while not gameOver:
    if player1:
        choice = input("Please enter Choice Player 1 (You are X): ")
        player1 = False
    else:
        choice = input("Please enter Choice Player 2 (You are O): ")
        player1 = True
