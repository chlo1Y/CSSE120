"""
This module lets you practice:
  -- calling functions from the MATH and RANDOM modules
  -- sending ARGUMENTS to those functions
  -- capturing RETURNED VALUES from those functions, in variables
  -- INPUT and OUTPUT

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import random


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # TODO: 2. Implement and test this function.
    input_angle()
    random_stuff()

def input_angle():
    """
    Prompts for and inputs an angle
    (in radians, the default units for all the trigonometric functions),
    and prints (each on its own line):
      -- the sine of that angle
      -- the cosine of that angle
      -- the sum of the squares of that sine and cosine
             (which should yield 1, as you learned in trigonometry)
      -- the minimum of that sine and cosine

    Warning:  The specification calls for printing ONLY those items.
    Printing anything else violates the specification.

    Here are two sample runs (where the input is to the right of the
    colon sign, in each sample run).
        Enter an angle (in radians): 1.04
        0.8624042272433384
        0.5062202572327784
        1.0
        0.5062202572327784

        Enter an angle (in radians): 3.14
        0.0015926529164868282
        -0.9999987317275395
        0.9999999999999999
       -0.9999987317275395

    """
    # Done: 3. Implement and test this function.
    # Hint:  Use the builtins   min   function as needed.


    angle = float(input('what is the angle'))
    sine = math.sin(angle)
    print('the sine of the angle is', sine)
    cosine = math.cos(angle)
    print('the cosine of the angle is', cosine)
    sum1 = (sine ** 2) + (cosine ** 2)
    print('the sum of squares of sine and cosine is', sum1)
    minimum = min(sine, cosine)
    print('the minimum is', minimum)

def random_stuff():
    """
    Calls the   random.uniform   function 3 times to get 3 pseudo-random
    numbers (see example below).  The first pseudo-random number should
    be between -10 and 30 (and will be, via the example line that we
    supplied below).  The second should be between 0 and 20.  The
    third should be between -5 and 40.
    This function then prints:
      -- the 3 random numbers (all 3 on one line, separated by spaces)
      -- the minimum of the 3 random numbers (on the next line)
      -- the maximum of the 3 random numbers (on the line after that)
    Warning:  The specification calls for printing ONLY those items.
    Printing anything else violates the specification.

    Here are two sample runs:
        17.064833733360388 10.481563768407767 -1.8918286255179821
        -1.8918286255179821
        17.064833733360388

        6.868767317876539 0.8015143920196866 6.833367477059385
        0.8015143920196866
        6.868767317876539
    """
    # Done: 4. Implement and test this function.
    #          We already wrote the first line for you.
    # Hint:  Use the builtins   min   and   max   functions as needed.
    random1 = random.uniform(-10, 30)
    random2 = random.uniform(0, 20)
    random3 = random.uniform(-5, 40)
    print('all three numbers', random1, random2, random3)
    print('the minimum is', min(random1, random2, random3))
    print('the maxmium is', max(random1, random2, random3))
#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
