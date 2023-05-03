from structur import piboard, squares 
from board import Board
import numpy as np
from sys import getsizeof
import random



position = [['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']]

#x = Board(position)
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


class MovsAttks():

    def __init__(self, a):
        self.freschblack = a.allpices[0]
        self.freschwhite = a.allpices[1]
        self.blackPawnLine = np.array([38,39,40,41,42,43,44,45],dtype=np.uint8)
        self.whitePawnLine = np.array([98,99,100,101,102,103,104,105],dtype=np.uint8)
        self.fullboard = np.arange(0,144,dtype=np.uint8).reshape(12,12)
        self.white = np.array(('R','N','B','Q','K','P'),dtype=np.chararray)
        self.black = ('r','n','b','q','k','p')
        self.outofboard  =  np.array((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,116,30,40,50,60,70,80,90,29,39,49,59,69,79,89,99,100,101,117,102,103,104,105,106,107,108,109,110,111,112,113,114,115,118,119), dtype= np.uint8)
        self.whitePawnProp = False
        self.blackPawnProp = False
        self.whiteKingDown = False
        self.blackKingDown = False
        self.weights = []

    
    def iterate(self):
        for i , x in enumerate(self.freschblack):
            for j, pice in enumerate(x):
                print(i,j,pice)
            #if pice in COLOR_OF_PICES:
                #squarenum = TABLE[str(i)+str(j)][0][0]

    def weights(self):
        for i in range(64):
            self.weights.append(random())
            print(self.weights)
        return self.weights 
xy = MovsAttks(aaaa)

xy.iterate()
print('einfach unsinn')
print('dfghjklö',getsizeof(aaaa))

print(xy.weights())