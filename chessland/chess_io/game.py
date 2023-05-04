import pygame
from piece import Piece
from board import Board

x = Board()

pieces = []
for i in range(8):
    x = Piece("b", i, 1, "pawn")
    pieces.append(x)
    y = Piece("w", i, 6, "pawn")
    pieces.append(y)
    print(x.x,x.y,x.color)

for piece in pieces:
    piece.draw(board)

pygame.init()

# set up the window
size = (640, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess Game")

# set up the board
board = pygame.Surface((600, 600))
board.fill((255, 206, 158))

# draw the board
for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (210, 180, 140), (x*75, y*75, 75, 75))
        pygame.draw.rect(board, (210, 180, 140), ((x+1)*75, (y+1)*75, 75, 75))

# add the board to the screen
screen.blit(board, (20, 20))

pygame.display.flip()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # get the position of the click
            pos = pygame.mouse.get_pos()

            # convert the position to board coordinates
            x = (pos[0] - 20) // 75
            y = (pos[1] - 20) // 75

            # find the piece at the clicked position
            for piece in pieces:
                if piece.x == x and piece.y == y:
                    # move the piece
                    pos = pygame.mouse.get_pos()
                    x = (pos[0] - 20) // 75
                    y = (pos[1] - 20) // 75
                    piece.x = x
                    piece.y = y

    # redraw the board and pieces
    board.fill((255, 206, 158))
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(board, (210, 180, 140), (x*75, y*75, 75, 75))
            pygame.draw.rect(board, (210, 180, 140), ((x+1)*75, (y+1)*75, 75, 75))

    for piece in pieces:
        piece.draw(board)

    # add the board to the screen
    screen.blit(board, (20, 20))

    # update the display
    pygame.display.update()