from __future__ import annotations
from pyglet import shapes
from educs.structure import State
from educs.shapes.shape_classes import BorderableCircle, BorderableEllipse, BorderableTriangle


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


def circle(x: float, y: float, d: float, border: int = 0,
           border_color: tuple[int] = (255, 255, 255), fill_color: tuple[int] = (255, 255, 255)) -> BorderableCircle :
    shape = BorderableCircle(x, y, d/2, border=border, border_color=border_color, fill_color=fill_color, batch=State.batch)
    State.batch_list.append(shape)
    return shape

def ellipse(x: float, y: float, width: float, height: float, border: int = 0,
           border_color: tuple[int] = (255, 255, 255), fill_color: tuple[int] = (255, 255, 255)) -> BorderableEllipse :
    shape = BorderableEllipse(x, y, width, height, border=border, border_color=border_color, fill_color=fill_color, batch=State.batch)
    State.batch_list.append(shape)
    return shape

def triangle(x1: float, y1: float,
             x2: float, y2: float,
             x3: float, y3: float,
             border: int = 0,
             border_color: tuple[int] = (255, 255, 255),
             fill_color: tuple[int] = (255, 255, 255)) -> BorderableTriangle :
    shape = BorderableTriangle(x1, y1, x2, y2, x3, y3, border=border, border_color=border_color, fill_color=fill_color, batch=State.batch)
    State.batch_list.append(shape)
    return shape

def point(x: float, y: float) -> BorderableCircle :
    shape = shapes.Circle(x, y, 1, color=(255, 255, 255), batch=State.batch)
    State.batch_list.append(shape)
    return shape