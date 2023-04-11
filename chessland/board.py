from planeboard import startboard

x = [['br','bn','bb','bq','bk','bb','bn','br'],
    ['bp','bp','bp','bp','bp','bp','bp','bp'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['wp','wp','wp','wp','wp','wp','wp','wp'],
    ['wr','wn','wb','wq','wk','wb','wn','wr']]


class Board():

    def __init__(self,spielgroesse,spielerw, spielersch, positionen):
        self.spielgr = spielgroesse
        self.spielerw = spielerw
        self.spielersch = spielersch
        self.positionen = positionen
        
    def player(self):
        spielersch = input('spieler 1:')
        spielerw = input('spieler 2:')
        return spielersch, spielerw
    
    def createboard(self,spielerw, spielersch):
        startboard(spielersch, spielerw)