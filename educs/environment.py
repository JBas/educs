from __future__ import annotations
from educs.structure import State
import pyglet

def frameCount() -> int:
    return State.framecount

def frameRate(fps: float) -> None:
    State.framerate = fps

    pyglet.clock.unschedule(State.wrapper_draw)
    pyglet.clock.schedule_interval(State.wrapper_draw, 1 / fps)

    return

def noCursor() -> None:
    State.window.set_mouse_visible(False)
    return

def cursor(cursor_type: str, x: int = None, y: int = None) -> None:
    State.windowset_mouse_cursor(cursor=cursor_type)
    return

def fullscreen(val: bool = None) -> bool:

    if val != None:
        State.window.set_fullscreen(val)
        return
    else:
        return State.window.fullscreen

