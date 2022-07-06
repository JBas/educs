from __future__ import annotations
from ctypes import resize

import pyglet


class State:
    # "private" variables
    width: int = 0
    height: int = 0
    framerate: float = 60.0
    batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
    batch_list = []
    window: pyglet.window.Window = pyglet.window.Window(resizable=True)
    settings_stack = []
    settings = {
        "fill_color": (255, 0, 255),
        "no_fill": False,
        "stroke_weight": 1,
        "stroke_color": (0, 0, 0),
        "rotate_deg": 0
    }
    wrapper_draw: function = None
    pass


def setup(func: function) -> function:

    @pyglet.app.event_loop.event
    def on_enter():
        # preload and any initialization
        func()
        return

    return on_enter

@State.window.event
def on_draw():
    State.window.clear()
    State.batch.draw()


def draw(func: function) -> function:

    def wrapper_draw(dt):
        func()
        return

    pyglet.clock.schedule_interval(wrapper_draw, 1 / State.framerate)
    State.wrapper_draw = wrapper_draw # keeping on hand in case i need to change framerate

    return wrapper_draw

def run():
    pyglet.app.run()
    return

