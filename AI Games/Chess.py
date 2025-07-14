import chess
import math

def eval_board(b):
    return sum(len(b.pieces(p, chess.WHITE)) - len(b.pieces(p, chess.BLACK)) for p in [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN])

def ab(b, d, a, be, mx):
    if d==0 or b.is_game_over(): return eval_board(b)
    v = -math.inf if mx else math.inf
    for m in b.legal_moves:
        b.push(m)
        val = ab(b, d-1, a, be, not mx)
        b.pop()
        if mx:
            v = max(v, val); a = max(a, v)
            if be <= a: break
        else:
            v = min(v, val); be = min(be, v)
            if be <= a: break
    return v

def best(b, d):
    mv, sc = None, -math.inf
    for m in b.legal_moves:
        b.push(m)
        s = ab(b, d-1, -math.inf, math.inf, False)
        b.pop()
        if s > sc: sc, mv = s, m
    return mv

def main():
    b = chess.Board()
    print(b)
    while not b.is_game_over():
        if b.turn:
            try:
                m = chess.Move.from_uci(input("Your move: "))
                if m in b.legal_moves: b.push(m)
                else: print("Illegal"); continue
            except: print("Invalid"); continue
        else:
            print("AI thinking...")
            b.push(best(b,2))
        print(b)
    print("Result:", b.result())

if __name__=="__main__": main()