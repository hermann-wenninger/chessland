from structur import piboard, squares 
from board import Board


position = [['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']]

x = Board(position)


class Positions():

    def __init__(self, a):
        self.object = a

    def iterate(self):
        for i , x in enumerate(self.object):
            for j, pice in enumerate(x):
                print(i,j,pice)
            #if pice in COLOR_OF_PICES:
                #squarenum = TABLE[str(i)+str(j)][0][0]


xy = Positions(x)

xy.iterate()