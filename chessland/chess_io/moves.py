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

class Helper():
    '''helper class to translate the boardposition between the several boards'''
    uni_sym = {'K':'♔','Q':'♕','R':'♖','B':'♗','N':'♘','P':'♙',
               'k':'♚','q':'♛','r':'♜','b':'♝','n':'♞','p':'♟︎'
                     }
    sqa = {'A8':26,'B8':27,'C8':28,'D8':29,'E8':30,'F8':31,'G8':32,'H8':33,
           'A7':38,'B7':39,'C7':40,'D7':41,'E7':42,'F7':43,'G7':44,'H7':45,
           'A6':50,'B6':51,'C6':52,'D6':53,'E6':54,'F6':55,'G6':56,'H6':57,
           'A5':62,'B5':63,'C5':64,'D5':65,'E5':66,'F5':67,'G5':68,'H5':69,
           'A4':74,'B4':75,'C4':76,'D4':77,'E4':78,'F4':79,'G4':80,'H4':81,
           'A3':86,'B3':87,'C3':88,'D3':89,'E3':90,'F3':91,'G3':92,'H3':93,
           'A2':98,'B2':99,'C2':100,'D2':101,'E2':102,'F2':103,'G2':104,'H2':105,
           'A1':110,'B1':111,'C1':112,'D1':113,'E1':114,'F1':115,'G1':116,'H1':117
          }


    numsqa ={0:26,1:27,2:28,3:29,4:30,5:31,6:32,7:33,
             8:38,9:39,10:40,11:41,12:42,13:43,14:44,15:45,
             16:50,17:51,18:52,19:53,20:54,21:55,22:56,23:57,
             24:62,25:63,26:64,27:65,28:66,29:67,30:68,31:69,
             32:74,33:75,34:76,35:77,36:78,37:79,38:80,39:81,
             40:86,41:87,42:88,43:89,44:90,45:91,46:92,47:93,
             48:98,49:99,50:100,51:101,52:102,53:103,54:104,55:105,
             56:110,56:111,58:112,59:113,60:114,61:115,62:116,63:117
             }
    def changer(self,arg):
        if arg == isinstance(   )

class MovsAttks():
    
    __slots__ = 'weight','freschblack'
    def __init__(self, a):
        self.freschblack = a.allpices[0]
        #self.freschwhite = a.allpices[1]
        #self.blackPawnLine = np.array([38,39,40,41,42,43,44,45],dtype=np.uint8)
       
        #self.fullboard = np.arange(0,144,dtype=np.uint8).reshape(12,12)
        #self.white = np.array(('R','N','B','Q','K','P'),dtype=np.chararray)
        #self.black = ('r','n','b','q','k','p')
        #self.outofboard  =  np.array((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,116,30,40,50,60,70,80,90,29,39,49,59,69,79,89,99,100,101,117,102,103,104,105,106,107,108,109,110,111,112,113,114,115,118,119), dtype= np.uint8)
        #self.whitePawnProp = False
        #self.blackPawnProp = False
        #self.whiteKingDown = False
        #self.blackKingDown = False
        self.weight = self.weights()

    
    def iterate(self):
        for i , x in enumerate(self.freschblack):
            for j, pice in enumerate(x):
                print(i,j,pice)
            #if pice in COLOR_OF_PICES:
    def pawn(self):
   
    def weights(self):
        self.weight = []
        for i in range(64):
            self.weight.append([i,random.random()])
            print(self.weight)
        return self.weight 
xy = MovsAttks(aaaa)

xy.iterate()
print('einfach unsinn')
print('dfghjklö',getsizeof(aaaa))

print(xy.weight)