# Connect Four Computer Game with artificial intelligence and GUI

## Outlines:
* [Connect Four Game](#Game-Play-Logic)
* [Connect Four with AI](#Connect-Four-with-AI)
* [GUI](#GUI)


## Connect Four Game:

   Mainly it built with three classes Player, Board, and Connect Four, Player class object carry the player name and score,
  it also contain setters and getters for the two values(name, score).
  
  Borad class is a general class for any board based game, to initiate it you just need to give it the width and height of the board, also it validate if the place that the player want to place his piece or mark empty and get the valid row for placing the mark or piece, these two methods used to form the put the player mark method by validating the place is empty and get the first valid row to place this mark belong to current player
  
  ```
    def isEmptyPlace(self, col):
        return self.boardMat[self.nRow-1][col] == 0
    
  ```
  
  ```
  def firstValidRow(self, col):
        for eachRow in range(self.nRow):
            if self.boardMat[eachRow][col] == 0:
                return eachRow
  ```
  
  ```
  def placePiece(self, col, playerMark):
        if self.isEmptyPlace(col):
            dropRow = self.firstValidRow(col)
            self.boardMat[dropRow][col] = playerMark

  ```
  
