"""
rosegraphics.py - a simple Graphics library for Python.
Its key feature is:
  -- USING this library provides a simple introduction to USING objects.

Other key features include:
  -- It has a rich set of classes, methods and instance variables.
       -- In addition to classes like Circles that are natural for
            students, it has other kinds of classes like RoseWindow
            and FortuneTeller to provide a richer set of examples
            than "just" a graphics library.
  -- It allows one to do a reasonable set of graphics operations
       with reasonable efficiency. The API mimics Java's Shape API
       for the most part.
  -- It is built on top of tkinter and its extension ttk
       (the standard graphics libraries that come with Python).
  -- Unlike tkinter, it is NOT event-driven and hence can be used
       before students see that paradigm.  (There is a behind-the-scenes
       facilty for listening for and responding to events,
       for those who want to do so.)
  -- It attempts to be as bullet-proof as possible, to make it easy
       for beginners to use it.  In particular, it attempts to provide
       reasonable error messages when a student misuses the API.
  -- It was inspired by zellegraphics but is a complete re-implemenation
       that attempts to:
       -- Be more bullet-proof.
       -- Provide a richer set of examples for using objects.
       -- Have an API that is more like Java's Shape API than tkinter's
            (older) API.
  -- While it can serve as an example for defining classes,
        it is NOT intended to do so for beginners.
        It is excellent for helping students learn to USE objects;
        it is NOT perfect for helping students learn to WRITE CLASSES.

See the MAIN function below for typical examples of its use.

Authors: David Mutchler, Mark Hays, Michael Wollowswki, Matt Boutell,
         Chandan Rupakheti, Claude Anderson and their colleagues,
         with thanks to John Zelle for inspiration and hints.
         First completed version: September 2014.
"""

# FIXME (things that have yet to be implemented):
#  -- Allow multiple canvasses.
#  -- Better close_on ... ala zellegraphics.
#  -- Keyboard.
#  -- Better Mouse.
#  -- Add type hints.
#  -- Catch all Exceptions and react appropriately.
#  -- Implement unimplemented classes.
#  -- Add and allow FortuneTellers and other non-canvas classes.

import tkinter
from tkinter import font as tkinter_font
import time

# ----------------------------------------------------------------------
# All the windows that are constructed during a run share the single
#    _master_Tk   (a tkinter.Tk object)
# as their common root.  The first construction of a RoseWindow
# sets this  _master_Tk to a Tkinter.Tk object.
# ----------------------------------------------------------------------
_master_Tk = None


# ----------------------------------------------------------------------
# At the risk of not being Pythonic, we provide a simple type-checking
# facility that attempts to provide meaningful error messages to
# students when they pass arguments that are not of the expected type.
# ----------------------------------------------------------------------
class WrongTypeException(Exception):
    """ Not yet implemented. """
    pass


def check_types(triples):
    """ Not yet implemented fully. """
    for triple in triples:
        value = triple[1]
        expected_type = triple[2]
        if not isinstance(value, expected_type):
            print('Error:', value, expected_type)
            raise WrongTypeException(triple)


# ----------------------------------------------------------------------
# RoseWindow is the top-level object.
# It starts with a single RoseCanvas.
# ----------------------------------------------------------------------
class RoseWindow(object):
    """
    A RoseWindow is a window that pops up when constructed.
    It can have   RoseWidgets   on it and starts by default with
    a single  RoseCanvas   upon which one can draw shapes.

    Public data attributes: width, height, title, color, widgets.
    Public methods:
      close, update, render, wait_for_mouse_click, wait_for_key_press,
      check_for_mouse_click, check_for_key_press, close_on_mouse_click.
    """

    def __init__(self, width=400, height=300, title='Rose Graphics',
                 color='black', canvas_color=None,
                 make_initial_canvas=True):
        """
        Pops up a   tkinter.Toplevel   window with (by default)
        a   RoseCanvas  (and associated tkinter.Canvas) on it.

        Arguments are:
          -- width, height: dimensions of the window (in pixels).
          -- title:  title displayed on the windoww.
          -- color:  background color of the window
          -- canvas_color:  background color of the canvas
                            displayed on the window by default
          -- make_initial_canvas:
               -- If True, a default canvas is placed on the window.
               -- Otherwise, no default canvas is placed on the window.

        If this is the first RoseWindow constructed, then a
        hidden   Tk   object is constructed to control the event loop.

        Preconditions:
          :type width: int
          :type height: int
          :type title: str
          :type color: Color
          :type canvas_color: Color
          :type make_initial_canvas: bool
        """
