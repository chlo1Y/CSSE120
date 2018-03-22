"""
rosegraphics.py - a simple Graphics library for Python.
Its key feature is:
  -- USING this library provides a simple introduction to USING objects.

Other key features include:
  -- It is a simple graphics library that allows one to:
        -- Construct objects like circles, lines, etc. on windows
        -- Apply methods like move_by, spin
        -- Access fields like a point's x and y coordinates.
  -- It is built on top of tkinter
        (the standard graphics library that comes with Python)
  -- Unlike tkinter, it is NOT event-driven
        (and hence can be used before students see that paradigm).
  -- It was inspired by zellegraphics, but is a complete
        re-implementation that is designed to be more bullet-proof
        for beginners than zellegraphics is.
  -- While it can serve as an example for defining classes,
        it is NOT intended to do so for beginners.
        It is excellent for helping students learn to USE objects;
        it is NOT perfect for helping students learn to WRITE CLASSES.

A typical use of rosegraphics.py might be something like:
   TODO: Give a simple example, showing attach and render.

Authors: David Mutchler, Mark Hays, Michael Wollowswki, Matt Boutell,
         Chandan Rupakheti, Claude Anderson and their colleagues,
         with thanks to John Zelle for inspiration and hints.
         First completed version: September 2014.
"""

import tkinter
import time

# CONSIDER: Maybe add curve (various kinds), path, area, and ??
# See Java's _Shape.

# ----------------------------------------------------------------------
# All the windows that are constructed during a run share the single
#    _master_Tk   (a tkinter.Tk object)
# as their common root.  The first construction of a RoseWindow
# sets this  _master_Tk to a Tkinter.Tk object.
# ----------------------------------------------------------------------
_master_Tk = None


# ----------------------------------------------------------------------
# RoseWindow is the top-level object.
# It starts with a single RoseCanvas.
# ----------------------------------------------------------------------
class RoseWindow():
    """
    A RoseWindow is a "window" that pops up when constructed.
    It starts with a RoseCanvas upon which one can draw shapes.
    One can add other widgets (FortuneTeller, ttk.Button, etc) to it.
    """

    def __init__(self, width=400, height=300, title='Rose Graphics',
                 window_color='black', canvas_color=None,
                 make_initial_canvas=True):
        """
        Constructs a Window with a RoseCanvas on it.

        The optional (keyword) arguments:
          -- height, width, title, window_color, canvas_color.
        are each stored in an instance variable of the same name.

        Additional public instance variables argre:
          -- initial_canvas:  A RoseCanvas created automatically.
          -- widgets:   The list of widgets (initial_canvas et al)
                          that are on this RoseWindow.
          -- mouse:     The Mouse bound to this RoseWindow.
          -- keyboard:  The Keyboard bound to this RoseWindow.
          -- toplevel:  The tkinter Toplevel that is the graphical
                          incarnation of this RoseWindow.
        """
        # --------------------------------------------------------------
        # The _master_Tk controls the mainloop for ALL the RoseWindows.
        # If this is the first RoseWindow constructed in this run,
        # then construct the _master_Tk object.
        # --------------------------------------------------------------
        global _master_Tk
        if not _master_Tk:
            _master_Tk = tkinter.Tk()
            _master_Tk.withdraw()
        else:
            time.sleep(0.1)  # Helps the window appear on TOP of Eclipse

        # --------------------------------------------------------------
        # Has a tkinter.Toplevel, and a tkinter.Canvas on the Toplevel.
        # --------------------------------------------------------------
        self.toplevel = tkinter.Toplevel(_master_Tk,
                                         background=window_color,
                                         width=width, height=height)
        self.toplevel.title(title)
        self._is_closed = False
        self.toplevel.protocol("WM_DELETE_WINDOW", self.close)

        if make_initial_canvas:
            self.initial_canvas = RoseCanvas(self, width, height,
                                             canvas_color)
        else:
            self.initial_canvas = None

        self.widgets = [self.initial_canvas]

        # TODO: Do any other tailoring of the toplevel as desired,
        #       e.g. borderwidth and style...

        # --------------------------------------------------------------
        # Catch mouse clicks and key presses.
        # --------------------------------------------------------------
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.toplevel.bind('<Button>', self._on_mouse_click)
        self.toplevel.bind('<KeyPress>', self._on_key_press)

        self.update()

    def close_on_mouse_click(self):
        self.get_next_mouse_click()
        self.close()

    def get_next_mouse_click(self):
        self.render()  # update graphics and flush any prior clicks
        self.mouse.position = None
        while True:
            if self._is_closed:
                return None
            if self.mouse.position is not None:
                break
            self.update()
            time.sleep(.05)  # allow time for other events to be handled

        click_point = self.mouse.position
        self.mouse.position = None

        return click_point

    def close(self):
        """ Close this window """
        if self.toplevel:
            self.toplevel.destroy()
            self.toplevel = None
        self.update()
        self._is_closed = True

    def update(self):
        global _master_Tk
        _master_Tk.update()

    def render(self, seconds_to_pause=None):
        for widget in self.widgets:
            if type(widget) == RoseCanvas:
                widget.render()

        self.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def _on_mouse_click(self, event):
        self.mouse._update(event)

    def _on_key_press(self, event):
        self.keyboard._update(event)

