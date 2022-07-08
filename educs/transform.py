import pyglet

def translate(x, y, z=0):
    pyglet.gl.glTranslatef(x, y, 0)
    return

def rotate(angle):
    pyglet.gl.glRotatef(angle, 0, 0, 1)
    return

def scale(s, y=None, z=None):
    if y and z:
        pyglet.gl.glScalef(s, y, z)
    elif y:
        pyglet.gl.glScalef(s, y, s)
    elif z:
        pyglet.gl.glScalef(s, s, z)
    else:
        pyglet.gl.glScalef(s, s, s)
    return

def applyMatrix(a, b, c, d, e, f):

    # column-major order -> https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glMultMatrix.xml
    matrix = [
        a, d, 0, 0,
        b, e, 0, 0,
        c, f, 1, 0,
        0, 0, 0, 1
    ]
    pyglet.gl.glMultMatrixf(matrix)
    return

def resetMatrix():
    pyglet.gl.glLoadIdentity()
    return

def shearX(angle):
    pass

def shearY(angle):
    pass