"""
This module is an example of a simple   GRAPHICS   program.
It demonstrates:
  -- DEFINING functions:
       -- main
       -- wiggle
  -- How    main   CALLS the    wiggle    function.
  -- Giving values to VARIABLES using the ASSIGNMENT
        operator = (read it as "gets")
  -- CONSTRUCTING OBJECTS (GraphWin, Point, Circle, Text)
  -- USING OBJECTS, as in:    circle.move(delta_x, delta_y)
  -- Running a LOOP a fixed number of times (a "counting" loop),
         using a FOR statement and a RANGE expression.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, and their colleagues.  December 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example to see:
#   Cool graphics!  (We'll study this example in detail in Session 3.)
#-----------------------------------------------------------------------

import zellegraphics as zg
import time
import random


def main():
    """ Calls the   wiggle   function to demonstrate it. """
    wiggle()


def wiggle():
    """
    Draws circles that start at the center of a graphics window.
    Each circle moves randomly ("wiggles")
    until it hits an edge of the window.
    """
    width = 400
    height = 300
    window = zg.GraphWin('Wiggles', width, height)

    center = zg.Point(width / 2, height / 2)
    radius = 20
    circle = zg.Circle(center, radius)
    circle.setFill('green')
    circle.draw(window)

    for k in range(500):
        delta_x = random.randrange(-12, 13)  # between -12 and 12
        delta_y = random.randrange(-5, 13)  # between -5 and 12

        circle.move(delta_x, delta_y)
        time.sleep(5 / (k + 5))  # units are seconds so starts at 1 sec

        x = circle.getCenter().x
        y = circle.getCenter().y
        if x < 0 or x > width or y < 0 or y > height:
            circle = zg.Circle(center, radius)  # A new circle
            color = zg.color_rgb(random.randrange(255),  # red
                                 random.randrange(255),  # green
                                 random.randrange(255))  # blue
            circle.setFill(color)
            circle.draw(window)

    message = 'Click the mouse anywhere in here to exit'
    message_box = zg.Text(zg.Point(width / 2, 20), message)
    message_box.draw(window)

    window.getMouse()
    window.close()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
