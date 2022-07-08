from __future__ import annotations

from pyglet import shapes, graphics, gl
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
    _width = 0
    _height = 0
    _anchor_x = 0
    _anchor_y = 0
    _rotation = 0
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
        self._group.set_state_recursive()  # type: ignore
        self._vertex_list_shape.draw(gl.GL_TRIANGLES) # type: ignore
        self._vertex_list_border.draw(gl.GL_TRIANGLES) # type: ignore
        self._group.unset_state_recursive() # type: ignore

    def delete(self):
        if self._vertex_list_shape is not None:
            self._vertex_list_shape.delete()

        if self._vertex_list_border is not None:
            self._vertex_list_border.delete()

        self._vertex_list_shape = None
        self._vertex_list_border = None

    @staticmethod
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
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._update_position()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._update_position()

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value
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

    def __init__(self, x: float|int, y: float|int, radius: float|int, border: int = 1, segments: int = None,
                 fill_color: tuple[int, int, int] = (255, 255, 255),
                 border_color: tuple[int, int, int] = (0, 0, 0),
                 batch: graphics.Batch = None,
                 group: graphics.Group = None):
        self._rgb_fill = fill_color
        self._rgb_border = border_color
        self._opacity_fill = 255
        self._opacity_border = 255
        self._visible = True
        self._x = x
        self._y = y
        self._width = 2*radius
        self._height = 2*radius
        self._anchor_x = 0
        self._anchor_y = 0
        self._radius = radius
        self._border = border
        self._batch = batch or graphics.Batch()
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
        x = self._x + self._anchor_x
        y = self._y + self._anchor_y
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
        x = self._x + self._anchor_x
        y = self._y + self._anchor_y
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
        self._vertex_list_shape.draw(gl.GL_TRIANGLES)
        self._vertex_list_border.draw(gl.GL_TRIANGLE_STRIP)
        self._group.unset_state_recursive()

