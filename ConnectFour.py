# connect four class

from Board import *
from Player import *


class ConnectFour:
    connectFourBoard = Board(6, 7)
    player1 = None
    player2 = None

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

