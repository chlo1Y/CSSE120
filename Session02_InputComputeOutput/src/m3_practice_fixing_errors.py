"""
This module lets you practice correcting SYNTAX (notation) errors.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

#-----------------------------------------------------------------------
# Done: 2.
#   Locate the syntax errors in this file by looking for red Xs
#   to the left of the line numbers.
#
#   For each error, try to make sense of its message.
#     -- Hover or expand as needed -- make sure you see the message!
#
#   Then fix the errors, one by one.
#     -- Fixing one error may bring up additional errors.
#     -- Sometimes the error is on the line just BEFORE
#          the line with a red X.
#
#    Finish by running the corrected program
#    and making sure that it runs correctly.
#-----------------------------------------------------------------------

def main():
    """ Calls the other functions to demonstrate and/or test them. """
    print_greeting()
    circle_area()


def print_greeting():
    """ Prints a slang greeting. """
    print('Whuz up, kiddo?')


def circle_area():
    """ Inputs the radius of a circle and prints its area. """
    input_string = input("What is the radius of the circle? ")
    radius = float(input_string)
    area = math.pi * radius ** 2
    print('The area is', area)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
