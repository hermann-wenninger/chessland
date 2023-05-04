import pygame
class Piece:
    def __init__(self, type, pos, color, board):
        self.pos = pos
        self.color = color
        self.board = board
        self.type = self.type()
    
    def draw(self, surface):
        img = pygame.image.load(f"img/{self.color}_{self.type}.png")
        surface.blit(img, (self.x*75+10, self.y*75+10))
        pass

    def get_poss_moves_attacts_shelters(self):
        pass

    def type(self):
        return ord(type)

print('P',ord('P'))
print('R',ord('R'))
print('N',ord('N'))
print('B',ord('B'))
print('Q',ord('Q'))
print('K',ord('K'))