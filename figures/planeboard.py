#CHESSBOARD

import numpy as np
import cv2
from PIL import Image
from numpy import asarray


x = [['br','bn','bb','bq','bk','bb','bn','br'],
    ['bp','bp','bp','bp','bp','bp','bp','bp'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['wp','wp','wp','wp','wp','wp','wp','wp'],
    ['wr','wn','wb','wq','wk','wb','wn','wr']]





def startboard(a, b):
   
    number = 1
    titel = "Spiel"+ str(number) + " " + a +" spielt weis " + "gegen " + b + " spielt schwarz"
    spielfeldgr = 640
    feld = int(spielfeldgr/8)
    npo = np.zeros((spielfeldgr,spielfeldgr)) 
    
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
    # for i in range(len(x)):
    #     for j in range(len(x[i])):
            
    #         datei = str(x[i][j]) + ".png"
           
            
    #         if x[i][j] == "":
    #             continue
    #         img = Image.open(datei)
    #         img1.paste(img,(j*80,i*80))
    img1.show('titel')
    data = asarray(img1)
    cv2.imshow('titel', data)
    #a,i = 3,3
    #img1.save(f'../images/spiel{a}_zug{i}.jpg', quality=95)
        

    
    cv2.waitKey()
    cv2.destroyAllWindows()

    



