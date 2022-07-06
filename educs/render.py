from educs.pyglet_wrapper import State

def createCanvas(w: int = 400, h: int = 400) -> None:
    State.width = w
    State.height = h
    

    State.window.set_size(w, h)
    return