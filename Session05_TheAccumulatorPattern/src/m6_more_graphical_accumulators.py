"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
from tkinter.test.support import pixels_conv


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    test_draw_ellipses()


def test_draw_ellipses():
    """ Tests the   draw_ellipses   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least THREE tests (i.e., three DIFFERENT calls
    #   to draw_ovals, e.g. the calls in the attached pictures).
    draw_ellipses(50, 70, 6)
    draw_ellipses(40, 60, 12)
    draw_ellipses(80, 40, 16)

def draw_ellipses(width, height, n):
    """
    See   ellipses.pdf   in this project for pictures that may
    help you better understand the following specification:

    Constructs a rg.RoseWindow and draws 3 SETS of rg.Ellipse objects
    on it, where each SET contains   n   rg.Ellipse objects
    (for the given parameter n).

    The parameters specify:
      -- the width and height, respectively, of each rg.Ellipse
           (all dimensions are in pixels)
      -- the number of rg.Ellipse objects to draw in EACH
           of the three sets.

    The first set of rg.Ellipse objects is a COLUMN on the LEFT side
    of the window, with each rg.Ellipse barely touching the previous one.
    These rg.Ellipse objects should be filled 'blue'.

    The second set of rg.Ellipse objects is a COLUMN on the RIGHT side
    of the window, with each rg.Ellipse barely touching the previous one.
    These rg.Ellipse objects should be filled 'green'.

    The third set of rg.Ellipse objects is a DIAGONAL from the
    UPPER-RIGHT side of the window toward the LOWER-LEFT side
    of the window, with each rg.Ellipse INTERSECTING the previous one,
    with nice "even" intersections.  (The exact amount of overlap is up
    to you.  One possibility is to move each oval by half of its width
    and half of its height. That's what I did in the attached pictures.)
    These rg.Ellipse objects should be filled 'red'.

    It is OK if the third set overlaps the first and/or second set
    somewhat.  The third set has to go 'down and to the left', but any
    reasonable choice for how much down and how much to the left is OK.

    Pauses after drawing, waiting for the user to click the mouse
    in the window, then closes the window.
    """
    # TODO: 2b. Implement and test this function.

    width_g = width * n
    height_g = height * n
    windows = rg.RoseWindow(width_g, height_g)

    for k in range (1, n + 1):

        center1x = width * 0.5
        center1y = height_g - (height * (2 * k - 1) / 2)
        point1 = rg.Point(center1x, center1y)
        elli = rg.Ellipse(point1, width, height)
        elli.fill_color = 'violet'
        elli.attach_to(windows.initial_canvas)

        center2x = width_g - (width * 0.5)
        center2y = height_g - (height * (2 * k - 1) / 2)
        point2 = rg.Point(center2x, center2y)
        elli = rg.Ellipse(point2, width, height)
        elli.fill_color = 'pink'
        elli.attach_to(windows.initial_canvas)

        center3x = width_g - (width * (1 + 0.5 * k))
        center3y = height * 0.5 * k
        point3 = rg.Point(center3x, center3y)
        elli = rg.Ellipse(point3, width, height)
        elli.fill_color = 'light blue'
        elli.attach_to(windows.initial_canvas)



    windows.render()
    windows.close_on_mouse_click()





# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
