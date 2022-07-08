from curses import wrapper
from educs.structure import State
from pyglet import window

def createCanvas(w: int = 400, h: int = 400, fullscreen=False, resizable=True) -> None:
    State.width = w
    State.height = h
    

    State.window = window.Window(width=w, height=h, fullscreen=fullscreen, resizable=resizable)

    # setup window event
    # @State.window.event
    # def on_draw():
    #     State.window.clear()
    #     State.batch.draw()

    if State.wrapper_key_pressed:
        State.window.on_key_press = State.wrapper_key_pressed

    if State.wrapper_key_released:
        State.window.on_key_release = State.wrapper_key_released

    if State.wrapper_key_typed:
        State.window.on_text = State.wrapper_key_typed
    return

def resizeCanvas(w: int = 400, h: int = 400, fullscreen=False, resizable=True) -> None:
    if State.window:
        State.width = w
        State.height = h
        

        State.window.set_size(w, h)

    # setup window event
    # @State.window.event
    # def on_draw():
    #     State.window.clear()
    #     State.batch.draw()
    return