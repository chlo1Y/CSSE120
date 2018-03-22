"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  February 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    test_keep_integers()
    test_largest_negative_number()


def test_keep_integers():
    """ Tests the    keep_integers    function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    # ------------------------------------------------------------------
    print()
    print('---------------------------------------')
    print('Testing the   KEEP_INTEGERS   function:')
    print('---------------------------------------')
    a = [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [30, -4]
        ]
    print('the answer should be:')
    print('[(3, 1, 4),'
         '[],'
         '[30, -4]'
        ']')
    print('yours is', keep_integers(a))
    b = [(3, 5, 8), ['hi', 'you', 5], (7, 9)]
    print('the answer should be:')
    print('[(3,5,8)',
          '(7,9)]')
    print('yours is:', keep_integers(b))

def keep_integers(seq_seq):
    """
    MUTATES the given list of sequences as follows:  It keeps ONLY
    the items in the sequence that contain ONLY integers.
    For example, if the given argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [30, -4]
        ]
    then this function MUTATES that argument into:
        [(3, 1, 4),
         [],
         [30, -4]
        ]
    Preconditions:  the given argument is a list of sequences.
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    #
    # HINTS:
    #  -- An elegant way to keep the indexing consistent while
    #     deleting items from the exterior sequence is to go through the
    #     exterior sequence BACKWARDS.
    #  -- One way to delete an item from a list is like this:
    #        del x[r]
    #     This example deletes the item at index r in the list x.
    # ------------------------------------------------------------------
    seq1 = []
    for k in range(len(seq_seq)):
        for j in range(len(seq_seq[k])):
            if type(seq_seq[k][j]) != int:
                seq1 = seq1 + [seq_seq[k]]
                break
    for r in range(len(seq1)):
        nogood = seq_seq.index(seq1[r])
        del seq_seq[nogood]

    return seq_seq



def test_largest_negative_number():
    """ Tests the    largest_negative_number    function. """
    # ------------------------------------------------------------------
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    # ------------------------------------------------------------------
    print()
    print('-------------------------------------------------')
    print('Testing the   LARGEST_NEGATIVE_NUMBER   function:')
    print('-------------------------------------------------')
    a = [(30, -5, 8, -20),
         (100, -2.6, 88, -40, -5),
         (400, 500)
        ]
    print('the test result should be:-2.6.')
    print('yours is,', largest_negative_number(a))

    b = [(200, 2, 20), (500, 400)]
    print('the test result should be:0.')
    print('yours is,', largest_negative_number(b))


def largest_negative_number(seq_seq):
    """
    Returns the largest negative number in the given sequence of
    sequences of numbers.  Returns 0 if there are no negative numbers
    in the sequence of sequences.

    For example, if the given argument is:
        [(30, -5, 8, -20),
         (100, -2.6, 88, -40, -5),
         (400, 500)
        ]
    then this function returns -2.6.

    As another example, if the given argument is:
      [(200, 2, 20), (500, 400)]
    then this function returns 0.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences,
    where each subsequence contains only numbers.
    """
    # ------------------------------------------------------------------
    # TODO: 3b. Implement and test this function.
    # ------------------------------------------------------------------
    zero = 0
    list1 = []
    for k in range(len(seq_seq)):
        for j in range(len(seq_seq[k])):
            if seq_seq[k][j] < 0:
                list1 = list1 + [seq_seq[k][j]]
    if list1 == []:
        return 0

    a = list1[0]
    for i in range(len(list1)):
        if list1[i] > a:
            a = list1[i]
    return a





#     biggest = -1000
#     for i in range(len(list1)):
#         if biggest < list1[i]:
#             biggest = list1[i]
#     return biggest

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
