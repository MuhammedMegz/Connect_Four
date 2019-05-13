# connect four class

from Board import *
from Player import *


class ConnectFour:
    connectFourBoard = Board(6, 7)
    player1 = None
    player2 = None
    anyWin = False

    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)

    def printBoard(self):
        print(self.connectFourBoard.printBoared())

    def getPlayer1Name(self):
        return self.player1.getPlayerName()

    def getPlayer2Name(self):
        return self.player2.getPlayerName()

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
        for col in range(nCol - 1):
            for row in range(nRow):
                if boardMat[row][col] == playerMark and \
                        boardMat[row][col + 1] == playerMark and \
                        boardMat[row][col + 2] == playerMark and \
                        boardMat[row][col + 3] == playerMark:
                    return True

        # horizontal marks check
        for col in range(nCol):
            for row in range(nRow - 3):
                if boardMat[row][col] == playerMark and \
                        boardMat[row + 1][col] == playerMark and \
                        boardMat[row + 2][col] == playerMark and \
                        boardMat[row + 3][col] == playerMark:
                    return True

        # 45 degree marks check
        for col in range(nCol - 3):
            for row in range(nRow - 3):
                if boardMat[row][col] == playerMark and \
                        boardMat[row + 1][col + 1] == playerMark and \
                        boardMat[row + 2][col + 2] == playerMark and \
                        boardMat[row + 3][col + 3] == playerMark:
                    return True

        # -45 degree marls check
        for col in range(nCol - 3):
            for row in range(3, nRow):
                if boardMat[row][col] == playerMark and \
                        boardMat[row - 1][col + 1] == playerMark and \
                        boardMat[row - 2][col + 2] == playerMark and \
                        boardMat[row - 3][col + 3] == playerMark:
                    return True




    def startGame(self):

        while not self.anyWin:




connect = ConnectFour("megz", "atta")
connect.connectFourBoard.placePiece(1,1)
connect.connectFourBoard.placePiece(2,2)
connect.connectFourBoard.placePiece(1,1)
connect.connectFourBoard.placePiece(2,2)
connect.connectFourBoard.placePiece(1,1)
connect.connectFourBoard.placePiece(2,2)
connect.connectFourBoard.placePiece(1,1)

print(connect.isWinMovement(2))