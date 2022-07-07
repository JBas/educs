from __future__ import annotations
from educs.pyglet_wrapper import State
from pyglet.gl.gl import glClearColor, GLfloat

class Color:

    @staticmethod
    # def _input2Tuple(color_data: int|str|tuple[int]) -> tuple[int]:
    def _input2Tuple(*args) -> tuple[int]:

        if len(args) == 4: # RGBA

            r: int = args[0]
            g: int = args[1]
            b: int = args[2]
            a: float = args[3]
            return (r, g, b, a)

        elif len(args) == 3: # RGB

            r: int = args[0]
            g: int = args[1]
            b: int = args[2]
            return (r, g, b)

        elif len(args) == 1:

            color_data = args[0]

            if type(color_data) == int:

                if color_data >= 0 and color_data <= 255:
                    return (color_data, color_data, color_data)
                else:
                    return None

            elif type(color_data) == str:

                if color_data[0] == '#':

                    if len(color_data[1:]) == 3:
                        # 3 digit hex rgb notation
                        r = int(color_data[1], 16)
                        g = int(color_data[2], 16)
                        b = int(color_data[3], 16)
                        return (r, g, b)

                    elif len(color_data[1:]) == 6:
                        # 6 digit hex rgb notation
                        r = int(color_data[1:3], 16)
                        g = int(color_data[3:5], 16)
                        b = int(color_data[5:7], 16)
                        return (r, g, b)

                    else:
                        return None

                else:
                    # CSS color names
                    pass

            elif type(color_data) == tuple:

                return color_data
            else:
                return None
        
        else:
            return None

    @staticmethod
    def _isValid(c: int) -> bool:
        return not (c < 0 or c > 255)

    def __init__(self, color_data: int|str|tuple[int]):

        self._r: int = 255
        self._g: int = 255
        self._b: int = 255
        self._a: float = 1.0   

        return
    
    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    @property
    def a(self):
        return self._a

    def hue(self) -> float:
        x: float = self._r / 255.0

        cmax:float = max(self._r, self._g, self._b)
        cmin:float = min(self._r, self._g, self._b)
        diff:float = cmax - cmin

        if cmax == 0 and cmin == 0:
            return 0
        elif cmax == self._r:
            return ((60*(self._g - self._b) / diff) + 360) % 360
        elif cmax == self._g:
            return ((60*(self._b - self._r) / diff) + 120) % 360
        elif cmax == self._b:
            return ((60*(self._r - self._g) / diff) + 240) % 360
        else:
            print("Error in hue calculation!")
            return -1

    def saturation(self) -> float:
        cmax:float = max(self._r, self._g, self._b)
        cmin:float = min(self._r, self._g, self._b)
        diff:float = cmax - cmin

        if cmax == 0:
            return 0
        else:
            return (diff / cmax)*100

    def value(self) -> float:
        cmax:float = max(self._r, self._g, self._b)
        return cmax*100





def alpha(color: Color) -> int:
    return color.a

def blue(color: Color) -> int:
    return color.b

def value(color: Color) -> float:
    return color.value()

def green(color: Color) -> int:
    return color.g

def hue(color: Color) -> float:
    return color.hue()

def red(color: Color) -> int:
    return color.r

def saturation(color: Color) -> float:
    return color.saturation()

def background(color: tuple|Color) -> None:

    # https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearColor.xhtml
    r: GLfloat = color[0] / 255
    g: GLfloat = color[1] / 255
    b: GLfloat = color[2] / 255
    glClearColor(r, g, b, 1.0)
    return

def clear() -> None:
    State.window.clear()
    return

def fill(color: tuple|Color) -> None:
    State.settings["fill_color"] = _input2Color((r, g, b))
    State.settings["no_fill"] = False
    pass

if __name__=="__main__":
    color_tuple = Color((255, 255, 255))

