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
from validation import one_to_144
import pprint



class Neight(Piece):
    #whitePawnLine = [48,49,50,51,52,53,54,55]# np.array([98,99,100,101,102,103,104,105],dtype=np.uint8)
    #blackPawnLine = [8,9,10,11,12,13,14,15]#np.array([38,39,40,41,42,43,44,45],dtype=np.uint8)
    one_to_64 = one_to_64
    table = table
    tableswitch = tableswitch
    outofboard = outofboard
    one_to_144 = one_to_144

    def __init__(self, typ, pos, board):
        super().__init__(typ, pos, board)
        self.mov = []
        self.attac =[]
        self.schelt =[]

    def mov_attac_shelt(self):
        hl = []
        x = [25,23,14,-10,-23,-25,10,-14]
        for i in x:
            y = self.table[self.pos] +i
            print(self.table[self.pos])
            if y not in outofboard:
                hl.append(y)
                print(self.board[tableswitch[y]])
        for i in hl:
            x = ord(self.board[tableswitch[i]])
            a = self.board[tableswitch[i]]
            print('ord .', ord('.'))
            if x >82:
                self.attac.append(['N',i,a])
            if x == 46:
                self.mov.append(['N',i,a])
            if x < 82 and x > 46:
                self.schelt.append(['N',i,a])

                pass

            
        print('inner',hl)
        
aaaa = Board(position)
x = Neight('N',57,aaaa)
x.mov_attac_shelt()
print('aatack',x.attac)
print('mov', x.mov)
print('schelt',x.schelt)

#print(x.typ,x.p,x.pos,x.board[0])
#x.update(0)
print('typ',x.typ)
print('pos',x.pos)
print('board',x.board[57])