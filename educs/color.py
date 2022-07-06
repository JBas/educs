from __future__ import annotations

class Color:

    @staticmethod
    def _isValid(c: int) -> bool:
        return not (c < 0 or c > 255)

    def __init__(self, *args, **kwargs):

        self._r: int = 255
        self._g: int = 255
        self._b: int = 255
        self._a: int = 255

        if type(args[0]) == tuple and len(args[0]) < 5:

            rgb = args[0]
            if Color._isValid(rgb[0]):
                self._r = rgb[0]

            if Color._isValid(rgb[1]):
                self._g = rgb[1]

            if Color._isValid(rgb[2]):
                self._b = rgb[2]

            if len(args[0]) == 4:
             if Color._isValid(rgb[3]):
                self._a = rgb[3]    

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

if __name__=="__main__":
    color_tuple = Color((255, 255, 255))

