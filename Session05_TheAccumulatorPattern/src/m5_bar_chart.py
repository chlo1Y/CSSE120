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
    test_draw_bar_chart()


def test_draw_bar_chart():
    """ Tests the   bar_chart   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_bar_chart   function:')
    print('See the graphics window(s) that pop up.')
    print('--------------------------------------------------')

    title = 'draw_bar_chart({}, {}, {}, {}'.format(60, 40, 100, 4)
    draw_bar_chart(60, 40, 100, 4, title)

    title = 'draw_bar_chart({}, {}, {}, {}'.format(100, 20, 50, 10)
    draw_bar_chart(100, 20, 50, 10, title)

    title = 'draw_bar_chart({}, {}, {}, {}'.format(50, 100, 75, 5)
    draw_bar_chart(50, 100, 75, 5, title)


def draw_bar_chart(height_of_first_bar, height_increment, bar_width,
                   number_of_bars, title):
    """
    See   bar_chart.pdf   in this project for pictures that may
    help you better understand the following specification:

    1. Constructs a rg.RoseWindow that has the given title.
         -- The window should be large enough to hold the
            entire bar chart, with (say) 50 extra pixels on each side.
    2. Draws a bar chart on it.
         The bars are vertical.  As you go left-to-right,
         the bar heights increase by the constant increment specified.
    3. Pauses after drawing, waiting for the user to click the mouse
         in the window, then closes the window.

    The parameters specify:
      -- the height of the first bar (all dimensions are in pixels)
      -- the constant amount by which the bar heights increase,
             as you move left-to-right across the chart
      -- the width of each bar (all are the same width)
      -- the number of bars to draw
      -- the title to use in the rg.RoseWindow that you construct.
    Other characteristics of the bar chart can be set in any reasonable
    way you choose.

    Preconditions: All the arguments are reasonable numbers.
    """
    # TODO: 2. Implement and test this function.
    # HINT: Consider using the accumulator pattern
    #       instead of directly using the loop variable.
    # Also: ** FIRST DO A CONCRETE EXAMPLE BY HAND! **

    widthofbar = bar_width * number_of_bars + 100
    heightofbar = height_of_first_bar + number_of_bars * height_increment + 100
    windows = rg.RoseWindow(widthofbar, heightofbar)
    for k in range(1, number_of_bars + 1):

        centerx = 50 + bar_width / 2 + bar_width * (k - 1)
        centery = heightofbar - (height_of_first_bar / 2 + (height_of_first_bar + (k - 1) * height_increment) / 2 + 50)

        barheight = height_of_first_bar + (k - 1) * height_increment
        barwidth = bar_width
        point = rg.Point(centerx, centery)

        rect = rg.Rectangle(point, barwidth, barheight)
        rect.attach_to(windows.initial_canvas)

    windows.render()
    windows.close_on_mouse_click()








# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
