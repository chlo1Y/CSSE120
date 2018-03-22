"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_cosines()
    test_sum_square_roots()


def test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')
    a = sum_cosines(5)
    print('the sum of cosine is', a)
    a = sum_cosines(6)
    print('the sum of cosine is', a)
    a = sum_cosines(8)
    print('the sum of cosine is', a)


def sum_cosines(n):
    """
    Returns the sum of the cosines of the integers 0, 1, 2, ... n,
    for the given n.

    For example, sum_cosines(3) returns
       cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.

    Precondition: n is a non-negative integer.
    """
    # Done: 2b. Implement and test this function.

    total = 0
    for k in range (0, n + 1):
        total = total + math.cos(int(n))

        return total


def test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')
    a = sum_square_roots(5)
    print('the sum is', a)
    a = sum_square_roots(15)
    print('the sum is', a)
    a = sum_square_roots(18)
    print('the sum is', a)

def sum_square_roots(n):
    """
    Returns the sum of the square roots of the integers
        2, 4, 6, 8, ... 2n    for the given n.
    So if n is 7, the last term of the sum is for 14 (not 7).

    For example, sum_square_roots(5) returns
       sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
    which is about 11.854408.

    Precondition: n is a non-negative integer.
    """
    # TODO: 3b. Implement and test this function.
    total = 0
    for k in range (1, n + 1):
        total = total + math.sqrt(k * 2)

    return total


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
