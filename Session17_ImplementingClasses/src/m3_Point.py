"""
A simple   Point   class.
NOTE: This is NOT rosegraphics -- it is your OWN Point class.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.
from math import sqrt


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   m3_test_Point  module, NOT here.
    pass


# TODO:  Define here a class called   Point
#        that represents a point in two dimensions.
#        It has:
#   Instance variables:  x and y, for its two coordinates.
#   Methods:
#     __init__: Takes two optional arguments, x and y, both numbers.
#               Sets this Point's coordinates to the given x and y.
#               The defaults for x and y are 0.
#     __repr__: Returns a string that represents this Point
#               as in this example:  'Point(100, 32.7)'
#     move_to:  Takes two arguments, x and y, both numbers.
#               Sets this Point's x and y to those values.
#     move_by:  Takes two arguments, dx and dy, both numbers.
#               Increases this Point's x and y by those values.
#     distance_from:  Takes a Point and returns the distance
#                     that this Point is from the given Point.
#     closer_to:  Takes two Points p2 and p3.
#                 Returns whichever of p2 and p3 is closer
#                 to this Point.  (Returns p2 if they are tied).
#     halfway_to:  Takes a Point.
#                  Returns a new Point whose x coordinate is
#                  the average of the x-coordinates of this Point
#                  and the given Point, and whose y coordinate is
#                  the average of the y-coordinates of this Point
#                  and the given Point.
#
# Include appropriate docstrings with the methods that you define
# (copy-and-paste from the above makes it easy to do so).
# Test your class definition using the   m3_test_Point    module.
#   ** TEST EACH METHOD AS YOU DEFINE IT. **
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        x = self.x
        y = self.y
        str1 = 'Point({}, {})'
        return str1.format(x, y)

    def move_to(self, x, y):
        self.x = x
        self.y = y
        return self

    def move_by(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self

    def distance_from(self, given_point):
        a = given_point.x - self.x
        b = given_point.y - self.y
        distance = sqrt(a ** 2 + b ** 2)
        return distance

    def closer_to(self, another_point1, another_point2):
        a = another_point1.x - self.x
        b = another_point1.y - self.y
        distancep1p2 = sqrt(a ** 2 + b ** 2)
        c = another_point2.x - self.x
        d = another_point2.y - self.y
        distancep1p3 = sqrt(c ** 2 + d ** 2)
        if distancep1p2 > distancep1p3:
            return another_point2
        else:
            return another_point1

    def halfway_to(self, given_point):
        a = (given_point.x + self.x) * 0.5
        b = (given_point.y + self.y) * 0.5
        halfway = Point(a, b)
        return halfway


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
