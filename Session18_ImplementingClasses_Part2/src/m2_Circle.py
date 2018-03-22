"""
A simple   Circle   class.
NOTE: This is NOT rosegraphics -- it is your OWN Circle class.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m1e_Point as pt
from math import sqrt


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   m2_test_Circle  module, NOT here.
    pass


# ----------------------------------------------------------------------
# TODO:  Define here a class called   Circle   that represents a circle.
#        It has:
#   Instance variables:
#     -- center (stored as a Point)
#     -- radius
#   Methods:
#     __init__: Takes two optional parameters, center and radius.
#               Sets this Circle's center and radius to the given values.
#               The defaults are a Point at (0, 0) and a radius of 1.
#     __repr__: Returns a string that represents this Circle
#               as in this example:
#                 'Circle(center = Point(100, 32.7), radius = 43)'
#     clone:    Returns a new Circle that is a copy of this Circle.
#     move_by:  Takes two arguments, dx and dy, both numbers.
#               Increases the x and y of this Circle's center
#               by dx and dy, respectively.
#     intersects:  Takes another Circle as an argument.
#                  Returns True if this Circle and the other Circle
#                  intersect, else returns False.  (If they barely
#                  touch, we will NOT call that an "intersection.")
#                    -- Hint: they intersect if the distance from their
#                       centers is less than the sum of their radii.
#     closer_to_origin: Takes another Circle as an argument.
#                       Returns this Circle or the other Circle,
#                       whichever one's center is closer to (0, 0).
#                       Breaks ties in favor of this Circle.
#     super_circle: Takes another Circle as an argument.
#                   Returns a new Circle that is the smallest Circle
#                   that contains both this Circle and the other Circle.
#
# Include appropriate docstrings with the methods that you define
# (copy-and-paste from the above makes it easy to do so).
# Test your class definition using the   m2_test_Circle    module.
#   ** TEST EACH METHOD AS YOU DEFINE IT. **
#
# Wherever reasonable, CALL methods previously defined rather than
# copying the code of those methods.
# ----------------------------------------------------------------------
class Circle:
    def __init__(self, center=(0, 0), radius=1):
        self.center = center
        self.radius = radius
    def __repr__(self):
        return 'Circle(center=Point{}),radius={})'.format(self.center, self.radius)
    def clone(self):
        return self
    def move_by(self, dx, dy):
        self.center.x = self.center.x + dx
        self.center.y = self.center.y + dy
        return self
    def intersects(self, another_circle):
        a = another_circle.center.x - self.center.x
        b = another_circle.center.y - self.center.y
        d = sqrt(a ** 2 + b ** 2)
        if d < self.radius + another_circle.radius:
            return True
        else:
            return False
    def closer_to_origin(self, the_other_circle):
        d1 = sqrt(the_other_circle.center.x ** 2 + the_other_circle.center.y ** 2)
        d2 = sqrt(self.center.x ** 2 + self.center.y ** 2)
        if d1 > d2:
            return self
        if d2 < d1:
            return 'Circle(center=Point{}),radius={}'.format(the_other_circle.center, the_other_circle.radius)
    def super_circle(self, fat_circle):
        a = (self.center.x + fat_circle.center.x) * 0.5
        b = (self.center.y + fat_circle.center.y) * 0.5
        radius = self.radius + fat_circle.radius
        fat_circle = Circle(pt.Point(a, b), radius)
        return "Circle(center=Point{}),radius={}".format(fat_circle.center, fat_circle.radius)





# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