class BorderableEllipse(_BorderableShapeBase):

    def __init__(self, x: float|int, y: float|int, width: float|int, height: float|int,
                 border: int = 1, segments: int = None,
                 fill_color: tuple[int, int, int] = (255, 255, 255),
                 border_color: tuple[int, int, int] = (0, 0, 0),
                 batch: graphics.Batch = None,
                 group: graphics.Group = None):
        self._rgb_fill = fill_color
        self._rgb_border = border_color
        self._opacity_fill = 255
        self._opacity_border = 255
        self._visible = True
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._a = width / 2
        self._b = height / 2
        self._anchor_x = 0
        self._anchor_y = 0
        self._border = border
        self._batch = batch
        self._group = shapes._ShapeGroup(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA, group)
        self._segments = segments or int(max(self._a, self._b) / 1.25)

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
        x = self._x + self._anchor_x
        y = self._y + self._anchor_y
        a = self._a
        b = self._b

        if self._border:
            a = a - self._border/2
            b = b - self._border/2

        segment_arc_angle = math.pi*2 / self._segments

        points = [(x + a*math.cos(i*segment_arc_angle),
                   y + b*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        if self._rotation:
            points = _BorderableShapeBase._rotate(points, self._rotation, self._x, self._y)

        vertices = []
        for i, point in enumerate(points):
            triangle = x, y, *point, *points[i-1]
            vertices.extend(triangle)

        self._vertex_list_shape.vertices[:] = vertices

    def _update_border_position(self):
        x = self._x + self._anchor_x
        y = self._y + self._anchor_y
        a = self._a
        b = self._b

        bd = self._border
        segment_arc_angle = math.pi*2 / self._segments

        outer_points = [(x + (a+bd/2)*math.cos(i*segment_arc_angle),
                   y + (b+bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        inner_points = [(x + (a-bd/2)*math.cos(i*segment_arc_angle),
                   y + (b-bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        vertices = [None]*(2*self._segments)
        vertices[::2] = outer_points
        vertices[1::2] = inner_points

        vertices.append(outer_points[0])
        vertices.append(inner_points[0])

        if self._rotation:
            vertices = _BorderableShapeBase._rotate(vertices, self._rotation, self._x, self._y)

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
        self._vertex_list_shape.draw(gl.GL_TRIANGLES)
        self._vertex_list_border.draw(gl.GL_TRIANGLE_STRIP)
        self._group.unset_state_recursive()

class BorderableTriangle(_BorderableShapeBase):

    def __init__(self, x1: float|int, y1: float|int,
                 x2: float|int, y2: float|int,
                 x3: float|int, y3: float|int,
                 border: int = 1,
                 fill_color: tuple[int, int, int] = (255, 255, 255),
                 border_color: tuple[int, int, int] = (0, 0, 0),
                 batch: graphics.Batch = None,
                 group: graphics.Group = None):
        self._rgb_fill = fill_color
        self._rgb_border = border_color
        self._opacity_fill = 255
        self._opacity_border = 255
        self._visible = True
        self._x = x1
        self._y = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3
        self._anchor_x = 0
        self._anchor_y = 0
        self._border = border
        self._batch = batch
        self._group = shapes._ShapeGroup(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA, group)

        self._vertex_list_shape = None
        self._vertex_list_border = None


        # how many vertices will I need?
        # N = 0
        # if border:
        #     N = 2*(self._segments+1)
        #     tempv = [0, 0]*N
        #     tempc = [border_color[0], border_color[1], border_color[2], self._opacity_border]*N
        #     self._vertex_list_border = self._batch.add(N, gl.GL_TRIANGLE_STRIP, self._group,
        #                                               ('v2f', tempv),
        #                                               ('c4B', tempc))
            
        tempv = [0, 0]*3
        tempc = [fill_color[0], fill_color[1], fill_color[2], self._opacity_fill]*3
        self._vertex_list_shape = self._batch.add(3, gl.GL_TRIANGLES, self._group,
                                                    ('v2f', tempv),
                                                    ('c4B', tempc))

        self._update_shape_position()
        self._update_shape_color()

    def _update_shape_position(self):
        x1 = self._x + self._anchor_x
        y1 = self._y + self._anchor_y
        x2 = self._x2 + self._anchor_x
        y2 = self._y2 + self._anchor_y
        x3 = self._x3 + self._anchor_x
        y3 = self._y3 + self._anchor_y

        # if self._border:
        #     a = a - self._border/2
        #     b = b - self._border/2

        points = [(x1, y1), (x2, y2), (x3, y3)]

        if self._rotation:
            points = _BorderableShapeBase._rotate(points, self._rotation, self._x, self._y)

        temp = np.array(points)
        vertices = list(temp.flatten())

        self._vertex_list_shape.vertices[:] = vertices

    def _update_border_position(self):
        x = self._x + self._anchor_x
        y = self._y + self._anchor_y
        a = self._a
        b = self._b

        bd = self._border
        segment_arc_angle = math.pi*2 / self._segments

        outer_points = [(x + (a+bd/2)*math.cos(i*segment_arc_angle),
                   y + (b+bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        inner_points = [(x + (a-bd/2)*math.cos(i*segment_arc_angle),
                   y + (b-bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        vertices = [None]*(2*self._segments)
        vertices[::2] = outer_points
        vertices[1::2] = inner_points

        vertices.append(outer_points[0])
        vertices.append(inner_points[0])

        if self._rotation:
            vertices = _BorderableShapeBase._rotate(vertices, self._rotation, self._x, self._y)

        temp = np.array(vertices)
        vertices = list(temp.flatten())

        self._vertex_list_border.vertices[:] = vertices

    def _update_border_color(self):
        N = len(self._vertex_list_border.colors) // 4
        colors = [self._rgb_border[0], self._rgb_border[1], self._rgb_border[2], int(self._opacity_border)]*N
        self._vertex_list_border.colors[:] = colors

    def _update_shape_color(self):
        colors = [self._rgb_fill[0], self._rgb_fill[1], self._rgb_fill[2], int(self._opacity_fill)]*3
        self._vertex_list_shape.colors[:] = colors


    def draw(self):
        self._group.set_state_recursive()
        self._vertex_list_shape.draw(gl.GL_TRIANGLES)
        self._vertex_list_border.draw(gl.GL_TRIANGLE_STRIP)
        self._group.unset_state_recursive()

class BorderableRectangle(_BorderableShapeBase):

    def __init__(self, x: float|int, y: float|int,
                 width: float|int, height: float|int,
                 border: int = 1,
                 fill_color: tuple[int, int, int] = (255, 255, 255),
                 border_color: tuple[int, int, int] = (0, 0, 0),
                 batch: graphics.Batch = None,
                 group: graphics.Group = None):
        self._rgb_fill = fill_color
        self._rgb_border = border_color
        self._opacity_fill = 255
        self._opacity_border = 255
        self._visible = True
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._anchor_x = 0
        self._anchor_y = 0
        self._border = border
        self._batch = batch
        self._group = shapes._ShapeGroup(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA, group)

        self._vertex_list_shape = None
        self._vertex_list_border = None


        # how many vertices will I need?
        # N = 0
        # if border:
        #     N = 2*(self._segments+1)
        #     tempv = [0, 0]*N
        #     tempc = [border_color[0], border_color[1], border_color[2], self._opacity_border]*N
        #     self._vertex_list_border = self._batch.add(N, gl.GL_TRIANGLE_STRIP, self._group,
        #                                               ('v2f', tempv),
        #                                               ('c4B', tempc))
            
        tempv = [0, 0]*6
        tempc = [fill_color[0], fill_color[1], fill_color[2], self._opacity_fill]*6
        self._vertex_list_shape = self._batch.add(6, gl.GL_TRIANGLES, self._group,
                                                    ('v2f', tempv),
                                                    ('c4B', tempc))

        self._update_shape_position()
        self._update_shape_color()

    def _update_shape_position(self):
        x1 = self._x + self._anchor_x
        y1 = self._y + self._anchor_y
        x2 = self._x + self._width + self._anchor_x
        y2 = self._y + self._height + self._anchor_y

        # if self._border:
        #     a = a - self._border/2
        #     b = b - self._border/2

        points = [(x1, y1), (x1, y2), (x2, y2), (x1, y1), (x2, y1), (x2, y2)]

        if self._rotation:
            points = _BorderableShapeBase._rotate(points, self._rotation, self._x, self._y)

        temp = np.array(points)
        vertices = list(temp.flatten())

        self._vertex_list_shape.vertices[:] = vertices

    def _update_border_position(self):
        x = self._x + self._anchor_x
        y = self._y + self._anchor_y
        a = self._a
        b = self._b

        bd = self._border
        segment_arc_angle = math.pi*2 / self._segments

        outer_points = [(x + (a+bd/2)*math.cos(i*segment_arc_angle),
                   y + (b+bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        inner_points = [(x + (a-bd/2)*math.cos(i*segment_arc_angle),
                   y + (b-bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        vertices = [None]*(2*self._segments)
        vertices[::2] = outer_points
        vertices[1::2] = inner_points

        vertices.append(outer_points[0])
        vertices.append(inner_points[0])

        if self._rotation:
            vertices = _BorderableShapeBase._rotate(vertices, self._rotation, self._x, self._y)

        temp = np.array(vertices)
        vertices = list(temp.flatten())

        self._vertex_list_border.vertices[:] = vertices

    def _update_border_color(self):
        N = len(self._vertex_list_border.colors) // 4
        colors = [self._rgb_border[0], self._rgb_border[1], self._rgb_border[2], int(self._opacity_border)]*N
        self._vertex_list_border.colors[:] = colors

    def _update_shape_color(self):
        colors = [self._rgb_fill[0], self._rgb_fill[1], self._rgb_fill[2], int(self._opacity_fill)]*6
        self._vertex_list_shape.colors[:] = colors


    def draw(self):
        self._group.set_state_recursive()
        self._vertex_list_shape.draw(gl.GL_TRIANGLES)
        # self._vertex_list_border.draw(gl.GL_TRIANGLE_STRIP)
        self._group.unset_state_recursive()

class BorderableQuadrilateral(_BorderableShapeBase):

    def __init__(self, x: float|int, y: float|int,
                 x2: float|int, y2: float|int,
                 x3: float|int, y3: float|int,
                 x4: float|int, y4: float|int,
                 border: int = 1,
                 fill_color: tuple[int, int, int] = (255, 255, 255),
                 border_color: tuple[int, int, int] = (0, 0, 0),
                 batch: graphics.Batch = None,
                 group: graphics.Group = None):
        self._rgb_fill = fill_color
        self._rgb_border = border_color
        self._opacity_fill = 255
        self._opacity_border = 255
        self._visible = True
        self._x = x # coordinate points are counter-clockwise
        self._y = y
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3
        self._x4 = x4
        self._y4 = y4
        self._anchor_x = 0
        self._anchor_y = 0
        self._border = border
        self._batch = batch
        self._group = shapes._ShapeGroup(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA, group)

        self._vertex_list_shape = None
        self._vertex_list_border = None


        # how many vertices will I need?
        # N = 0
        # if border:
        #     N = 2*(self._segments+1)
        #     tempv = [0, 0]*N
        #     tempc = [border_color[0], border_color[1], border_color[2], self._opacity_border]*N
        #     self._vertex_list_border = self._batch.add(N, gl.GL_TRIANGLE_STRIP, self._group,
        #                                               ('v2f', tempv),
        #                                               ('c4B', tempc))
            
        tempv = [0, 0]*4
        tempc = [fill_color[0], fill_color[1], fill_color[2], self._opacity_fill]*4
        self._vertex_list_shape = self._batch.add(4, gl.GL_TRIANGLE_STRIP, self._group,
                                                    ('v2f', tempv),
                                                    ('c4B', tempc))

        self._update_shape_position()
        self._update_shape_color()

    def _update_shape_position(self):
        x1 = self._x + self._anchor_x
        y1 = self._y + self._anchor_y
        x2 = self._x2 + self._anchor_x
        y2 = self._y2 + self._anchor_y
        x3 = self._x3 + self._anchor_x
        y3 = self._y3 + self._anchor_y
        x4 = self._x4 + self._anchor_x
        y4 = self._y4 + self._anchor_y

        # if self._border:
        #     a = a - self._border/2
        #     b = b - self._border/2

        points = [(x1, y1), (x2, y2), (x4, y4), (x3, y3)]

        if self._rotation:
            points = _BorderableShapeBase._rotate(points, self._rotation, self._x, self._y)

        temp = np.array(points)
        vertices = list(temp.flatten())

        self._vertex_list_shape.vertices[:] = vertices

    def _update_border_position(self):
        x = self._x + self._anchor_x
        y = self._y + self._anchor_y
        a = self._a
        b = self._b

        bd = self._border
        segment_arc_angle = math.pi*2 / self._segments

        outer_points = [(x + (a+bd/2)*math.cos(i*segment_arc_angle),
                   y + (b+bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        inner_points = [(x + (a-bd/2)*math.cos(i*segment_arc_angle),
                   y + (b-bd/2)*math.sin(i*segment_arc_angle)) for i in range(self._segments)]

        vertices = [None]*(2*self._segments)
        vertices[::2] = outer_points
        vertices[1::2] = inner_points

        vertices.append(outer_points[0])
        vertices.append(inner_points[0])

        if self._rotation:
            vertices = _BorderableShapeBase._rotate(vertices, self._rotation, self._x, self._y)

        temp = np.array(vertices)
        vertices = list(temp.flatten())

        self._vertex_list_border.vertices[:] = vertices

    def _update_border_color(self):
        N = len(self._vertex_list_border.colors) // 4
        colors = [self._rgb_border[0], self._rgb_border[1], self._rgb_border[2], int(self._opacity_border)]*N
        self._vertex_list_border.colors[:] = colors

    def _update_shape_color(self):
        colors = [self._rgb_fill[0], self._rgb_fill[1], self._rgb_fill[2], int(self._opacity_fill)]*4
        self._vertex_list_shape.colors[:] = colors


    def draw(self):
        self._group.set_state_recursive()
        self._vertex_list_shape.draw(gl.GL_TRIANGLE_STRIP)
        # self._vertex_list_border.draw(gl.GL_TRIANGLE_STRIP)
        self._group.unset_state_recursive()