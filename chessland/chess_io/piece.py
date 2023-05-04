import pygame

class Piece:
    def __init__(self, typ, pos, board):
        self.pos = pos
        self.board = board
        self.typ = typ
        self.p = self.typei()
        self.posmoves = []
        self.attacs =[]
        self.schelters =[]
    
    def draw(self, surface):
        img = pygame.image.load(f"img/{self.color}_{self.type}.png")
        surface.blit(img, (self.x*75+10, self.y*75+10))
        pass

    def get_poss_moves_attacts_shelters(self):
        pass

    def typei(self):
        self.p = ord(self.typ)
        return self.p

print('P',ord('P'))
print('R',ord('R'))
print('N',ord('N'))
print('B',ord('B'))
print('Q',ord('Q'))
print('K',ord('K'))