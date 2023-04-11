king_is_alive = True
zug = 1
while king_is_alive:
    if zug % 2 == 0:
        print('black')
    else:
        print('white')
    zug +=1