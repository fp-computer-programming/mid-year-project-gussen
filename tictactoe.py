# Author: CCG 3/2/22

def gameboard(board): # make the visual board and replace the chosen spots with the chosen marker
    blankBoard="""
1 2 3
4 5 6
7 8 9
"""
    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
    print(blankBoard)

def markerchoice(): # Asks which player will be using which marker and sets them equal to their correct marker
    player1 = input("Enter the marker you want to use (Either 'X' or 'O'): ")
    while True:
        if player1.upper() == 'X':
            player2 = 'O'
            print("Player 1 is X. Player 2 is O.")
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2 = 'X'
            print("Player 1 is O. Player 2 is X.")
            return player1.upper(),player2
        else:
            player1 = input("Enter the marker you want to use (Either 'X' or 'O'): ")

def placemarker(board, marker, place): # place the marker on the board
    board[place] = marker
    return board

def opencheck(board, place): # check if selected spot is avaiable
    return board[place] == '-'

def playerchoice(board): # ask users which spot they want to choose and uses previous function to help user if they choose an unavaiable spot
    choice = input("Choose you move based of the numbers on the board (Between 1 and 9): ")
    while not opencheck(board, int(choice)):
        choice = input("That space isn't avaiable. Please choose an open space between 1 and 9: ")
    return choice

def tie(board): # make sure board isn't filled aka a tie
    return len([x for x in board if x == '-']) == 1


def xwin(board, mark): # check to see if X won
    if mark == "X":
        if board[1] == board[2] == board[3] == mark:
            return True
        if board[4] == board[5] == board[6] == mark:
            return True
        if board[7] == board[8] == board[9] == mark:
            return True
        if board[1] == board[4] == board[7] == mark:
            return True
        if board[2] == board[5] == board[8] == mark:
            return True
        if board[3] == board[6] == board[9] == mark:
            return True
        if board[1] == board[5] == board[9] == mark:
            return True
        if board[3] == board[5] == board[7] == mark:
            return True
    else:
        return False

def owin(board, mark): # check to see if O won
    if mark == "O":
        if board[1] == board[2] == board[3] == mark:
            return True
        if board[4] == board[5] == board[6] == mark:
            return True
        if board[7] == board[8] == board[9] == mark:
            return True
        if board[1] == board[4] == board[7] == mark:
            return True
        if board[2] == board[5] == board[8] == mark:
            return True
        if board[3] == board[6] == board[9] == mark:
            return True
        if board[1] == board[5] == board[9] == mark:
            return True
        if board[3] == board[5] == board[7] == mark:
            return True
    else:
        return False

def replay(): # ask users if they want to play again
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False
    if playAgain.lower() != 'y' or playAgain.lower() != 'y':
        playAgain = input("Please enter either 'y' or 'n' ")

print('This is Tic Tac Toe!')
i = 1 # helps program determine whose turn it is
players = markerchoice() # choose marker
board = ['-'] * 10 # set board
while True: # set visual to show users the board and the correlating numbers  
    print('1 2 3')
    print('4 5 6')
    print('7 8 9')
    game_on = tie(board)
    while not game_on: # make sure game isnt tied 
        place = playerchoice(board) # place markers
        if i % 2 == 0: # program determining whose move it is
            marker = players[1]
        else:
            marker = players[0]
        placemarker(board, marker, int(place))
        gameboard(board)
        i += 1 # make sure correct player is going
        if xwin(board, marker): # check if x won
            print("The player using X won!")
            break
        if owin(board, marker): # check if o won
            print("The player using O won!")
            break
        game_on = tie(board) # check if game was tied
    if not replay(): # if statement to end loop of playing
        print('Thank you for playing!')
        break
    else: # else to play again
        i = 1
        players = markerchoice()
        board = ['-'] * 10
