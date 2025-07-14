import math

def minimax(sticks, is_maximizing):
    if sticks == 0:
        return -1 if is_maximizing else 1  # Last stick loser

    if is_maximizing:
        best_score = -math.inf
        for move in range(1, 4):
            if sticks - move >= 0:
                score = minimax(sticks - move, False)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in range(1, 4):
            if sticks - move >= 0:
                score = minimax(sticks - move, True)
                best_score = min(score, best_score)
        return best_score

def best_move(sticks):
    best_score = -math.inf
    move_choice = 1
    for move in range(1, 4):
        if sticks - move >= 0:
            score = minimax(sticks - move, False)
            if score > best_score:
                best_score = score
                move_choice = move
    return move_choice

def play():
    sticks = 15
    print("Nim Game: Don't take the last stick!")
    print("You and AI will take turns removing 1-3 sticks.")
    
    is_player_turn = True
    while sticks > 0:
        print(f"\nSticks remaining: {sticks}")
        if is_player_turn:
            try:
                move = int(input("Your move (1-3): "))
                if move < 1 or move > 3 or move > sticks:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            move = best_move(sticks)
            print(f"AI takes {move} stick(s).")
        
        sticks -= move
        if sticks == 0:
            if is_player_turn:
                print("You took the last stick. You lose!")
            else:
                print("AI took the last stick. AI loses! You win!")
            break
        
        is_player_turn = not is_player_turn

if __name__ == "__main__":
    play()
