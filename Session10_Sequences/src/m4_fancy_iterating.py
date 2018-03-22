"""
This module lets you practice ITERATING (i.e. looping)
through a SEQUENCE:
  -- list
  -- string
  -- tuple

Note that there are two ways to iterate through a sequence:
  -- using RANGE
  -- using just IN (no RANGE)
The former works for all iterating problems; the latter is a cleaner
notation but does NOT apply to all iterating problems.

In some of these problems you iterate through the ENTIRE sequence
(both forwards and backwards)
and in others you iterate through just PART of a sequence, e.g. just:
  -- the items at odd-numbered indices
  -- the items in the second half of the sequence

You also practice how to SELECT items in a sequence, e.g.:
  -- the items that are strings
  -- the items that are odd integers

Note that:
  -- SELECTING items that ARE odd integers
is different from:
  -- LOOKING only at items AT odd-numbered indices.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  January 2014.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    sequence1 = [55, 'hello', 33, rg.Point(90, 25)]  # List
    sequence2 = [90, 'dog', 87, 95, 92, 33, 100]  # List
    sequence3 = 'Yo! Whazup?'  # String
    sequence4 = ('This', 'is a', 'tuple', 55)  # Tuple

    # ------------------------------------------------------------------
    # STUDENTS: Do a problem and test it.  When satisfied,
    #           comment-out the call below to its test function.
    #           Otherwise, you will be overwhelmed by the output.
    # ------------------------------------------------------------------

    test_print_all_items_forwards(sequence1, sequence2,
                                  sequence3, sequence4)
    test_print_all_items_backwards(sequence1, sequence2,
                                   sequence3, sequence4)
    test_print_items_at_odd_indices(sequence1, sequence2,
                                    sequence3, sequence4)
    test_print_items_in_second_half(sequence1, sequence2,
                                    sequence3, sequence4)
    test_print_items_that_are_bigger_than_5(sequence1, sequence2,
                                            sequence3, sequence4)
    test_print_items_that_are_strings(sequence1, sequence2,
                                      sequence3, sequence4)
    test_print_items_that_are_odd_integers(sequence1, sequence2,
                                           sequence3, sequence4)


def test_print_all_items_forwards(sequence1, sequence2, sequence3,
                                  sequence4):
    """ Tests the   print_all_items_forwards   function. """
    print()
    print('***********************************************************')
    print('Testing the   print_all_items_forwards   function.')
    print('Iterate through an ENTIRE sequence, forwards:')
    print('***********************************************************')
    print_all_items_forwards(sequence1)
    print('-------------------------------------------------------')
    print_all_items_forwards(sequence2)
    print('-------------------------------------------------------')
    print_all_items_forwards(sequence3)
    print('-------------------------------------------------------')
    print_all_items_forwards(sequence4)
    print('-------------------------------------------------------')



def test_print_all_items_backwards(sequence1, sequence2,
                                   sequence3, sequence4):
    """ Tests the   print_all_items_backwards   function. """
    print()
    print('***********************************************************')
    print('Testing the   print_all_items_backwards   function.')
    print('Iterate through an ENTIRE sequence, backwards:')
    print('***********************************************************')
    print_all_items_backwards(sequence1)
    print('-------------------------------------------------------')
    print_all_items_backwards(sequence2)
    print('-------------------------------------------------------')
    print_all_items_backwards(sequence3)
    print('-------------------------------------------------------')
    print_all_items_backwards(sequence4)
    print('-------------------------------------------------------')


def test_print_items_at_odd_indices(sequence1, sequence2,
                                    sequence3, sequence4):
    print()
    print('***********************************************************')
    print('Testing the   print_items_at_odd_indices   function.')
    print('Iterate through PART of a sequence, namely,')
    print('the items at odd-numbered indices:')
    print('***********************************************************')
    print_items_at_odd_indices(sequence1)
    print('-------------------------------------------------------')
    print_items_at_odd_indices(sequence2)
    print('-------------------------------------------------------')
    print_items_at_odd_indices(sequence3)
    print('-------------------------------------------------------')
    print_items_at_odd_indices(sequence4)
    print('-------------------------------------------------------')


def test_print_items_in_second_half(sequence1, sequence2,
                                    sequence3, sequence4):
    print()
    print('***********************************************************')
    print('Testing the   print_items_in_second_half   function.')
    print('Iterate through PART of a sequence, namely,')
    print('the items in the second half of the sequence:')
    print('***********************************************************')
    print_items_in_second_half(sequence1)
    print('-------------------------------------------------------')
    print_items_in_second_half(sequence2)
    print('-------------------------------------------------------')
    print_items_in_second_half(sequence3)
    print('-------------------------------------------------------')
    print_items_in_second_half(sequence4)
    print('-------------------------------------------------------')


def test_print_items_that_are_bigger_than_5(sequence1, sequence2,
                                            sequence3, sequence4):
    print()
    print('***********************************************************')
    print('Testing the  print_items_that_are_bigger_than_5  function.')
    print('Iterate through a sequence, selecting items, namely,')
    print('the items that are bigger than 5:')
    print('Note that the test sequences for this are NOT the same as')
    print('the test sequences for the other exercises herein.')
    print('***********************************************************')
    print_items_that_are_bigger_than_5([45, 3, -50, 6, 5, 3, 100, 100])
    print('-------------------------------------------------------')
    print_items_that_are_bigger_than_5([7, 30, 6])
    print('-------------------------------------------------------')
    print_items_that_are_bigger_than_5([5, 5, 5])
    print('-------------------------------------------------------')


def test_print_items_that_are_strings(sequence1, sequence2,
                                      sequence3, sequence4):
    print()
    print('***********************************************************')
    print('Testing the   print_items_that_are_strings   function.')
    print('Iterate through a sequence, selecting items, namely,')
    print('the items that are strings:')
    print('***********************************************************')
    print_items_that_are_strings(sequence1)
    print('-------------------------------------------------------')
    print_items_that_are_strings(sequence2)
    print('-------------------------------------------------------')
    print_items_that_are_strings(sequence3)
    print('-------------------------------------------------------')
    print_items_that_are_strings(sequence4)
    print('-------------------------------------------------------')


def test_print_items_that_are_odd_integers(sequence1, sequence2,
                                           sequence3, sequence4):
    print()
    print('***********************************************************')
    print('Testing the   print_items_that_are_odd_integers   function.')
    print('Iterate through a sequence, selecting items, namely,')
    print('the items that are odd integers:')
    print('Note that there is 1 extra test sequence for this problem.')
    print('***********************************************************')
    print_items_that_are_odd_integers(sequence1)
    print('-------------------------------------------------------')
    print_items_that_are_odd_integers(sequence2)
    print('-------------------------------------------------------')
    print_items_that_are_odd_integers(sequence3)
    print('-------------------------------------------------------')
    print_items_that_are_odd_integers(sequence4)
    print('-------------------------------------------------------')
    print_items_that_are_odd_integers([90, 'dog', 87, 95, 8, 10, 5, 77])
    print('-------------------------------------------------------')


# ----------------------------------------------------------------------
# Iterating through the ENTIRE sequence, FORWARDs.
# ----------------------------------------------------------------------
def print_all_items_forwards(sequence):
    """
    Prints the items in the given sequence in the order that
    they appear, that is, forwards.  Prints them one item per line.

    For example, if the sequence is [55, 'hello', 33, zg.Point(90, 25)],
    then this function prints:
       55
       hello
       33
       Point(90, 25)
    """
    # TODO: 2. Implement and test this function.
    print('print_all_items_forwards')
    for k in range(len(sequence)):
        print(sequence[k])



# ----------------------------------------------------------------------
# Iterating through the ENTIRE sequence, BACKWARDs.
# ----------------------------------------------------------------------
def print_all_items_backwards(sequence):
    """
    Prints the items in the given sequence in the REVERSE of the order
    in which they appear, that is, prints them in backwards order.
    Prints them one item per line.

    For example, if the sequence is [55, 'hello', 33, zg.Point(90, 25)],
    then this function prints:
       Point(90,25)
       33
       hello
       55
    """
    # TODO: 3. Implement and test this function.
    for k in range(len(sequence) - 1, -1, -1):
        print(sequence[k])


# ----------------------------------------------------------------------
# Iterating through PART of a sequence:
#   -- in this sample problem, every other item in the sequence.
# ----------------------------------------------------------------------
def print_items_at_odd_indices(sequence):
    """
    Prints the items at the odd-numbered indices in the given sequence,
    along with their positions (indices) in the sequence.
    with ' is at index ' in between (see example).

    For example, if the sequence is [90, 'dog', 87, 95, 92, 33, 100],
    then this function prints:
      dog is at index 1
      95 is at index 3
      33 is at index 5
    """
    # TODO: 4. Implement and test this function.
    for k in range(len(sequence)):
        if type(sequence[k]) == int and sequence[k] // 2 != 0:
            print(sequence[k])


# ----------------------------------------------------------------------
# Iterating through PART of a sequence:
#   -- in this sample problem, the second half.
# ----------------------------------------------------------------------
def print_items_in_second_half(sequence):
    """
    Prints the items in the second half of the given sequence.
    For odd-length sequences, includes the middle item in the sequence.

    For example, if the sequence is [90, 'dog', 87, 95, 92, 33, 100],
    then this function prints:
      95
      92
      33
      100
    """
    # TODO: 5. Implement and test this function.
    #   HINT: Don't get hung up on including the middle item, just try
    #         it (use a // for integer division) and adjust if needed.
    #         No conditional is needed under most implementations.
    for k in range(len(sequence) // 2, len(sequence)):
        print(sequence[k])


# ----------------------------------------------------------------------
# Iterating through a sequence, selecting items:
#   -- in this sample problem, the items that are bigger than 5.
# ----------------------------------------------------------------------
def print_items_that_are_bigger_than_5(sequence):
    """
    Prints the items in the given sequence that are bigger than 5,
    along with their positions (indices) in the sequence,
    with ' is at index ' in between (see example).

    For example, if the sequence is [45, 3, -50, 6, 5, 3, 100, 100],
    then this function prints:
      45 is at index 0
      6 is at index 3
      100 is at index 6
      100 is at index 7

    Precondition: All the items in the sequence are integers.
    """
    # TODO: 6. Implement and test this function.
    for k in range(len(sequence)):
        if sequence[k] > 5:
            print(sequence[k])


# ----------------------------------------------------------------------
# Iterating through a sequence, selecting items:
#   -- in this sample problem, the items that are strings.
# ----------------------------------------------------------------------
def print_items_that_are_strings(sequence):
    """
    Prints the items in the given sequence that are strings,
    along with their positions (indices) in the sequence,
    with ' is at index ' in between (see example).

    For example, if the sequence is [90, 'dog', 8, 'cat, 'bone', 33, 1],
    then this function prints:
      dog is at index 1
      cat is at index 3
      bone is at index 4
    """
    # TODO: 7. Implement and test this function.
    #    HINTS:
    #     -- A string is, by definition, an object whose type is   str.
    #     -- The   type   function gives the type of an object.
    #        For example,   type('hello')   returns   str   (NO quotes).
    for k in range(len(sequence)):
        if type(sequence[k]) == str:
            print(sequence[k], 'is at index', k)

# ----------------------------------------------------------------------
# Iterating through a sequence, selecting items:
#   -- in this sample problem, the items that are odd integers.
# ----------------------------------------------------------------------
def print_items_that_are_odd_integers(sequence):
    """
    Prints the items in the given sequence that are odd integers,
    along with their positions in the sequence,
    with ' is at index ' in between (see example).

    For example, if the sequence is [90, 'dog', 87, 95, 92, 10, 5, 777],
    then this function prints:
      87 is at index 2
      95 is at index 3
      5 is at index 6
      777 is at index 7
    """
    # TODO: 8. Implement and test this function.
    for k in range(len(sequence)):
        if type(sequence) == int and sequence // 2 != 0:
            print(sequence[k])


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
