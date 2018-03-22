"""
This module demonstrates a simple   GRAPHICS   program.
You can (and should) modify it!

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         their colleagues and PUT Zesun Yang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

#-----------------------------------------------------------------------
# TODO: 2. Play around with this file.  First, run it.
#          Try changing a number, whatever you feel comfortable with,
#          and then run the program again to see the effect.
#          Repeatedly:
#            -- Make a SMALL change, then
#            -- Run the program again, to see the effect of your change.
#
#          You'll probably get red error messages at some point.
#          If so, try briefly to fix them,
#          but fixing errors is what we will learn in the NEXT session.
#          So:
#             ***  IT IS PERFECTLY   OK   IF YOU MESS THIS FILE UP!  ***
#
#  *** YOU ARE ** not ** EXPECTED TO UNDERSTAND EVERYTHING IN HERE.
#  *** Just start getting used to EDITING and RUNNING a PROGRAM.
#
#  *** FULL CREDIT JUST FOR MAKING ** ANY ** CHANGES
#                           AND RUNNING THIS FILE!
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
    width = 200
    height = 400
    window = zg.GraphWin('Wiggles', width, height)

    center = zg.Point(width / 3, height / 3)
    radius = 25
    circle = zg.Circle(center, radius)
    circle.setFill('purple')
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
            color = zg.color_rgb(random.randrange(255),  # pink
                                 random.randrange(255),  # pinkish blue
                                 random.randrange(255))  # grey
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
