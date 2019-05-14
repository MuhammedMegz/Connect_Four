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

    def printBoard(self):
        print(np.flip(self.boardMat, 0))

    def isEmptyPlace(self, col):
        return self.boardMat[self.nRow-1][col] == 0

    def firstValidRow(self, col):
        for eachRow in range(self.nRow):
            if self.boardMat[eachRow][col] == 0:
                return eachRow

    
    def placePiece(self, col, playerMark):
        if self.isEmptyPlace(col):
            dropRow = self.firstValidRow(col)
            self.boardMat[dropRow][col] = playerMark
            
    def get_valid_locations(self):
        valid_locations = []
        for col in range(self.nCol):
            if self.isEmptyPlace( col):
                valid_locations.append(col)
        return valid_locations
