"""
This module lets you practice correcting SYNTAX (notation) errors.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

#-----------------------------------------------------------------------
# TODO: 2.
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
    print_greeting
    print_farewell()


def print_greeting():
    """ Prints a sci-fi greeting. """
    print("Greetings, Earthling")


def print_farewell():
    """ Prints a sci-fi farewell based on an input from the user. """
    s = input('Enter a positive number: ')
    number = int(s)
    print('Farewell, Earthling number', number)
    print('By the way, the square root of your number is', math.sqrt(number))

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
