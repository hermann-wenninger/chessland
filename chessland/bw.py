#CHESSBOARD
import numpy
import cv2

a = input('spieler 1:')
b = input('spieler 2:')


def createboard(a, b):
    number = 1
    titel = "Spiel"+ str(number) + " " + a +" spielt weis " + "gegen " + b + " spielt schwarz"
    spielfeldgr = 640
    feld = int(spielfeldgr/8)
    np = numpy.zeros((spielfeldgr,spielfeldgr)) 
    print(np)
    cb = 0
    cw = 1
    r1 = 0
    c1 = feld
    for i in range(0,8):
        r = 0
        c = feld
        for j in range(0,8):
            if i % 2 == 0:
                if j % 2 == 0:
                    np[r:c, r1:c1]=[cw]
                    print(np)
                else:
                    np[r:c, r1:c1]=[cb]
            else:
                if j%2==0:
                    np[r:c, r1:c1]=[cb]
                else:
                    np[r:c, r1:c1]=[cw]
            r = r + feld
            c = c + feld
        r1 = r1 + feld
        c1 = c1 + feld
        print(np)

    cv2.imshow(titel, np)
    cv2.waitKey()
    cv2.destroyAllWindows()

    print(np)


createboard(a, b)