#     def add_canvas(self, width=None, height=None, background_color=None):
# TODO: Set defaults based on the main canvas.
#         new_canvas = RoseCanvas(self, background_color='white')
#         self.widgets.append(new_canvas)
#
#         _root.update()


class RoseWidget():
    """
       A Widget is a thing that one can put on a Window,
       e.g. a Canvas, FortuneTeller, etc.
    """

    def __init__(self, window):
        self._window = window


class RoseCanvas(RoseWidget):
    """
       A RoseCanvas is a RoseWidget (i.e., a thing on a RoseWindow)
       upon which one can draw shapes and other Drawable things.
    """
    def __init__(self, window, width=200, height=200,
                 background_color=None):
        super().__init__(window)

        tk_canvas = tkinter.Canvas(window.toplevel,
                                   width=width, height=height,
                                   background=background_color)
        self._tkinter_canvas = tk_canvas

        # FIXME: Automate gridding better.
        self._tkinter_canvas.grid(padx=5, pady=5)
        self.shapes = {}

    def render(self, seconds_to_pause=None):
        self._update_shapes()
        self._window.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def _draw(self, shape):
        if shape not in self.shapes.items():
            method = shape._method_for_drawing
            coordinates = shape._get_coordinates_for_drawing()
            options = shape._get_options_for_drawing()

            shape_id = method(self._tkinter_canvas, *coordinates)
            self._tkinter_canvas.itemconfigure(shape_id, options)

            self.shapes[shape_id] = shape

    def _update_shapes(self):
        for shape_id in self.shapes:
            shape = self.shapes[shape_id]

            coordinates = shape._get_coordinates_for_drawing()
            options = shape._get_options_for_drawing()

            self._tkinter_canvas.coords(shape_id, *coordinates)
            self._tkinter_canvas.itemconfigure(shape_id, options)


class Mouse(object):
    def __init__(self):
        self.position = None

    def _update(self, event):
        self.position = Point(event.x, event.y)


class Keyboard(object):
    def __init__(self):
        self.key_pressed = None

    def _update(self, event):
        pass


class _Shape(object):
    """
    A Shape is a thing that can be drawn on a RoseCanvas
    (which itself draws on a tkinter Canvas).

    Its constructor provides the tkinter method to be used to
    draw this Shape.

    This abstract type has concrete subclasses that include:
      Arc, Bitmap, Circle, Ellipse, Image, Line, Path, Polygon,
      Rectangle, RoundedRectangle, Square, Text and Window.

    Public data attributes:  None.
    Public methods: attach_to.
    """
    def __init__(self, method_for_drawing):
        """  Arguments:
          -- the tkinter method for drawing the Shape.
        """
        self._method_for_drawing = method_for_drawing

    def attach_to(self, rose_canvas):
        """ Attach this Shape to the given RoseCanvas. """
        rose_canvas._draw(self)


