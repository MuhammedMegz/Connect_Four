# connect four class

from Board import *
from Player import *
import math
import random

opponentMark=1
AIMark=2

class ConnectFour:
    connectFourBoard = None
    player1 = None
    player2 = None
    anyWin = False

    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        self.connectFourBoard = Board(6, 7)

    def printBoard(self):
        print(self.connectFourBoard.printBoard())

    def getPlayer1Name(self):
        return self.player1.getPlayerName()

    def getPlayer2Name(self):
        return self.player2.getPlayerName()
    def copy(self):
        return self

    def getPlayer1Score(self):
        return self.player2.getPlayerScore()

    def getPlayer2Score(self):
        return self.player2.getPlayerScore()

    def setPlayer1Score(self, newScore):
        self.player1.setPlayerScore(newScore)

    def setPlayer2Score(self, newScore):
        self.player2.setPlayerScore(newScore)

    def isWinMovement(self, playerMark):

        nRow = self.connectFourBoard.nRow
        nCol = self.connectFourBoard.nCol
        boardMat = self.connectFourBoard.boardMat

        # vertical marks check
        for col in range(nCol - 3):
            for row in range(nRow):
                if boardMat[row][col] == playerMark and \
                        boardMat[row][col + 1] == playerMark and \
                        boardMat[row][col + 2] == playerMark and \
                        boardMat[row][col + 3] == playerMark:
                    return True

        # horizontal  check
        for col in range(nCol):
            for row in range(nRow - 3):
                if boardMat[row][col] == playerMark and \
                        boardMat[row + 1][col] == playerMark and \
                        boardMat[row + 2][col] == playerMark and \
                        boardMat[row + 3][col] == playerMark:
                    return True

        # 45 degree check
        for col in range(nCol - 3):
            for row in range(nRow - 3):
                if boardMat[row][col] == playerMark and \
                        boardMat[row + 1][col + 1] == playerMark and \
                        boardMat[row + 2][col + 2] == playerMark and \
                        boardMat[row + 3][col + 3] == playerMark:
                    return True

        # -45 degree  check
        for col in range(nCol - 3):
            for row in range(3, nRow):
                if boardMat[row][col] == playerMark and \
                        boardMat[row - 1][col + 1] == playerMark and \
                        boardMat[row - 2][col + 2] == playerMark and \
                        boardMat[row - 3][col + 3] == playerMark:
                    return True

    def evaluate_score(self,values, mark):
        score = 0
        opp_piece = opponentMark
        if mark == opponentMark:
            opp_piece = AIMark

        if values.count(mark) == 4:
            score += 100
        elif values.count(mark) == 3 and values.count(0) == 1:
            score += 5
        elif values.count(mark) == 2 and values.count(0) == 2:
            score += 2

        if values.count(opp_piece) == 3 and values.count(0) == 1:
            score -= 4

        return score

    def score(self, playerMark):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(self.connectFourBoard.boardMat[:, 7//2])]
        center_count = center_array.count(playerMark)
        score += center_count * 3

        ## Score Horizontal
        for r in range(self.connectFourBoard.nRow):
            row_array = [int(i) for i in list(self.connectFourBoard.boardMat[r,:])]
            for c in range(self.connectFourBoard.nCol-3):
                values = row_array[c:c+4]
                score += self.evaluate_score(values, playerMark)

        ## Score Vertical
        for c in range(self.connectFourBoard.nCol):
            col_array = [int(i) for i in list(self.connectFourBoard.boardMat[:,c])]
            for r in range(self.connectFourBoard.nRow-3):
                values = col_array[r:r+4]
                score += self.evaluate_score(values, playerMark)

        ## Score  diagonal
        for r in range(self.connectFourBoard.nRow-3):
            for c in range(self.connectFourBoard.nCol-3):
                values = [self.connectFourBoard.boardMat[r+i][c+i] for i in range(4)]
                score += self.evaluate_score(values, playerMark)

        for r in range(self.connectFourBoard.nRow-3):
            for c in range(self.connectFourBoard.nCol-3):
                values = [self.connectFourBoard.boardMat[r+3-i][c+i] for i in range(4)]
                score += self.evaluate_score(values, playerMark)

        return score
		
    def is_terminal_node(self):
        return self.isWinMovement(opponentMark) or self.isWinMovement( AIMark) or len(self.connectFourBoard.get_valid_locations()) == 0

    def minimax(self, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.connectFourBoard.get_valid_locations()
        is_terminal = self.is_terminal_node()
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.isWinMovement( AIMark):
                    return (None, 100000000000000)
                elif self.isWinMovement( opponentMark):
                    return (None, -10000000000000)
                else: 
                    return (None, 0)
            else: # Depth is zero
                return (None, self.score( AIMark))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:

                board_copy = self.connectFourBoard.boardMat.copy()
                self.connectFourBoard.placePiece( col, AIMark)
                new_score = self.minimax( depth-1, alpha, beta, False)[1]
                self.connectFourBoard.boardMat=board_copy
                if new_score > value :
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else: # Minimizing 
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                board_copy = self.connectFourBoard.boardMat.copy()
                self.connectFourBoard.placePiece(  col, opponentMark)
                new_score = self.minimax( depth-1, alpha, beta, True)[1]
                self.connectFourBoard.boardMat=board_copy
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value