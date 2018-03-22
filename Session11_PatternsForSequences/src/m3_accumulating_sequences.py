"""
This module lets you practice BUILDING-UP a new SEQUENCE,
one item at a time, using the ACCUMULATOR pattern.
  -- We will later see a more efficient way to build-up and/or modify
        sequences, namely by MUTATING their elements.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  January 2014.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the various   TEST   functions in this module. """
    test_make_simple_list()
    test_make_simple_string()
    test_make_less_simple_string()
    test_draw_shapes()
    test_rectangles_from_circles()


def test_make_simple_list():
    """ Tests the   make_simple_list    function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   make_simple_list   function:')
    print('--------------------------------------------------')
    a1 = make_simple_list(5, 13)
    print(a1)
    a2 = make_simple_list(7, 16)
    print(a2)

def make_simple_list(m, n):
    """
    Returns the list [m, m+1, m+2, ... n],
        where m and n are the given arguments.
    For example, if m is 5 and n is 13, then this function returns:
        [5, 6, 7, 8, 9, 10, 11, 12, 13]

    Precondition: The arguments are integers with m <= n.
    """
    # TODO: 2b. Implement and test this function.
    simple_list = [m]
    for k in range(m + 1, n + 1):
        simple_list = simple_list + [k]

    return simple_list


def test_make_simple_string():
    """ Tests the   make_simple_string    function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   make_simple_string   function:')
    print('--------------------------------------------------')
    a1 = make_simple_string(5, 13)
    print(a1)
    a2 = make_simple_string(7, 16)
    print(a2)

def make_simple_string(m, n):
    """
    Returns the STRING whose characters are m, m+1, m+2, ... n,
    each with a '-' character after it, where m and n are the given
    arguments.  For example, if m is 5 and n is 13, then this function
    returns:  '5-6-7-8-9-10-11-12-13-'.

    Precondition: The arguments are integers with m <= n.
    """
    # TODO: 3b. Implement and test this function.
    simple_string = ''
    for k in range(m, n + 1):
        simple_string = simple_string + str(k) + '-'
    return simple_string



def test_make_less_simple_string():
    """ Tests the   make_less_simple_string    function. """
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   make_less_simple_string   function:')
    print('--------------------------------------------------')
    a1 = make_less_simple_string(5, 13)
    print(a1)
    a2 = make_less_simple_string(205, 205)
    print(a2)

def make_less_simple_string(m, n):
    """
    Same as the previous problem, but WITHOUT the hyphen after the
    last number.  That is, hyphens are BETWEEN the numbers.
    For example:
      -- If m is 5 and n is 13, then this function returns:
              '5-6-7-8-9-10-11-12-13'
      -- If m and n are both 205, then this function returns:
              '205'
    """
    # TODO: 4b. Implement and test this function.
    less_simple_string = str(m)
    for k in range(m + 1, n + 1):
        less_simple_string = less_simple_string + '-' + str(k)
    return less_simple_string


