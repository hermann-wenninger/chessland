'''Representation for the Chesspices and Bitboard'''
# ENGLISH          DEUTSCH
# Bishop = B | b      = Läufer   = L | l
# King   = K | k      = King     = K | k
# Queen  = Q | q      = Dame     = D | d
# Pawn   = P | p      = Bauer    = B | b
# Rock   = R | r      = Turm     = T | t
# Horse  = S | s      = Springer = S | s


CHESS_SYMBOLS_ENG = {
    "R": "♖", "r": "♜",
    "S": "♘", "s": "♞",
    "B": "♗", "b": "♝",
    "Q": "♕", "q": "♛",
    "K": "♔", "k": "♚",
    "P": "♙", "p": "♟",
}


CHESS_SYMBOLS_DE = {
    "T": "♖", "t": "♜",
    "S": "♘", "s": "♞",
    "L": "♗", "l": "♝",
    "D": "♕", "d": "♛",
    "K": "♔", "k": "♚",
    "B": "♙", "b": "♟",
}

startposition = [['r','n','b','q','k','b','n','r']
                 ['p','p','p','p','p','p','p','p']
                 ['x','x','x','x','x','x','x','x']
                 ['x','x','x','x','x','x','x','x']
                 ['x','x','x','x','x','x','x','x']
                 ['x','x','x','x','x','x','x','x']
                 ['P','P','P','P','P','P','P','P']
                 ['R','N','B','Q','K','B','N','R']]