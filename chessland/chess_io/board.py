class Board():
    def __init__(self,startpos):
        self.startpos = startpos
        self.history = []
    
    def update(self, oldPos, oldPosSquare, newPos, newPosSquare, attac=False):
        self.startpos[newPos] = self.startpos[oldPos]
        self.startpos[oldPos] = '.'
        if attac == False:
            self.history.append((self.startpos[oldPos],oldPosSquare,newPosSquare))
        else:
            self.history.append((self.startpos[oldPos],oldPosSquare,'X',self.startpos[newPos],newPosSquare))

    def reset(self):
        self.startpos[newPos] = self.startpos[oldPos]
        self.startpos[oldPos] = '.'
        del self.history[-1]      