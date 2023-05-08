import numpy as np
#blackpices_ = [(i,j) for i,j  in enumerate(all_) if j != '.'and ord(j) >82]
#whitepices_ = [(i,j) for i,j  in enumerate(all_) if j != '.'and ord(j) <=82]

start = [['br','bn','bb','bq','bk','bb','bn','br'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wr','wn','wb','wq','wk','wb','wn','wr']]
one_to_64 = np.arange(0,64).reshape(8, 8)
one_to_120 = np.arange(0,120).reshape(12,10)
one_to_144 = np.arange(0,144).reshape(12,12)
print(one_to_144)
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
# SQUARES ={'A8':91,'B8':92,'C8':93,'D8':94,'E8':95,'F8':96,'G8':97,'H8':98,
#           'A7':81,'B7':82,'C7':83,'D7':84,'E7':85,'F7':86,'G7':87,'H7':88,
#           'A6':71,'B6':72,'C6':73,'D6':74,'E6':75,'F6':76,'G6':77,'H6':78,
#           'A5':61,'B5':62,'C5':63,'D5':64,'E5':65,'F5':66,'G5':67,'H5':68,
#           'A4':51,'B4':52,'C4':53,'D4':54,'E4':55,'F4':56,'G4':57,'H4':58,
#           'A3':41,'B3':42,'C3':43,'D3':44,'E3':45,'F3':46,'G3':47,'H3':48,
#           'A2':31,'B2':32,'C2':33,'D2':34,'E2':35,'F2':36,'G2':37,'H2':38,
#           'A1':21,'B1':22,'C1':23,'D1':24,'E1':25,'F1':26,'G1':27,'H1':28,}

piceboard= {'A8':'br','B8':'bn','C8':'bb','D8':'bq','E8':'bk','F8':'bb','G8':'bn','H8':'br',
            'A7':'bp','B7':'bp','C7':'bp','D7':'bp','E7':'bp','F7':'bp','G7':'bp','H7':'bp',
            'A6':'','B6':'','C6':'','D6':'','E6':'','F6':'','G6':'','H6':'',
            'A5':'','B5':'','C5':'','D5':'','E5':'','F5':'','G5':'','H5':'',
            'A4':'','B4':'','C4':'','D4':'','E4':'','F4':'','G4':'','H4':'',
            'A3':'','B3':'','C3':'','D3':'','E3':'','F3':'','G3':'','H3':'',
            'A2':'wp','B2':'wp','C2':'wp','D2':'wp','E2':'wp','F2':'wp','G2':'wp','H2':'wp',
            'A1':'wr','B1':'wn','C1':'wb','D1':'wq','E1':'wk','F1':'wb','G1':'wn','H1':'wr',}


# TABLE =  {'70':21,'71':22,'72':23,'73':24,'74':25,'75':26,'76':27,'77':28,
#           '60':31,'61':32,'62':33,'63':34,'64':35,'65':36,'66':37,'67':38,
#           '50':41,'51':42,'52':43,'53':44,'54':45,'55':46,'56':47,'57':48,
#           '40':51,'41':52,'42':53,'43':34,'44':55,'45':56,'46':57,'47':58,
#           '30':61,'31':62,'32':63,'33':64,'34':65,'35':66,'36':67,'37':68,
#           '20':71,'21':72,'22':73,'23':74,'24':75,'25':76,'26':77,'27':78,
#           '10':81,'11':82,'12':83,'13':84,'14':85,'15':86,'16':87,'17':88,
#           '00':91,'01':92,'02':93,'03':94,'04':95,'05':96,'06':97,'07':98,}

table =  {0:26,1:27,2:28,3:29,4:30,5:31,6:32,7:33,
          8:38,9:39,10:40,11:41,12:42,13:43,14:44,15:45,
          16:50,17:51,18:52,19:53,20:54,21:55,22:56,23:57,
          24:62,25:63,26:64,27:65,28:66,29:67,30:68,31:69,
          32:74,33:75,34:76,35:77,36:78,37:79,38:80,39:81,
          40:86,41:87,42:88,43:89,44:90,45:91,46:92,47:93,
          48:98,49:99,50:100,51:101,52:102,53:103,54:104,55:105,
          56:110,57:111,58:112,59:113,60:114,61:115,62:116,63:117,}

tableswitch = {y: x for x, y in table.items()}

# const THETRUTH =  {TRUE:1, FALSE:0}
THETRUTH = {'TRUE':1, 'FALSE':0}

outofboard =(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
             24,25,36,37,48,49,60,61,72,73,84,85,96,97,108,109,120,121,
             122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,
             139,140,141,142,143,34,35,46,47,58,59,70,71,82,83,94,95,106,107,118,119)
print('länge',len(outofboard))
print('länge set', len(set(outofboard)))


whites = ['R','N','B','Q','K','P']
blacks = ['r','n','b','q','k','p']
all = whites + blacks

WKCA = 1 #0001
WQCA = 2 #0010
BKCA = 4 #0100
BQCA = 8 #1000

CASTELBIT = {WKCA:1,WQCA:2,BKCA:4,BQCA:8} # idee from bluefeversoft



OUTOFB_white = []
OUTOFB_black = []

whitepawnline = [110,111,112,113,114,115,116,117]
blackpawnline = [26,27,28,29,30,31,32,33]







# def structtest():
#     print('one_to_64',one_to_64)
#     print('ones',ones)
#     print('zeros',zeros)
#     print('board',board)
#     print('filonum',filonum)
    
#     print('PIECES',PIECES)
#     print('FILES',FILES)
#     print('RANKS',RANKS)
  
#     print('COLOURS',COLOURS)
#     print('THETRUTH',THETRUTH)
#     print('piceboard', piceboard)
#     print('table',table)
#     print('one-to_120',one_to_120)

# structtest()