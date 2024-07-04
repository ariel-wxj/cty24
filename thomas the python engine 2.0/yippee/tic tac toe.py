board = [
    ["-","-","-",],
    ["-","-","-",],
    ["-","-","-",]
]



print("welome to tic tac toe")
for i in board:
    print(i)

#endTheGame = False

playerNumber = input("are you player 1 or 2?")
#if playerNumber > 2 or playerNumber < 1:
    #print("error")
userSymbol = input("what number do you want to be?")

class str:

    topLeft = board[0][0],
    topMiddle = board[0][1],
    topRight = board[0][2],
    middleLeft = board[1][0],
    middle = board[1][1],
    middleRight = board[1][2],
    bottomLeft = board[2][0],
    bottomMiddle = board[2][1],
    bottomRight = board[2][2]

userInput = input("where do you want to go?")



board.pop(int(userInput))
board.insert(int(userInput), userSymbol)

if i in board:
    print(board)










#printing board

"""


playing game
while (endTheGame == False):
    for i in board:
        print(i)
        print(playerInput)
       

"""

