"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


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
    test_draw_lines()


def test_draw_lines():
    """ Tests the   draw_lines  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_lines   function:')
    print('See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    window1 = rg.RoseWindow(300, 400, '4 and 12 lines!')

    draw_lines(4, rg.Point(20, 120), window1)
    draw_lines(12, rg.Point(150, 230), window1)
    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    window2 = rg.RoseWindow(275, 300, '7 lines!')
    draw_lines(7, rg.Point(50, 120), window2)
    window2.close_on_mouse_click()


def draw_lines(n, point, window):
    """
    See   lines.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws n lines on the given window.
      -- The leftmost point of each of the lines is the given point.
      -- For the rightmost point of each of the lines:
         -- Its x-coordinate is (pX + 100),
              where pX is the x-coordinate of the given point.
         -- The y-coordinates of the lines vary evenly
              from (pY - 100) to (pY + 100),
              where pY is the y-coordinate of the given point.

    Preconditions: n is an integer > 1, window is a zg.Graphwin
                   and point is a reasonable zg.Point in the window.
    """
    # Done: 2. Implement and test this function.
    # HINT: To figure out the code that determines the right-most point
    #         of each line, ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    y = point.y - 100
    x = point.x + 100
    for k in range(n):
        point1 = rg.Point(x, y)
        line = rg.Line(point, point1)
        line.attach_to(window.initial_canvas)
        y = y + 200 / (n - 1)
    window.render()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
