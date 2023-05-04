import pygame

class Piece:
    def __init__(self, color, x, y, piece_type):
        self.color = color
        self.x = x
        self.y = y
        self.type = piece_type

    def draw(self, surface):
        img = pygame.image.load(f"img/{self.color}_{self.type}.png")
        surface.blit(img, (self.x*75+10, self.y*75+10))

# set up the pieces


# draw the pieces
#for piece in pieces:
   #piece.draw(board)