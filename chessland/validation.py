import numpy as np

one_to_64 = np.arange(1,65).reshape(8, 8)[::-1]
one_to_120 = np.arange(0,120).reshape(10,12)
ones = np.ones((8,8), dtype=np.uint8)
zeros  = np.zeros((8,8),dtype=np.uint8)
board  = np.zeros((8,8),dtype=np.uint8)
board[1::2,::2] = 1
board[::2,1::2] = 1
Filo = ["a", "b", "c", "d", "e", "f", "g", "h"]
Numbr = ["1", "2", "3", "4", "5", "6", "7", "8"]

filonum = [f+n for f in Numbr for n in Filo]
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
SQUARES ={'A1':21,'B1':22,'C1':23,'D1':24,'E1':25,'F1':26,'G1':27,'H1':28,'A8':91,'B8':92,'C8':93,'D8':94,'E8':95,'F8':96,'G8':97,'H8':98,'NO_SQ':99,'OFFBOARD':100}
# const THETRUTH =  {TRUE:1, FALSE:0}
THETRUTH = {'TRUE':1, 'FALSE':0}
OUTOFBOARD =(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,36,37,
             48,49,60,61,72,73,84,85,96,97,98,99,100,101,102,103,104,105,106,107,108,109,
             110,11,112,113,114,115,116,117,118,119,34,35,46,47,58,59,70,71,82,83,94,95)
WKCA = 1 #0001
WQCA = 2 #0010
BKCA = 4 #0100
BQCA = 8 #1000

CASTELBIT = {WKCA:1,WQCA:2,BKCA:4,BQCA:8}
def structtest():
    print(one_to_64)
    print(ones)
    print(zeros)
    print(board)
    print(filonum)
    print(one_to_120)
    print(PIECES)
    print(FILES)
    print(RANKS)
    print(SQUARES)
    print(COLOURS)
    print(THETRUTH)

structtest()