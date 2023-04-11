import numpy as np

one_to_64 = np.arange(1,65).reshape(8, 8)[::-1]
one_to_120 = np.arange(0,120).reshape(12,10)[::-1]
ones = np.ones((8,8), dtype=np.uint8)
zeros  = np.zeros((8,8),dtype=np.uint8)
board  = np.zeros((8,8),dtype=np.uint8)
board[1::2,::2] = 1
board[::2,1::2] = 1
Filo = ["a", "b", "c", "d", "e", "f", "g", "h"]
Numbr = ["1", "2", "3", "4", "5", "6", "7", "8"]

filonum = [n+f for f in Numbr for n in Filo]
filonum = np.array(filonum, dtype = np.chararray).reshape(8,8)[::-1]


#valid js and python
# const PIECES = {EMPTY:0,wP:1,wN:2,wB:3,wR:4,wQ:5,wK:6,bP:7,bN:8,bB:9,bR:10,bQ:11,bK:12}
PIECES = {'EMPTY':0,'wP':1,'wN':2,'wB':3,'wR':4,'wQ':5,'wK':6,'bP':7,'bN':8,'bB':9,'bR':10,'bQ':11,'bK':12}
# const LEN_LONG_BOARD = 120
LEN_LONG_BOARD = 120
# const FILES = {FILE_A:0,FILE_B:1,FILE_C:2,FILE_D:3,FILE_E:4,FILE_F:5,FILE_G:6,FILE_H:7,FILE_NONE:8}
FILES = {'FILE_A':0,'FILE_B':1,'FILE_C':2,'FILE_D':3,'FILE_E':4,'FILE_F':5,'FILE_G':6,'FILE_H':7,'FILE_NONE':8}
# const RANKS = {RANK_1=0,RANK_2=1,RANK_3=2,RANK_4=3,RANK_5=4,RANK_6=5,RANK_7=6,RANK_8=7,RANK_NONE=8}
RANKS = {'RANK_1':0,'RANK_2':1,'RANK_3':2,'RANK_4':3,'RANK_5':4,'RANK_6':5,'RANK_7':6,'RANK_8':7,'RANK_NONE':8}
# const COLOURS = {WHITE:0, BLACK:1,BOTH:2}
COLOURS = {'WHITE':0, 'BLACK':1,'BOTH':2}
# const SQUARES ={A1:21,B1:22,C1:23,D1:24,E1:25,F1:26,G1:27,H1:28,A8:91,B8:92,C8:93,D8:94,E8:95,F8:96,G8:97,H8:98,NO_SQ:99,OFFBOARD:100}
SQUARES ={'A1':21,'B1':22,'C1':23,'D1':24,'E1':25,'F1':26,'G1':27,'H1':28,
          'A2':31,'B2':32,'C2':33,'D2':34,'E2':35,'F2':36,'G2':37,'H2':38,
          'A3':41,'B3':42,'C3':43,'D3':44,'E3':45,'F3':46,'G3':47,'H3':48,
          'A4':51,'B4':52,'C4':53,'D4':54,'E4':55,'F4':56,'G4':57,'H4':58,
          'A5':61,'B5':62,'C5':63,'D5':64,'E5':65,'F5':66,'G5':67,'H5':68,
          'A6':71,'B6':72,'C6':73,'D6':74,'E6':75,'F6':76,'G6':77,'H6':78,
          'A7':81,'B7':82,'C7':83,'D7':84,'E7':85,'F7':86,'G7':87,'H7':88,
          'A8':91,'B8':92,'C8':93,'D8':94,'E8':95,'F8':96,'G8':97,'H8':98,'NO_SQ':99,'OFFBOARD':100}

SQUARESSWITCH = {y: x for x, y in SQUARES.items()}

# const THETRUTH =  {TRUE:1, FALSE:0}
THETRUTH = {'TRUE':1, 'FALSE':0}

OUTOFBOARD =(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,116,
             30,40,50,60,70,80,90,29,39,49,59,69,79,89,99,100,101,117,
             102,103,104,105,106,107,108,109,110,111,112,113,114,115,118,119)


WHITEPIECES = ['wr','wn','wb','wq','wk','bp']
BLACKPIECES = ['br','bn','bb','bq','bk','bp']
ALLPIECES = WHITEPIECES + BLACKPIECES

WKCA = 1 #0001
WQCA = 2 #0010
BKCA = 4 #0100
BQCA = 8 #1000

CASTELBIT = {WKCA:1,WQCA:2,BKCA:4,BQCA:8} # idee from bluefeversoft
def structtest():
    print('one_to_64',one_to_64)
    print('ones',ones)
    print('zeros',zeros)
    print('board',board)
    print('filonum',filonum)
    print('one-to_120',one_to_120)
    print('PIECES',PIECES)
    print('FILES',FILES)
    print('RANKS',RANKS)
    print('SQUARES',SQUARES)
    print('COLOURS',COLOURS)
    print('THETRUTH',THETRUTH)
    print('ALLPIECES', ALLPIECES)
    print('SQUARESWITCH',SQUARESSWITCH)

structtest()