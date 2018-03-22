"""
<describe what this module has/does>

Created on Oct 19, 2014.
Written by: mutchler.
"""

import rosegraphics as rg
import tkinter


def main():
    """ Demonstrates the use of the classes in this module. """
    window = rg.RoseWindow()

    point1 = rg.Point(100, 100)
    point2 = rg.Point(200, 150)
    point3 = rg.Point(100, 200)
    point4 = rg.Point(300, 100)
    point5 = rg.Point(250, 150)

    # ------------------------------------------------------------------
    # The following uses classes defined in THIS module instead
    # of the (more elaborate) versions in the rosegraphics module.
    # ------------------------------------------------------------------
    rectangle1 = Rectangle(point1, 60, 20)
    rectangle2 = Rectangle(point2, 50, 100)
    ellipse1 = Ellipse(point3, 80, 40)
    ellipse2 = Ellipse(point4, 50, 50)
    circle1 = Circle(point4, 15)

    shapes = (rectangle1, rectangle2, ellipse1, ellipse2, circle1)

    for shape in shapes:
        print(shape)
        shape.attach_to(window.initial_canvas)

    window.render()
    window.continue_on_mouse_click()

    circle2 = Circle(point5, 30)
    for _ in range(40):
        circle2.attach_to(window.initial_canvas)
        window.render(0.10)
        circle2.move_down_and_right(1)

    window.close_on_mouse_click()


class Shape(object):
    """
    A Shape has a center, width and height, plus a method for drawing.
    """

    def __init__(self, center, width, height,
                 method_for_drawing, shape_type):
        """
        Sets the center, width and height, plus method for drawing.
        """
        self.center = center
        self.width = width
        self.height = height
        self._method_for_drawing = method_for_drawing
        self.shape_type = shape_type  # Used by __repr__

    def __repr__(self):
        """ A string representation of this Shape. """
        format_string = '{}(center = {}, width = {}, height = {})'
        return format_string.format(self.shape_type,
                                    self.center,
                                    self.width,
                                    self.height)

    def move_by(self, dx, dy):
        """
        Moves this Shape dx units in the x-direction
        and dy units in the y-direction,
        """
        self.center.move_by(dx, dy)

    def attach_to(self, rose_canvas):
        """
        Attach this Shape to the given RoseCanvas.
        When that RoseCanvas is rendered, this shape will appear
        on that RoseCanvas.
        """
        rose_canvas._draw(self)

    def _get_coordinates_for_drawing(self):
        return [self.center.x - self.width // 2,
                self.center.y - self.height // 2,
                self.center.x + self.width // 2,
                self.center.y + self.height // 2]

    def _get_options_for_drawing(self):
        return []


class Rectangle(Shape):
    """ A representation of a Rectangle, suitable for drawing. """

    # An example of a method that OVERRIDES its superclass method
    # by AUGMENTING the superclass method.
    def __init__(self, center, width, height):
        """
        Sets the Rectangle's center, width and height per the arguments.
        Sets the method_for_drawing and shape_name as appropriate
        for a Rectangle.
        """
        method_for_drawing = tkinter.Canvas.create_rectangle
        shape_name = 'Rectangle'
        # Shows how to call the SUPERCLASS method to AUGMENT this one.
        super().__init__(center, width, height,
                         method_for_drawing, shape_name)

    def get_upper_left_corner(self):
        return rg.Point(self.center.x - self.width // 2,
                        self.center.y - self.height // 2)


class Ellipse(Shape):
    """ A representation of an Ellipse, suitable for drawing. """

    # An example of a method that OVERRIDES its superclass method
    # by AUGMENTING the superclass method.
    def __init__(self, center, width, height):
        """
        Sets the Ellipse's center, width and height per the arguments.
        Sets the method_for_drawing and shape_name as appropriate
        for an Ellipse.
        """
        method_for_drawing = tkinter.Canvas.create_oval
        shape_name = 'Ellipse'
        # Shows how to call the SUPERCLASS method to AUGMENT this one.
        super().__init__(center, width, height,
                         method_for_drawing, shape_name)


class Circle(Ellipse):
    """ A representation of a Circle, suitable for drawing. """

    # An example of a method that OVERRIDES its superclass method
    # by AUGMENTING the superclass method.
    def __init__(self, center, radius):
        """
        Sets the Circle's center, width and height per the arguments.
        (The code treats a Circle as an Ellipse.)
        Sets the method_for_drawing and shape_name as appropriate
        for a Circle.
        """
        # Shows how to call a SUPERCLASS method to AUGMENT this method.
        super().__init__(center, radius * 2, radius * 2)

    # An example of a method that OVERRIDES its superclass method.
    # Done here because we want a Circle to print as a CIRCLE instead of
    # as an ELLIPSE that happens to have the same width and height.
    def __repr__(self):
        """ A string representation of this Circle. """
        format_string = 'Circle(center = {}, radius = {})'
        return format_string.format(self.center,
                                    self.width // 2)

    # An example of a method that uses a superclass method.
    # This requires NO SPECIAL NOTATION - just call the method as usual!
    def move_down_and_right(self, amount_to_move):
        self.move_by(amount_to_move, amount_to_move)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