#         check_types([('width', width, (int, float)),
#                      ('height', height, (int, float)),
#                      ('title', title, str,),
#                      ('color', color, (Color, str)),
#                      ('canvas_color', canvas_color, (Color, str)),
#                      ('make_initial_canvas', make_initial_canvas, bool)])

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
                                         background=color,
                                         width=width, height=height)
        self.toplevel.title(title)
        self._is_closed = False
        self.toplevel.protocol("WM_DELETE_WINDOW", self.close)

        # FIXME: The next two need to be properties to have
        # setting happen correctly.  Really belongs to RoseCanvas.
        # See comments elsewhere on this.

        self.width = width
        self.height = height

        if make_initial_canvas:
            self.initial_canvas = RoseCanvas(self, width, height,
                                             canvas_color)
        else:
            self.initial_canvas = None

        self.widgets = [self.initial_canvas]

        # FIXME: Do any other tailoring of the toplevel as desired,
        #       e.g. borderwidth and style...

        # --------------------------------------------------------------
        # Catch mouse clicks and key presses.
        # --------------------------------------------------------------
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.toplevel.bind('<Button>', self._on_mouse_click)
        self.toplevel.bind('<KeyPress>', self._on_key_press)

        self.update()

    def close(self):
        """ Closes this RoseWindow. """
        if self.toplevel:
            self.toplevel.destroy()
            self.toplevel = None
        self.update()
        self._is_closed = True

    def update(self):
        """
        Checks for and handles events that has happened
        in this RoseWindow (e.g. mouse clicks, drawing shapes).
        """
        global _master_Tk
        _master_Tk.update()

    def render(self, seconds_to_pause=None):
        """
        Updates all the Shapes attached to RoseCanvas objects
        associated with this RoseWindow, then draws all those Shapes.
        After doing so, pauses the given number of seconds.

        Arguments:
          -- seconds_to_pause: the number of seconds to pause
        """
        for widget in self.widgets:
            if type(widget) == RoseCanvas:
                widget.render()

        self.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def close_on_mouse_click(self):
        if self.initial_canvas:
            msg = 'To exit, click anywhere in this window'
            click_position = self.continue_on_mouse_click(message=msg,
                                                          close_it=True)
            return click_position
        else:
            self.get_next_mouse_click()
            self.close()
            return None

    def continue_on_mouse_click(self,
                                message=None,
                                x_position=None,
                                y_position=None,
                                close_it=False,
                                erase_it=True):
        """
        Displays a message at the bottom center of the window and
        waits for the user to click the mouse, then erases the message.

        Optional parameters let you:
          -- Display a different message
          -- Place the message at a different place in the window
               (xpos and ypos are as in Text)
          -- Close the window after the mouse is clicked
               (and ignore the GraphicsError that results if the user
               instead chooses to click the   X   in the window)
          -- NOT erase the message when done
        """
        if self._is_closed:
            return
        if x_position is None:
            x_position = self.width / 2
        if y_position is None:
            y_position = self.height - 20
        if message is None:
            message = 'To continue, click anywhere in this window'
        anchor_point = Point(x_position, y_position)
        text = Text(anchor_point, message)

        # FIXME: Really should do all this on a per-RoseCanvas basis.

        text.attach_to(self.initial_canvas)

        click_position = self.get_next_mouse_click()

        if erase_it:
            text.detach_from(self.initial_canvas)

        if close_it:
            self.close()  # then close the window

        return click_position

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

    def _on_mouse_click(self, event):
        self.mouse._update(event)

    def _on_key_press(self, event):
        self.keyboard._update(event)

#      def add_canvas(self, width=None, height=None, background_color=0):
# FIXME: Set defaults based on the main canvas.
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

    def get_window(self):
        return self._window


class RoseCanvas(RoseWidget):
    defaults = {'colors': [None, 'yellow', 'light blue', 'dark grey']}
    count = 0

    """
       A RoseCanvas is a RoseWidget (i.e., a thing on a RoseWindow)
       upon which one can draw shapes and other Drawable things.
    """
    def __init__(self, window, width=200, height=200,
                 background_color=0):
        super().__init__(window)

        RoseCanvas.count = RoseCanvas.count + 1

        # FIXME: Deal with default background colors.
        # FIXME: Store background color as a property
        #        so that modifying it changes the tkinter canvas.
        #        Ditto width and height.


