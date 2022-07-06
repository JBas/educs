from educs import *

num = 2000
r = 6

ax = []
ay = []

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
    createCanvas(710, 400);
    for i in range(num):
        ax.append(getWidth() / 2)
        ay.append(getHeight() / 2)
    
    frameRate(10);
    pass

@draw
def draw():
    background(51);
    
    # Shift all elements 1 place to the left
    lastx = ax[-1]
    lasty = ay[-1]
    ax.pop(0)
    ay.pop(0)
    
    # Put a new value at the end of the array
    ax.append(lastx + random(-r, r))
    ay.append(lasty + random(-r, r))
    
    # Constrain all points to the screen
    ax[-1] = constrain(ax[-1], 0, getWidth())
    ay[-1] = constrain(ay[-1], 0, getHeight())
    
    # Draw a line connecting the points
    for j in range(1, num):
        val = j / num * 204.0 + 51;
        stroke(val);
        line(ax[j - 1], ay[j - 1], ax[j], ay[j])
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