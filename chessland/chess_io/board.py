from pprint import pprint
import numpy as np
from sys import getsizeof


position = [['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']]

reset  = {'A8':0,'B8':1,'C8':2,'D8':3,'E8':4,'F8':5,'G8':6,'H8':7,
          'A7':8,'B7':9,'C7':10,'D7':11,'E7':12,'F7':13,'G7':14,'H7':15,
          'A6':16,'B6':17,'C6':18,'D6':19,'E6':20,'F6':21,'G6':22,'H6':23,
          'A5':24,'B5':25,'C5':26,'D5':27,'E5':28,'F5':29,'G5':30,'H5':31,
          'A4':32,'B4':33,'C4':34,'D4':35,'E4':36,'F4':37,'G4':38,'H4':39,
          'A3':40,'B3':41,'C3':42,'D3':43,'E3':44,'F3':45,'G3':46,'H3':47,
          'A2':48,'B2':49,'C2':50,'D2':51,'E2':52,'F2':53,'G2':54,'H2':55,
          'A1':56,'B1':57,'C1':58,'D1':59,'E1':60,'F1':61,'G1':62,'H1':63,}

switchReset = {y: x for x, y in reset.items()}

class Board():

    __slots__ = 'startpos', 'history'

    def __init__(self,startpos):
        self.startpos = startpos
        self.history = []
        #self.line = self.inline()

    def __getitem__(self, i):
        return self.startpos[i]
    
    def abbild(self):
        pprint(self.startpos)

    def update(self, oldPos, oldPosSquare, newPos, newPosSquare, attac=False):
        self.startpos = np.array(self.startpos, dtype = np.chararray).reshape(64)
       
        self.startpos[newPos] = self.startpos[oldPos]
        self.startpos[oldPos] = '.'
        
        if attac == False:
            self.history.append((self.startpos[newPos],oldPos,oldPosSquare,newPos,newPosSquare))
        else:
            self.history.append((self.startpos[oldPos],oldPosSquare,oldPos,'X',self.startpos[newPos],newPos,newPosSquare))
        self.startpos = self.startpos.reshape(8,8)
    
    def reset(self):
        self.startpos = self.startpos.reshape(64)
        lastE = self.history[-1]
        if lastE[2] is not 'X':
            del self.history[-1] 
            self.startpos[lastE[1]] = lastE[0] 
            self.startpos[lastE[3]] = '.'
            self.startpos = self.startpos.reshape(8,8)

    def inline(self):
        return self.startpos.reshape(64)

    




def test():
    a = Board(position)
    a.abbild()
    a.update(48,'A2',32,'A3')
    a.abbild()
    print(a.history)
    a.update(49,'B2',33,'B4')
    a.abbild()
    a.update(8,'A7',24,'A5')
    print(a.history)
    a.abbild()
    a.reset()
    print(a.history)
    a.abbild()
    a.update(8,'A7',24,'A5')
    print(a.history)
    a.abbild()
    a.update(33,'B4',24,'A5',attac=True)
    a.abbild()
    print(a.history)
    x = a.startpos
    print(x[5][3])
    x = a.inline()
    print(x[0:9])
    print(a[0][2])
    print(getsizeof(Board(position)))
    print(a.__slots__)
    print(getsizeof(a))
test()