from educs import *

w = None
columns = None
rows = None
board = None
next = None

@setup
def setup():
    global w, columns, rows, board, next
    createCanvas(720, 400);
    w = 20
    
    # Calculate columns and rows
    columns = floor(getWidth() / w)
    rows = floor(getHeight() / w)
    # Wacky way to make a 2D array in Python
    board = []
    for i in range(columns):
        board.append([None for j in range(rows)])
    
    # Going to use multiple 2D arrays and swap them
    next = []
    for i in range(columns):
        next.append([None for j in range(rows)])
    init()

@draw
def draw():
    global board
    
    background(255)
    generate();
    for i in range(columns):
        for j in range(rows):
            if board[i][j] == 1:
                fill(0)
            else:
                fill(255)
            stroke(0)
            rect(i * w, j * w, w-1, w-1)

# reset board when mouse is pressed
@mouseClicked
def onMouseClicked(event):
    init()

@mouseDragged
def onMouseDragged(event):
    pass

@keyPressed
def onKeyPressed(event):
    pass

# Fill board randomly
def init():
    global board, next, columns, rows
    for i in range(columns):
        for j in range(rows):
            # Lining the edges with 0s
            if (i == 0 or j == 0 or i == columns-1 or j == rows-1):
                board[i][j] = 0
            # Filling the rest randomly
            else:
                board[i][j] = floor(random(0, 2));
            next[i][j] = 0

# The process of creating the new generation
def generate():
    global board, next, columns, rows
    # Loop through every spot in our 2D array and check spots neighbors
    for x in range(1, columns-1):
        for y in range(1, rows-1):
            # Add up all the states in a 3x3 surrounding grid
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbors += board[x+i][y+j]

            # A little trick to subtract the current cell's state since
            # we added it in the above loop
            neighbors -= board[x][y];
            # Rules of Life
            if (board[x][y] == 1) and (neighbors <  2):
                next[x][y] = 0 # Loneliness
            elif (board[x][y] == 1) and (neighbors >  3):
                next[x][y] = 0 # Overpopulation
            elif (board[x][y] == 0) and (neighbors == 3):
                next[x][y] = 1 # Reproduction
            else:
                next[x][y] = board[x][y] # Stasis

    # Swap!
    temp = board
    board = next
    next = temp
    return

if __name__=="__main__":
    onMouseDragged(None) # registers your onMouseDragged function
    onKeyPressed(None) # registers your onKeyPress function
    onMouseClicked(None) # registers your onMouseClick function
    setup() # sets up the window
    draw() # starts running your draw function 60 times a second