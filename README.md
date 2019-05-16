# Connect Four Computer Game with artificial intelligence and GUI

   
     
     
   

## Outlines:
* [Connect Four Game](#Connect-Four-Game)
* [Connect Four with AI](#Connect-Four-with-AI)
* [GUI](#GUI)
* [Work Split](#Work-Split)


## Connect Four Game:

  This game was built in python and AI as a player against the user depending on ALPHA-BETA pruning, The design pattern used is MVC (Model, View, and controller), the Model consists of main three classes, First one is the "Player.py" which have two main propreties (Name, Score), Second class is "Board.py" it is a general class for any board game.
   
   Board class simply create in it's constructor a board with zero places in it, the width and height of the board determined in the constructor of the class in our case was 6x7 board for connect four, The main metods in this class are 3,
one to check this place is empty or not to validate the player movement, second one to get the final valid row to place the player mark (it was more specified for connect four game), Third and last one use the two previous methods to place the use mark if he/her marked valid place and in the row determined by the second method.

```
  def placePiece(self, col, playerMark):
        if self.isEmptyPlace(col):
            dropRow = self.firstValidRow(col)
            self.boardMat[dropRow][col] = playerMark
```

   
   Third and last class is the "connectFour.py" which take two instances of Player class (in case of two normal players), and one instance of Board class with dimensions of 6X7 for connect Four Game, The only logic is in this class one method that check winning state after every player movement or replacement of coin it check the winning states verticall, horizontaly, 45 degree line, and -45 degree line
   
    ```
     def isWinMovement(self, playerMark):
          # vertical marks check
          # horizontal marks check
          # 45 degree marks check
          # -45 degree marks check
     
     ```
     
 ## Connect Four with AI
 
   This part developed using ALPHA-BETA pruning after every placement it looks in the four directions if it have 3 serial marks it gives it high score, if 2 it gives it lower score, if 1 it gives it the lowest score to play, Also if it have 4 serial placements of the opponent it gives score by -ve sign.
   
   Here is the sudo code to summarize the idea
  
```
function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if α ≥ β then
                break (* β cut-off *)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if α ≥ β then
                break (* α cut-off *)
        return value

```


## GUI

![alt text](https://github.com/MuhammedMegz/Connect_Four/blob/master/1sc.png)
![alt text](https://github.com/MuhammedMegz/Connect_Four/blob/master/2sc.png)
![alt text](https://github.com/MuhammedMegz/Connect_Four/blob/master/3sc.png)

## Work Split

Name | Role 
--- | --- 
Muhammed Magdy Taha | Build the three classes Player, Board, Connect Four 
Muhammed Ashraf Abdelrahman Elattar | Build the GUI and integration of classes with AI
Muhammed Ahmed Fouad | Build the AI algorithm following ALPH-BETA algoritm
  
  
  

  
  
  
