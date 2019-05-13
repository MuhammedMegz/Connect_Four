# Connect Four Computer Game with artificial intelligence and GUI

## Outlines:
* [Connect Four Game](#Connect-Four-Game)
* [Connect Four with AI](#Connect-Four-with-AI)
* [GUI](#GUI)


## Connect Four Game:

   Mainly it built with three classes Player, Board, and Connect Four, Player class object carry the player name and score,
  it also contain setters and getters for the two values(name, score).
  
  Board class is a general class for any board based game, to initiate it you just need to give it the width and height of the  board, also it validate if the place that the player want to place his piece or mark empty and get the valid row for placing the mark or piece, these two methods used to form the put the player mark method by validating the place is empty and get the first valid row to place this mark belong to current player
  
  
  ```
  def placePiece(self, col, playerMark):
        if self.isEmptyPlace(col):
            dropRow = self.firstValidRow(col)
            self.boardMat[dropRow][col] = playerMark
  ```
  
  ConnectFour class is the more specified class for connect four game play, it has two player instances and a board instance with width of 7 and height of 6, and the most important and specified thing is checking if the movement the payer done is a win one or not, it is done by checking for four side marks of this player next to each other by vertical, horizontal, 45 degree line or -45 degree line.
  
 ```
     def isWinMovement(self, playerMark):
          # vertical marks check
          # horizontal marks check
          # 45 degree marks check
          # -45 degree marks check
 ```
  
  