class _ShapeWithOutline(object):
    """
    A Shape that has an interior (which can be filled with a color)
    and an outline (which has a color and thickness).

    This abstract type has concrete subclasses that include:
      Arc, Circle, Ellipse, Image, Line, Path,
      Polygon, Rectangle, Square, Text and Window.

    Public data attributes:  fill_color, outline_color, outline_thickness.
    Public methods:  initialize_options.
    """
    defaults = {'fill_color': None,
                'outline_color': 'black',
                'outline_thickness': 1}

    def initialize_options(self):
        self.fill_color = _ShapeWithOutline.defaults['fill_color']
        self.outline_color = _ShapeWithOutline.defaults['outline_color']
        self.outline_thickness = _ShapeWithOutline.defaults['outline_thickness']

    def _get_options_for_drawing(self):
        options = {'fill': self.fill_color,
                   'outline': self.outline_color,
                   'width': self.outline_thickness}

        # If a color is None, that means transparent here:
        for option in ('fill', 'outline'):
            if not options[option]:
                options[option] = ''

        return options


class _ShapeWithFill(object):
    """
    A Shape that can be (and almost always is) filled with a color
    and has a thickness but no outline.

    This abstract type has concrete subclasses that include:
      Line and Path.

    Public data attributes:  color, thickness.
    Public methods:  initialize_options.
    """
    defaults = {'color': 'black',
                'thickness': 1}

    def initialize_options(self):
        self.color = _ShapeWithFill.defaults['color']
        self.thickness = _ShapeWithFill.defaults['thickness']

    def _get_options_for_drawing(self):
        options = {'fill': self.color,
                   'width': self.thickness}

        # If a color is None, that means 'black' here:
        if options['fill'] is None:
            options['fill'] = 'black'

        return options


class _ShapeWithCenter(_Shape):
    """
    A Shape that has a center (and for which moving its center
    moves the entire Shape).  Its constructor provides the center
    of the Shape along with its method for drawing this Shape.

    This abstract type has concrete subclasses that include:
      Arc, Bitmap, Circle, Ellipse, Image,
      Rectangle, RoundedRectangle, Square, Text and Window.

    Public data attributes: center.
    Public methods: move_by, move_center_to.
    """
    def __init__(self, center, method_for_drawing):
        """
        Arguments:
          -- the Point that is the center of the Shape
               (the Shape stores a CLONE of that Point)
          -- the tkinter method for drawing the Shape.
        """
        # Clone the   center   argument, so that if the caller
        # mutates the argument, it does NOT affect this Shape.
        super().__init__(method_for_drawing)
        self.center = center.clone()

    def move_by(self, dx, dy):
        """
        Moves this Shape dx units in the x-direction and dy units in
        the y-direction,
        """
        self.center.move_by(dx, dy)

    def move_center_to(self, x, y):
        """
        Moves this Shape's center to position (x, y), thus translating
        the entire Shape by however much its center moved.
        """
        self.center.move_to(x, y)


