# Creating the Board and some variable
import random


tictactoeboard = ["_", "_", "_", "_", "_", "_", "_",
                  "_", "_", "_", "_", "_", "_", "_",
                  "_", "_", "_", "_", "_", "_", "_",
                  "_", "_", "_", "_", "_", "_", "_",
                  "_", "_", "_", "_", "_", "_", "_",
                  "_", "_", "_", "_", "_", "_", "_",
                  "_", "_", "_", "_", "_", "_", "_"]

Player1 = "X"
winner = None
gameRunning = True

#Printing the board game
def printtictactoeboard(tictactoeboard):
    print(tictactoeboard[0] + " | " + tictactoeboard[1] + " | " + tictactoeboard[2] + " | " + tictactoeboard[3] + " | " + tictactoeboard[4] + " | " + tictactoeboard[5] + " | " + tictactoeboard[6])
    print("_________________________")
    print(tictactoeboard[7] + " | " + tictactoeboard[8] + " | " + tictactoeboard[9] + " | " + tictactoeboard[10] + " | " + tictactoeboard[11] + " | " + tictactoeboard[12] + " | " + tictactoeboard[13])
    print("_________________________")
    print(tictactoeboard[14] + " | " + tictactoeboard[15] + " | " + tictactoeboard[16] + " | " + tictactoeboard[17] + " | " + tictactoeboard[18] + " | " + tictactoeboard[19] + " | " + tictactoeboard[20])
    print("_________________________")
    print(tictactoeboard[21] + " | " + tictactoeboard[22] + " | " + tictactoeboard[23] + " | " + tictactoeboard[24] + " | " + tictactoeboard[25] + " | " + tictactoeboard[26] + " | " + tictactoeboard[27]) 
    print("_________________________")
    print(tictactoeboard[28] + " | " + tictactoeboard[29] + " | " + tictactoeboard[30] + " | " + tictactoeboard[31] + " | " + tictactoeboard[32] + " | " + tictactoeboard[33] + " | " + tictactoeboard[34])
    print("_________________________")
    print(tictactoeboard[35] + " | " + tictactoeboard[36] + " | " + tictactoeboard[37] + " | " + tictactoeboard[38] + " | " + tictactoeboard[39] + " | " + tictactoeboard[40] + " | " + tictactoeboard[41])
    print("_________________________")
    print(tictactoeboard[42] + " | " + tictactoeboard[43] + " | " + tictactoeboard[44] + " | " + tictactoeboard[45] + " | " + tictactoeboard[46] + " | " + tictactoeboard[47] + " | " + tictactoeboard[48])
    print("_________________________")
printtictactoeboard(tictactoeboard)


#take player input
def playerInput (tictactoeboard):
    playerinp = int(input("Input a number from 1-49: "))
    if playerinp >= 1 and playerinp <= 49 and tictactoeboard[playerinp-1] == "_":
        tictactoeboard[playerinp-1] = Player1
    else:
        print("Sorry! Player already owns that spot")

#check for win or tie
def Horizontlecheck(tictactoeboard):
    global winner
    if  tictactoeboard[0] == tictactoeboard[1] == tictactoeboard[2] == tictactoeboard[3] == tictactoeboard[4]  == tictactoeboard[5] == tictactoeboard[6]  == tictactoeboard[1] !="_":
        winner = tictactoeboard[0]
        return True
    elif tictactoeboard[7] == tictactoeboard[8] == tictactoeboard[9] == tictactoeboard[10] == tictactoeboard[11] == tictactoeboard[12] == tictactoeboard[13]  == tictactoeboard[7] !="_":
        winner = tictactoeboard[7]
        return True 
    elif tictactoeboard[14] == tictactoeboard[15] == tictactoeboard[16] == tictactoeboard[17] == tictactoeboard[18] == tictactoeboard[19] == tictactoeboard[20]  == tictactoeboard[14] !="_":
        winner = tictactoeboard[14]
        return True 
    elif tictactoeboard[21] == tictactoeboard[22] == tictactoeboard[23] == tictactoeboard[24] == tictactoeboard[25] == tictactoeboard[26] == tictactoeboard[27]  == tictactoeboard[21] !="_":
        winner = tictactoeboard[21]
        return True 
    elif tictactoeboard[28] == tictactoeboard[29] == tictactoeboard[30] == tictactoeboard[31] == tictactoeboard[32] == tictactoeboard[33] == tictactoeboard[34]  == tictactoeboard[28] !="_":
        winner = tictactoeboard[28]
        return True 
    elif tictactoeboard[35] == tictactoeboard[36] == tictactoeboard[37] == tictactoeboard[38] == tictactoeboard[39] == tictactoeboard[40] == tictactoeboard[41]  == tictactoeboard[35] !="_":
        winner = tictactoeboard[35]
        return True 
    elif tictactoeboard[42] == tictactoeboard[43] == tictactoeboard[44] == tictactoeboard[45] == tictactoeboard[46] == tictactoeboard[47] == tictactoeboard[48]  == tictactoeboard[42] !="_":
        winner = tictactoeboard[36]
        return True 


