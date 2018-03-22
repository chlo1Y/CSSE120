"""
This module demonstrates the ACCUMULATOR pattern in three classic forms:
   SUMMING:       total = total + number
   COUNTING:      count = count + 1
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example.
#           Before you leave this example:
#   *** MAKE SURE YOU UNDERSTAND THE 3 ACCUMULATOR PATTERNS          ***
#   *** shown in this module:  SUMMING, COUNTING, and IN GRAPHICS    ***
# ----------------------------------------------------------------------

import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_summing_example()
    test_counting_example()
    test_draw_row_of_circles()


def test_summing_example():
    """ Tests the   summing_example   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   summing_example   function:')
    print('--------------------------------------------------')

    answer1 = summing_example(2)
    answer2 = summing_example(20)
    answer3 = summing_example(0)

    print('The next line should be:  9  44100  0')
    print(answer1, answer2, answer3)


def summing_example(n):
    """
    Returns (1 cubed) + (2 cubed) + (3 cubed) + ... + (n cubed).
    For example, summing_example(2) returns (1 cubed) + (2 cubed),
                 which is 9, and summing_example(20) returns 44,100.
    Precondition: n is a nonnegative integer.
    """
    total = 0  # Initialize to 0 BEFORE the loop
    for k in range(1, n + 1):  # Loop
        total = total + (k ** 3)  # Accumulate INSIDE the loop.

    return total


def test_counting_example():
    """ Tests the   counting_example   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   counting_example   function:')
    print('--------------------------------------------------')

    answer1 = counting_example(2)
    answer2 = counting_example(20)
    answer3 = counting_example(0)

    print('The next line should be:  1  11  0')
    print(answer1, answer2, answer3)


def counting_example(n):
    """
    Returns the number of integers from 1 to n, inclusive,
    whose cosine is positive.
    For example, counting_example(2) returns 1, and
                 counting_example(20) returns 11, and
                 counting_example(0) returns 0.
    Precondition: n is a nonnegative integer.
    """
    count = 0  # Initialize to 0 BEFORE the loop
    for k in range(1, n + 1):  # Loop
        if math.cos(k) > 0:  # If the condition holds:
            count = count + 1  # Increment INSIDE the loop.

    return count


def test_draw_row_of_circles():
    """ Tests the   draw_row_of_circles   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_row_of_circles   function:')
    print('See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    window1 = rg.RoseWindow(800, 600,
                            'Rows of 7 GREEN & 4 BLUE circles!')
    center = rg.Point(50, 50)
    draw_row_of_circles(7, center, 'green', window1)

    center = rg.Point(100, 150)
    draw_row_of_circles(4, center, 'blue', window1)
    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    window2 = rg.RoseWindow(800, 600, 'Row of 12 RED circles!')
    center = rg.Point(50, 50)
    draw_row_of_circles(12, center, 'red', window2)
    window2.close_on_mouse_click()


def draw_row_of_circles(n, point, color, window):
    """
    Draws n rg.Circles in a row, such that:
      -- The first rg.Circle is centered at the given point.
      -- Each rg.Circle just touches the previous one (to its left).
      -- Each rg.Circle has radius 20.
      -- Each rg.Circle is filled with the given color.
      -- Each rg.Circle is drawn on the given window.

    Preconditions: The first argument is a positive integer,
                   the next argument is an appropriate point
                       inside the given window,
                   the next argument is a zellegraphics color,
                   and the last argument is an appropriate rg.RoseWindow.
    """
    radius = 20

    x = point.x  # Initialize x and y BEFORE the loop
    y = point.y
    for _ in range(n):  # Loop

        # Construct the relevant object,
        # based on the current x, y and other variables.
        point = rg.Point(x, y)
        circle = rg.Circle(point, radius)
        circle.fill_color = color

        # Attach the object to the window's RoseCanvas.
        circle.attach_to(window.initial_canvas)

        # Increment x (and in other problems, other variables)
        # for the thing(s) to draw in the next iteration of the loop.
        x = x + (radius * 2)

    window.render()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
