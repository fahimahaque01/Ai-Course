import math

# Initialize board
board = [" " for _ in range(9)]

# Print board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check winner
def check_winner(brd, player):
    win_cond = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
    for (x,y,z) in win_cond:
        if brd[x] == brd[y] == brd[z] == player:
            return True
    return False

# Check for draw
def is_draw(brd):
    return " " not in brd

# Get available moves
def available_moves(brd):
    return [i for i in range(9) if brd[i] == " "]

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if check_winner(brd, "O"):#AI
        return 1
    elif check_winner(brd, "X"):#human
        return -1
    elif is_draw(brd):
        return 0
 
    if is_maximizing:
        best_score = -math.inf      #cuto man dore jate onno valu er cheye boro hoy 
        for move in available_moves(brd):
            brd[move] = "O"
            score = minimax(brd, depth + 1, False)
            brd[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(brd):
            brd[move] = "X"
            score = minimax(brd, depth + 1, True)
            brd[move] = " "
            best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("Computer's turn:")
        ai_move()
        print_board()

        if check_winner(board, "O"):
            print("Computer wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

play_game()


