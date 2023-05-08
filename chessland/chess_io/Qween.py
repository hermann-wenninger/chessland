#third party module
import numpy as np

#first part module
from piece import Piece

from board import Board
from board import position
from validation import table
from validation import tableswitch
from validation import outofboard
from validation import one_to_64
from validation import one_to_144
import pprint



class Qween(Piece):
    #whitePawnLine = [48,49,50,51,52,53,54,55]# np.array([98,99,100,101,102,103,104,105],dtype=np.uint8)
    #blackPawnLine = [8,9,10,11,12,13,14,15]#np.array([38,39,40,41,42,43,44,45],dtype=np.uint8)
    one_to_64 = one_to_64
    table = table
    tableswitch = tableswitch
    outofboard = outofboard
    one_to_144 = one_to_144

    def __init__(self, typ, pos, board):
        super().__init__(typ, pos, board)
        self.mov = []
        self.attac =[]
        self.schelt =[]