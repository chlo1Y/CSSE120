"""
This module demonstrates and practices:
  -- using ARGUMENTs in function CALLs,
  -- having PARAMETERs in function DEFINITIONs, and
  -- RETURNING a value from a function,
        possibly CAPTURING the RETURNED VALUE in a VARIABLE.

It also lets you contrast PRINTING versus RETURNING.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and ZEsun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.
from m2e_arguments_and_returned_values import sum_of_digits


def main():
    """ Calls the   TEST   functions in this module. """
    test_print_it()
    test_return_it()
    test_digits_in_squares_and_cubes()
    test_digits_in_power()


# ----------------------------------------------------------------------
# The following function has no TODO associated with it,
# so do NOT modify it.  Simply CALL it when you do the TODOs below.
# ASK FOR HELP if you do not know what it means to CALL a function.
# ----------------------------------------------------------------------
def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135, this function returns 20.

    Precondition: the given argument is an integer.
    """
    # Students: While you are welcome to try to understand this
    #           function definition, all you have to do is trust
    #           that the green doc-string is correct (it is!).
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit = number % 10  # Get the digit
        digit_sum = digit_sum + digit  # Accumulate it into the sum
        number = number // 10  # Get ready for the next digit

    return digit_sum


def test_print_it():
    """ Tests the   print_it   function. """
    # Done: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, one of which is n=10.
    #
    # HINT: Testing a function that PRINTS things is easy:
    #       just call the function.  Each call is one test.
    #       We have provided your first test for you.
    print()
    print('--------------------------------------------------')
    print('Testing the   print_it   function:')
    print('--------------------------------------------------')

    # Done: 2b. Change   -999   below to what it should be,
    #           by figuring out BY HAND what the function should print.
    expected = 1
    print('The next line should print', expected)
    print_it(10)
    expected = 49984
    print('The next line should print', expected)
    print_it(5)
    expected = 19084
    print('The next line should print', expected)
    print_it(2)



def print_it(n):
    """
    Given an integer n:
      -- Let X denote the sum of the digits in n ** 1000.
      -- Let Y denote the sum of the digits in n ** 999.
    PRINTs the sum of the digits in X ** Y.

    Test cases that you can use include:
      -- If n is 2, then:
            -- the sum of the digits in n ** 1000 is 1366.
            -- the sum of the digits in n ** 999 is 1367.
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- and the function should print 19084.
      -- If n is 35, then:
            -- the sum of the digits in n ** 1000 is 7021.
            -- the sum of the digits in n ** 999 is 7145.
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- and the function should print 124309.

    Precondition: the given argument is an integer.
    """
    # Done: 2c. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    x = sum_of_digits(n ** 1000)
    y = sum_of_digits(n ** 999)
    result = sum_of_digits(x ** y)
    print('the sum of digits is', result)



def test_return_it():
    """ Tests the   return_it   function. """
    # Todo: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, one of which is m=10.
    #
    # HINT: To test a function that RETURNs a value,
    #       the usual approach is either to:
    #         -- Use a unit testing tool
    #              (more on that in a subsequent lesson), or
    #         -- Call the function, capture the returned value in a
    #              variable, and print the variable's value.
    #              It is helpful to print the "expected" value too.
    #              Each call is one test.
    #       Use the latter approach here.
    #       We have provided part of your first test for you.
    print()
    print('--------------------------------------------------')
    print('Testing the   return_it   function:')
    print('--------------------------------------------------')


    # TODO: 3b. Change   -999   below to what it should be,
    #           by figuring out BY HAND what the function should return.
    answer1 = return_it(10)
    print('Expected, returned:', 1, answer1)
    answer2 = return_it(5)
    print('Expected, returned:', 49984, answer2)
    answer3 = return_it(2)
    print('Expected, returned:', 19084, answer3)


def return_it(m):
    """
    Same specification as for   print_it   (defined above),
    except this function  RETURNs   the sum of the digits in X ** Y
    (where    print_it    PRINTED   that sum).
    """
    # TODO: 3c. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    #
    # *** WHEN YOU ARE DONE WITH THIS PROBLEM, ***
    # *** GET AN ASSISTANT TO CHECK IT!        ***
    x = sum_of_digits(m ** 1000)
    y = sum_of_digits(m ** 999)
#     print("..")
    result = sum_of_digits(x ** y)
#     print("......")
    return(result)

def test_digits_in_squares_and_cubes():
    """ Tests the   digits_in_squares_and_cubes   function. """
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests.
    print()
    print('-----------------------------------------------------')
    print('Testing the   digits_in_squares_and_cubes   function:')
    print('-----------------------------------------------------')
    digits_in_squares_and_cubes(2)
    digits_in_squares_and_cubes(8)
    digits_in_squares_and_cubes(10)


def digits_in_squares_and_cubes(n):
    """
    Given an integer n, prints (on separate lines):
      - the integer and the sum of its digits
      - the integer squared and the sum of the digits in that number
      - the integer cubed and the sum of the digits in that number.
    For example, if the argument is 12, then this function prints:
      12 3
      144 9
      1728 18

    Precondition: the given argument is a positive integer.
    """
    # TODO: 4b. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.

    b = sum_of_digits(n)
    print(n, b)
    print(n ** 2, b)
    print(n ** 3, b)

def test_digits_in_power():
    """ Tests the   digits_in_power   function. """
    # TODO: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   digits_in_power   function:')
    print('--------------------------------------------------')
    digits_in_power(8, 10)
    digits_in_power(3, 2)
    digits_in_power(4, 5)

def digits_in_power(n, k):
    """
    Given integers n and k, returns the sum of the digits
    in n raised to the kth power. For example, if the arguments
    are 12 and 3, respectively, then this function returns 18
    since 12 to the 3rd power is 1728 (whose digits sum to 18).

    Preconditions: the arguments are positive integers.
    """
    # TODO: 5b. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.

    answer = sum_of_digits(n ** k)
    print('the answer is', answer)
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
