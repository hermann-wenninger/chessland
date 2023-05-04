from piece import Piece
from

class Pawn(Piece):

	blackPawnLine = np.array([26,27,28,29,30,31,32,33],dtype=np.uint8)
	whitePawnLine = np.array([110,111,112,113,114,115,116,117],dtype=np.uint8)

	def __init__(self, type, pos, board):
		super().__init__(type, pos, board)

x = Pawn('p',52,)