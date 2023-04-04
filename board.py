import numpy as np

one_to_64 = np.arange(1,65).reshape(8, 8)[::-1]
ones = np.ones((8,8), dtype=np.uint8)
zeros  = np.zeros((8,8),dtype=np.uint8)
board  = np.zeros((8,8),dtype=np.uint8)
board[1::2,::2] = 1
board[::2,1::2] = 1
Filo = ["a", "b", "c", "d", "e", "f", "g", "h"]
Numbr = ["1", "2", "3", "4", "5", "6", "7", "8"]

filonum = [f+n for f in Filo for n in Numbr]
filonum = np.array(filonum, dtype = np.chararray).reshape(8,8)[::-1]


print(one_to_64)
print(ones)
print(zeros)
print(board[::-1])
print(filonum)