import chess  # Python chess library to handle board and rules
import math   # For infinity values used in Minimax
import random # To shuffle move order for variability
import time   # To simulate AI thinking delay

# Assign simple values to pieces for evaluation
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0  # King value is set to 0 because checkmate is handled separately
}

# Evaluate the board from the perspective of Black (AI positive, White negative)
def evaluate_board(board):
    score = 0
    for piece_type in piece_values:
        # Add AI (black) pieces' value
        score += len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
        # Subtract player's (white) pieces' value
        score -= len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
    return score

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    # Base case: reached depth or game over
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if is_maximizing:
        max_eval = -math.inf
        for move in legal_moves:
            board.push(move)  # Make the move
            eval = minimax(board, depth - 1, alpha, beta, False)  # Recurse as minimizing
            board.pop()  # Undo move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for move in legal_moves:
            board.push(move)  # Make the move
            eval = minimax(board, depth - 1, alpha, beta, True)  # Recurse as maximizing
            board.pop()  # Undo move
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Get the best move for the AI using Minimax
def get_best_move(board, depth):
    best_score = -math.inf
    best_move = None
    legal_moves = list(board.legal_moves)
    random.shuffle(legal_moves)  # Shuffle to add randomness when scores are equal

    for move in legal_moves:
        board.push(move)  # Try move
        score = minimax(board, depth - 1, -math.inf, math.inf, False)  # Opponent's turn
        board.pop()  # Undo move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def main():
    board = chess.Board()  # Initialize board
    print("Welcome to Minimax Chess (You are White). Move format: e2e4")
    print(board)

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            # Player's turn
            move_input = input("Your move: ")
            try:
                move = chess.Move.from_uci(move_input)  # Convert input to move
                if move in board.legal_moves:
                    board.push(move)  # Make the move
                else:
                    print("Illegal move. Try again.")
                    continue
            except (ValueError, AttributeError):
                print("Invalid move format. Try again.")
                continue
        else:
            # AI's turn
            print("Computer thinking...")
            time.sleep(2)  # Simulate thinking
            best_move = get_best_move(board, depth=3)  # Search depth 3
            board.push(best_move)  # AI makes the move
            print(f"Computer played: {best_move}")

        print(board)  # Display the board
        if board.is_check():
            print("Check! King is under attack!")

    # Game over
    print("Game over!")
    print(f"Result: {board.result()}")  # Show result like 1-0, 0-1, or 1/2-1/2

# Only run the game if this script is executed directly
if __name__ == "__main__":
    main()
