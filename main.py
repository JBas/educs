from cspy import *

@keyPressed
def onKeyPressed(event):
    pass

@mouseClicked
def onMouseClicked(event):
    pass

@mouseDragged
def onMouseDragged(event):
    pass

@setup
def setup():
    createCanvas(400, 400)
    
    background(100)
    strokeWeight(5)
    stroke("white")

    pass

@draw
def draw():
    if isMousedPressed():
        fill(0)
    else:
        fill(255)

    ellipse(getMouseX(), getMouseY(), 80, 80);
    
    pass


if __name__=="__main__":
    onMouseDragged(None) # registers your onMouseDragged function
    onKeyPressed(None) # registers your onKeyPress function
    onMouseClicked(None) # registers your onMouseClick function
    setup() # sets up the window
    draw() # starts running your draw function 60 times a second