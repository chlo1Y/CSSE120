"""
This module (in Python, a module is the code in a single file)
demonstrates:

  a. Execution begins at the beginning of the function called   main.

  b. Execution continues line by line (sequentially) except:
      -- When a function is CALLED,
            execution JUMPS to the beginning of that function.
      -- When a function REACHES ITS END (or reaches a RETURN statement)
            execution continues from the point
            at which the function WAS CALLED.
     Note: We will soon see two more exceptions to line-by-line
           execution: LOOPs and IF statements.

  c. DEFINING a function versus CALLING a function.
       -- The former begins     def blah(): ...
       -- The latter uses the notation     blah()    in an expression.

  d. The PRINT statement.

  e. Literal STRINGS like   'Hello!  How are things?'

Authors: Many, many people over many, many years.
         David Mutchler, Amanda Stouder, Chandan Rupakheti,
         and Claude Anderson wrote this version.  December 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do here.  Just use it as an example to see:
#   -- the order in which statements are executed:  sequential,
#      but interrupted by function calls.
#-----------------------------------------------------------------------


def main():
    """ Calls the other functions to demonstrate them. """
    hello()
    goodbye()
    hello()
    hello()

    print('---------------------------------------------')
    print('The remaining output comes from CALLING')
    print('the  hello_and_goodbye  FUNCTION.')
    print('---------------------------------------------')
    hello_and_goodbye()


def hello():
    """ Prints a bad message on the console. """
    print('I lost 5 dollars?')


def goodbye():
    """ Prints a happy message on the console, in 3 languages. """
    print('I found 10 dollars!')
    print('   fand ich 10 Dollar!')
    print('   Wo Zhao Dao le Shi Kuai Qian!')


def hello_and_goodbye():
    """ Prints bad and good messages on the console. """
    hello()
    goodbye()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
