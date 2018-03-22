"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  February 2014.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE..

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    test_draw_wall_on_right()


def test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), 30, 20)
    draw_wall_on_right(rectangle1, 8, window)

    rectangle2 = rg.Rectangle(rg.Point(470, 40), 50, 50)
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    center_x = rectangle.center.x
    center_y = rectangle.center.y
    width = rectangle.width
    height = rectangle.height
    x = center_x
    y = center_y

    for k in range(n):
        for j in range(k + 1):
            re = rg.Rectangle(rg.Point(x, y), width, height)
            re.attach_to(window.initial_canvas)
            x = x - width
            window.render(0.1)
        y = y + height
        x = center_x











# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
