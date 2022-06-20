from pygame import Color

def _input2Color(c):
    if (type(c) == int) and (0 <= c) and (255 >= c):
        return Color(c, c, c)
    elif (type(c) == float) and (0 <= c) and (255 >= c):
        return Color(int(c), int(c), int(c))
    elif (type(c) == str):
        return Color(c)
    elif (type(c) == tuple):
        return Color(c)

# COLOR
def color(r, g, b):
    return Color(r, g, b)

def alpha(c):
    return c.a

def red(c):
    return c.r

def green(c):
    return c.g

def blue(c):
    return c.b

def brightness(c):
    return c.hsva[2]

def hue(c):
    return c.hsva[0]

def lightness(c):
    return c.hsla[2]

def saturation(c):
    return c.hsla[1]

def lerpColor(c1, c2, amnt):
    return c1.lerp(c2, amnt)