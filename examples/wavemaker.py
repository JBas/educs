from educs import *

t = 0 # time variable

@setup
def setup():
    createCanvas(600, 600)
    noStroke()
    fill(40, 200, 40)

@draw
def draw():
    global t
    background(10, 10) # translucent background (creates trails)
    # make a x and y grid of ellipses
    for x in range(0, getWidth()+1, 30):
        for y in range(0, getHeight()+1, 30):
            # starting point of each circle depends on mouse position
            xAngle = rerange(getMouseX(), 0, getWidth(), -4 * PI, 4 * PI, True)
            yAngle = rerange(getMouseY(), 0, getHeight(), -4 * PI, 4 * PI, True)
            
            # and also varies based on the particle's location
            angle = xAngle * (x / getWidth()) + yAngle * (y / getHeight())
            
            # each particle moves in a circle
            myX = x + 20 * cos(2 * PI * t + angle)
            myY = y + 20 * sin(2 * PI * t + angle)
            
            ellipse(myX, myY, 10)
            
    t = t + 0.01 # update time
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

def main():
    onMouseDragged(None) # registers your onMouseDragged function
    onKeyPressed(None) # registers your onKeyPress function
    onMouseClicked(None) # registers your onMouseClick function
    setup() # sets up the window
    draw() # starts running your draw function
           # framerate (default is 60) times a second

if __name__=="__main__":
    main()