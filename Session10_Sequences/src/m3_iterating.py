"""
This module lets you practice the ITERATE-THROUGH-A-SEQUENCE pattern
in its most classic form:
  -- Iterate all the way through the sequence, from beginning to end.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  January 2014.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_count_negative()
    test_count_short_ones()
    test_draw_circles()


def test_count_negative():
    """ Tests the   count_negative   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   count_negative   function:')
    print('--------------------------------------------------')

    # Here is one test case to get you started.
    total1 = count_negative([8, 13, 7, 5])
    print('Returned, expected:', total1, 0)
    total2 = count_negative([-2, -3, 3, 2])
    print('Returned,expected:', total2, 2)
    total3 = count_negative([4, -5, -2, 6, -4])
    print('Returned,expected:', total3, 3)



def count_negative(seq):
    """
    Returns the number of items in the given sequence of numbers
    that are negative.

    Precondition: The argument is a sequence of numbers.
    """
    # TODO: 2b. Implement and test this function.
    total = 0
    for k in range(len(seq)):
        if seq[k] < 0:
            total = total + 1
    return total


def test_count_short_ones():
    """ Tests the   count_short_ones   function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least ** 3 ** tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   count_short_ones   function:')
    print('--------------------------------------------------')

    # Here are 2 test cases to get you started.
    seq = [[3, 5],
           [3, 9, 0, 4],
           [5],
           [5],
           [],
           [9, 8, 7],
           [5, 6]]
    total1 = count_short_ones(seq)
    print('Returned, expected:', total1, 5)

    seq = ['abc', 'a', '', 'foo', 'de', 'dd', 'x', 'foo', 'argh', 'a']
    total2 = count_short_ones(seq)
    print('Returned, expected:', total2, 6)

    # Add your ADDITIONAL test(s) here:
    seq = ['eat', [3], "I have a furry", [8, 9], 'black egg']
    total3 = count_short_ones(seq)
    print('Returned,expected:', total3, 2)

def count_short_ones(seq_of_lists):
    """
    The argument is a sequence of lists.  Returns the number of
    items in that sequence whose length is less than 3.

    For example, if the argument is:
        [ [3, 5],  [3, 9, 0, 4],  [5],  [5],  [],  [9, 8, 7],  [5, 6] ]
    then this function returns 5, since 5 of the 7 lists in the
    above sequence have length less than 3.

    Precondition: The argument is a sequence of lists.
    """
    # TODO: 3b. Implement and test this function.
    total = 0
    for k in range(len(seq_of_lists)):
        if len(seq_of_lists[k]) < 3:
            total = total + 1
    return (total)


def test_draw_circles():
    """ Tests the   draw_circles   function. """
    # We have already supplied two tests for you, on a single window.
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_circles   function:')
    print('--------------------------------------------------')

    window = rg.RoseWindow(400, 300, 'Points to Circles')

    points1 = [rg.Point(200, 100),
               rg.Point(100, 130),
               rg.Point(150, 200)]

    points2 = [rg.Point(50, 50),
               rg.Point(250, 250)]

    draw_circles(window, points1, 25)  # Test 1
    window.continue_on_mouse_click()

    draw_circles(window, points2, 40)  # Test 2
    window.close_on_mouse_click()


def draw_circles(window, points, radius):
    """
    For each point in the given sequence of rg.Points,
    constructs and draws a rg.Circle centered at that point,
    with the given radius, on the given rg.RoseWindow.

    Preconditions:
      :type window: rg.RoseWindow
      :type points: (list, tuple)
      :type radius: (int, float)
    where the second argument is a sequence of rg.Point objects
    and the third argument is a reasonable positive number.
    """
    # TODO: 4. Implement and test this function.
    for k in range(len(points)):
        circle = rg.Circle(points[k], radius)
        circle.attach_to(window.initial_canvas)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
