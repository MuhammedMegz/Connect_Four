import tkinter as tk
from tkinter import messagebox
from ConnectFour import ConnectFour
import math
import random
import sys

NROWS = 6
NCOL = 7

HEIGHT = 600
WIDTH = 700

playingWindow = tk.Tk()
playingModeWindow = tk.Tk()


playingCanvas = None
connectFour = None

playingMode = ""

player1Name = "p1"
player2Name = "p2"

playing = False

piecesColor = ["red", "yellow"]

turn = "" #It can be "Human", "Computer"
playerMark = 1


def init():
    playingModeWindow.title("Connect four")

    tk.Label(playingModeWindow, text="Choose playing mode").grid(row=0)

    tk.Button(playingModeWindow, text="Human vs Human", command=HvsH).grid(row=1)
    tk.Button(playingModeWindow, text="Human vs Computer", command=HvsC).grid(row=2)
    tk.Button(playingModeWindow, text="Computer vs Computer", command=CvsC).grid(row=3)

    playingWindow.title("Connect four")
    playingWindow.withdraw()

    playingModeWindow.mainloop()

def HvsH():
    global playingMode
    global turn
    playingMode = "HvsH"
    turn = "Human"
    start()

def HvsC():
    global playingMode
    global turn
    playingMode = "HvsC"
    temp = ["Human", "Computer"]
    turn = random.choice(temp)
    start()

def CvsC():
    global playingMode
    global turn
    playingMode = "CvsC"
    turn = "Computer"
    start()

def start():
    #Close player names window
    playingModeWindow.withdraw()
    
    #Open the main playing window
    playingWindow.deiconify()
    playingWindow.focus()
    drawBoard()
    playingLoop()

def drawBoard():
    global playingCanvas
    playingCanvas = tk.Canvas(playingWindow, bg='blue', height=HEIGHT, width=WIDTH)
    
    global connectFour
    connectFour = ConnectFour(player1Name, player2Name)

    for i in range(NROWS):
        for j in range(NCOL):
            x0 = j*(WIDTH/NCOL)
            y0 = i*(HEIGHT/NROWS)
            x1 = x0 + (WIDTH/NCOL)
            y1 = y0 + (HEIGHT/NROWS)
            playingCanvas.create_rectangle(x0, y0, x1, y1, width=0)
            playingCanvas.create_oval(x0+4, y0+4, x1-4, y1-4, fill='white', tags=(str(j)+","+str(i)))

    playingCanvas.create_text(WIDTH/2, HEIGHT/2, tags="thinkingLabel", state=tk.HIDDEN,  font=('Helvetica', 60, 'bold'))

    playingCanvas.bind('<Button-1>', mousePressed)

    playingCanvas.pack()

def playingLoop():
    global turn
    global playerMark
    global playing
    playing = True
    while playing:
        if turn == "Computer":
            labelTag = playingCanvas.find_withtag("thinkingLabel")
            playingCanvas.itemconfig(labelTag, text ="P" + str(playerMark) + " Thinking...", fill=piecesColor[playerMark-1], state=tk.NORMAL)
            playingWindow.update()
            col, minmaxScore = connectFour.minimax(5, -math.inf, math.inf, True)
            addPiece(col, piecesColor[playerMark-1])
            connectFour.connectFourBoard.placePiece(col, playerMark)
            playingCanvas.itemconfig(labelTag, state=tk.HIDDEN)
            if connectFour.isWinMovement(playerMark):
                playing = False
                playAgain = messagebox.askyesno("Connect four", "Player" + str(playerMark) +   " (Computer) WON.\nDo you want to play again?")
                if playAgain == True:
                    resetAndPlayAgain()
                else:
                    sys.exit(0)
        playingWindow.update()
        playingWindow.update_idletasks()
        
        


def mousePressed(event):
    global turn
    global playerMark
    global playing
    if turn == "Human":
        x = event.x
        col = int(x/(WIDTH/NCOL))
        addPiece(col, piecesColor[playerMark-1])
        connectFour.connectFourBoard.placePiece(col, playerMark)
        if connectFour.isWinMovement(playerMark):
            playing = False
            playAgain = messagebox.askyesno("Connect four", "Player" + str(playerMark) + " (Human) WON.\nDo you want to play again?")
            if playAgain == True:
                resetAndPlayAgain()
            else:
                sys.exit(0)

def addPiece(col, color):
    for i in range(NROWS):
        tag = playingCanvas.find_withtag(str(col) + "," + str(NROWS - i - 1))
        if playingCanvas.itemcget(tag, "fill") == "white":
                playingCanvas.itemconfig(tag, fill=color)
                break
    switchTurns()

def switchTurns():
    global turn
    global playerMark
    global playingMode
    playerMark = (playerMark%2) + 1
    if playingMode == "HvsC":
        if turn == "Human":
            turn = "Computer"
        elif turn == "Computer":
            turn = "Human"

def resetAndPlayAgain():
    global playingCanvas
    global connectFour
    if playingCanvas != None:
        playingCanvas.destroy()
    if connectFour != None:
        del(connectFour)
    playingWindow.withdraw()
    playingModeWindow.deiconify()
    playingModeWindow.focus()
        

if __name__ == "__main__":
    init()
