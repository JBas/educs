from __future__ import annotations
from pyglet import shapes
from educs.pyglet_wrapper import State


def moveX(obj, x: int = None):
    if obj and x:
        try:
            obj.x = x
        except:
            print(f"This object {obj} has no member x!")

def moveY(obj, y: int = None):
    if obj and y:
        try:
            obj.y = y
        except:
            print(f"This object {obj} has no member y!")

def movePos(obj, position: tuple = None):
    if obj and position:
        try:
            obj.position = position
        except:
            print(f"This object {obj} has no member position!")





class BorderableShape(shapes._ShapeBase):

    def __init__(self, *args, **kwargs):
        pass


def circle(x: float, y: float, d: float) -> shapes.Circle :
    shape = shapes.Circle(x, y, d/2, color=(255, 255, 255), batch=State.batch)
    State.batch_list.append(shape)
    return shape

def point(x: float, y: float) -> shapes.Circle :
    shape = shapes.Circle(x, y, 1, color=(255, 255, 255), batch=State.batch)
    State.batch_list.append(shape)
    return shape