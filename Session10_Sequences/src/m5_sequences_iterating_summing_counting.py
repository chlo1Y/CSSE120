"""
This module lets you practice two forms of the ACCUMULATOR pattern:
  -- SUMMING
  -- COUNTING
where the accumulation is done via ITERATING (i.e., looping)
through a SEQUENCE.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  January 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math

def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_sequence()
    test_count_items_bigger_than()
    test_count_positive_sines()
    test_sum_first_n()


def test_sum_sequence():
    """ Tests the   sum_sequence   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_sequence   function:')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # Here is an example of using an ORACLE for testing, that is, using
    # a separate way of gaining the correct tests as if by "magic".
    # (Look up the Delphic Oracle for the history of this phrase.)
    # The oracle here is the built-in    sum    function.
    # ------------------------------------------------------------------

    sequence1 = [48, -10]
    actual_answer = sum_sequence(sequence1)
    oracle_answer = sum(sequence1)
    print('Testing sum_sequence([48, -10]). ', end='')
    print('Actual, Oracle =', actual_answer, oracle_answer)

    sequence2 = [48, 180, -47.5, 20.5, 88]
    actual_answer = sum_sequence(sequence2)
    oracle_answer = sum(sequence2)
    print('Testing sum_sequence([48, 180, 47.5, 20.5, 88]). ', end='')
    print('Actual, Oracle =', actual_answer, oracle_answer)

    # ------------------------------------------------------------------
    # This test uses a KNOWN answer (here, one easily computed by hand).
    # ------------------------------------------------------------------
    sequence3 = []
    actual_answer = sum_sequence(sequence3)
    known_answer = 0
    print('Testing sum_sequence([]). ', end='')
    print('Actual, Known =', actual_answer, known_answer)


def sum_sequence(sequence):
    """
    Returns the sum of the items in the given sequence.
    Precondition: The items in the sequence are numbers.
    """
    # TODO: 2. Implement and test this function.
    #    You may NOT use the built-in  sum   function in IMPLEMENTING
    #    this function, but the testing code above uses it
    #    as an ORACLE in TESTING this function.
    total = 0
    for k in range(len(sequence)):
        total = total + sequence[k]
    return total


def test_count_items_bigger_than():
    """ Tests the   count_items_bigger_than   function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    print()
    print('--------------------------------------------------')
    print('Testing the   count_items_bigger_than   function:')
    print('--------------------------------------------------')


def count_items_bigger_than(numbers, threshold):
    """
    Returns the number of items in the given sequence of numbers
    that are bigger than the given 'threshold' number.
    For example, if numbers is [45, 84, 32, 70] and threshold is 50,
    then this function returns 2 (since 84 and 70 are bigger than 50).

    Preconditions: the first argument is a sequence of numbers and
                   the second argument is a number.
    """
    # TODO: 3b. Implement and test this function.
    total = 0
    for k in range(len(numbers)):
        if numbers[k] > threshold:
            total = total + 1
    return total


def test_count_positive_sines():
    """ Tests the   count_positive_sines   function. """
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    #
    # NOTE: Some numbers that you might expect to be zero,
    #   for example math.sin(math.pi), are in fact slightly positive.
    #   That is because   math.pi   is not exact (nor is math.sin).
    #   Simply stay away from such test cases in this problem.
    print()
    print('--------------------------------------------------')
    print('Testing the   count_positive_sines   function:')
    print('--------------------------------------------------')


def count_positive_sines(numbers):
    """
    Returns the number of items in the given sequence whose sine
    is positive. For example, since:
       sine(3) is about 0.14
       sine(4) is about -0.76
       sine(5) is about -0.96
       sine(6) is about -0.28
       sine(7) is about 0.66
       sine(8) is about 0.99
       sine(9) is about 0.41
    count_positive_sines([3, 4, 5, 6, 7, 8, 9) returns 4
    and count_positive_sines([3, 6, 8]) returns 2

    Precondition: The argument is a sequence of numbers.
    """
    # TODO: 4b. Implement and test this function.
    total = 0
    for k in range(len(numbers)):
        if math.sin(numbers[k]) > 0:
            total = total + 1
    return total



def test_sum_first_n():
    """ Tests the   sum_first_n   function. """
    # TODO: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_first_n   function:')
    print('--------------------------------------------------')


def sum_first_n(numbers, n):
    """
    Returns the sum of the first n items
    in the given sequence of numbers.
    For example, if numbers is   [48, -10, 50, 5], then:
      - sum_first_n(numbers, 0) returns 0
      - sum_first_n(numbers, 1) returns 48
      - sum_first_n(numbers, 2) returns 38
      - sum_first_n(numbers, 3) returns 88
      - sum_first_n(numbers, 4) returns 93

    Preconditions: the first argument is a sequence of numbers and
                   the second argument is a nonnegative integer
                      less than or equal to the length of the sequence.
    """
    # TODO: 5b. Implement and test this function.
    total = 0
    for k in range(n):
        total = total + numbers[k]
    return total

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