class _RectangularShape(_ShapeWithCenter):
    """
    A Shape determined by its rectangular bounding box
    (plus possibly other information).
    Its constructor provides the center of the Shape along with its
    width and height, from which the bounding box can be determined.
    Its constructor also provides the method for drawing this Shape.

    This abstract type has concrete subclasses that include:
      Arc, Ellipse, Rectangle and RoundedRectangle.

    Public data attributes: width, height.
    Public methods: clone, get_bounding_box.
    """
    def __init__(self, center, width, height, method_for_drawing):
        super().__init__(center, method_for_drawing)

        self.width = width
        self.height = height

    def __repr__(self):
        string = '{} with center at ({}, {})'
        string = string + ', width {} and height {}'
        return string.format(self.__class__.__name__,
                             self.center.x,
                             self.center.y,
                             self.width,
                             self.height)

    def clone(self):
        return self.__class__(self.center, self.width, self.height)

    def get_bounding_box(self):
        return Rectangle(self.center, self.width, self.height)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Arc(_RectangularShape, _ShapeWithOutline):
    """ Not yet implemented. """


class Bitmap(_Shape):
    """ Not yet implemented. """


class Circle(_ShapeWithCenter, _ShapeWithOutline):
    """
    A Shape that is a Circle.
    Its constructor specifies its center and radius,
    as well as the method for drawing this Shape.

    Public data attributes: center, radius, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, move_by, move_center_to,
                    clone, get_bounding_box.
    """
    def __init__(self, center, radius):
        super().__init__(center, tkinter.Canvas.create_oval)
        super().initialize_options()

        self.radius = radius

    def __repr__(self):
        string = 'Circle with center at ({}, {}) and radius {})'
        return string.format(self.center.x, self.center.y,
                             self.radius)

    def clone(self):
        return Circle(self.center, self.radius)

    def get_bounding_box(self):
        return Rectangle(self.center, 2 * self.radius, 2 * self.radius)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Ellipse(_RectangularShape, _ShapeWithOutline):
    """
    A Shape that is an Ellipse (aka oval).  Its constructor
    specifies its center (a Point) and the width and height
    of its bounding box, as well as the method for drawing this Shape.

    Public data attributes: center, width, height, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, move_by, move_center_to,
                    get_bounding_box.
    """
    def __init__(self, center, width, height):
        super().__init__(center, width, height,
                         tkinter.Canvas.create_oval)
        super().initialize_options()


