from educs import *

def drawCircle(x, radius, level):
  # 'level' is the variable that terminates the recursion once it reaches 
  # a certain value (here, 1). If a terminating condition is not 
  # specified, a recursive function keeps calling itself again and again
  # until it runs out of stack space - not a favourable outcome! 
  tt = (100 * level) / 4.0
  fill(tt)
  ellipse(x, getHeight() / 2, radius * 2, radius * 2)
  if (level > 1):
      # 'level' decreases by 1 at every step and
      # thus makes the terminating condition attainable
    level = level - 1;  
    drawCircle(x - radius / 2, radius / 2, level)
    drawCircle(x + radius / 2, radius / 2, level)

@setup
def setup():
    createCanvas(720, 560)
    noStroke()
    noLoop()

@draw
def draw():
    print("in draw")
    drawCircle(getWidth() / 2, 280, 10)
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
           # framerate (default is 60) times a second