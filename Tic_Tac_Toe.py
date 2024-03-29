import pyfiglet
import random
import time


title = pyfiglet.figlet_format("Tic Tac Toe", font='slant')
print(title)


game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]


def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()


def check_game():
    for i in range(3):
        # check rows
        if game_board[i][0] == game_board[i][1] == game_board[i][2] and game_board[i][0] != "-":
            print("Player ", game_board[i][0], " wins")
            return False
        # check columns
        if game_board[0][i] == game_board[1][i] == game_board[2][i] and game_board[0][i] != "-":
            print("Player ", game_board[0][i], " wins")
            return False
        # check diagonals
        if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != "-":
            print("Player ", game_board[1][1], " wins")
            return False
        # check diagonals
        if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[1][1] != "-":
            print("Player ", game_board[1][1], " wins")
            return False
    return True


show()

Flag = True
counter = 0
while Flag and counter < 9:
    print("Player 1's turn")
    while True:
        row = int(input("row between 0 - 2: "))
        col = int(input("col between 0 - 2: "))
        print("row: ", row)
        print("col: ", col)
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                break
            else:
                print("you can't choose this cell")
        else:
            print("your choice is out of range")
    show()
    Flag = check_game()
    if not Flag:
        break
    counter += 1
    if counter == 9:
        break

    print("Player 2's turn")
    time.sleep(5)
    while True:
        row = random.randint(0, 2)  # select random row in range 0 - 2
        col = random.randint(0, 2)  # select random col in range 0 - 2
        print("row: ", row)
        print("col: ", col)
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                break
            else:
                print("you can't choose this cell")
        else:
            print("your choice is out of range")
    show()
    Flag = check_game()
    if not Flag:
        break
    counter += 1

if counter == 9:
    print("Two players are loss")
