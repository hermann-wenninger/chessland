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

def iterate_over_board(start, COLOR_OF_PICES):
    print('iterate over board')
    for i , x in enumerate(start):
        for j, y in enumerate(x):
            print(i,j,y)


def zug_black():
    print('zug schwarz')
    iterate_over_board(start, BLACKPIECES)
   

def zug_white():
    print('zug weiß')
    iterate_over_board(start, WHITEPIECES)

while w_king_alive and b_king_alive:
    if zug % 2 == 0:
       
        zug_black()
    else:
        print('')
        #zug_white()
    if zug > 10:
        break
    zug +=1