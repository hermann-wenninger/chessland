#third party module
import numpy as np

#first part module
from piece import Piece
from board import Board
from board import position
from validation import table


aaaa = Board(position)
aaaa.abbild()
aaaa.update(48,'A2',32,'A3')
aaaa.abbild()
print(aaaa.history)
aaaa.update(49,'B2',33,'B4')
aaaa.abbild()
aaaa.update(8,'A7',24,'A5')
print(aaaa.history)
aaaa.abbild()
#aaaa.reset()
print(aaaa.history)
aaaa.abbild()
aaaa.update(8,'A7',24,'A5')
print(aaaa.history)
aaaa.abbild()
aaaa.update(33,'B4',24,'A5',attac=True)
aaaa.abbild()
print(aaaa.allpices)

class Pawn(Piece):

	blackPawnLine = np.array([38,39,40,41,42,43,44,45],dtype=np.uint8)
	whitePawnLine = np.array([98,99,100,101,102,103,104,105],dtype=np.uint8)
	table = table
	def __init__(self, type, pos, board):
		super().__init__(type, pos, board)

x = Pawn('p',52,aaaa)

print(x.p,x.pos,x.board[0])