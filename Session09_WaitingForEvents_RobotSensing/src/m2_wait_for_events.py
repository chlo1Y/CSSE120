"""
This module lets you practice the WAIT-FOR-EVENT pattern:
   while True:
       ...
       if <event has occurred>:
           break
       ...
in the context of waiting for INPUT to end.  The input is:
  -- from the user in one problem, and
  -- from a random number generator in another.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random


def main():
    """ Calls the   TEST   functions in this module. """
    test_wait_for_prime()
    test_wait_for_90th_percentile()


# ----------------------------------------------------------------------
# Students: Use this  is_prime  function in your solution below to
#           wait_for_prime.  The function   is_prime   is ALREADY DONE;
#           no need to modify or add to it.
# ----------------------------------------------------------------------
def is_prime(n):
    """
    Returns True if the given integer is prime, else returns False.

    Note: The algorithm used here is simple and clear but slow.

    Precondition:  The given argument is an integer that is at least 2.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


def test_wait_for_prime():
    """ Tests the   wait_for_prime    function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_prime   function:')
    print('--------------------------------------------------')
    wait_for_prime()
    print('second test')
    wait_for_prime()

def wait_for_prime():
    """
    Repeatedly inputs integers from the user (on the console).
    Stops when the user enters any integer that is a prime number
    and returns that (prime) number.

    For the sake of simplicity, assumes that the user always enters
    integers that are at least 2 (so no bad input).

    Here is a sample run, where user input is to the right of
    each colon sign:

       Enter an integer: 45
       Enter an integer: 18
       Enter an integer: 6
       Enter an integer: 21
       Enter an integer: 22
       Enter an integer: 13

    Returns 13
    """
    # TODO: 2b. Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    -- Use (call) the   is_prime   function above appropriately.

    while True:
        a = int(input('eneter a number'))
        if is_prime(a)is True:
            break
    return a



def test_wait_for_90th_percentile():
    """ Tests the   wait_for_90th_percentile    function. """
    # NOTE: We implemented two tests for you.
    #       READ THIS FUNCTION DEFINITION and ASK QUESTIONS as needed.
    # FWIW, one can do some interesting STATISTICAL testing here
    #       pretty easily, despite dealing with random numbers.
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_90th_percentile   function:')
    print('--------------------------------------------------')

    # The following statement sets the random 'seed' so that the
    # random calls are predictable.  Given this particular seed,
    #   wait_for_90th_percentile(1000)
    # should return  the value indicated below on most of your computers
    # (it depends on the version of Python that you are using).
    seed = 411
    random.seed(seed)
    test_random = random.randrange(1000)

    expected_result = 221  # This is the expected result in Python 4.4.

    if test_random != expected_result:
        print('!!!!!!!!!!!!!!!!')
        print('You seemed to use a different random number generator')
        print('than I expected. The test run returned', test_random)
        print('where I expected {}.'.format(expected_result))
        print('Check with your instructor about this.')
        print('The next tests might NOT work for you.')
        print('!!!!!!!!!!!!!!!!')
        print()

    actual_result = wait_for_90th_percentile(1000)

    if actual_result is None:
        print('You returned None (nothing).')

        # Probably the function has not yet been implemented
        # by the student yet, so exit without running any tests.
        return

    expected_result = 7
    print('Returned, expected:', actual_result, expected_result)
    if (actual_result != expected_result):
        print('!!!!!!!!!!!!!!!!')
        print('Your  wait_for_90th_percentile  failed its first test!')
        print('!!!!!!!!!!!!!!!!')
        print()

    trials = 1000
    trials_to_print = 25
    largest_num_to_generate = 10000
    message = 'Each of the following should be ABOUT 10 but can vary lots!'
    print(message)

    total = 0
    for k in range(trials):
        result = wait_for_90th_percentile(largest_num_to_generate)
        if (k % int(trials / trials_to_print)) == 0:
            print(' {:2}'.format(result), end='')
        total = total + result
    print()

    print()
    print('The following average should be quite close to 10:')
    print(total / trials)


def wait_for_90th_percentile(m):
    """
    Repeatedly generates random integers
      per random.randrange(...)
    each of which is in the range [0, m).

    Stops generating random integers when one is generated that is
    in the 90th percentile of the range, that is, when the generated
    random number is greater than or equal to 0.90 * m.

    Returns the number of generated random numbers,
    INCLUDING the randomly generated number that terminates
    generation of random numbers.

    Example:  If m is (say) 70, so that 0.90 * m is 63,
    then this function might generate the following random numbers:
        3  41  24  25  29  60  51  26  1  67
    It would STOP at that point, since 67 >= 63.
    It would RETURN 10 in this example, since 10 numbers were generated.

    Precondition: m is an integer that is at least 10.
      :type m: int
    """
    # TODO: 3. Implement and test this function.
    # Use    random.randrange(m)    to get integers in the range [0, m).
    count = 0

    while True:
        a = random.randrange(m)
        count = count + 1
        if a > 0.90 * m:
            break
    return count



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
