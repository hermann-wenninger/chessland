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
    "r": "♖", "R": "♜",
    "s": "♘", "S": "♞",
    "b": "♗", "B": "♝",
    "q": "♕", "Q": "♛",
    "k": "♔", "K": "♚",
    "p": "♙", "P": "♟",
}


position = [['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']]


starboard_left =   [['a1'],         #CGA 1AVOIDING ROTATED BITBOARDS WITH DIRECT LOOKUPSam Tannous1Durham, North Carolina, USA
                 ['b1','a2'],       #https://arxiv.org/pdf/0704.3773.pdf
               ['c1','b2','a3'] ,
            ['d1','c2','b3','a4'] ,
          ['e1','d2','c3','b4','a5'] ,
       ['f1','e2','d3','c4','b5','a6'] ,
     ['g1','f2','e3','d4','c5','b6','a7'] ,
  ['h1','g2','f3','e4','d5','c6','b7','a8'] ,
     ['h2','g3','f4','e5','d6','c7','b8'] ,
       ['h3','g4','f5','e6','d7','c8'] ,
          ['h4','g5','f6','e7','d8'] ,
            ['h5','g6','f7','e8'] ,
               ['h6','g7','f8'] ,
                 ['h7','g8'] ,
                   ['h8']]



starboard_h =      [['h1'],
                 ['h2','g1'],
              ['h3','g2','f1'],
            ['h4','g3','f2','e1'],
          ['h5','g4','f3','e2','d1'],
        ['h6','g5','f4','e3','d2','c1'],
      ['h7','g6','f5','e4','d3','c2','b1'],
   ['h8','g7','f6','e5','d4','c3','b2','a1'],
      ['g8','f7','e6','d5','c4','b3','a2'],
        ['f8','e7','d6','c5','b4','a3'],
          ['e8','d7','c6','b5','a4'],
            ['d8','c7','b6','a5'],
               ['c8','b7','a6'],
                  ['b8','a7'],
                     ['a8']]


piboard = {'A8':'r','B8':'n','C8':'b','D8':'q','E8':'k','F8':'b','G8':'n','H8':'r',
           'A7':'p','B7':'p','C7':'p','D7':'p','E7':'p','F7':'p','G7':'p','H7':'p',
           'A6':'.','B6':'.','C6':'.','D6':'.','E6':'.','F6':'.','G6':'.','H6':'.',
           'A5':'.','B5':'.','C5':'.','D5':'.','E5':'.','F5':'.','G5':'.','H5':'.',
           'A4':'.','B4':'.','C4':'.','D4':'.','E4':'.','F4':'.','G4':'.','H4':'.',
           'A3':'.','B3':'.','C3':'.','D3':'.','E3':'.','F3':'.','G3':'.','H3':'.',
           'A2':'P','B2':'P','C2':'P','D2':'P','E2':'P','F2':'P','G2':'P','H2':'P',
           'A1':'R','B1':'N','C1':'B','D1':'Q','E1':'K','F1':'B','G1':'N','H1':'R',
}
one_to_64 = np.arange(1,65).reshape(8, 8)[::-1]
one_to_120 = np.arange(0,120).reshape(12,10)[::-1]
one_to_144 = np.arange(0,144).reshape(12,12)[::-1]
print(one_to_144)


ones = np.ones((8,8), dtype=np.uint8)
zeros  = np.zeros((8,8),dtype=np.uint8)
board  = np.zeros((8,8),dtype=np.uint8)
board[1::2,::2] = 1
board[::2,1::2] = 1
Filo = ["a", "b", "c", "d", "e", "f", "g", "h"]
Numbr = ["1", "2", "3", "4", "5", "6", "7", "8"]

filonum = [n+f for f in Numbr for n in Filo]
filonum = np.array(filonum, dtype = np.chararray).reshape(8,8)[::-1]