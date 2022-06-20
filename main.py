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
    createCanvas(720, 400);
    background(0);
    noStroke();
    
    fill(204);
    triangle(18, 18, 18, 360, 81, 360);
    
    fill(102);
    rect(81, 81, 63, 63);
    
    fill(204);
    quad(189, 18, 216, 18, 216, 360, 144, 360);
    
    fill(255);
    ellipse(252, 144, 72, 72);
    
    fill(204);
    triangle(288, 18, 351, 360, 288, 360);
    
    # fill(255);
    # arc(479, 300, 280, 280, PI, TWO_PI);
    pass

@draw
def draw():
    pass


if __name__=="__main__":
    onMouseDragged(None) # registers your onMouseDragged function
    onKeyPressed(None) # registers your onKeyPress function
    onMouseClicked(None) # registers your onMouseClick function
    setup() # sets up the window
    draw() # starts running your draw function 60 times a second