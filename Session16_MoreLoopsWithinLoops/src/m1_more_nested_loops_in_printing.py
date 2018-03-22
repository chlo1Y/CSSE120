"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  May 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    test_triangle_right_justified()
    test_triangle_upside_down()
    test_numbers_constant_forward()
    test_numbers_constant_backwards()
    test_numbers_increasing_forward()


def test_triangle_right_justified():
    """ Tests the    triangle_right_justified    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   TRIANGLE_RIGHT_JUSTIFIED   function:')
    print('--------------------------------------------------')

    print('Test 1 of triangle_right_justified: (5)')
    triangle_right_justified(5)

    print('Test 2 of triangle_right_justified: (1)')
    triangle_right_justified(1)

    print('Test 3 of triangle_right_justified: (3)')
    triangle_right_justified(3)

    print('Test 4 of triangle_right_justified: (6)')
    triangle_right_justified(6)


def triangle_right_justified(r):
    """
    Prints a triangle of numbers, with r rows.
    It looks the same as the previous example, but right-justified.
    So the first row has some spaces, then a 1,
    the 2nd row has some spaces, then a 12,
    the 3rd row has some spaces, then a 123,
    and so forth, in such a way that the rightmost numbers line up.
    For example, when r = 5:
           1
          12
         123
        1234
       12345
    Precondition:  r is a non-negative integer.
    For purposes of "lining up", assume r is a single digit.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # HINT: Do the following problem FIRST, then convert x's to spaces:
    #          xxxx1
    #          xxx12
    #          xx123
    #          x1234
    #          12345
    #
    # HINT: One way to solve this problem is to have TWO inner loops,
    #       one after the other.
    #
    # IMPLEMENTATION RESTRICTION:
    #   ** You may NOT use string multiplication **
    #   in this or the following problems, as doing so would defeat
    #   the goal of providing practice at loops within loops.
#     ------------------------------------------------------------------
    for z in range(r):
        for k in range(r - z - 1):
            print(' ', end='')
        for j in range(1, z + 2):
            print(j, end='')
        print()

def test_triangle_upside_down():
    """ Tests the    triangle_upside_down    function. """
    print()
    print('----------------------------------------------')
    print('Testing the   TRIANGLE_UPSIDE_DOWN   function:')
    print('----------------------------------------------')

    print('Test 1 of triangle_upside_down: (5)')
    triangle_upside_down(5)

    print('Test 2 of triangle_upside_down: (1)')
    triangle_upside_down(1)

    print('Test 3 of triangle_upside_down: (3)')
    triangle_upside_down(3)

    print('Test 4 of triangle_upside_down: (6)')
    triangle_upside_down(6)


def triangle_upside_down(r):
    """
    Prints a triangle of numbers, with r rows.
    It looks the same as the previous problem,
    but with rows in reversed order.  For example, when r = 5:
       12345
        1234
         123
          12
           1
    Precondition:  r is a non-negative integer.
    For purposes of "lining up", assume r is a single digit.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   ** You may NOT use string multiplication **
    #   in this or the following problems, as doing so would defeat
    #   the goal of providing practice at loops within loops.
    # ------------------------------------------------------------------
    for k in range(r):
        for z in range(k):
            print(' ', end='')
        for x in range(1, r - k + 1):
            print(x, end='')
        print()


def test_numbers_constant_forward():
    """ Tests the    numbers_constant_forward    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   NUMBERS_CONSTANT_FORWARD   function:')
    print('--------------------------------------------------')

    print('Test 1 of numbers_constant_forward: (4, 7, 3)')
    numbers_constant_forward(4, 7, 3)

    print('Test 2 of numbers_constant_forward: (3, 5, 8)')
    numbers_constant_forward(3, 5, 8)

    print('Test 3 of numbers_constant_forward: (1, 5, 4)')
    numbers_constant_forward(1, 5, 4)

    print('Test 4 of numbers_constant_forward: (7, 3, 4)')
    numbers_constant_forward(7, 3, 4)


