"""
This module shows how to:
  -- DEFINE a function with a PARAMETER
  -- CALL that function with an ACTUAL ARGUMENT
  -- RETURN a value from a function, and
     CAPTURE that returned value in a VARIABLE

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti,
         Claude Anderson, Katie Dion, Delvin Defoe, Curt Clifton
         and their colleagues, based on the work of Jacob Bernoulli
         and other mathematicians.  December 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example to see:
#           how functions that YOU write (like those in this file)
#                -- can call OTHER functions that YOU write
#                -- can call functions in other modules
#                     (like the math module)
#                -- can use RETURNED VALUES from functions.
#-----------------------------------------------------------------------
import math


def main():
    """ Calls the other functions herein to demonstrate them. """
    print_exp(4.5, 3)
    print_exp(4.5, 10)

    total1 = return_exp(4.5, 3)
    total2 = return_exp(4.5, 15)
    total3 = return_exp(4.5, 100)
    print()
    print('Three approximations are:', total1, total2, total3)
    print('My computer claims that e to the 4.5th power is: ',
          math.pow(math.e, 4.5))

    lousy_approximation = return_exp(1, 2)
    good_approximation = return_exp(1, 1000)
    print()
    print('A lousy approximation of e is:', lousy_approximation)
    print('A good approximation of e is: ', good_approximation)
    print('My computer claims that e is: ', math.e)


def print_exp(x, n):
    """
    Prints the sums:
       0
       0  +  (x / 1!)
       0  +  (x / 1!)  +  (x**2 / 2!)
       0  +  (x / 1!)  +  (x**2 / 2!)  +  (x**3 / 3!)
         ...
       0  +  (x / 1!)  +  (x**2 / 2!)  +  (x**3 / 3!)  +
                                                   ... +  (x**n / n!)
    where n! is (n factorial), that is, n * (n-1) * (n-2) * ... * 2 * 1.

    It so happens that these sums
    are increasingly good approximations to    (e ** x)
    (that is, e raised to the xth power, where e is about 2.618).
    """
    print()
    print('Here are some approximations of e to the', x, 'th power:')
    total = 0
    for k in range(n + 1):
        total = total + ((x ** k) / math.factorial(k))
        print(k, ':', total)


def return_exp(x, n):
    """
    RETURNs the sum:
       0  +  (x / 1!)  +  (x**2 / 2!)  +  (x**3 / 3!)  +
                                                   ... +  (x**n / n!)
    where n! is (n factorial), that is, n * (n-1) * (n-2) * ... * 2 * 1.

    It so happens that this sum is a good approximation to (e ** x)
    (that is, e raised to the xth power, where e is about 2.618),
    when n is large.
    """
    total = 0
    for k in range(n + 1):
        total = total + ((x ** k) / math.factorial(k))

    return total

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
