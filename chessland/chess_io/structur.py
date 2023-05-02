import numpy as np
from pprint import pprint

#https://arxiv.org/pdf/0704.3773.pdf
 #CGA 1AVOIDING ROTATED BITBOARDS WITH DIRECT LOOKUPSam Tannous1Durham, North Carolina, USA





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

startpos = np.array(position, dtype = np.chararray).reshape(64)
print(startpos)


star_left =        [['a1'],        
                 ['b1','a2'],       #https://arxiv.org/pdf/0704.3773.pdf
               ['c1','b2','a3'],
            ['d1','c2','b3','a4'],
          ['e1','d2','c3','b4','a5'],
       ['f1','e2','d3','c4','b5','a6'],
     ['g1','f2','e3','d4','c5','b6','a7'],
  ['h1','g2','f3','e4','d5','c6','b7','a8'],
     ['h2','g3','f4','e5','d6','c7','b8'],
       ['h3','g4','f5','e6','d7','c8'],
          ['h4','g5','f6','e7','d8'],
            ['h5','g6','f7','e8'],
               ['h6','g7','f8'],
                 ['h7','g8'],          
                   ['h8']]


num_star_left  =    [[56],        
                   [57, 48],       
                 [58, 49, 40],
               [59, 50, 41, 32],
             [60, 51, 42, 33, 24],
           [61, 52, 43, 34, 25, 16],
         [62, 53, 44, 35, 26, 17, 8],
       [63, 54, 45, 36, 27, 18, 9,  0],
         [55, 46, 37, 28, 19, 10, 1],        
           [47, 38, 29, 20, 11, 2],
             [39, 30, 21, 12, 3],
               [31, 22, 13, 4],
                 [23, 14, 5],
                   [15, 6],          
                     [7]]
num_start_left = np.array(num_star_left, dtype = np.uint8)


star_right =        [['h1'],
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
star_right = np.array(num_star_left, dtype = np.chararray)

num_star_right =    [[63],
                  [55, 62],
                [47,  54, 61],
              [39, 46,  53, 60],
            [31, 38, 45,  52, 59],
          [23, 30, 37, 44,  51, 58],
         [15, 22, 29, 36, 43, 50, 57],
      [7, 14,  21, 28, 35,  42, 49, 56],
         [6, 13, 20, 27, 34,  41, 48],
           [5, 12, 19, 26, 33,  40],
             [4, 11, 18, 25, 32],
               [3, 10, 17, 24],
                  [2, 9, 16],
                    [1, 8],
                     [0]]

num_start_right = np.array(num_star_right, dtype = np.uint8)





piboard = {'A8':'r','B8':'n','C8':'b','D8':'q','E8':'k','F8':'b','G8':'n','H8':'r',
           'A7':'p','B7':'p','C7':'p','D7':'p','E7':'p','F7':'p','G7':'p','H7':'p',
           'A6':'.','B6':'.','C6':'.','D6':'.','E6':'.','F6':'.','G6':'.','H6':'.',
           'A5':'.','B5':'.','C5':'.','D5':'.','E5':'.','F5':'.','G5':'.','H5':'.',
           'A4':'.','B4':'.','C4':'.','D4':'.','E4':'.','F4':'.','G4':'.','H4':'.',
           'A3':'.','B3':'.','C3':'.','D3':'.','E3':'.','F3':'.','G3':'.','H3':'.',
           'A2':'P','B2':'P','C2':'P','D2':'P','E2':'P','F2':'P','G2':'P','H2':'P',
           'A1':'R','B1':'N','C1':'B','D1':'Q','E1':'K','F1':'B','G1':'N','H1':'R',
}
one_to_64 = np.arange(0,64).reshape(8, 8)
one_to_120 = np.arange(0,120,dtype=np.uint8).reshape(12,10)
fullboard = np.arange(0,144,dtype=np.uint8).reshape(12,12)
pprint(fullboard)


oneBoard = np.ones((8,8), dtype=np.uint8)
zeroBoard  = np.zeros((8,8),dtype=np.uint8)

bwBoard  = np.zeros((8,8),dtype=np.uint8)
bwBoard[1::2,::2] = 1
bwBoard[::2,1::2] = 1


Filo = ["a", "b", "c", "d", "e", "f", "g", "h"]
Numbr = ["1", "2", "3", "4", "5", "6", "7", "8"]
filonum = [n+f for f in Numbr for n in Filo]
filonum = np.array(filonum, dtype = np.chararray).reshape(8,8)[::-1]




reset  = {'A8': 0,'B8': 1,'C8': 2,'D8': 3,'E8': 4,'F8': 5,'G8': 6,'H8': 7,
          'A7': 8,'B7': 9,'C7':10,'D7':11,'E7':12,'F7':13,'G7':14,'H7':15,
          'A6':16,'B6':17,'C6':18,'D6':19,'E6':20,'F6':21,'G6':22,'H6':23,
          'A5':24,'B5':25,'C5':26,'D5':27,'E5':28,'F5':29,'G5':30,'H5':31,
          'A4':32,'B4':33,'C4':34,'D4':35,'E4':36,'F4':37,'G4':38,'H4':39,
          'A3':40,'B3':41,'C3':42,'D3':43,'E3':44,'F3':45,'G3':46,'H3':47,
          'A2':48,'B2':49,'C2':50,'D2':51,'E2':52,'F2':53,'G2':54,'H2':55,
          'A1':56,'B1':57,'C1':58,'D1':59,'E1':60,'F1':61,'G1':62,'H1':63,}

switchReset = {y: x for x, y in reset.items()}

outOfBoard = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
             22,23,120,121,122,123,124,125,126,127,128,129,130,131,
             132,133,134,135,136,137,138,139,140,141,142,143,108,109,
             96,97,84,85,72,73,60,61,48,49,36,37,24,25,34,35,46,47,58,
             59,70,71,82,83,94,95,106,107,118,119]






