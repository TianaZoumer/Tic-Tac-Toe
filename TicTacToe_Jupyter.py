from IPython.display import clear_output

# Establish list of game placement options
board = [0,1,2,3,4,5,6,7,8]

# Print 3x3 game board
def display_game(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

#  Let user choose a placement
def position_choice(board):
    choice = 'wrong'
    game = [str(i) for i in board]
    while choice not in game:
        choice = input("Please pick a position (0-8): ")
        if choice.isdigit() == False:
            print("I'm sorry, that's not a number.")
        elif choice not in game:
            print("I'm sorry, that position isn't available.")
    return int(choice)

# Allow user to choose X or O
# Place X or O at their placement location
def replacement_choice(board,position):
    choice = 'wrong'
    while choice not in ['X','O']:
        choice = input("Type an X or an O: ")
        if choice not in ['X','O']:
            print("I'm sorry, that isn't an X or O.")
        else:
            board[position] = choice
    return board

# Ask player if they want to keep playing Y or N
# Y game on, N game off
def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N: ")
        if choice not in ['Y', 'N']:
            print("I'm sorry, I don't understand.")
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False

# GAME PLAY

# variable to keep game play
game_on = True

while game_on:
    clear_output()
    display_game(board)
    
# Player chooses position
    position = position_choice(board)

# Position updates game board
    board = replacement_choice(board,position)

# Ask to keep playing
    game_on = gameon_choice()
