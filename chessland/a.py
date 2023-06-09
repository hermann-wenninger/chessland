import numpy as np

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

sandboard = [["♜","♞","♝","♛","♚","♝","♞","♜"],
            ["♟","♟","♟","♟","♟","♟","♟","♟"],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["♙","♙","♙","♙","♙","♙","♙","♙"],
            ["♖","♘","♗","♔","♛","♗","♘","♖"]]


start =[['br','bn','bb','bq','bk','bb','bn','br'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['  ','  ','  ','  ','  ','  ','  ','  '],
        ['  ','  ','  ','  ','  ','  ','  ','  '],
        ['  ','  ','  ','  ','  ','  ','  ','  '],
        ['  ','  ','  ','  ','  ','  ','  ','  '],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wr','wn','wb','wq','wk','wb','wn','wr']]
<<<<<<< HEAD

position = [['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']]

print(start[0][0])


d = [[ h1 ] ,
[ h2 , g1 ] ,
[ h3 , g2 , f1 ] ,
[ h4 , g3 , f2 , e1 ] ,
[ h5 , g4 , f3 , e2 , d1 ] ,
[ h6 , g5 , f4 , e3 , d2 , c1 ] ,
[ h7 , g6 , f5 , e4 , d3 , c2 , b1 ] ,
[ h8 , g7 , f6 , e5 , d4 , c3 , b2 , a1 ] ,
[ g8 , f7 , e6 , d5 , c4 , b3 , a2 ] ,
[ f8 , e7 , d6 , c5 , b4 , a3 ] ,
[ e8 , d7 , c6 , b5 , a4 ] ,
[ d8 , c7 , b6 , a5 ] ,
[ c8 , b7 , a6 ] ,
[ b8 , a7 ] ,
[ a8 ] ]



s =            [[ a1 ],
              [ b1, a2 ],
            [ c1, b2 , a3 ] ,
         [ d1, c2 , b3 , a4 ] ,
       [ e1, d2 , c3 , b4 , a5 ] ,
    [ f1, e2 , d3 , c4 , b5 , a6 ] ,
  [ g1, f2 , e3 , d4 , c5 , b6 , a7 ] ,
[ h1 , g2 , f3 , e4 , d5 , c6 , b7 , a8 ] ,
  [ h2 , g3 , f4 , e5 , d6 , c7 , b8 ] ,
    [ h3 , g4 , f5 , e6 , d7 , c8 ] ,
       [ h4 , g5 , f6 , e7 , d8 ] ,
          [ h5 , g6 , f7 , e8 ] ,
            [ h6 , g7 , f 8 ] ,
               [ h7 , g8 ] ,
                  [ h8 ] ]
=======
startstr = np.array(start, dtype=str)
sandboardstr = np.array(sandboard, dtype='U1')
print(startstr[[6][0],7])#numpy fancy copy with [[][],]
print(sandboardstr[6][0])
>>>>>>> 840e7b282e1a6301f605c50f519b9fc9e1d1e832
