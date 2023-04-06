from planeboard import startboard


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
    
    def createboard(self,):
        startboard()