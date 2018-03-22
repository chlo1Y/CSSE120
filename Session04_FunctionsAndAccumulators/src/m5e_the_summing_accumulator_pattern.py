"""
This module lets you study the ACCUMULATOR pattern for SUMMING.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example.
# BUT: Also run it in the DEBUGGER, for a few iterations of the loop,
#      so that you are sure you see the "accumulating" going on.
# ----------------------------------------------------------------------


def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_squares()


def test_sum_squares():
    """ Tests the   sum_squares   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_squares   function:')
    print('--------------------------------------------------')

    total1 = sum_squares(6)
    print('Returned, expected:', total1, 91)

    total2 = sum_squares(1000)
    print('Returned, expected:', total2, 333833500)


def sum_squares(n):
    """
    Returns the sum of the squares of the integers 1, 2, ... n,
    inclusive, for the given n.

    For example, sum_squares(5) returns
       1 + 4 + 9 + 16 + 25   which is 55.

    Precondition: n is a positive integer.
    """
    total = 0
    for k in range(1, n + 1):
        total = total + (k ** 2)

    return total

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
