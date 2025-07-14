import time

# Define board dimensions
ROWS = 6
COLUMNS = 7

# Define game pieces
EMPTY = ' '    # Empty cell
PLAYER = 'X'   # Human player
AI = 'O'       # Computer (AI) player

# Create an empty 6x7 board
board = [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

# Print the current state of the board
def print_board():
    print()
    for row in board:
        print('|', ' | '.join(row), '|')  # Display each row with separators
    print(' ', '   '.join(str(i + 1) for i in range(COLUMNS)))  # Column numbers for input
    print()

# Check if a column can accept a new piece
def is_valid_location(column):
    return board[0][column] == EMPTY  # Top row must be empty to drop a piece

# Return the next available row in a column (from bottom up)
def get_next_open_row(column):
    for row in range(ROWS - 1, -1, -1):  # Start from bottom row
        if board[row][column] == EMPTY:
            return row
    return None  # Column is full

# Place a piece on the board
def drop_piece(row, column, piece):
    board[row][column] = piece

# Check if a player has four in a row (win condition)
def winning_move(piece):
    # Horizontal check
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical check
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Positive diagonal check (/)
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Negative diagonal check (\)
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

# Check if the top row is fully filled (i.e., board is full)
def is_board_full():
    return all(board[0][c] != EMPTY for c in range(COLUMNS))

# Minimax algorithm with alpha-beta pruning to choose the best move
def minimax(depth, alpha, beta, is_maximizing):
    # Terminal conditions: someone won or board is full or max depth reached
    if winning_move(AI):
        return (None, 1000000)  # Very good for AI
    elif winning_move(PLAYER):
        return (None, -1000000)  # Very bad for AI
    elif is_board_full() or depth == 0:
        return (None, 0)  # Tie or max depth reached

    if is_maximizing:
        max_eval = -float('inf')
        best_col = None
        for col in range(COLUMNS):
            if is_valid_location(col):
                row = get_next_open_row(col)
                board[row][col] = AI  # Try AI move
                current_score = minimax(depth - 1, alpha, beta, False)[1]
                board[row][col] = EMPTY  # Undo move

                if current_score > max_eval:
                    max_eval = current_score
                    best_col = col

                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break  # Alpha-beta pruning
        return best_col, max_eval
    else:
        min_eval = float('inf')
        best_col = None
        for col in range(COLUMNS):
            if is_valid_location(col):
                row = get_next_open_row(col)
                board[row][col] = PLAYER  # Try player move
                current_score = minimax(depth - 1, alpha, beta, True)[1]
                board[row][col] = EMPTY  # Undo move

                if current_score < min_eval:
                    min_eval = current_score
                    best_col = col

                beta = min(beta, min_eval)
                if beta <= alpha:
                    break  # Alpha-beta pruning
        return best_col, min_eval

# Handle player's move
def player_move():
    while True:
        try:
            col = int(input("Choose a column to drop your piece (1-7): ")) - 1
            if 0 <= col < COLUMNS and is_valid_location(col):
                row = get_next_open_row(col)
                drop_piece(row, col, PLAYER)
                break
            else:
                print("Oops! That column is full or invalid. Try a different column.")
        except ValueError:
            print("Please enter a valid number between 1 and 7.")

# Handle AI's move
def ai_move():
    print("AI is thinking...")
    time.sleep(1)  # Pause for dramatic effect
    col, _ = minimax(4, -float('inf'), float('inf'), True)  # Depth 4: medium difficulty
    if col is not None:
        row = get_next_open_row(col)
        drop_piece(row, col, AI)
        print(f"AI dropped a piece in column {col + 1}.")

# Main game function
def main():
    print("Welcome to Connect Four!")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()

        if winning_move(PLAYER):
            print("Congratulations! You won!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        # AI's turn
        ai_move()
        print_board()

        if winning_move(AI):
            print("AI wins! Better luck next time.")
            break
        if is_board_full():
            print("It's a tie!")
            break

# Ensure main() runs only when this file is the entry point
if __name__ == "__main__":
    main()
