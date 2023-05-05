#third party module
import numpy as np

#first part module
from piece import Piece
from board import Board
from board import position
from validation import table
from validation import tableswitch
from validation import outofboard
from validation import one_to_64


aaaa = Board(position)
aaaa.abbild()
aaaa.update(48,'A2',32,'A3')
aaaa.abbild()
print(aaaa.history)
aaaa.update(49,'B2',33,'B4')
aaaa.abbild()
aaaa.update(8,'A7',24,'A5')
print(aaaa.history)
aaaa.abbild()
#aaaa.reset()
print(aaaa.history)
aaaa.abbild()
aaaa.update(8,'A7',24,'A5')
print(aaaa.history)
aaaa.abbild()
aaaa.update(33,'B4',24,'A5',attac=True)
aaaa.abbild()
print(aaaa.allpices)

class Pawn(Piece):
    whitePawnLine = [48,49,50,51,52,53,54,55]# np.array([98,99,100,101,102,103,104,105],dtype=np.uint8)
    blackPawnLine = [8,9,10,11,12,13,14,15]#np.array([38,39,40,41,42,43,44,45],dtype=np.uint8)
    one_to_64 = one_to_64
    table = table
    tableswitch = tableswitch
    outofboard = outofboard

    def __init__(self, typ, pos, board):
        super().__init__(typ, pos, board)
        self.mov = []
        self.attac =[]
        self.schelt =[]
	
    def mov_attac_shelt(self):
        if self.typ == 'P' and self.pos in self.whitePawnLine:
            a = self.table[self.pos] -13
            b = self.table[self.pos] -11
            c = self.pos -8
            d = self.pos -16
            self.attacs.append(23)
        if self.type == 'p' and self.pos in self.blackPawnLine:
            return self.attac, self.mov,self.schelt
            
x = Pawn('P',52,aaaa)
x.mov_attac_shelt()
print(x.attac)

print(x.typ,x.p,x.pos,x.board[0])