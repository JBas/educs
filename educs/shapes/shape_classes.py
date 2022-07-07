from pyglet import shapes, gl
import numpy as np
import math

class _BorderableShapeBase:
    """Base class for Shape objects"""
    """Modified from pyglet.shapes._ShapeBase"""

    _rgb_fill = (255, 255, 255)
    _rgb_border = (255, 255, 255)
    _opacity_fill = 255
    _opacity_border = 255
    _border = 0
    _visible = True
    _x = 0
    _y = 0
    _anchor_x = 0
    _anchor_y = 0
    _batch = None
    _group = None
    _vertex_list_shape = None
    _vertex_list_border = None

    def __del__(self):
        if self._vertex_list_shape is not None:
            self._vertex_list_shape.delete()

        if self._vertex_list_border is not None:
            self._vertex_list_border.delete()

    def _update_border_position(self):
        raise NotImplementedError

    def _update_shape_position(self):
        raise NotImplementedError

    def _update_position(self):
        self._update_shape_position()

        if self._border:
            self._update_border_position()

    def _update_border_color(self):
        raise NotImplementedError

    def _update_shape_color(self):
        raise NotImplementedError

    def _update_color(self):
        self._update_shape_color()

        if self._border:
            self._update_border_color()

    def draw(self):
        self._group.set_state_recursive()
        self._vertex_list_shape.draw(gl.GL_TRIANGLES)
        self._vertex_list_border.draw(gl.GL_TRIANGLES)
        self._group.unset_state_recursive()

    def delete(self):
        if self._vertex_list_shape is not None:
            self._vertex_list_shape.delete()

        if self._vertex_list_border is not None:
            self._vertex_list_border.delete()

        self._vertex_list_shape = None
        self._vertex_list_border = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._update_position()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._update_position()

    @property
    def position(self):
        return self._x, self._y

    @position.setter
    def position(self, values):
        self._x, self._y = values
        self._update_position()

    @property
    def anchor_x(self):
        return self._anchor_x

    @anchor_x.setter
    def anchor_x(self, value):
        self._anchor_x = value
        self._update_position()

    @property
    def anchor_y(self):
        return self._anchor_y

    @anchor_y.setter
    def anchor_y(self, value):
        self._anchor_y = value
        self._update_position()

    @property
    def anchor_position(self):
        return self._anchor_x, self._anchor_y

    @anchor_position.setter
    def anchor_position(self, values):
        self._anchor_x, self._anchor_y = values
        self._update_position()

    @property
    def fill_color(self):
        return self._rgb_fill

    @property
    def border_color(self):
        return self._rgb_border

    @fill_color.setter
    def fill_color(self, values):
        self._rgb_fill = tuple(map(int, values))
        self._update_color()

    @border_color.setter
    def border_color(self, values):
        self._rgb_border = tuple(map(int, values))
        self._update_color()

    @property
    def opacity_fill(self):
        return self._opacity_fill

    @property
    def opacity_border(self):
        return self._opacity_border

    @opacity_fill.setter
    def opacity_fill(self, value):
        self._opacity_fill = value
        self._update_color()

    @opacity_border.setter
    def opacity_border(self, value):
        self._opacity_border = value
        self._update_color()

    @property
    def visible(self):
        """True if the shape will be drawn.

        :type: bool
        """
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value
        self._update_position()

class BorderableCircle(_BorderableShapeBase):

    def __init__(self, x, y, radius, border=1, segments=None,
                 fill_color=(255, 255, 255), border_color = (0, 0, 0),
                 batch=None, group=None):
        self._rgb_fill = fill_color
        self._rgb_border = border_color
        self._opacity_fill = 255
        self._opacity_border = 255
        self._visible = True
        self._x = x
        self._y = y
        self. _anchor_x = 0
        self._anchor_y = 0
        self._radius = radius
        self._border = border
        self._batch = batch
        self._group = shapes._ShapeGroup(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA, group)
        self._segments = segments or max(14, int(radius / 1.25))

        self._vertex_list_shape = None
        self._vertex_list_border = None


        # how many vertices will I need?
        N = 0
        if border:
            N = 2*(self._segments+1)
            tempv = [0, 0]*N
            tempc = [border_color[0], border_color[1], border_color[2], self._opacity_border]*N
            self._vertex_list_border = self._batch.add(N, gl.GL_TRIANGLE_STRIP, self._group,
                                                      ('v2f', tempv),
                                                      ('c4B', tempc))
            
        N = self._segments*3
        tempv = [0, 0]*N
        tempc = [fill_color[0], fill_color[1], fill_color[2], self._opacity_fill]*N
        self._vertex_list_shape = self._batch.add(N, gl.GL_TRIANGLES, self._group,
                                                    ('v2f', tempv),
                                                    ('c4B', tempc))

        self._update_position()
        self._update_color()

    def _update_shape_position(self):
        x = self._x
        y = self._y
        r = self._radius

        if self._border:
            r = r - self._border/2

        segment_arc_angle = math.pi*2 / self._segments

        points = [(x + r*math.cos(i*segment_arc_angle),
                   y + r*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        vertices = []
        for i, point in enumerate(points):
            triangle = x, y, *point, *points[i-1]
            vertices.extend(triangle)

        self._vertex_list_shape.vertices[:] = vertices

    def _update_border_position(self):
        x = self._x
        y = self._y
        r = self._radius

        b = self._border
        segment_arc_angle = math.pi*2 / self._segments

        outer_points = [(x + (r+b/2)*math.cos(i*segment_arc_angle),
                        y + (r+b/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        inner_points = [(x + (r-b/2)*math.cos(i*segment_arc_angle),
                        y + (r-b/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        vertices = [None]*(2*self._segments)
        vertices[::2] = outer_points
        vertices[1::2] = inner_points

        vertices.append(outer_points[0])
        vertices.append(inner_points[0])

        temp = np.array(vertices)
        vertices = list(temp.flatten())

        self._vertex_list_border.vertices[:] = vertices

    def _update_border_color(self):
        N = len(self._vertex_list_border.colors) // 4
        colors = [self._rgb_border[0], self._rgb_border[1], self._rgb_border[2], int(self._opacity_border)]*N
        self._vertex_list_border.colors[:] = colors

    def _update_shape_color(self):
        N = len(self._vertex_list_shape.colors) // 4
        colors = [self._rgb_fill[0], self._rgb_fill[1], self._rgb_fill[2], int(self._opacity_fill)]*N
        self._vertex_list_shape.colors[:] = colors


    def draw(self):
        self._group.set_state_recursive()
        self._vertex_list_border.draw(gl.GL_TRIANGLE_STRIP)
        self._group.unset_state_recursive()










def _rotate(vertices, angle, x, y):
    """Rotate the vertices by the angle around x, y.
    :Parameters:
        `vertices` : list
            A list of (x, y) tuples, representing each vertex to rotate.
        `angle` : float
            The angle of the rotation in degrees.
        `x` : int or float
            X coordinate of the center of rotation.
        `y` : int or float
            Y coordinate of the center of rotation.
    """
    r = -math.radians(angle)
    cr = math.cos(r)
    sr = math.sin(r)

    rotated_vertices = []
    for vertex in vertices:
        rotated_x = (vertex[0] - x) * cr - (vertex[1] - y) * sr + x
        rotated_y = (vertex[1] - y) * cr + (vertex[0] - x) * sr + y
        rotated_vertices.append((rotated_x, rotated_y))

    return rotated_vertices