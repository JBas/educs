from __future__ import annotations
import time

import pyglet
from enum import Enum, auto

from educs import ROUND

class ModeConstant(Enum):
    CENTER  = auto()
    RADIUS  = auto()
    CORNER  = auto()
    CORNERS = auto()
    DEGREES = auto()
    RADIANS = auto()

class State:
    # "private" variables
    width: int = 0
    height: int = 0
    framerate: float = 60.0
    framecount: int = 0
    batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
    batch_list = []
    window: pyglet.window.Window = None
    start_time = -1
    settings_stack = []
    settings = {
        "fill_color": (255, 0, 255),
        "no_fill": False,
        "stroke_weight": 1,
        "stroke_color": (0, 0, 0),
        "stroke_join": ROUND,
        "stroke_cap": ROUND
    }
    ellipseModeConstant = ModeConstant.CENTER
    rectModeConstant = ModeConstant.CORNER
    wrapper_draw: function = None
    pass


def setup(func: function) -> function:

    @pyglet.app.event_loop.event
    def on_enter():
        State.start_time = time.time_ns()*1000000 # nanoseconds to milliseconds
        # preload and any initialization
        func()
        return

    return on_enter

def draw(func: function) -> function:

    def wrapper_draw(dt):
        func()

        State.framecount += 1
        return

    pyglet.clock.schedule_interval(wrapper_draw, 1 / State.framerate)
    State.wrapper_draw = wrapper_draw # keeping on hand in case i need to change framerate

    return wrapper_draw

def run():
    pyglet.app.run()
    return

def push():
    pyglet.gl.glPushMatrix()
    pass

def pop():
    pyglet.gl.glPopMatrix()
    pass

