from __future__ import annotations

import pyglet


class State:
    # "private" variables
    width: int = 0
    height: int = 0
    framerate: int = 60
    batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
    batch_list = []
    window: pyglet.window.Window = pyglet.window.Window()
    settings_stack = []
    settings = {
        "fill_color": (255, 0, 255),
        "no_fill": False,
        "stroke_weight": 1,
        "stroke_color": (0, 0, 0),
        "rotate_deg": 0
    }
    pass


# STRUCTURE
def setup(func: function) -> function:

    @pyglet.app.event_loop.event
    def on_enter():
        # preload and any initialization
        func()
        return

    return on_enter


def draw(func: function) -> function:

    @State.window.event
    def on_draw():
        func()
        return

    return on_draw

