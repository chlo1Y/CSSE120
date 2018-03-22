"""
This module lets you practice:
  -- calling functions from the  ** current **   module
  -- sending ARGUMENTS to those functions
  -- capturing RETURNED VALUES from those functions, in variables
  -- INPUT and OUTPUT

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """
    Calls the   do_sums   and   do_shared_factors   functions
    to demonstrate and test them.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the   do_sums   function:')
    print('--------------------------------------------------')
    do_sums()
    sum_of_digits(15)
    do_sums()
    x = int(input('key in integer1 '))
    y = int(input('key in integer2'))
    z = int(input('key in integer 3'))
    print('the sum of integer1 is', sum_of_digits(x))
    print('the sum of integer2 is', sum_of_digits(y))
    print('the sum of integer3 is', sum_of_digits(z))
    ab = sum_of_digits(x)
    cd = sum_of_digits(y)
    ef = sum_of_digits(z)
    print('the sum of three sums is', int(ab + cd + ef))
    print('the product of three sum is', int(ab * cd * ef))
    g = int(ab * cd * ef)
    print('the sum of the product is', sum_of_digits(g))

    print()
    print('--------------------------------------------------')
    print('Testing the   do_shared_factors   function:')
    print('--------------------------------------------------')
    M = int(input('give me a number'))
    N = int(input('give me another number'))
    print('the number factors shared by M and N is', number_of_shared_factors(M, N))
    print('the number factors shared by M*M and N*N is', number_of_shared_factors(M * M, N * N))
    print('the number factors shared by M+1 and N+1 is', number_of_shared_factors(M + 1, N + 1))
def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135, this function returns 20.

    Precondition: the given argument is an integer.
    """
    # Do NOT touch this function.  Do NOT copy code from this function.
    # Instead, ** CALL ** this function as needed.
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the green doc-string above.  Treat this function as a black box.
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def do_sums():
    """
    Prompts for and inputs three integers, one at a time
        (i.e., via 3 input statements).
        (The user is responsible for being sure to input integers.
        This function should NOT bother checking for valid input.)
    Then prints (each on its own line):
      -- the sum of the digits of the first integer
      -- the sum of the digits of the second integer
      -- the sum of the digits of the third integer
      -- the sum of those three sums
      -- the product of those three sums
      -- the sum of the digits in that product

    For example, if the user were to input 97, 13 and 204,
    then the function should print (on separate lines):
      16   4   6   26   384   15
    since (16 + 4 + 6) = 26 and (16 * 4 * 6) = 384

    Another example:  if the user were to input 52, 184 and 3000,
    then the function should print (on separate lines):
       7   13   3   23   273   12
    since (7 + 13 + 3) = 23 and (7 * 13 * 3) = 273
    """
    # Done: 2. Implement and test this function.
    #   Implementation requirement: ** CALL**, as many times as needed,
    #   the    sum_of_digits    function that is DEFINED ABOVE.
    #   That function returns the sum of the digits of a given integer.
    #
    # HINT: To test this program:
    #   1. Run it, and actually input 97, 13 and 204.
    #      Confirm that your program prints:
    #         16   4   6   26   384   15
    #      per the example in the comment above.
    #
    #   2. Run it again, and actually input 52, 184 and 3000.
    #         7   13   3   23   273   12
    #   per the second example in the comment above.


def number_of_shared_factors(m, n):
    """
    Returns the number of factors shared by m and n.

    For example, if m is 210 and n is 280, then this function returns 8,
    since   1  2  5  7  10  14  35  and 70  are the 8 integers that
    divide evenly into both 210 and 280.
    """
    # Do NOT touch this function.  Do NOT copy code from this function.
    # Instead, ** CALL ** this function as needed.
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the green doc-string above.  Treat this function as a black box.
    count = 0
    for k in range(1, min(m + 1, n + 1)):
        if m % k == 0 and n % k == 0:
            count = count + 1

    return count


def do_shared_factors():
    """
    Prompts for an inputs two integers M and N, one at a time (i.e.,
    via 2 input statements -- no checking for valid input is necessary).
    Then prints:
      -- the number of factors shared by M and N
      -- the number of factors shared by M*M and N*N
      -- the number of factors shared by M+1 and N+1

    Here are two sample runs (where the inputs are to the right of the
    colon signs, in each sample run).
        Enter an integer: 210
        Enter a second integer: 280
        8
        27
        1

        Enter an integer: 1038
        Enter a second integer: 123450
        4
        9
        1
    """
    # Done: 3. Implement and test this function.
    #   Implementation requirement: ** CALL**, as many times as needed,
    #   the   number_of_shared_factors   function that is DEFINED ABOVE.

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
