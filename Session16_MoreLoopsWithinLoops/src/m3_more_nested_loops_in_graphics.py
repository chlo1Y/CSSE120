"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  February 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    test_draw_upside_down_wall()


def test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(140, 240), 30, 20)
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(400, 200), 50, 50)
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" where:
      -- The BOITOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    width = rectangle.width
    height = rectangle.height
    rectangle_x = rectangle.center.x
    rectangle_y = rectangle.center.y
    rectangle.attach_to(window.initial_canvas)
    for k in range(1, n):
        rectangle_x = rectangle_x - 0.5 * width
        rectangle_y = rectangle_y - height
        rectangle = rg.Rectangle(rg.Point(rectangle_x, rectangle_y), width, height)
        rectangle.attach_to(window.initial_canvas)
        for j in range(k + 1):
            rectangle1_x = rectangle_x + width * j
            rectangle1 = rg.Rectangle(rg.Point(rectangle1_x, rectangle_y), width, height)
            rectangle1.attach_to(window.initial_canvas)
    window.render()
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.

# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
