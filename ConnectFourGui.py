import tkinter as tk
from ConnectFour import ConnectFour

NROWS = 6
NCOL = 7

HEIGHT = 600
WIDTH = 700

playerNamesWindow = tk.Tk()
playingWindow = tk.Tk()

playingCanvas = None

player1NameEntry = tk.Entry(playerNamesWindow)
player2NameEntry = tk.Entry(playerNamesWindow)

player1Name = ""
player2Name = ""

turn = "player1" #It can be "player1", "computer"


def init():
    playerNamesWindow.title("Connect four")
    tk.Label(playerNamesWindow, text="First player name:").grid(row=0)
    tk.Label(playerNamesWindow, text="Second player name:").grid(row=1)

    tk.Button(playerNamesWindow, text="Start", command=startPressed).grid(row=2)

    player1NameEntry.grid(row=0, column=1)
    player2NameEntry.grid(row=1, column=1)

    playingWindow.title("Connect four")
    playingWindow.withdraw()

    playerNamesWindow.mainloop()

def startPressed():
    #Get players names
    global player1Name
    global player2Name
    player1Name = player1NameEntry.get()
    player2Name = player2NameEntry.get()

    #Close player names window
    playerNamesWindow.destroy()
    
    #Open the main playing window
    playingWindow.deiconify()
    playingWindow.focus()
    playingLoop()

def playingLoop():
    global playingCanvas
    playingCanvas = tk.Canvas(playingWindow, bg='blue', height=HEIGHT, width=WIDTH)
    

    for i in range(NROWS):
        for j in range(NCOL):
            x0 = j*(WIDTH/NCOL)
            y0 = i*(HEIGHT/NROWS)
            x1 = x0 + (WIDTH/NCOL)
            y1 = y0 + (HEIGHT/NROWS)
            playingCanvas.create_rectangle(x0, y0, x1, y1, width=0)
            playingCanvas.create_oval(x0+4, y0+4, x1-4, y1-4, fill='white', tags=(str(j)+","+str(i)))

    playingCanvas.bind('<Button-1>', mousePressed)

    playingCanvas.pack()
    playingWindow.mainloop()


def mousePressed(event):
    global turn
    if turn == "player1":
        x = event.x
        col = int(x/(WIDTH/NCOL))
        addPiece(col, "green")

def addPiece(col, color):
    for i in range(NROWS):
        tag = playingCanvas.find_withtag(str(col) + "," + str(NROWS - i - 1))
        if playingCanvas.itemcget(tag, "fill") == "white":
                playingCanvas.itemconfig(tag, fill=color)
                break
    switchTurns()

def switchTurns():
    global turn
    if turn == "player1":
        turn = "compupter"
    elif turn == "computer":
        turn = "player1"
        


init()
