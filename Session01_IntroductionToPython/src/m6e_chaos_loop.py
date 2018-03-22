"""
This is the    chaos   program that John Zelle uses as a first example
in his text, Python Programming - An Introduction to Computer Science.

It shows how to:
  -- Call the   main   function, and how it can CALL other functions.
  -- Use comments:  internal (single-line, using the # sign)
            and docstrings (multi-line, using a triply-quoted string)
  -- Prompt for and input a string, using the    input    function.
  -- Convert a string into a floating-point number (e.g. 3.409),
         using the   float   function
  -- Use variables to store values
  -- Print strings and the values of variables
  -- Call functions
  -- Define functions
  -- Run a LOOP a fixed number of times (a "counting" loop),
         using a FOR statement and a RANGE expression

Authors: John Zelle, modified by David Mutchler, Amanda Stouder,
         Chandan Rupakheti, Claude Anderson and their colleagues.
         December 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do here.  Just use it as an example to see:
#   1. Getting input, computing with it, and printing output.
#   2. Loops
#-----------------------------------------------------------------------


def main():
    """ Calls the   chaos   function to demonstrate it. """
    chaos()


def chaos():
    """
    Computes and prints a chaotic sequence of numbers,
    as a function of a number input from the user.
    """
    print('-----------------------------------------------------------')
    print('This function illustrates a (possibly) chaotic sequence.')
    print('-----------------------------------------------------------')

    input_string = input('Enter a number between 0 and 1: ')
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
