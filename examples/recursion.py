from educs import *

@setup
def setup():
    createCanvas(720, 560);
    noStroke();
    noLoop();
    pass

@draw
def draw():
    pass

@mouseClicked
def onMouseClicked(event):
    pass

@mouseDragged
def onMouseDragged(event):
    pass

@keyPressed
def onKeyPressed(event):
    pass

if __name__=="__main__":
    onMouseDragged(None) # registers your onMouseDragged function
    onKeyPressed(None) # registers your onKeyPress function
    onMouseClicked(None) # registers your onMouseClick function
    setup() # sets up the window
    draw() # starts running your draw function
           #framerate (default is 60) times a second