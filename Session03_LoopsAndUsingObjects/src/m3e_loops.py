"""
This module lets you study simple FOR loops using RANGE expressions:
    -- With one argument: range(x)
    -- With two arguments: range(x, y)
    -- With three arguments: range(x, y, z)

The bodies of these loops just PRINT things, but of course the bodies
of the loops could do whatever you want them to.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example.
#-----------------------------------------------------------------------

import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    loop_through_ranges()
    loop_more_than_one_way()


def loop_through_ranges():
    """
    Loops through certain ranges,
    printing the elements of the range and their sines.
    """
    print()
    print('Looping through range(10)')
    for k in range(10):
        print(k, '   ', math.sin(k))

    print()
    print('Looping through range(3, 7)')
    for k in range(3, 7):
        print(k, '   ', k * k)

    print()
    print('Looping through range(3, 20, 4)')
    for k in range(3, 20, 4):
        print(k, '   ', 5 + 3 * k)

    print()
    print('Looping through range(20, -10, -5)')
    for k in range(20, -10, -5):
        print(k, '   ', math.sin(k))

    print()
    print('Looping through range(10, 20, -5) [probably an "oops"]')
    for k in range(10, 20, -5):
        print(k, '   ', math.sin(k))


def loop_more_than_one_way():
    """
    Produces the numbers   100 90 80 ... 0
    using four DIFFERENT ways to think about how to solve
    problems that involve a loop.
    """
    print()
    print('Producing 100 90 80 ... 0 one way.')
    for k in range(100, -1, -10):
        print(k)

    print()
    print('Producing 100 90 80 ... 0 another way.')
    for k in range(11):
        print(100 - (k * 10))

    print()
    print('Producing 100 90 80 ... 0 yet another way.')
    for k in range(0, 101, 10):
        print(100 - k)

    print()
    print('Producing 100 90 80 ... 0 still another way.')
    m = 100
    for k in range(11):
        print(m)
        m = m - 10

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