whitePice = ['R','N','B','Q','K','P']
blackPice = ['r','n','b','q','k','p']

print(len(outOfBoard))
pprint(num_star_left)




squares ={'A8':26,'B8':27,'C8':28,'D8':29,'E8':30,'F8':31,'G8':32,'H8':33,
          'A7':38,'B7':39,'C7':40,'D7':41,'E7':42,'F7':43,'G7':44,'H7':45,
          'A6':50,'B6':51,'C6':52,'D6':53,'E6':54,'F6':55,'G6':56,'H6':57,
          'A5':62,'B5':63,'C5':64,'D5':65,'E5':66,'F5':67,'G5':68,'H5':69,
          'A4':74,'B4':75,'C4':76,'D4':77,'E4':78,'F4':79,'G4':80,'H4':81,
          'A3':86,'B3':87,'C3':88,'D3':89,'E3':90,'F3':91,'G3':92,'H3':93,
          'A2':98,'B2':99,'C2':100,'D2':101,'E2':102,'F2':103,'G2':104,'H2':105,
          'A1':110,'B1':111,'C1':112,'D1':113,'E1':114,'F1':115,'G1':116,'H1':117,}

numsquares ={0:26,1:27,2:28,3:29,4:30,5:31,6:32,7:33,
             8:38,9:39,10:40,11:41,12:42,13:43,14:44,15:45,
             16:50,17:51,18:52,19:53,20:54,21:55,22:56,23:57,
             24:62,25:63,26:64,27:65,28:66,29:67,30:68,31:69,
             32:74,33:75,34:76,35:77,36:78,37:79,38:80,39:81,
             40:86,41:87,42:88,43:89,44:90,45:91,46:92,47:93,
             48:98,49:99,50:100,51:101,52:102,53:103,54:104,55:105,
             56:110,56:111,58:112,59:113,60:114,61:115,62:116,63:117,}


wPLine = [48,49,50,51,52,53,54,55]
bPLine = [8,9,10,11,12,13,14,15]

blackPawnLine = [38,39,40,41,42,43,44,45]
whitePawnLine = [98,99,100,101,102,103,104,105]


numrankvalues=[[56 , 57 , 58 , 59 , 60 , 61 , 62 , 63],
              [ 48 , 49 , 50 , 51 , 52 , 53 , 54 , 55],
              [ 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47],
              [ 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39],
              [ 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31],
              [ 16 , 17 , 18 ,  9 , 20 , 21 , 22 , 23],
              [ 8 ,   9 , 10 , 11 , 12 , 13 , 14 , 15],
              [ 0 ,   1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7]]



rankvalues=[[ 'a1' , 'b1' , 'c1' , 'd1' , 'e1' , 'f1' , 'g1' , 'h1'],
            [ 'a2' , 'b2' , 'c2' , 'd2' , 'e2' , 'f2' , 'g2' , 'h2'],
            [ 'a3' , 'b3' , 'c3' , 'd3' , 'e3' , 'f3' , 'g3' , 'h3'],
            [ 'a4' , 'b4' , 'c4' , 'd4' , 'e4' , 'f4' , 'g4' , 'h4'],
            [ 'a5' , 'b5' , 'c5' , 'd5' , 'e5' , 'f5' , 'g5' , 'h5'],
            [ 'a6' , 'b6' , 'c6' , 'd6' , 'e6' , 'f6' , 'g6' , 'h6'],
            [ 'a7' , 'b7' , 'c7' , 'd7' , 'e7' , 'f7' , 'g7' , 'h7'],
            [ 'a8' , 'b8' , 'c8' , 'd8' , 'e8' , 'f8' , 'g8' , 'h8']]

filevalues=[[ 'a1' , 'a2' , 'a3' , 'a4' , 'a5' , 'a6' , 'a7' , 'a8'],
            [ 'b1' , 'b2' , 'b3' , 'b4' , 'b5' , 'b6' , 'b7' , 'b8'],
            [ 'c1' , 'c2' , 'c3' , 'c4' , 'c5' , 'c6' , 'c7' , 'c8'],
            [ 'd1' , 'd2' , 'd3' , 'd4' , 'd5' , 'd6' , 'd7' , 'd8'],
            [ 'e1' , 'e2' , 'e3' , 'e4' , 'e5' , 'e6' , 'e7' , 'e8'],
            [ 'f1' , 'f2' , 'f3' , 'f4' , 'f5' , 'f6' , 'f7' , 'f8'],
            [ 'g1' , 'g2' , 'g3' , 'g4' , 'g5' , 'g6' , 'g7' , 'g8'],
            [ 'h1' , 'h2' , 'h3' , 'h4' , 'h5' , 'h6' , 'h7' , 'h8']]
numfilevalues = [[ 56 , 48 , 40 , 32 , 24 , 16 , 8  , 0],
                 [ 57 , 49 , 41 , 33 , 25 , 17 , 9  , 1],
                 [ 58 , 50 , 42 , 34 , 26 , 18 , 10 , 2],
                 [ 59 , 51 , 43 , 35 , 27 , 19 , 11 , 3],
                 [ 60 , 52 , 44 , 36 , 28 , 20 , 12 , 4],
                 [ 61 , 53 , 45 , 37 , 29 , 21 , 13 , 5],
                 [ 62 , 54 , 46 , 38 , 30 , 22 , 14 , 6],
                 [ 63 , 55 , 47 , 39 , 31 , 23 , 15 , 7]]