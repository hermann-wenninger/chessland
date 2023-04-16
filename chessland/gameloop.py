from numba import jit
from validation import *


start = [['br','bn','bb','bq','bk','bb','bn','br'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','bq','','','','','',''],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wr','wn','wb','wq','wk','wb','wn','wr']]


w_king_alive = True
b_king_alive = True
zug = 1
#WHITEPIECES = ['wr','wn','wb','wq','wk','bp']
#BLACKPIECES = ['br','bn','bb','bq','bk','bp']
ALLPIECES = WHITEPIECES + BLACKPIECES

#@jit
def iterate_over_black(start, COLOR_OF_PICES):
    '''iterate over all pices from one black pices and give back 
    the number of the 120er board 
    the identity of sqares
    the rank of the pice
    '''
    print('iterate over black board')
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
    print('end of black board iteration')
    return OUTCOME_B, justnum_b

#@jit
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
                #OUTCOME is a list with data from white[pice boardposition 120ernummer]
                OUTCOME_W.append([pice,SQUARESSWITCH[squarenum],squarenum])
                justnum_w.append(squarenum)
    print(OUTCOME_W)
    print(justnum_w)
    print(len(OUTCOME_W))
    print('end of whiteboarditeration')
    return OUTCOME_W, justnum_w


#@jit
def take_spezial_pices(pool,color_rank):
    '''extrakt the OUTCOME list by color and rank'''
    ranklist = [i for i in pool if i[0]== color_rank]
    ranklist_justnum = [i[2] for i in pool if i[0] == color_rank]
    print('take special pices')
    print(ranklist)
    print(ranklist_justnum)
    print('end of take special pices')
    return ranklist ,ranklist_justnum

#@jit
def search_pice_by_num(outcome_list, number):
    for i in outcome_list:
        if i[2] == number:
            return i[0]
        
def sort_attacs_by_rank():
    pass


#@jit
def whitepawn_start(OUTCOME_W,justnum_w,justnum_b):
    '''first step of a pawn'''
    allpieno = justnum_w +justnum_b
    possible_moves = []
    possible_attacs = []
    whitepawns, whitepawns_justnum = take_spezial_pices(OUTCOME_W,'wp')
    print(whitepawns)
    print('justnum_b',justnum_b)
    print(justnum_w)
    print(OUTOFBOARD)
    print('whitepawns_justnum', whitepawns_justnum)
    for pawn in  whitepawns:
        
        x = pawn[2] + 10
        if x not in allpieno:
            possible_moves.append(['wp',pawn[2],x,])
        else:
            continue
        
        y = pawn[2] + 20
        if y not in allpieno:
            possible_moves.append(['wp',pawn[2],y])
        print(x,y)
    print(possible_moves)
    for pawn in whitepawns:
        a = pawn[2] + 9
        b = pawn[2] +11
        if a in justnum_b:
            possible_attacs.append(['wp',pawn[2],a])
        if b in justnum_b:
            possible_attacs.append(['wp',pawn[2],b])
    print(possible_attacs)


#@jit
def zug_black():
    print('zug schwarz')
    #x, y = iterate_over_black(start, BLACKPIECES)
   
   
#@jit
def zug_white():
    print('zug weiß')
    OUTCOME_B, justnum_b = iterate_over_black(start, BLACKPIECES)
    OUTCOME_W, justnum_w = iterate_over_white(start, WHITEPIECES)
    POSSIBLE_MOVES =[]
    POSSIBLE_ATTACS = []
    
    whitepawn_start(OUTCOME_W,justnum_w, justnum_b)
    
   

while w_king_alive and b_king_alive:
    
    if zug % 2 == 0:
       
        zug_black()
    else:
        print('')
        zug_white()
    if zug > 2:
        break
    zug +=1



#print(SQUARES)

x = np.arange(100).reshape(10, 10)

@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def go_fast(a): # Function is compiled to machine code when called the first time
    trace = 0.0
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i])*0.3 # Numba likes NumPy functions
    return a + trace              # Numba likes NumPy broadcasting

print(go_fast(x))