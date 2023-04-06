'''Representation for the Chesspices and Bitboard'''
# ENGLISH               DEUTSCH
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

start =[['br','bn','bb','bq','bk','bb','bn','br']
        ['bp','bp','bp','bp','bp','bp','bp','bp']
        ['','','','','','','','']
        ['','','','','','','','']
        ['','','','','','','','']
        ['','','','','','','','']
        ['wp','wp','wp','wp','wp','wp','wp','wp']
        ['wr','wn','wb','wq','wk','wb','wn','wr']]

print(start)