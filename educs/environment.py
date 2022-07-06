from __future__ import annotations
from educs.pyglet_wrapper import State
import pyglet

def frameCount():
    return State.framecount

def frameRate(fps: float):
    State.framerate = fps

    pyglet.clock.unschedule(State.wrapper_draw)
    pyglet.clock.schedule_interval(State.wrapper_draw, 1 / fps)

    return