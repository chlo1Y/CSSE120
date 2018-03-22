"""
This module lets you practice the ACCUMULATOR pattern
in several classic forms:
   SUMMING:    total = total + number
   COUNTING:   count = count + 1
   AVERAGING:  summing and counting combined
and
   FACTORIAL:  x = x * k

Subsequent modules let you practice the ACCUMULATOR pattern
in its "in graphics" form:
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun yang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import random
import builtins  # Never necessary, but here for pedagogical reasons


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_from()
    test_factorial()
    test_count_cosines_from()
    test_average()
    test_sum_unit_fractions_from()


# ----------------------------------------------------------------------
# Students: This test function is ALREADY DONE.
#           READ IT, but no need to modify or add to it.
#    BUT:
#    Ask for help if you do not understand from the example below
#       what an ORACLE answer is, and what a KNOWN answer is,
#       and what a FORMULA answer is, and how they are used in testing.
# ----------------------------------------------------------------------
def test_sum_from():
    """ Tests the   sum_from   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_from   function:')
    print('--------------------------------------------------')

    # These first two tests use an ORACLE for testing.
    #   The oracle here is the built-in    sum    function.
    actual_answer = sum_from(6, 9)
    oracle_answer = builtins.sum(range(6, 10))
    test_case = 'sum_from(6, 9).  Actual, Oracle answers:'
    print('   Called ', test_case, actual_answer, oracle_answer)

    actual_answer = sum_from(100, 10000)
    oracle_answer = builtins.sum(range(100, 10001))
    test_case = 'sum_from(100, 10000).  Actual, Oracle answers:'
    print('   Called ', test_case, actual_answer, oracle_answer)

    # This test uses a KNOWN answer
    #   (Everyone "knows" that the sum from 0 to 0 is 0.)
    actual_answer = sum_from(0, 0)
    known_answer = 0
    test_case = 'sum_from(0, 0).  Actual, Known answers:'
    print('   Called ', test_case, actual_answer, known_answer)

    # This test uses a FORMULA answer
    #   (which is a kind of ORACLE answer) that uses the formula:
    #     m + (m+1) + (m+2) +  ...  + n  =  (m + n) * (n - m + 1) / 2
    actual_answer = sum_from(53, 4999)
    formula_answer = (53 + 4999) * (4999 - 53 + 1) // 2
    test_case = 'sum_from(53, 4999).  Actual, Formula answers:'
    print('   Called ', test_case, actual_answer, formula_answer)


def sum_from(m, n):
    """
    Returns the sum of the integers from m to n, inclusive.
    For example, sum_from(6, 9) returns 6 + 7 + 8 + 9, that is, 30.

    Precondition: m and n are integers and m <= n.
    """
    # Done: 2. Implement and test this function
    #          using an explicit    for ... in range(...)     statement.
    total = 0
    for k in range(m, n + 1):
        total = total + k
    return total

def test_factorial():
    """ Tests the   factorial   function. """
    # Done: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.
    #
    # ** Use the  math.factorial  function as an ORACLE for testing. **
    print()
    print('--------------------------------------------------')
    print('Testing the   factorial   function:')
    print('--------------------------------------------------')
    a1 = factorial(10)
    a2 = factorial(21)
    a3 = factorial(36)
    a4 = factorial(5)
    print('the factorials are', a1, a2, a3, a4)



def factorial(n):
    """
    Returns n!, that is, n x (n-1) x (n-2) x ... x 1.
    For example, factorial(5) returns 5 x 4 x 3 x 2 x 1, that is, 120.

    Precondition: n is a non-negative integer.
    """
    # Done: 3b. Implement and test this function
    #          using an explicit    for ... in range(...)     statement.
    total = 1
    for k in range(1, n + 1):
        total = total * k
    return total


def test_count_cosines_from():
    """ Tests the   count_cosines_from   function. """
    # Done: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   count_cosines_from   function:')
    print('--------------------------------------------------')
    a1 = count_cosines_from(3, 7, 0.24)
    a2 = count_cosines_from(2, 7, 0.3)
    a3 = count_cosines_from(5, 12, 0.5)
    a4 = count_cosines_from(6, 9, 0.1)
    print("the # of integers greater than 0.24 is", a1)
    print("the # of integers greater than 0.3 is", a2)
    print("the # of integers greater than 0.5 is", a3)
    print("the # of integers greater than 0.1 is", a4)