def test_draw_shapes():
    """ Tests the   draw_shapes    function. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   draw_shapes   function:')
    print('-----------------------------------------------------------')
    print('See the graphics window that pops up.')
    print('It should show 3 circles: red, white and blue.')
    print()
    print('Then it should ask the user to click the mouse to continue')
    print('Then it should show 4 more shapes: a green circle,')
    print('  a yellow rectangle, a red circle and a thick black line.')

    # Test 1 is ALREADY DONE (here).
    window = rg.RoseWindow(500, 330, 'draw_shapes, two tests')
    circles = [rg.Circle(rg.Point(50, 50), 50),
               rg.Circle(rg.Point(120, 50), 20),
               rg.Circle(rg.Point(250, 170), 130)]

    circles[0].fill_color = 'red'
    circles[1].fill_color = 'white'
    circles[2].fill_color = 'blue'

    draw_shapes(circles, window)
    window.continue_on_mouse_click()

    # Test 2 is ALREADY DONE (here).
    # It runs in the same window as Test 1.
    # The bottom circle should appear only PARTIALLY in the window;
    # that is purposeful.
    various = [rg.Circle(rg.Point(400, 50), 30),
               rg.Rectangle(rg.Point(350, 100), 100, 100),
               rg.Circle(rg.Point(400, 300), 80),
               rg.Line(rg.Point(0, 0), rg.Point(100, 330))]
    various[0].fill_color = 'green'
    various[1].fill_color = 'yellow'
    various[2].fill_color = 'red'
    various[3].thickness = 10


    draw_shapes(various, window)

    window.close_on_mouse_click()


def draw_shapes(shapes, window):
    """
    For each shape in the given sequence of rg.Shape items,
      1. Attaches the shape to the given window.
      2. Renders the shape with a 0.3 pause after each render.

    Preconditions:
      :type shapes: (list, tuple)
      :type window: rg.RoseWindow
    where the first argument is a sequence of rg.Shape items.
    """
    # TODO: 5. Implement and test this function.
    #
    # HINT: the same   attach_to   method works for ALL the rosegraphics
    # shapes!  FWIW: The word for ideas like this is "polymorphism".
    for k in range():
        
        
    


def test_rectangles_from_circles():
    """ Tests the   rectangles_from_circles    function. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   rectangles_from_circles   function:')
    print('-----------------------------------------------------------')
    print('See the graphics window that pops up.')
    print('It should show circles, then the circles circumscribed,')
    print('then more circles, then the new circles circumscribed too.')
    print('See   rectangles_from_circles.pdf   in this project')
    print('for pictures of the anticipated results.')

    # ------------------------------------------------------------------
    # Test 1 is ALREADY DONE (here).
    # ------------------------------------------------------------------
    window = rg.RoseWindow(650, 350,
                           'rectangles_from_circles, two tests')
    circles = [rg.Circle(rg.Point(50, 80), 40),
               rg.Circle(rg.Point(150, 50), 30),
               rg.Circle(rg.Point(300, 100), 50),
               rg.Circle(rg.Point(220, 70), 60)]
    circles[0].fill_color = 'red'
    circles[1].fill_color = 'white'
    circles[2].fill_color = 'blue'
    circles[3].fill_color = 'green'

    # ------------------------------------------------------------------
    # This test calls the   draw_shapes   function that YOU write,
    # above.  So if your   draw_shapes   breaks, so will this test.
    # ------------------------------------------------------------------
    draw_shapes(circles, window)

    message = 'The circles to be circumscribed are shown above.'
    message = message + '  Click to continue.'
    window.continue_on_mouse_click(message)

    rectangles = rectangles_from_circles(circles)

    draw_shapes(rectangles, window)
    message = 'Now you should see the circumscribing rectangles too.'
    window.continue_on_mouse_click(message)

    # ------------------------------------------------------------------
    # Test 2 is ALREADY DONE (here).
    # It runs in the same window as Test 1.
    # ------------------------------------------------------------------
    circles = []
    center = rg.Point(50, 150)
    radius = 35
    for _ in range(10):
        circle = rg.Circle(center, radius)
        circle.fill_color = 'magenta'
        circles = circles + [circle]
        center.x = center.x + 2 * radius
        center.y = center.y + 15
        radius = radius - 3

    draw_shapes(circles, window)
    message = 'More circles to be circumscribed are shown above.'
    message = message + '  Click to continue.'
    window.continue_on_mouse_click(message)

    rectangles = rectangles_from_circles(circles)

    draw_shapes(rectangles, window)
    message = 'Now you should see the circumscribing rectangles too.'
    message = message + '  Click to continue.'

    window.continue_on_mouse_click(message, close_it=True)


def rectangles_from_circles(circles):
    """
    See   rectangles_from_circles.pdf   in this project for pictures
    that may help you better understand the following specification:

    RETURNs a list of rectangles, where each rectangle circumscribes
    its corresponding circle in the given list of circles.

    Preconditions:
      :type circles: (list, tuple)
    where the argument is a sequence of rg.Circle shapes.
    """
    # TODO: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    #
    # IMPORTANT: Examine the testing code above carefully.  Be sure
    #            that you understand WHY the tests are adequate tests!
    #
    # IMPORTANT: The specification does NOT say to draw anything
    #            in this function, so DON'T draw anything in here!

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
