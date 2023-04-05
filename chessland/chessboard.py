#CHESSBOARD
#CHESSBOARD
import numpy as np
import cv2
from PIL import Image


im = cv2.imread('k.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)  
print(img)
print(np.shape(img))
front = (img[:,:,0] / 255).astype(int)
print(np.shape(front))

a = input('spieler 1:')
b = input('spieler 2:')


def createboard(a, b):
    number = 1
    titel = "Spiel"+ str(number) + " " + a +" spielt weis " + "gegen " + b + " spielt schwarz"
    spielfeldgr = 640
    feld = int(spielfeldgr/8)
    npo = np.zeros((spielfeldgr,spielfeldgr)) 
    print(npo)
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
                    npo[r:c, r1:c1]=[cw]
                    print(npo)
                else:
                    npo[r:c, r1:c1]=[cb]
            else:
                if j%2==0:
                    npo[r:c, r1:c1]=[cb]
                else:
                    npo[r:c, r1:c1]=[cw]
            r = r + feld
            c = c + feld
        r1 = r1 + feld
        c1 = c1 + feld
   
        img1 = Image.fromarray(np.uint8(npo * 255) , 'L')
        img2 = Image.open('k.png')
        img1.paste(img2)
        img1.save('paste.jpg', quality=95)
        

    cv2.imshow(titel, npo)
    cv2.waitKey()
    cv2.destroyAllWindows()

    print(npo)


createboard(a, b)