#         if background_color == 0:
#             index = RoseCanvas.count % len(defaults['colors'])
#             self.background_color = defaults['colors'][index]
#         else:
#             self.background_color = background_color

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

    def _undraw(self, shape):
        if shape in self.shapes.values():
            for shape_id in self.shapes.keys():
                if self.shapes[shape_id] is shape:
                    self._tkinter_canvas.delete(shape_id)
                    del self.shapes[shape_id]
                    break

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


class Color(object):
    """ Not implemented yet. """


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

    def __eq__(self, other):
        """
        Two Shape objects are equal (==) if all their attributes
        are equal to each other.
        """
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def attach_to(self, rose_canvas):
        """
        Attach this Shape to the given RoseCanvas.
        When that RoseCanvas is rendered, this shape will appear
        on that RoseCanvas.
        """
        rose_canvas._draw(self)

    def detach_from(self, rose_canvas):
        """
        Detach this Shape to the given RoseCanvas.
        When that RoseCanvas is rendered, this shape no longer appear
        on that RoseCanvas.
        """
        rose_canvas._undraw(self)


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
        s = 'outline_thickness'
        self.outline_thickness = _ShapeWithOutline.defaults[s]

    def _get_options_for_drawing(self):
        options = {'fill': self.fill_color,
                   'outline': self.outline_color,
                   'width': self.outline_thickness}

        # If a color is None, that means transparent here:
        for option in ('fill', 'outline'):
            if not options[option]:
                options[option] = ''

        return options


class _ShapeWithThickness(object):
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
        self.color = _ShapeWithThickness.defaults['color']
        self.thickness = _ShapeWithThickness.defaults['thickness']

    def _get_options_for_drawing(self):
        options = {'fill': self.color,
                   'width': self.thickness}

        # If a color is None, that means 'black' here:
        if options['fill'] is None:
            options['fill'] = 'black'

        return options


