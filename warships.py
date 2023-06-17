from random import randint
import platform
import os

def clear():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

# Function to create the game board
def create_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Function to print the game board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to generate a random position for the warship
def generate_ship_position(size):
    return (randint(0, size-1), randint(0, size-1))

# Function to set warship position in two player mode
def positionate_ship(x, y):
    return(x, y)

# Function to check if the guess is correct
def check_guess(guess, ship_position):
    return guess == ship_position

# Game setup
board_size = 5
board = create_board(board_size)

# Game loop
print("Welcome to the Warships Game!")
print("Guess the position of the hidden warship.")

print("Who do you want to play against?")
print("Type C for Computer")
print("Type P for Player 2")

choice = input("Your choice: ")

if(choice == 'C'):

    ship_position = generate_ship_position(board_size)

    while True:
        print_board(board)
        guess_row = int(input("Enter the row (0-4): "))
        guess_col = int(input("Enter the column (0-4): "))

        if check_guess((guess_row, guess_col), ship_position):
            clear()
            print("Congratulations! You sank the warship!")
            break
        else:
            clear()
            print("Oops! Try again.")
            board[guess_row][guess_col] = 'X'

elif(choice == 'P'):

    board_2 = create_board(board_size)

    print("Player 1 turn.")
    print("Your warship position")
    x = input("Enter the row (0-4): ")
    y = input("Enter the column (0-4): ")

    ship_position = positionate_ship(x, y)

    print("Player 1 turn.")
    print("Your warship position")
    x = input("Enter the row (0-4): ")
    y = input("Enter the column (0-4): ")

    ship_2_position = positionate_ship(x, y)

    while True:
        print("Player 1 turn.")
        print_board(board)
        guess_row = int(input("Enter the row (0-4): "))
        guess_col = int(input("Enter the column (0-4): "))

        if check_guess((guess_row, guess_col), ship_position):
            clear()
            print("Congratulations! You sank the warship!")
            print("Player 2 wins!")
            break
        else:
            clear()
            print("Oops! You've missed.")
            board[guess_row][guess_col] = 'X'
        
        print("Player 2 turn.")
        print_board(board_2)
        guess_row = int(input("Enter the row (0-4): "))
        guess_col = int(input("Enter the column (0-4): "))

        if check_guess((guess_row, guess_col), ship_2_position):
            clear()
            print("Congratulations! You sank the warship!")
            print("Player 2 wins!")
            break
        else:
            clear()
            print("Oops! You've missed.")
            board_2[guess_row][guess_col] = 'X'
