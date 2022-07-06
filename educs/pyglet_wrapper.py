from __future__ import annotations

import pyglet
from window import Window

# "private" variables
width: int = 0
height: int = 0
framerate: int = 60
batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
window: Window = Window(batch)

# RENDERING
def createCanvas(w: int = 400, h: int = 400) -> None:
    global width
    global height
    global window
    
    width = w
    height = h

    window.set_size(w, h)
    return


# STRUCTURE
def setup(func: function) -> function:

    @pyglet.app.event_loop.event
    def on_enter():
        # preload and any initialization
        func()
        return

    return on_enter


def draw(func: function) -> function:

    @window.event
    def on_draw():
        func()
        return

    return on_draw










if __name__=="__main__":

    @setup
    def my_setup():
        print("in setup")
        createCanvas()
        return

    @draw
    def my_draw():
        print("in draw")
        return

    pyglet.app.run()

