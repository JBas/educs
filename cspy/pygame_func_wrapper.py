import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import math
# from lib.pygame_class_wrapper import EventManager

class EventManager:
    def __init__(self):
        pass
        
    def keyPressed(self):
        pass

    def mouseClicked(self):
        pass

    def mouseDragged(self):
        pass

class Image(pygame.Surface):
    def __init__(self):
        pass

# "private" variables
screen = None
clock = None
eventManager = EventManager()
mouseX = None
mouseY = None
mouseUp = True
width = 200
height = 200
settings_stack = []
settings = {
    "fill_color": "white",
    "no_fill": False,
    "stroke_weight": 1,
    "stroke_color": "black",
    "rotate_amnt": 0
}

# COLOR
def color(r, g, b):
    return pygame.Color(r, g, b)

def alpha(c):
    return c.a

def red(c):
    return c.r

def green(c):
    return c.g

def blue(c):
    return c.b

def brightness(c):
    return c.hsva[2]

def hue(c):
    return c.hsva[0]

def lightness(c):
    return c.hsla[2]

def saturation(c):
    return c.hsla[1]

def lerpColor(c1, c2, amnt):
    return c1.lerp(c2, amnt) 

# CONSTANTS
HALF_PI = math.pi/2.0
PI = math.pi
QUARTER_PI = math.pi/4.0
TAU = math.tau

CURSOR_ARROW = pygame.cursors.arrow
CURSOR_DIAMOND = pygame.cursors.diamond
CURSOR_BROKEN_X = pygame.cursors.broken_x
CURSOR_TRI_LEFT = pygame.cursors.tri_left
CURSOR_TRI_RIGHT = pygame.cursors.tri_right

# IMAGE
def loadImage(path):
    return pygame.image.load(path)

def image(img, x, y):
    screen.blit(img, (x, y))

# DATA

# ENVIRONMENT
def getWidth():
    return width

def getHeight():
    return height
    
def cursor(type):
    pygame.mouse.set_cursor(*type)
    pass

def noCursor():
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    pass

# EVENTS
def getMouseX():
    return mouseX

def getMouseY():
    return mouseY

# SHAPE  
def _filledShape(func, *args, **kwargs):
    if (not settings["no_fill"]):
        func(screen, settings["fill_color"], *args, **kwargs, width=0)

    if (settings["stroke_weight"] > 0):
        func(screen, settings["stroke_color"], *args, **kwargs, width=settings["stroke_weight"])
    return
    
def arc(x, y, w, h, start, stop):
    r = pygame.Rect(x-w/2, y-h/2, w, h)
    _filledShape(pygame.draw.arc, r, start, stop)
    pass

def ellipse(x, y, w, h):
    r = pygame.Rect(x-w/2, y-h/2, w, h)
    _filledShape(pygame.draw.ellipse, r)
    pass

def circle(x, y, d):
    _filledShape(pygame.draw.circle, (x, y), d/2)
    pass

def line(x1, y1, x2, y2):
    _filledShape(pygame.draw.line, (x1, y1), (x2, y2))
    pass

def point(x, y):
    _filledShape(pygame.draw.circle, (x, y), 1)
    pass

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    _filledShape(pygame.draw.polygon, ((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
    pass

def rect(x, y, w, h):
    r = pygame.Rect(x, y, w, h)
    _filledShape(pygame.draw.rect, r)
    pass

def square(x, y, s):
    r = pygame.Rect(x, y, s, s)
    _filledShape(pygame.draw.rect, r)
    pass

def triangle(x1, y1, x2, y2, x3, y3):
    _filledShape(pygame.draw.polygon, ((x1, y1), (x2, y2), (x3, y3)))
    pass

# TRANSFORM
def rotate(angle):
    global screen
    screen = pygame.transform.rotate(screen, angle)
    settings["rotate_amnt"] += angle
    pass

def createCanvas(w=100, h=100):
    global screen
    global elementManager
    global width
    global height
    
    width = w
    height = h

    screen = pygame.display.set_mode((w, h), pygame.NOFRAME)
    pass

def background(c):
    a = input2Color(c)
    screen.fill(a)
    pass

def fill(c):
    settings["fill_color"] = input2Color(c)
    settings["no_fill"] = False
    pass

def noFill():
    settings["no_fill"] = True
    pass

def stroke(c):
    settings["stroke_color"] = input2Color(c)
    pass

def strokeWeight(weight):
    if (weight == 0):
        settings["stroke_weight"] = -1
    else:
        settings["stroke_weight"] = weight
    pass

def noStroke(c):
    settings["stroke_color"] = "black"
    pass

# STRUCTURE
def push():
    global settings
    settings_stack.append(settings)
    settings = dict()
    pass

def pop():
    global settings
    settings = settings_stack.pop()
    pass

def setup(func):

    def wrapper_setup():
        global clock
        
        pygame.init()
        func()
        clock = pygame.time.Clock()
        
    return wrapper_setup

def draw(func):
    
    def wrapper_draw():
        global screen
        global clock
        global mouseX
        global mouseY
        global mouseUp

        
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    eventManager.keyPressed(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouseUp = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseUp = False
                    eventManager.mouseClicked(event)
                elif event.type == pygame.MOUSEMOTION:
                    if (not mouseUp):
                        eventManager.mouseDragged(event)
            mouseX, mouseY = pygame.mouse.get_pos()
            
            func()
            
            pygame.display.flip()
            clock.tick(60)
    return wrapper_draw

def keyPressed(func):
    def wrapped_keyPressed(event):
        eventManager.keyPressed = func
        pass
    return wrapped_keyPressed

def mouseClicked(func):
    def wrapped_mouseClicked(event):
        eventManager.mouseClicked = func
        pass
    return wrapped_mouseClicked

def mouseDragged(func):
    def wrapped_mouseDragged(event):
        eventManager.mouseDragged = func
        pass
    return wrapped_mouseDragged

def isMousedPressed():
    return not mouseUp

def input2Color(c):
    if (type(c) == int) and (0 <= c) and (255 >= c):
        return pygame.Color(c, c, c)
    elif (type(c) == str):
        return pygame.Color(c)