def numbers_constant_forward(r, maxnum, n):
    """
    Prints a rectangle of numbers, with r rows.
    Each row has n 1s, then n 2s, then n 3s, etc. up to n maxnum's.
    For example, when r = 4, maxnum = 7 and n = 3:
       111222333444555666777
       111222333444555666777
       111222333444555666777
       111222333444555666777
    Notice that there were r = 4 rows;
    each row had numbers that went from 1 to maxnum = 7; and
    there were n occurrences of each number on each row.
    Here is another example,
    when r = 3, maxnum = 5 and n = 8:
       1111111122222222333333334444444455555555
       1111111122222222333333334444444455555555
       1111111122222222333333334444444455555555
    Preconditions:  r, maxnum and n are positive integers.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # HINT: What loop structure do you need for this problem?
    #
    # IMPLEMENTATION RESTRICTION:
    #   ** You may NOT use string multiplication **
    #   in this or the following problems, as doing so would defeat
    #   the goal of providing practice at loops within loops.
    # ------------------------------------------------------------------
    for k in range(r):
        for r in range(1, maxnum + 1):
            for j in range(n):
                print(r, end='')
        print()
    print()




def test_numbers_constant_backwards():
    """ Tests the    numbers_constant_backwards    function. """
    print()
    print('----------------------------------------------------')
    print('Testing the   NUMBERS_CONSTANT_BACKWARDS   function:')
    print('----------------------------------------------------')

    print('Test 1 of numbers_constant_backwards: (4, 7, 3)')
    numbers_constant_backwards(4, 7, 3)

    print('Test 2 of numbers_constant_backwards: (3, 5, 8)')
    numbers_constant_backwards(3, 5, 8)

    print('Test 3 of numbers_constant_backwards: (1, 5, 4)')
    numbers_constant_backwards(1, 5, 4)

    print('Test 4 of numbers_constant_backwards: (7, 3, 4)')
    numbers_constant_backwards(7, 3, 4)


def numbers_constant_backwards(r, maxnum, n):
    """
    Prints a rectangle of numbers, with r rows.
    It looks the same as the previous problem, but with
    numbers reversed. For example, when r = 4, maxnum = 7 and n = 3:
       777666555444333222111
       777666555444333222111
       777666555444333222111
       777666555444333222111
    Preconditions:  r, maxnum and n are positive integers.
    """
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   ** You may NOT use string multiplication **
    #   in this or the following problems, as doing so would defeat
    #   the goal of providing practice at loops within loops.
    # ------------------------------------------------------------------
    for k in range(r):
        for j in range(maxnum, 0, -1):
            for t in range(n):
                print(j, end='')
        print()
    print()



def test_numbers_increasing_forward():
    """ Tests the    numbers_increasing_forward    function. """
    print()
    print('----------------------------------------------------')
    print('Testing the   NUMBERS_INCREASING_FORWARD   function:')
    print('----------------------------------------------------')

    print('Test 1 of numbers_increasing_forward: (4, 3)')
    numbers_increasing_forward(4, 3)

    print('Test 2 of numbers_increasing_forward: (2, 7)')
    numbers_increasing_forward(2, 7)

    print('Test 3 of numbers_increasing_forward: (5, 6)')
    numbers_increasing_forward(5, 6)

    print('Test 4 of numbers_increasing_forward: (1, 7)')
    numbers_increasing_forward(1, 7)

    print('Test 5 of numbers_increasing_forward: (2, 1)')
    numbers_increasing_forward(2, 1)


def numbers_increasing_forward(r, maxnum):
    """
    Prints a rectangle of numbers, with r rows, as in the previous
    two problems.  But now each row has one 1, two 2s, three 3s,
    four 4s, etc up to the given maxnum.
    For example, when r = 4 and maxnum = 3:
       122333
       122333
       122333
       122333
    Another example, when r = 2 and maxnum = 7:
       1223334444555556666667777777
       1223334444555556666667777777
    Preconditions:  r and maxnum are positive integers.
    """
    # ------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   ** You may NOT use string multiplication **
    #   in this or the following problems, as doing so would defeat
    #   the goal of providing practice at loops within loops.
    # ------------------------------------------------------------------
    for k in range(r):
        for j in range(1, maxnum + 1):
            for z in range(j):
                print(j, end='')
        print()
    print()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