class _ShapeWithText(object):
    """
    A Shape that has text and a font for displaying that text.

    This abstract type has concrete subclasses that include:
      Text.

    Public data attributes:  font_family, font_size,
      is_bold, is_italic, is_underline, is_overstrike.

    Public methods:  initialize_options.
    """
    # FIXME: Add more to the above docstring.

    defaults = {'font_family': 'helvetica',
                'font_size': 14,
                'weight':  'normal',
                'slant':  'roman',
                'underline':  0,
                'overstrike':  0,
                'justify': tkinter.CENTER,
                'text_box_width': None,
                'text_color': 'black',
                'text': ''}

    def initialize_options(self):
        self.font_family = _ShapeWithText.defaults['font_family']
        self.font_size = _ShapeWithText.defaults['font_size']
        self.is_bold = _ShapeWithText.defaults['weight'] == 'bold'
        self.is_italic = _ShapeWithText.defaults['slant'] == 'italic'
        self.is_underline = _ShapeWithText.defaults['underline'] == 1
        self.is_overstrike = _ShapeWithText.defaults['overstrike'] == 1

        self.justify = _ShapeWithText.defaults['justify']
        self.text_box_width = _ShapeWithText.defaults['text_box_width']
        self.text_color = _ShapeWithText.defaults['text_color']
        self.text = _ShapeWithText.defaults['text']

    def _get_options_for_drawing(self):
        weight = 'bold' if self.is_bold else 'normal'
        slant = 'italic' if self.is_italic else 'roman'
        underline = 1 if self.is_underline else 0
        overstrike = 1 if self.is_overstrike else 0
        font = tkinter_font.Font(family=self.font_family,
                                 size=self.font_size,
                                 weight=weight,
                                 slant=slant,
                                 underline=underline,
                                 overstrike=overstrike)

        options = {'font': font,
                   'justify': self.justify,
                   'fill': self.text_color,
                   'text': self.text}
        if self.text_box_width:
            options['width'] = self.text_box_width

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

    def __ne__(self, other):
        return not self.__eq__(other)

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

        self._update_corners()

    def __repr__(self):
        string = '{} with center at ({}, {})'
        string = string + ', width {} and height {}'
        return string.format(self.__class__.__name__,
                             self.center.x,
                             self.center.y,
                             self.width,
                             self.height)

    @property
    def upper_left_corner(self):
        self._update_corners()
        return self._upper_left_corner

    @upper_left_corner.setter
    def upper_left_corner(self, point):
        self.center = Point(point.x + self.width / 2,
                            point.y + self.height / 2)
        self._update_corners()

    @property
    def upper_right_corner(self):
        self._update_corners()
        return self._upper_right_corner

    @upper_right_corner.setter
    def upper_right_corner(self, point):
        self.center = Point(point.x - self.width / 2,
                            point.y + self.height / 2)
        self._update_corners()

    @property
    def lower_left_corner(self):
        self._update_corners()
        return self._lower_left_corner

    @lower_left_corner.setter
    def lower_left_corner(self, point):
        self.center = Point(point.x + self.width / 2,
                            point.y - self.height / 2)
        self._update_corners()

    @property
    def lower_right_corner(self):
        self._update_corners()
        return self._lower_right_corner

    @lower_right_corner.setter
    def lower_right_corner(self, point):
        self.center = Point(point.x - self.width / 2,
                            point.y - self.height / 2)
        self._update_corners()

    def _update_corners(self):
        self._upper_left_corner = Point(self.center.x - self.width / 2,
                                        self.center.y - self.height / 2)
        self._upper_right_corner = Point(self.center.x + self.width / 2,
                                         self.center.y - self.height / 2)
        self._lower_left_corner = Point(self.center.x - self.width / 2,
                                        self.center.y + self.height / 2)
        self._lower_right_corner = Point(self.center.x + self.width / 2,
                                         self.center.y + self.height / 2)

    def clone(self):
        return self.__class__(self.center, self.width, self.height)

    def get_bounding_box(self):
        return Rectangle(self.center, self.width, self.height)

    def _get_coordinates_for_drawing(self):
        return [self.upper_left_corner.x,
                self.upper_left_corner.y,
                self.lower_right_corner.x,
                self.lower_right_corner.y]


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


class Line(_Shape, _ShapeWithThickness):
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


class Path(_Shape, _ShapeWithThickness):
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
                         self.length_of_each_side,
                         self.length_of_each_side)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Text(_ShapeWithCenter, _ShapeWithText):
    """
    A Shape that has a string of text on it, displayed horizontally.

    Its constructor specifies the rg.Point at which the text
    is centered and the string that is to be displayed.

    Public data attributes: center (an rg.Point),
      font_size (an integer, 5 to 80 or so are reasonable values),
      is_bold (True if the text is to be displayed in BOLD, else False),
      is_italic (True or False),
      is_underline (True or False),
      is _overstrike (True or False),
      text_color (color used to display the text, default is 'black')
      text (the string to be displayed).
    Public methods: attach_to, move_by, move_center_to.
    """
    def __init__(self, center, text):
        """
        The first argument must be a rg.Point.
        The second argument must be a string.

        When this Text object is rendered on a window,
        the string (2nd argument) is drawn horizontally on the window,
        centered at the rg.Point that is the 1st argument.

        Preconditions:
           :type center: rg.Point
           :type text str
        """
        super().__init__(center, tkinter.Canvas.create_text)
        super().initialize_options()

        self.text = text

        # FIXME: Allow __init__ to set the options.

    def __repr__(self):
        return self.text

    # FIXME: Have repr include characteristics??
    # FIXME: Do a clone?

#     def clone(self):
#         return Square(self.center, self.length_of_each_side)

#     def get_bounding_box(self):
#         return Rectangle(self.center,
#                          2 * self.length_of_each_side,
#                          2 * self.length_of_each_side)

# FIXME: Implement bounding_box using the tkinter function for it.

    def _get_coordinates_for_drawing(self):
        return [self.center.x, self.center.y]


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
                         color='blue', canvas_color='yellow')

    center = Point(300, 100)
    circle = Circle(center, 40)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = 'red'
    window2.render(3)
    circle.fill_color = ''
    print(window2.width, window2.height)
    window2.continue_on_mouse_click()

    center.move_by(-200, -50)
    circle = Circle(center, 70)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = None

    print(window2.width, window2.height)

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