def count_cosines_from(m, n, x):
    """
    Returns the number of integers from m to n, inclusive,
    whose cosine is greater than x.
    For example, since:
       cosine(3) is about -0.99
       cosine(4) is about -0.65
       cosine(5) is about 0.28
       cosine(6) is about 0.96
       cosine(7) is about 0.75
       cosine(8) is about -0.15
       cosine(9) is about -0.91
    count_cosines_from(3, 9, 0.29) returns 2
    count_cosines_from(3, 9, 0.27) returns 3
    count_cosines_from(4, 8, -0.5) returns 4

    Precondition: m and n are integers and m <= n, and x is a number.
    """
    # Done: 4b. Implement and test this function.
    count = 0
    for k in range(m, n + 1):
        if math.cos(k) > x:
            count = count + 1
    return count

def test_average():
    """ Tests the   average   function. """
    # Done: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.
    # HINT: Since the function to be tested is not deterministic,
    #       your tests may need to be STATISTICAL tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   average   function:')
    print('--------------------------------------------------')

    # This is one way to test a randomized function.
    # Here, we set the "seed" to a particular (but arbitrary) value.
    # That determines the sequence of pseudo-random numbers
    # that will be generated.  So, assuming that the function generates
    # the psuedo-random numbers per that sequence, an oracle
    # can predict the answer.
    random.seed(42)

    # Test 1:
    avg = average(3, 100)
    print()
    print('You returned', avg)
    print('If you used the same random sequence as I did (as is likely),')
    print('Then the above should be about 32.666666666666664')

    # Test 2:
    avg = average(5, 10)
    print()
    print('You returned', avg)
    print('If you used the same random sequence as I did (as is likely),')
    print('Then the above should be about 2.6')

    # Done: Add two more STATISTICAL tests here:
    # Test 3:
    avg = average(4, 65)
    print()
    print('you returned', avg)
    print('If you used the same random sequence as I did (as is likely),')
    print('Then the above should be about 2.6')

    # Test 4:
    avg = average(7, 87)
    print('You returned', avg)
    print('If you used the same random sequence as I did (as is likely),')
    print('Then the above should be about 2.6')





def average(n, r):
    """
    Selects n random integers, each in the range [0, r).
    (That is, from 0 to r, but not including r.)
    Returns the AVERAGE of the selected numbers,
    that is, the SUM of the numbers divided by the NUMBER of numbers.

    Preconditions: n and r are positive integers.
    """
    # Done: 5b. Implement and test this function.
    #    HINT: Use the    random.randrange   function:
    #          random.randrange(0, r) returns a random number
    #          in the range [0, r).
    total = 0
    for k in range(0, n):
        a = random.randrange(0, r)
        total = total + a
    aaa = total / n
    return aaa

def test_sum_unit_fractions_from():
    """ Tests the   sum_unit_fractions_from   function. """
    # Done: 6a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_unit_fractions_from   function:')
    print('--------------------------------------------------')
    answer1 = sum_unit_fractions_from(4, 7)
    print("the sum is", answer1)
    answer2 = sum_unit_fractions_from(2, 7)
    print("the sum is", answer2)
    answer3 = sum_unit_fractions_from(9, 15)
    print("the sum is", answer3)
    answer4 = sum_unit_fractions_from(4, 10)
    print("the sum is", answer4)


def sum_unit_fractions_from(m, n):
    """
    Returns the sum of 1/m + 1/(m+1) + 1/(m+2) + ... + 1/n.
    For example, sum_unit_fractions_from(6, 9) returns
       1/6 + 1/7 + 1/8 + 1/9, which is about 0.545635.

    Precondition: m and n are positive integers and m <= n.
    """
    # Done: 6b. Implement and test this function.

    total = 0
    for k in range(m, n + 1):
        total = total + 1 / k
    return total

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
