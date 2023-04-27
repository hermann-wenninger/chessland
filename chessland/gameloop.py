
from validation import *
from validation import SQUARESSWITCH as switch
from validation import PICEBOARD as pibo
from validation import start as srt
import numpy as np
import random


start = [['br','bn','bb','bq','bk','bb','bn','br'],
        ['bp','bp','bp','bp','bp','bp','bp','bp'],
        ['','wq','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','bq','','','','','',''],
        ['wp','wp','wp','wp','wp','wp','wp','wp'],
        ['wr','wn','wb','wq','wk','wb','wn','wr']]

history = []

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



def take_spezial_pices(pool,color_rank):
    '''extrakt the OUTCOME list by color and rank'''
    ranklist = [i for i in pool if i[0]== color_rank]
    ranklist_justnum = [i[2] for i in pool if i[0] == color_rank]
    print('take special pices')
    print(ranklist)
    print(ranklist_justnum)
    print('end of take special pices')
    return ranklist ,ranklist_justnum


def search_pice_by_num(outcome_list, number):
    for i in outcome_list:
        if i[2] == number:
            return i[0]
       
def sort_attacs_by_rank():
    pass



def whitepawn_start(OUTCOME_W,justnum_w,justnum_b):
    '''first step of a pawn'''
    allpieno = justnum_w +justnum_b
    possible_moves = []
    possible_attacs = []
    whitepawns, whitepawns_justnum = take_spezial_pices(OUTCOME_W,'wp')
    #print(whitepawns)
    #print('justnum_b',justnum_b)
    #print(justnum_w)
    #print(OUTOFBOARD)
    #print('whitepawns_justnum', whitepawns_justnum)
    for pawn in  whitepawns:
        x = pawn[2] + 10
        if x not in allpieno:
            possible_moves.append(['wp',pawn[2],x,])
        else:
            continue
        y = pawn[2] + 20
        if y not in allpieno:
            possible_moves.append(['wp',pawn[2],y])
        #print(x,y)
    print('possible_moves',possible_moves)
    for pawn in whitepawns:
        a = pawn[2] + 9
        b = pawn[2] +11
        if a in justnum_b:
            possible_attacs.append(['wp',pawn[2],a])
        if b in justnum_b:
            possible_attacs.append(['wp',pawn[2],b])
    print('possible_attacs',possible_attacs)
    return possible_moves, possible_attacs



def append_moves_and_attacs(possible_moves, possible_attacs, moves, attacs):
    '''append possible moves and possible attacs to the lists'''
    moves.append(possible_moves)
    attacs.append(possible_attacs)
    print('append_moves',moves)
    print('append attacs', attacs)
    return moves, attacs


def take_best_move(moves,attacs):
    '''later i will implement this function with a sort algo'''
    all = moves[0] + attacs[0]
    x = random.choice(all)
    print('take best zug',x)
    return x


def write_move(best_move):
    '''all data for a real move and the annotation'''
    move = best_move
    print(move[0])
    print(switch[move[1]],move[1])
    print(switch[move[2]],move[2])
    print(move[0], ' move from ',switch[move[1]], ' to ',switch[move[2]], 'is a switch from number ',move[1], ' to number ',move[2])
    pice_move_from_to = move[0],switch[move[1]],move[1],switch[move[2]],move[2]
    return pice_move_from_to

def move_on_boards(bestmovefromto):
    print('move on boards')
    print('bestmove',bestmovefromto)
    pibo[bestmovefromto[1]]= ''
    pibo[bestmovefromto[3]] = bestmovefromto[0]
    print(pibo)
    for i in pibo:
        print(pibo[i])
        
    #for i , x in enumerate(start):
        #for j, pice in enumerate(x):
            #print(i,x,j,pice)
    
        
        #for j, pice in enumerate(x):
            #print(j,pice)

   


def zug_black():
    print('zug schwarz')
    #x, y = iterate_over_black(start, BLACKPIECES)
   
   

def zug_white():
    print('zug weiß')
    OUTCOME_B, justnum_b = iterate_over_black(start, BLACKPIECES)
    OUTCOME_W, justnum_w = iterate_over_white(start, WHITEPIECES)
    poss_moves =[]
    poss_attacs = []
    
    a,b = whitepawn_start(OUTCOME_W,justnum_w, justnum_b)
    append_moves_and_attacs(a,b,poss_moves,poss_attacs)
    bm = take_best_move(poss_moves, poss_attacs)
    pmfto = write_move(bm)
    move_on_boards(pmfto)
   

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



#@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
