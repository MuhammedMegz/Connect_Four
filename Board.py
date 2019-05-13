# General Board games Class

import numpy as np


class Board:

    nRow = 0
    nCol = 0
    boardMat = 0

    def __init__(self, rowNum, colNum):
        self.nRow = rowNum
        self.nCol = colNum
        self.boardMat = np.zeros((self.nRow, self.nCol))

    def printBoared(self):
        print(np.flip(self.boardMat, 0))
