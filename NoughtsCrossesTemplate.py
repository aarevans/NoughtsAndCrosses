def DisplayBoard():#display the board whenever needed by calling this function.
    for row in board:
        print(row[0],row[1],row[2])
    print()

def P1Turn():
    R=0
    C=0
    while R == 0 and C == 0:
        print("P1 please select a row (1-3)")
        while R != 1 and R != 2 and R != 3:
            R = int(input(">>>"))
            print()
        print("P1 please select a column (1-3)")
        while C != 1 and C != 2 and C != 3:
            C = int(input(">>>"))
            print()

        if board[R-1][C-1] == "[X]" or board[R-1][C-1] == "[0]":
            R=0
            C=0
            print("That space is taken, try again")
            print()
        else:
            board[R-1][C-1] = "[X]"
            
def P2Turn():
    R=0
    C=0
    while R == 0 and C == 0:
        print("P2 please select a row (1-3)")
        while R != 1 and R != 2 and R != 3:
            R = int(input(">>>"))
            print()
        print("P2 please select a column (1-3)")
        while C != 1 and C != 2 and C != 3:
            C = int(input(">>>"))
            print()

        if board[R-1][C-1] == "[X]" or board[R-1][C-1] == "[0]":
            R=0
            C=0
            print("That space is taken, try again")
            print()
        else:
            board[R-1][C-1] = "[0]"    

def GamePlay():
    win = False
    while win != True:
        P1Turn()
        DisplayBoard()
        win,draw = WinCheck()
        if win == True:
            print("Player 1 wins!")
        elif draw == True:
            print("It's a draw!")
            win = True
        else:
            P2Turn()
            DisplayBoard()
            win,draw = WinCheck()
            if win == True:
                print("Player 2 wins!")
            elif draw == True:
                print("It's a draw!")
                win = True
       

def WinCheck():
    win = False
    draw = False

    if board[0][0] != "[ ]" and board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        win = True
        return win,draw
    elif board[1][0] != "[ ]" and board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        win = True
        return win,draw
    elif board[2][0] != "[ ]" and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        win = True
        return win,draw
    elif board[0][0] != "[ ]" and board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        win = True
        return win,draw
    elif board[0][1] != "[ ]" and board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        win = True
        return win
    elif board[0][2] != "[ ]" and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        win = True
        return win,draw
    elif board[0][0] != "[ ]" and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        win = True
        return win,draw
    elif board[0][2] != "[ ]" and board[0][2] == board[1][1] and board[2][0] == board[2][2]:
        win = True
        return win,draw

    draw = True
    for row in board:
        for item in row:
            if item == "[ ]":
                draw = False
    return win,draw

board = [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]
win = False

#main    
print("Welcome to Noughts and Crosses")
print("0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X")
print()
input("Press enter to continue")
print()
print("To take your turn, first enter your row number (R)")
print()
input("Press enter to continue")
print()
print("Followed by your column number (C)")
print()
input("Press enter to continue")

#example of R and C numbers
print()
print("The board:")
x=0
for row in board:
        print("R"+str(x+1)+str(row[0]),row[1],row[2])
        x=x+1
print("   C1"+"  C2"+"  C3")
print()
input("Press enter to continue")
print()
print("Player 1 will go first, they are 0's")
print()
input("Press enter to continue")
print()
print("Player 2 will go second, they are X's")
print()
input("Press enter to continue")
print()

GamePlay()
print()
playAgain = True
while playAgain != False:
    playAgain = input("Press Y to play again")
    if playAgain == "y" or playAgain == "Y":
        playAgain = True
        board = [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]
        GamePlay()
    else:
        playAgain = False