class Line(_Shape, _ShapeWithFill):
    """
    A Shape that is a Line (more precisely, a line segment).
    Its constructor specifies its start and end points,
    as well as the method for drawing this Shape.

    Public data attributes: start, end, color, thickness.
    Public methods: attach_to, clone, move_by, get_midpoint.
    """

    def __init__(self, start, end):
        super().__init__(tkinter.Canvas.create_line)
        super().initialize_options()

        self.start = start.clone()
        self.end = end.clone()

    def __repr__(self):
        string = 'Line from ({}, {}) to ({}, {}))'
        return string.format(self.start.x, self.start.y,
                             self.end.x, self.end.y)

    def clone(self):
        return Line(self.start, self.end)

    def move_by(self, delta_x, delta_y):
        self.start.move_by(delta_x, delta_y)
        self.end.move_by(delta_x, delta_y)

    def get_midpoint(self):
        return Point((self.start.x + self.end.x) // 2,
                     (self.start.y + self.end.y) // 2)

    def _get_coordinates_for_drawing(self):
        return [self.start.x,
                self.start.y,
                self.end.x,
                self.end.y]


class Path(_Shape, _ShapeWithFill):
    """ Not yet implemented. """


class Point(_Shape, _ShapeWithOutline):
    # FIXME: Add comment
    defaults = {'width_for_drawing': 10,
                'height_for_drawing': 10,
                'fill_color': 'red'}

    def __init__(self, x, y):
        super().__init__(tkinter.Canvas.create_oval)
        super().initialize_options()

        self.x = x
        self.y = y

        self.width_for_drawing = Point.defaults['width_for_drawing']
        self.height_for_drawing = Point.defaults['height_for_drawing']
        self.fill_color = Point.defaults['fill_color']

    def __repr__(self):
        return 'Point at ({}, {})'.format(self.x, self.y)

    def clone(self):
        return Point(self.x, self.y)

    def move_by(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def get_bounding_box(self):
        return Rectangle(self,
                         self.width_for_drawing, self.height_for_drawing)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Polygon(_Shape, _ShapeWithOutline):
    """ Not yet implemented. """


class Rectangle(_RectangularShape, _ShapeWithOutline):
    """
    A Shape that is a Rectangle.  Its constructor specifies its center
    and the width and height of its bounding box.

    Public data attributes: center, width, height, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, clone,
                    move_by, move_center_to,
                    get_bounding_box,
                    get_upper_left_corner,
                    get_upper_right_corner,
                    get_lower_left_corner,
                    get_lower_right_corner.
    """
    def __init__(self, center, width, height):
        super().__init__(center, width, height,
                         tkinter.Canvas.create_rectangle)
        super().initialize_options()

    def get_bounding_box(self):
        return self.clone()

    def get_upper_left_corner(self):
        return Point(self.center.x - self.width / 2,
                     self.center.y - self.height / 2)

    def get_upper_right_corner(self):
        return Point(self.center.x + self.width / 2,
                     self.center.y - self.height / 2)

    def get_lower_left_corner(self):
        return Point(self.center.x - self.width / 2,
                     self.center.y + self.height / 2)

    def get_lower_right_corner(self):
        return Point(self.center.x + self.width / 2,
                     self.center.y + self.height / 2)

    def _get_coordinates_for_drawing(self):
        return [self.get_upper_left_corner().x,
                self.get_upper_left_corner().y,
                self.get_lower_right_corner().x,
                self.get_lower_right_corner().y]


class RoundedRectangle(_RectangularShape, _ShapeWithOutline):
    """ Not yet implemented. """


class Square(_ShapeWithCenter, _ShapeWithOutline):
    """
    A Shape that is a Square.
    Its constructor specifies its center and the length of each side,
    as well as the method for drawing this Shape.

    Public data attributes: center, length_of_each_side, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, move_by, move_center_to,
                    clone, get_bounding_box.
    """
    def __init__(self, center, length_of_each_side):
        super().__init__(center, tkinter.Canvas.create_rectangle)
        super().initialize_options()

        self.length_of_each_side = length_of_each_side

    def __repr__(self):
        string = 'Square with center at ({}, {}) and length of each side {})'
        return string.format(self.center.x, self.center.y,
                             self.length_of_each_side)

    def clone(self):
        return Square(self.center, self.length_of_each_side)

    def get_bounding_box(self):
        return Rectangle(self.center,
                         2 * self.length_of_each_side,
                         2 * self.length_of_each_side)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Text(_Shape):
    """ Not yet implemented. """
    default_options = {}


class Window(_Shape):
    """ Not yet implemented. """
    default_options = {}


# CONSIDER: Are these right for here?
class Button(_Shape):
    """ Not yet implemented. """
    default_options = {}


class Entry(_Shape):
    """ Not yet implemented. """
    default_options = {}


def main():
    """ Demonstrates some of the features of this module. """
    window1 = RoseWindow(title='An empty window',
                         make_initial_canvas=False)

    window1.close_on_mouse_click()

    window2 = RoseWindow(500, 300, 'Blue window with yellow canvas',
                         window_color='blue', canvas_color='yellow')

    center = Point(300, 100)
    circle = Circle(center, 40)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = 'red'
    window2.render(3)
    circle.fill_color = ''

    center.move_by(-200, -50)
    circle = Circle(center, 70)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = None

    window2.close_on_mouse_click()
    return

    window3 = RoseWindow()

    p1 = Point(100, 50)

    rect = Rectangle(p1, 100, 40)
    rect.attach_to(window2.initial_canvas)
    rect.attach_to(window3.initial_canvas)

    window2.render(3)
    window3.render(3)

    rect.fill_color = 'red'
    center.attach_to(window3.initial_canvas)

    window2.render(3)
    window3.render(3)

    center.move_by(50, 0)
    window3.render(3)

    window2.close_on_mouse_click()
    window3.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
