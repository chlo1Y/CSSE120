"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_powers()
    test_sum_powers_in_range()


def test_sum_powers():
    """ Tests the   sum_powers   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')
    sum_powers(2, 6.3)
    sum_powers(3, 8)
    sum_powers(4, 7)

def sum_powers(n, p):
    """
    Returns the sum      1**p + 2**p + 3**p + ... + n**p
    for the given numbers n and p.  The latter may be any number
    (possibly a floating point number, and possibly negative).

    Examples you can use for testing include:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655

    Preconditions: m is a non-negative integer and p is a number.
    """
    # TODO: 2b. Implement and test this function.
    # HINT:  The   math.pow   function will be helpful.
    total = 0
    for k in range (1, n + 1):
        total = total + pow(n, p)
    print(total)
    return total

def test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')
    sum_powers_in_range(4, 7, 0.2)
    sum_powers_in_range(5, 7, 0.4)
    sum_powers_in_range(3, 2, 0.6)



def sum_powers_in_range(m, n, p):
    """
    Returns the sum      m**p + (m+1)**p + (m+2)**p + ... + n**p
    for the given numbers m, n and p.  The latter may be any number
    (possibly a floating point number, and possibly negative).

    Examples you can use for testing include:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776

    Preconditions: m and n are a non-negative integers with n >= m,
                   and p is a number.
    """
    # TODO: 3b. Implement and test this function.
    # HINT:  The   math.pow   function may be helpful.
    # COMMENT: Do you see how you could use   sum_powers_in_range
    #    to test  sum_powers   and (to a lesser extent) vice-versa?

    total = 0
    for k in range (1, n + 1):
        total = total + ((m + k) ** p)
    print('the answer is', total)

    return total

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
