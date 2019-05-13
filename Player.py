# Player Class



class Player:

    name = ""
    score = ""

    def __init__(self, pName):
        self.name = pName
        self.score = 0

    def getPlayerName(self):
        return self.name

    def getPlayerScore(self):
        return self.score

    def setPlayerScore(self, newScore):
        self.score = newScore
