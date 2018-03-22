"""
This module demonstrates the INPUT-COMPUTE-OUTPUT pattern.
You can (and should) modify it!

Authors: Susan Computewell (aka John Zelle), modified by David Mutchler,
         Amanda Stouder, Chandan Rupakheti, Claude Anderson,
         their colleagues and ZESUN YANG .  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

#-----------------------------------------------------------------------
# TODO: 2. Play around with this file.  First, run it.
#          Try changing a number, whatever you feel comfortable with,
#          and then run the program again to see the effect.
#          Repeatedly:
#            -- Make a SMALL change, then
#            -- Run the program again, to see the effect of your change.
#
#          You'll probably get red error messages at some point.
#          If so, try briefly to fix them,
#          but fixing errors is what we will learn in the NEXT session.
#          So:
#             ***  IT IS PERFECTLY   OK   IF YOU MESS THIS FILE UP!  ***
#
#  *** YOU ARE ** not ** EXPECTED TO UNDERSTAND EVERYTHING IN HERE.
#  *** Just start getting used to EDITING and RUNNING a PROGRAM.
#
#  *** FULL CREDIT JUST FOR MAKING ** ANY ** CHANGES
#                           AND RUNNING THIS FILE!
#-----------------------------------------------------------------------


def main():
    """
    Calls the     convert_to_...    and     chaos    functions
    to demonstrate them.
    """
    convert_to_METER()

    convert_to_CENTIMETER()
    print()

    chaos()


def convert_to_METER():
    """
    Prompts for and inputs METER
    and prints (on the console) the equivalent CENTIMETER.
    """
    print('-----------------------------------------------------------')
    input_string = input('What is the METER? ')
    METER = float(input_string)
    CENTIMETER = (METER * 100)

    print('That METER is', CENTIMETER, 'CENTIMETER.')


def convert_to_CENTIMETER():
    """
    Prompts  for and inputs a CENTIMENT
    and prints (on the console) the equivalent METER.
    """
    print('-----------------------------------------------------------')
    CENTIMETER = float(input('What is the  CENTIMETER? '))
    METER = (CENTIMETER / 100)

    print('That CENTIMETER is', METER, 'METER.')


def chaos():
    """
    Computes and prints a chaotic sequence of numbers,
    as a function of a number input from the user.
    """
    print('-----------------------------------------------------------')
    print('This function illustrates a (possibly) chaotic sequence.')
    print('-----------------------------------------------------------')

    input_string = input('Enter a number between 0 and 2: ')
    x = float(input_string)

    for k in range(9):
        x = 4 * x * (1 - x)
        print(k, ':  ', x)

    print('-----------------------------------------------------------')
    print('Examine the sequence of numbers in the right column, above.')
    print('Depending on the number you chose between 0 and 1,')
    print('the sequence may or may not appear "chaotic".')
    print('Hint: most numbers yield chaos, but try:')
    print('   0.7435897435897436')
    print('as the number that you input.  Budding mathematicians:')
    print('can you figure out what is special about that number?')

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
