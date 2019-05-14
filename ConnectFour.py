# connect four class

from Board import *
from Player import *


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

        # -45 degree marks check
        for col in range(nCol - 3):
            for row in range(3, nRow):
                if boardMat[row][col] == playerMark and \
                        boardMat[row - 1][col + 1] == playerMark and \
                        boardMat[row - 2][col + 2] == playerMark and \
                        boardMat[row - 3][col + 3] == playerMark:
                    return True

    def startGame(self):

        playerTurn = 1
        while not self.anyWin:

            if playerTurn == 1:
                col = int(input("player 1 turn enter col number"))
                self.connectFourBoard.placePiece(col, 1)
                playerTurn = 2
                if self.isWinMovement(1):
                    print("player 1 won the game")
                    self.anyWin = True
                    break



            elif playerTurn == 2:
                col = int(input("player 2 turn enter col number"))
                self.connectFourBoard.placePiece(col, 2)
                playerTurn = 1
                if self.isWinMovement(2):
                    print("player 2 won the game")
                    self.anyWin = True
                    break


connect = ConnectFour("megz", "attar")

connect.startGame()
