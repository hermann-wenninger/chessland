from validation import *


start = [['br','bn','bb','bq','bk','bb','bn','br'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wr','wn','wb','wq','wk','wb','wn','wr']]


w_king_alive = True
b_king_alive = True
zug = 1
#WHITEPIECES = ['wr','wn','wb','wq','wk','bp']
#BLACKPIECES = ['br','bn','bb','bq','bk','bp']
ALLPIECES = WHITEPIECES + BLACKPIECES

def iterate_over_black(start, COLOR_OF_PICES):
    '''iterate over all pices from one black pices and give back 
    the number of the 120er board 
    the identity of sqares
    the rank of the pice
    '''
    print('iterate over board')
    OUTCOME_B = []
    justnum_b = []
    for i , x in enumerate(start):
        for j, pice in enumerate(x):
            if pice in COLOR_OF_PICES:
                squarenum = TABLE[str(i)+str(j)]
                #OUTCOME is a list with data from black or white[pice boardposition 120ernummer]
                OUTCOME_B.append([pice,SQUARESSWITCH[squarenum],squarenum])
                justnum_b.append(squarenum)
    print(OUTCOME_B)
    print(justnum_b)
    print(len(OUTCOME_B))
    return OUTCOME_B, justnum_b


def iterate_over_white(start, COLOR_OF_PICES):
    '''iterate over all pices from one whitepices and give back 
    the number of the 120er board 
    the identity of sqares
    the rank of the pice
    '''
    print('iterate over white board')
    OUTCOME_W = []
    justnum_w = []
    for i , x in enumerate(start):
        for j, pice in enumerate(x):
            if pice in COLOR_OF_PICES:
                squarenum = TABLE[str(i)+str(j)]
                #OUTCOME is a list with data from black or white[pice boardposition 120ernummer]
                OUTCOME_W.append([pice,SQUARESSWITCH[squarenum],squarenum])
                justnum_w.append(squarenum)
    print(OUTCOME_W)
    print(justnum_w)
    print(len(OUTCOME_W))
    return OUTCOME_W, justnum_w



def take_spezial_pices(pool,color_rank):
    '''extrakt the OUTCOME list by color and rank'''
    ranklist = [i for i in pool if i[0]== color_rank]
    print(ranklist)
    return ranklist


def whitepawn_start():
    '''first step of a pawn'''
    whitepawns = take_spezial_pices(x,'wp')
    print(whitepawns)
    #a = getnum + 9
    #b = getnum +11
    #x = getnum + 10
    #y = getnum + 20



def zug_black():
    print('zug schwarz')
    x, y = iterate_over_black(start, BLACKPIECES)
   
   

def zug_white():
    print('zug weiß')
    x, y = iterate_over_white(start, WHITEPIECES)
    
    whitepawn_start()
   

while w_king_alive and b_king_alive:
    iterate_over_black(start, BLACKPIECES)
    if zug % 2 == 0:
       
        zug_black()
    else:
        print('')
        zug_white()
    if zug > 2:
        break
    zug +=1



def whitepawn_start(getnum):
    '''first step of a pawn'''
    a = getnum + 9
    b = getnum +11
    x = getnum + 10
    y = getnum + 20


