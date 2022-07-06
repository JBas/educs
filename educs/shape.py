from __future__ import annotations
from turtle import color
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

# def _filledArc(r, start, stop):
#     # arc_image = np.zeros((r.height, r.width, 3), dtype = np.uint8)
#     # cf = settings["fill_color"]
#     # cv.ellipse(arc_image, r.center, (r.height, r.width), 0, math.degrees(start), math.degrees(stop), 0)

#     # img = pygame.image.frombuffer(arc_image, r.size, "RGB")
#     # print("hello")
#     # backgroundSurf.blit(img, img.get_rect(center=r.center))
#     # return
#     pass
    
# def arc(x, y, w, h, start, stop):
#     r = pygame.Rect(x-w/2, y-h/2, w, h)
#     _filledArc(r, start, stop)
#     pass

# def ellipse(x: int | float, y: int | float, w: int | float, h: int | float=None):
#     if not h:
#         h = w

#     Ellipse(x, y, a, b, color=(255, 255, 255), batch=None, group=None)
    
#     r = pygame.Rect(x-w/2, y-h/2, w, h)
#     _filledShape(pygame.draw.ellipse, r)
#     pass

def circle(x: float, y: float, d: float) -> shapes.Circle :
    shape = shapes.Circle(x, y, d/2, color=(255, 255, 255), batch=State.batch)
    State.batch_list.append(shape)
    return shape

# def line(x1, y1, x2, y2):
#     if (backgroundSurf):
#         pygame.draw.line(backgroundSurf, settings["stroke_color"], (x1, y1), (x2, y2), width=1)
#     pass

# def point(x, y):
#     _filledShape(pygame.draw.circle, (x, y), 1)
#     pass

# def quad(x1, y1, x2, y2, x3, y3, x4, y4):
#     _filledShape(pygame.draw.polygon, ((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
#     pass

# def rect(x, y, w, h):
#     r = pygame.Rect(x, y, w, h)
#     _filledShape(pygame.draw.rect, r)
#     pass

# def square(x, y, s):
#     r = pygame.Rect(x, y, s, s)
#     _filledShape(pygame.draw.rect, r)
#     pass

# def triangle(x1, y1, x2, y2, x3, y3):
#     _filledShape(pygame.draw.polygon, ((x1, y1), (x2, y2), (x3, y3)))
#     pass