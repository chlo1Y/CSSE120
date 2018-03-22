"""
This module lets you practice the ACCUMULATOR pattern in classic forms:
   SUMMING:    total = total + number
   COUNTING:   count = count + 1

A subsequent module lets you practice the ACCUMULATOR pattern
in another classic form:
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


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
import math

def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_more_cosines()
    test_count_sines_from()
    test_count_sines_vs_cosines()


def test_sum_more_cosines():
    """ Tests the   sum_more_cosines   function. """
    # Done: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_more_cosines   function:')
    print('--------------------------------------------------')
    answer1 = sum_more_cosines(4, 19)
    answer2 = sum_more_cosines(15, 25)
    answer3 = sum_more_cosines(1, 50)
    print('the sums are', answer1, answer2, answer3)

def sum_more_cosines(m, n):
    """
    Returns the sum of the cosines of the integers m, m+1, m+2, ... n,
    for the given n.

    For example, sum_more_cosines(0, 3) returns
       cos(0) + cos(1) + cos(2) + cos(3)  which is approximately 0.13416
    As another example, sum_more_cosines(-4, 2) returns
       cos(-4) + cos(-3) + cos(-2) + cos(-1) + cos(0) + cos(1) + cos(2)
       which is approximately -0.39533.

    Preconditions: m and n are integers and m <= n.
    """
    # Done: 2b. Implement and test this function.
    total = 0
    for k in range (m, n + 1):
        total = total + math.cos(k)
    return total


def test_count_sines_from():
    """ Tests the   count_sines_from   function. """
    # Done: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   count_sines_from   function:')
    print('--------------------------------------------------')
    a1 = count_sines_from(10, 15)
    a2 = count_sines_from(5, 7)
    a3 = count_sines_from(8, 130)
    print("the number of integers of sines are", a1, a2, a3)

def count_sines_from(m, n):
    """
    Returns the number of integers from m to n, inclusive,
    whose sine is less than 0.5.

    For example, since:
       sine(3) is about 0.14
       sine(4) is about -0.76
       sine(5) is about -0.96
       sine(6) is about -0.28
       sine(7) is about 0.66
       sine(8) is about 0.99
       sine(9) is about 0.41
    count_sines_from(3, 9) returns 5
    count_sines_from(4, 6) returns 3
    count_sines_from(7, 7) returns 0
    count_sines_from(9, 9) returns 1

    Preconditions: m and n are integers and m <= n.
    """
    # Done: 3b. Implement and test this function.

    count = 0
    for k in range(m, n + 1):
        if math.sin(k) < 0.5:
            count = count + 1
    return count

def test_count_sines_vs_cosines():
    """ Tests the   count_sines_vs_cosines   function. """
    # Done: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   count_sines_vs_cosines   function:')
    print('--------------------------------------------------')
    a1 = count_sines_vs_cosines(72)
    a2 = count_sines_vs_cosines(41)
    a3 = count_sines_vs_cosines(15)
    print('these numbers are', a1, a2, a3)

def count_sines_vs_cosines(m):
    """
    Returns the number of integers from -m to m, inclusive,
    whose sine is greater than its cosine.

    For example, since:
       sine(-5) is about 0.96 and cosine(-5) is about 0.28
       sine(-4) is about 0.76 and cosine(-4) is about -0.65
       sine(-3) is about -0.14 and cosine(-3) is about -0.99
       sine(-2) is about -0.91 and cosine(-2) is about -0.42
       sine(-1) is about -0.84 and cosine(-1) is about 0.54
       sine(0) is about 0.00 and cosine(0) is about 1.00
       sine(1) is about 0.84 and cosine(1) is about 0.54
       sine(2) is about 0.91 and cosine(2) is about -0.42
       sine(3) is about 0.14 and cosine(3) is about -0.99
       sine(4) is about -0.76 and cosine(4) is about -0.65
       sine(5) is about -0.96 and cosine(5) is about 0.28
    count_sines_vs_cosines(5) returns 6
    count_sines_vs_cosines(3) returns 4
    count_sines_vs_cosines(0) returns 0
    count_sines_vs_cosines(1) returns 1

    Here's another test case: count_sines_vs_cosines(101) returns 100.

    Precondition: m is a nonnegative integer.
    """
    # Done: 4b. Implement and test this function.
    count = 0
    for k in range (m):
        if math.sin(k) > math.cos(k):
            count = count + 1
    return count


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
