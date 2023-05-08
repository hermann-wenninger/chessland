#third party module
import numpy as np

#first part module
from piece import Piece
from Qween import Qween
from board import Board
from board import position
from validation import table
from validation import tableswitch
from validation import outofboard
from validation import one_to_64
from validation import one_to_144
import pprint


aaaa = Board(position)
# aaaa.abbild()
# aaaa.update(48,'A2',32,'A3')
# aaaa.abbild()
# print(aaaa.history)
# aaaa.update(49,'B2',33,'B4')
# aaaa.abbild()
# aaaa.update(8,'A7',24,'A5')
# print(aaaa.history)
# aaaa.abbild()
# #aaaa.reset()
# print(aaaa.history)
# aaaa.abbild()
# aaaa.update(8,'A7',24,'A5')
# print(aaaa.history)
# aaaa.abbild()
# aaaa.update(33,'B4',24,'A5',attac=True)
# aaaa.abbild()
# print(aaaa.allpices)

class Pawn(Piece):
    whitePawnLine = [48,49,50,51,52,53,54,55]# np.array([98,99,100,101,102,103,104,105],dtype=np.uint8)
    blackPawnLine = [8,9,10,11,12,13,14,15]#np.array([38,39,40,41,42,43,44,45],dtype=np.uint8)
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
        if self.typ == 'P' and self.pos in self.whitePawnLine:
            c = self.table[self.pos] -12 #go easy
            d = self.table[self.pos] -24 #go fast
            kl_onboard = self.tableswitch[c]
            gr_onboard = self.tableswitch[d]
            kleiner = self.board[self.tableswitch[c]]
            grosser = self.board[self.tableswitch[d]]
            if kleiner == '.':
                  self.mov.append(['P',kl_onboard])
            if kleiner == '.' and grosser == '.':
                  self.mov.append(['P', gr_onboard])#gut bis hie hin
            a = self.table[self.pos] -13 #attack east
            b = self.table[self.pos] -11 #attac west
            e = self.tableswitch[a] #attack east on easy bord
            f = self.tableswitch[b] #attack west on easy board
           
            i = self.board[e]
            j = self.board[f]
            if b not in outofboard and j != '.' and ord(j) >82:
                 self.attac.append(['P',f,j])
            if b not in outofboard and j != '.' and ord(j) <82:
                 self.schelt.append(['P',f,j])
            if a not in outofboard and i != '.' and ord(j) <82:
                 self.attac.append(['P',e,i])
            if a not in outofboard and i != '.' and ord(j) >82:
                 self.schelt.append(['P',e,i])

        if self.typ == 'p' and self.pos in self.whitePawnLine:
            c = self.table[self.pos] +12 #go easy
            d = self.table[self.pos] +24 #go fast
            kl_onboard = self.tableswitch[c]
            gr_onboard = self.tableswitch[d]
            kleiner = self.board[self.tableswitch[c]]
            grosser = self.board[self.tableswitch[d]]
            if kleiner == '.':
                  self.mov.append(['P',kl_onboard])
            if kleiner == '.' and grosser == '.':
                  self.mov.append(['P', gr_onboard])#gut bis hie hin
            a = self.table[self.pos] +13 #attack east
            b = self.table[self.pos] +11 #attac west
            e = self.tableswitch[a] #attack east on easy bord
            f = self.tableswitch[b] #attack west on easy board
           
            i = self.board[e]
            j = self.board[f]
            if b not in outofboard and j != '.' and ord(j) >82:
                 self.attac.append(['P',f,j])
            if b not in outofboard and j != '.' and ord(j) <82:
                 self.schelt.append(['P',f,j])
            if a not in outofboard and i != '.' and ord(j) <82:
                 self.attac.append(['P',e,i])
            if a not in outofboard and i != '.' and ord(j) >82:
                 self.schelt.append(['P',e,i])

    def __del__(self):
        print(self.typ,self.pos,"is now destroyed and live in")

    def update(self, num):
        wProLine = [0,1,2,3,4,5,6,7]
        bProLine = [56,57,58,59,60,61,62,63]
        if self.typ == 'P' and num in wProLine:
             self = Qween('Q',num, self.board)

             print('a new instance of a special whitepice')
        if self.typ == 'p' and num in bProLine:
             self.typ = 'q'
             self.pos = num
             self.board[num]= 'q'
             print('a new instance of a special whitepice')
        return 
            
x = Pawn('P',49,aaaa)
x.mov_attac_shelt()
print('aatack',x.attac)
print('mov', x.mov)
print('schelt',x.schelt)

print(x.typ,x.p,x.pos,x.board[0])
x.update(0)
print('typ',x.typ)
print('pos',x.pos)
print('board',x.board[0])

