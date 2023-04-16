from chessland.figures.planeboard import startboard

x = [['br','bn','bb','bq','bk','bb','bn','br'],
    ['bp','bp','bp','bp','bp','bp','bp','bp'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['wp','wp','wp','wp','wp','wp','wp','wp'],
    ['wr','wn','wb','wq','wk','wb','wn','wr']]
def player():
        spielersch = input('spieler 1:')
        spielerw = input('spieler 2:')
        return spielersch, spielerw

class Board():

    def __init__(self,spielgroesse,spielerw, spielersch, positionen = x):
        self.spielgr = spielgroesse
        self.spielerw = spielerw
        self.spielersch = spielersch
        self.positionen = positionen
        self.pict = startboard(spielersch,spielerw)
    
    
    #def createboard(self,spielerw, spielersch):
        #startboard(spielersch, spielerw)

xyz = Board(640,'hmann','xman')
print(xyz)