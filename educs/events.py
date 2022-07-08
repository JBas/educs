from educs.structure import State


def keyPressed(func):

    def wrapper_key_pressed(symbol, modifiers):
        func()
        return

    State.wrapper_key_pressed = wrapper_key_pressed

    return func

def keyReleased(func):

    def wrapper_key_released(symbol, modifiers):
        func()
        return

    State.wrapper_key_released = wrapper_key_released

    return func

def keyTyped(func):

    def wrapper_key_typed(text):
        func(text)
        return

    State.wrapper_key_typed = wrapper_key_typed

    return func