def Rowcheck(tictactoeboard):
    global winner
    if  tictactoeboard[0] == tictactoeboard[7] == tictactoeboard[14] == tictactoeboard[21] == tictactoeboard[28]  == tictactoeboard[35] == tictactoeboard[36]  == tictactoeboard[0] !="_":
        winner = tictactoeboard[0]
        return True
    elif tictactoeboard[1] == tictactoeboard[8] == tictactoeboard[15] == tictactoeboard[22] == tictactoeboard[29] == tictactoeboard[36] == tictactoeboard[37]  == tictactoeboard[1] !="_":
        winner = tictactoeboard[1]
        return True 
    elif tictactoeboard[2] == tictactoeboard[9] == tictactoeboard[16] == tictactoeboard[23] == tictactoeboard[30] == tictactoeboard[37] == tictactoeboard[38]  == tictactoeboard[2] !="_":
        winner = tictactoeboard[2]
        return True 
    elif tictactoeboard[3] == tictactoeboard[10] == tictactoeboard[17] == tictactoeboard[24] == tictactoeboard[31] == tictactoeboard[38] == tictactoeboard[39]  == tictactoeboard[3] !="_":
        winner = tictactoeboard[3]
        return True 
    elif tictactoeboard[4] == tictactoeboard[11] == tictactoeboard[18] == tictactoeboard[25] == tictactoeboard[32] == tictactoeboard[39] == tictactoeboard[40]  == tictactoeboard[4] !="_":
        winner = tictactoeboard[4]

    elif tictactoeboard[5] == tictactoeboard[12] == tictactoeboard[19] == tictactoeboard[26] == tictactoeboard[33] == tictactoeboard[40] == tictactoeboard[41]  == tictactoeboard[5] !="_":
        winner = tictactoeboard[5]
        return True 
    elif tictactoeboard[6] == tictactoeboard[13] == tictactoeboard[20] == tictactoeboard[27] == tictactoeboard[34] == tictactoeboard[41] == tictactoeboard[42]  == tictactoeboard[6] !="_":
        winner = tictactoeboard[6]
        return True 
    

def diagonalcheck(tictactoeboard):
    global winner
    if  tictactoeboard[0] == tictactoeboard[8] == tictactoeboard[16] == tictactoeboard[24] == tictactoeboard[32]  == tictactoeboard[40]  == tictactoeboard[48]  == tictactoeboard[0] !="_":
        winner = tictactoeboard[0]
        return True
    elif tictactoeboard[6] == tictactoeboard[12] == tictactoeboard[18] == tictactoeboard[24] == tictactoeboard[31] == tictactoeboard[36]  == tictactoeboard[43]  == tictactoeboard[6] !="_":
        winner = tictactoeboard[1]
        return True 

def Tiecheck(tictactoeboard):
    if "_" not in tictactoeboard:
        printtictactoeboard(tictactoeboard)
        print("Unfortunely it's a tie, try better next time")
        gameRunning = False
    


#switch the player
def swapPlayer():
    global Player1
    if Player1 =="X":
        Player1 = "O"
    else:
        Player1 = "X"


#check for the win or tie again
def Wincheck():
    if Horizontlecheck(tictactoeboard) or Rowcheck(tictactoeboard) or diagonalcheck(tictactoeboard):
        print(f" Winner is {winner}")

#Automated AI
def computer (tictactoeboard):
    while Player1 == "0":
        location = random.randint (0, 49)
        if tictactoeboard[location] == "_":
            tictactoeboard[location] = "0"
            swapPlayer()

#gameloops
while gameRunning:
    printtictactoeboard(tictactoeboard)
    playerInput(tictactoeboard)
    Tiecheck (tictactoeboard)
    swapPlayer()
    Wincheck()
    computer(tictactoeboard)
    Wincheck() 
    Tiecheck(tictactoeboard)





 








  