from piece import Piece

class Bishop(Piece):
	whitePawnLine = np.array([98,99,100,101,102,103,104,105],dtype=np.uint8)
	def __init__(self, type, pos, board):
		super().__init__(type, pos, board)