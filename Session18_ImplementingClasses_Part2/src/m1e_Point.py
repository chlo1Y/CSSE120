"""
A simple Point class.
NOTE: This is NOT rosegraphics -- it is your OWN Point class.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and SOLUTION by David Mutchler.  January 2014.
"""

import math


class Point:
    """ A class that represents a point in two dimensions."""

    def __init__(self, x=0, y=0):
        """
        Takes two optional parameters, x and y,
        and sets this Point's coordinates to the given
        coordinates.  The defaults for x and y are 0.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Returns a string that represents the Point
        as in this example:  'Point(100, 32.7)'
        """
        return 'Point({}, {})'.format(self.x, self.y)

    def move_to(self, x, y):
        """
        Takes two arguments, x and y, and sets the
        Point's x and y to those values.
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        Takes two arguments, dx and dy, and increases
        this Point's x and y by those values.
        """
        self.x = self.x + dx
        self.y = self.y + dy

    def distance_from(self, point):
        """
        Takes a Point and returns the distance
        that this Point is from the given Point.
        """
        dx = point.x - self.x
        dy = point.y - self.y
        return math.sqrt((dx * dx) + (dy * dy))

    def closer_to(self, p2, p3):
        """
        Takes two Points p2 and p3.  Returns whichever
        of p2 and p3 are closer to this Point.
        (Returns p2 if they are tied).
        """
        if self.distance_from(p2) <= self.distance_from(p3):
            return p2
        else:
            return p3

    def halfway_to(self, point):
        """
        Takes a Point and returns a new Point
        whose x and y coordinates are the averages
        of this Point and the given Point's x
        and y coordinates.
        """
        new_x = (self.x + point.x) / 2
        new_y = (self.y + point.y) / 2
        return Point(new_x, new_y)
