import math
import time

# Create a 1D board of 9 empty spaces (representing 3x3 grid)
board = [' ' for _ in range(9)]

# Function to display the current board
def print_board():
    for i in range(0, 9, 3):
        print(f'| {board[i]} | {board[i+1]} | {board[i+2]} |')

# Function to check if a given player ('X' or 'O') has won
def is_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],     # Horizontal
        [0,3,6],[1,4,7],[2,5,8],     # Vertical
        [0,4,8],[2,4,6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True  # Player has a winning combination
    return False  # No win

# Check if the board is full (no empty cells)
def is_board_full():
    return ' ' not in board

# Minimax algorithm to evaluate the best possible move
def minimax(is_maximizing):
    # Base conditions: Check for win or draw
    if is_winner('O'):
        return 1     # AI wins
    elif is_winner('X'):
        return -1    # Player wins
    elif is_board_full():
        return 0     # Draw

    if is_maximizing:
        # AI (O) is trying to maximize score
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'                # Try move
                score = minimax(False)        # Recur for minimizing player
                board[i] = ' '                # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        # Player (X) is trying to minimize score
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'                # Try move
                score = minimax(True)         # Recur for maximizing player
                board[i] = ' '                # Undo move
                best_score = min(score, best_score)
        return best_score

# AI chooses the best possible move using minimax
def best_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'                    # Try move
            score = minimax(False)            # Get score for this move
            board[i] = ' '                    # Undo move
            if score > best_score:
                best_score = score            # Update best score
                move = i                      # Store best move
    return move

# Get input from human player
def player_move():
    while True:
        move = int(input('Enter move between (1-9):')) - 1
        if move < 0 or move > 8:
            print('Invalid move')             # Out of range
        elif board[move] != ' ':
            print('Invalid move')             # Already filled
        else:
            board[move] = 'X'                 # Valid move
            break

# --- Main game loop ---
print("Welcome to Tic-tac-Toe! You are 'X' and AI is 'O'")
print_board()

while True:
    # Player's turn
    player_move()
    print_board()

    # Check if player won or if it's a tie
    if is_winner('X'):
        print('You win!')
        break
    elif is_board_full():
        print("It's a tie!")
        break

    # AI's turn
    print("AI is making a move...")
    time.sleep(2)
    ai_move = best_move()
    board[ai_move] = 'O'
    print_board()

    # Check if AI won or if it's a tie
    if is_winner('O'):
        print('AI wins!')
        break
    elif is_board_full():
        print("It's a tie!")
        break
