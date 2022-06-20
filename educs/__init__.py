from educs.pygame_wrapper import (setup, draw, createCanvas, background, fill, noFill, line, ellipse, circle, rect, quad, arc, triangle, push, pop, getMouseX, getMouseY, getWidth, getHeight, cursor, strokeWeight, stroke, noStroke, loadImage, image, keyPressed, mouseClicked, mouseDragged, isMousedPressed, Image, frameRate, random, constrain, floor, ceil)

from educs.color import (color, alpha,
                        red, green, blue, brightness,
                        hue, lightness, saturation, lerpColor)

from educs.constants import (TWO_PI, HALF_PI, PI, QUARTER_PI, TAU, CURSOR_ARROW, CURSOR_DIAMOND, CURSOR_BROKEN_X, CURSOR_TRI_LEFT, CURSOR_TRI_RIGHT)

__all__ = ["setup", "draw", "createCanvas", "background", "fill", "noFill", "line", "ellipse", "circle", "rect", "triangle", "quad", "arc", "push", "pop", "getMouseX", "getMouseY", "getWidth", "getHeight", "cursor", "TWO_PI", "HALF_PI", "PI", "QUARTER_PI", "TAU", "CURSOR_ARROW", "CURSOR_DIAMOND", "CURSOR_BROKEN_X", "CURSOR_TRI_LEFT", "CURSOR_TRI_RIGHT", "strokeWeight", "stroke", "noStroke", "loadImage", "image", "keyPressed", "mouseClicked", "mouseDragged", "isMousedPressed", "Image", "frameRate", "random", "constrain", "floor", "ceil"]

__version__ = "0.0.1"

print("Thank you for using educs!\n")