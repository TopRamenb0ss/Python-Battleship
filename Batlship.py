from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Battleship, b0ss"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Coumnl:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "U fokn wot, sunk my battleship"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Either you are out of the ocean, or my code thinks 5 is too big in a 5x5 square."
        elif(board[guess_row][guess_col] == "X"):
            print "Pick another one"
        elif turn == 3:
            print "u dun goofed"
        else:
            print "You missed, don't peek an AWP!"
            board[guess_row][guess_col] = "X"
        print (turn + 1)
        print_board(board)