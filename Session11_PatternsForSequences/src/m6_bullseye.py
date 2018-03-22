"""
This module lets you demonstrate your understanding of:
  -- the ACCUMULATOR pattern applied to GRAPHICS
  -- ITERATING through SEQUENCEs
  -- using OBJECTs in zellegraphics.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  January 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_bullseye()


def test_bullseye():
    """ Tests the   bullseye   function. """

    # ------------------------------------------------------------------
    # Test 1 is ALREADY DONE (here).
    # ------------------------------------------------------------------
    colors1 = ('black', 'white', 'blue', 'cornsilk1', 'green')
    window = rg.RoseWindow(450, 450, 'Bullseye 1')

    bullseye(window, colors1)

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Test 2 is ALREADY DONE (here).
    # ------------------------------------------------------------------
    colors2 = ('red', 'blue', 'green', 'aquamarine3',
               'cornsilk1', 'DeepSkyBlue', 'gray98',
               'misty rose', 'SteelBlue', 'tomato')
    window = rg.RoseWindow(800, 500, 'Bullseye 2')

    bullseye(window, colors2)

    window.close_on_mouse_click()


def bullseye(window, colors):
    """
    See   bullseye.pdf   in this project for pictures
    that may help you better understand the following specification:

    Draws a 'bulls-eye' diagram, that is, concentric filled circles,
    using the provided sequence of colors, on the given window.

    COLOR:
    The LARGEST circle should use the FIRST color in the sequence,
    the next-largest circle should use the second color in the sequence,
    and so forth.  They must be drawn in the order given.

    NUMBER OF CIRCLES:  There should be exactly as many concentric
    circles as items in the given sequence of colors
    (i.e., exactly one circle per item in the sequence of colors).

    POSITION: Each circle should be centered in the window.

    RADIUS:
      -- The radius of the SMALLEST circle should be 50.
      -- The radius of the LARGEST circle should be 25 less than
           half of the height of the given window (e.g., if the window's
           height is 450, then the radius of the largest circle is
           (450 / 2) - 25 = 200.  See the picture for examples.)
      -- The radii of the remaining circles should be sized EVENLY from
           the largest to the smallest.

           For example: if the largest circle has radius 200 and there
           are 5 circles, then each circle should have a radius
              (200 - 50) / 4 = 37.5
           less than the diameter of the previous (larger) circle.
           So in this example, the 5 circles would have radii
               200,  163.5,  125,  87.5,  and  50, respectively.

    Preconditions:
      :type window: rg.RoseWindow
      :type colors: (list, tuple)
    where the second argument is a sequence of items that RoseGraphics
    understands as colors (e.g. 'red', 'blue', etc).
    """
    # TODO: 2. Implement and test this function.
    #          Some tests (above) have already been written for you.
    #
    # HINT: As with ANY problem that you don't immediately know how
    #       to solve,
    #           ** WORK A CONCRETE EXAMPLE BY HAND **
    #       to help you determine how to implement a solution.
    for k in range(len(colors), -1, -1):
        radius = 50 + ((window.height * 0.5 - 50) / (len(colors) - 1)) * k
        circles = (rg.Point(window.width * 0.5, window.height * 0.5), radius)
        circles.fill_color = colors[(len(colors) - k - 1)]
        circles.attach_to(window.initial_canvas)



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
