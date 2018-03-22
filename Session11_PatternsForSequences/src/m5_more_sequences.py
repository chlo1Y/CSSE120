"""
This module lets you practice various patterns
for ITERATING through SEQUENCES, including:
  -- Beginning to end
  -- Other ranges (e.g., backwards and every-3rd-item)
  -- The COUNT/SUM/etc pattern
  -- The FIND pattern (via LINEAR SEARCH)
  -- The MAX/MIN pattern
  -- Looking two places in the sequence at once
  -- Looking at two sequences in parallel

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and PUT YOUR NAME HERE.  January 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
from builtins import range


def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_radii()
    test_count_last_n_odds()
    test_index_of_first_negative()
    test_contains_an_a()
    test_shortest_string()
    test_index_of_largest_number()
    test_number_of_stutters()
    test_is_palindrome()
    test_count_same()


# ----------------------------------------------------------------------
# Many problems simply iterate (loop) through ALL of the sequence,
# like this:
# ----------------------------------------------------------------------
def test_sum_radii():
    """ Tests the   sum_radii   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_radii   function:')
    print('--------------------------------------------------')

    # Test 1 is ALREADY DONE (here).
    circle1 = rg.Circle(rg.Point(100, 100), 25)
    circle2 = rg.Circle(rg.Point(100, 100), 50)
    circle3 = rg.Circle(rg.Point(100, 100), 10)

    seq = (circle1, circle2, circle3)
    answer = sum_radii(seq)
    print('Returned, expected:', answer, 85)

    # Test 2 is ALREADY DONE (here).
    circle1 = rg.Circle(rg.Point(200, 20), 80)
    circle2 = rg.Circle(rg.Point(300, 100), 60)
    circle3 = rg.Circle(rg.Point(100, 150), 0)
    circle4 = rg.Circle(rg.Point(0, 0), 30)

    seq = (circle1, circle2, circle3, circle4)
    answer = sum_radii(seq)
    print('Returned, expected:', answer, 170)


def sum_radii(circles):
    """
    Returns the sum of the radii of the given sequence of zg.Circles.

    Precondition: the argument is a sequence of zg.Circles.
    """
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    total = 0
    for k in range(len(circles)):
        total = total + circles[k].radius
    return total
# ----------------------------------------------------------------------
# Some problems iterate (loop) through PART of the sequence,
# perhaps BACKWARDS, like this:
# ----------------------------------------------------------------------
def test_count_last_n_odds():
    """ Tests the   count_last_n_odds   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   count_last_n_odds   function:')
    print('--------------------------------------------------')

    # Six tests - ALREADY DONE (here).
    seq = [1, 5, 88, 44, 33, 77, 10, 12, 9]
    answer1 = count_last_n_odds(seq, 0)
    answer2 = count_last_n_odds(seq, 1)
    answer3 = count_last_n_odds(seq, 6)
    answer4 = count_last_n_odds(seq, 7)
    answer5 = count_last_n_odds(seq, 8)
    answer6 = count_last_n_odds(seq, 9)

    print()
    print('Test set #1 of count_last_n_odds:',
          answer1, answer2, answer3, answer4, answer5, answer6)
    print('The above should be:    0 1 3 3 4 5')

    # Six more tests - ALREADY DONE (here).
    seq = [17, 88, -5, -10, 0]
    answer1 = count_last_n_odds(seq, 0)
    answer2 = count_last_n_odds(seq, 1)
    answer3 = count_last_n_odds(seq, 2)
    answer4 = count_last_n_odds(seq, 3)
    answer5 = count_last_n_odds(seq, 4)
    answer6 = count_last_n_odds(seq, 5)

    print('\nTest set #2 of count_last_n_odds:',
          answer1, answer2, answer3, answer4, answer5, answer6)
    print('The above should be:    0 0 0 1 1 2')


def count_last_n_odds(integers, n):
    """
    Returns the number of odd integers in the last n items
    of the given sequence.

    For example, if the sequence is (13, 66, 15, 3), then:
       count_last_n_odds(sequence, 0) is 0  [no odds]
       count_last_n_odds(sequence, 1) is 1  [1 odd, namely 3]
       count_last_n_odds(sequence, 2) is 2  [2 odds, namely 3 and 15]
       count_last_n_odds(sequence, 3) is 2  [2 odds, namely 3 and 15]
       count_last_n_odds(sequence, 4) is 3  [3 odds: 3, 15 and 13]

    Precondition: the first argument is a sequence of integers, and
                  the second argument is a non-negative integer
                  less than or equal to the length of the sequence.
    """
    # TODO: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    count = 0
    last = len(integers) - 1
    for k in range(last, (last - n), -1):
        if integers[k] % 2 != 0:
            count = count + 1
    return count




# ----------------------------------------------------------------------
# Some problems iterate (loop) through PART of the sequence,
# stopping when the loop FINDS something of interest (or continuing to
# the end if it does NOT find the thing of interest), like these:
# ----------------------------------------------------------------------
def test_index_of_first_negative():
    """ Tests the   index_of_first_negative   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   index_of_first_negative   function:')
    print('--------------------------------------------------')

    answer1 = index_of_first_negative([90, 0, 20, -5, 30, -10, 15])
    print('Returned, expected:', answer1, 3)

    answer2 = index_of_first_negative([-5, 30, -10, 15])
    print('Returned, expected:', answer2, 0)

    answer3 = index_of_first_negative([5, 30, 10, 15, -1])
    print('Returned, expected:', answer3, 4)

    answer4 = index_of_first_negative([5, 30, 10, 15, 1, 6])
    print('Returned, expected:', answer4, None)


def index_of_first_negative(numbers):
    """
    Returns the index of the first negative number in the given
    Sequence of numbers.  Returns None if the sequence contains
    no negative numbers.

    For example, if the argument is:
    -- [4, 30, -19, 8, -3, -50, 100], this function returns 2
    -- [-8, 44, 33], this function returns 0
    -- [1, 29, 22, 8], this function returns None

    Precondition: The argument is a sequence of numbers.
    """
    # TODO: 4. Implement and test this function.
    #     The testing code is already written for you (above).

    for k in range(len(numbers)):
        if numbers[k] < 0:
            index = k
            return index

    # if none
    return None


def test_contains_an_a():
    """ Tests the   contains_an_a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   contains_an_a   function:')
    print('--------------------------------------------------')

    # Four tests.
    answer1 = contains_an_a('nope')
    answer2 = contains_an_a('yes a is here')
    answer3 = contains_an_a('many aaaaas aaa aaa')
    answer4 = contains_an_a('not until the very end is a')

    print('Test contains_an_a: ', answer1, answer2, answer3, answer4)
    print('The above should be: False True True True')

    # Explicit checks, to help students who return STRINGS that LOOK
    # like    True    False.
    if answer1 is not False:
        print('Your code failed the first test for   contains_an_a.')
    if answer2 is not True:
        print('Your code failed the second test for   contains_an_a.')
    if answer3 is not True:
        print('Your code failed the third test for   contains_an_a.')
    if answer4 is not True:
        print('Your code failed the fourth test for   contains_an_a.')


def contains_an_a(string):
    """
    Returns True if the given string contains the character 'a',
    else returns False.

    Precondition: the argument is a string.
    """
    # TODO: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    # NOTE: True and False are built-in constants.
    #       Do NOT return the STRINGs 'True' and 'False'.
    # Implementation requirement: Use an explicit loop.
    # No fair using the   count   or   find   string methods.
    for k in range(len(string)):
        if string[k] == 'a':
            return True
    return False

# ----------------------------------------------------------------------
# Some problems iterate (loop) through the sequence to find the LARGEST
# (or SMALLEST) item in the sequence, returning its INDEX (or possibly
# the item itself), like this:
# ----------------------------------------------------------------------
def test_shortest_string():
    """ Tests the   shortest_string   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   shortest_string   function:')
    print('--------------------------------------------------')

    sequence1 = ('all', 'we', 'are', 'saying',
                 'is', 'give', 'peace', 'a', 'chance')
    sequence2 = ('all', 'we', 'are', 'saying',
                 'is', 'give', 'peace', 'a chance')
    sequence3 = ('all we', 'are saying',
                 'is', 'give', 'peace', 'a chance')
    sequence4 = ('all we are saying is give peace a chance',)
    sequence5 = ('a', '', 'a')

    answer1 = shortest_string(sequence1)
    print('Returned, expected:', answer1, 'a')

    answer2 = shortest_string(sequence2)
    print('Returned, expected:', answer2, 'we')

    answer3 = shortest_string(sequence3)
    print('Returned, expected:', answer3, 'is')

    answer4 = shortest_string(sequence4)
    print('Returned, expected:', answer4,
          'all we are saying is give peace a chance')

    answer5 = shortest_string(sequence5)
    print('Returned:', answer5, 'Expected the empty string.')


def shortest_string(strings):
    """
    Returns the shortest string in the given sequence of strings.
    If there is a tie for shortest string, returns the one
    (among the ties) whose index is smallest.

    For example, if the argument is a sequence containing
    the following strings (in the order listed):
    'all'  'we'  'are'  'saying'  'is'  'give'  'peace'  'a'  'chance'
    then this function returns   'a'

    As another example, if the argument is a sequence containing
    the following strings (in the order listed):
      'all'  'we'  'are'  'saying'  'is'  'give'  'peace'  'a chance'
    then this function returns   'we'

    Precondition: The argument is non-empty sequence of strings.
    """
    # TODO: 6. Implement and test this function.
    #     The testing code is already written for you (above).

    length = len(strings[0])
    h = strings[0]
    for k in range(len(strings)):
        if length > len(strings[k]):
            length = len(strings[k])
            h = strings[k]
    return h



def test_index_of_largest_number():
    """ Tests the   index_of_largest_number   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   index_of_largest_number   function:')
    print('--------------------------------------------------')

    answer1 = index_of_largest_number([90, 0, 100, -5, 100, -10, 15], 3)
    print('Returned, expected:', answer1, 2)

    answer2 = index_of_largest_number([90, 0, 95, -5, 95, -10, 15], 2)
    print('Returned, expected:', answer2, 0)

    answer3 = index_of_largest_number([90, 0, 93, -5, 93, -10, 15], 7)
    print('Returned, expected:', answer3, 2)

    answer4 = index_of_largest_number([5, 30, 10, 15, 1, 60], 6)
    print('Returned, expected:', answer4, 5)

    answer5 = index_of_largest_number([-5, 30, 10, 15, 1, 60], 1)
    print('Returned, expected:', answer5, 0)

    answer6 = index_of_largest_number([-500000000000000000000000000000,
                                       - 400000000000000000000000000000],
                                      2)
    print('Returned, expected:', answer6, 1)

    answer7 = index_of_largest_number([-40000000000000000000000000000000000,
                                       - 50000000000000000000000000000000000],
                                      2)
    print('Returned, expected:', answer7, 0)


def index_of_largest_number(numbers, n):
    """
    Returns the INDEX of the largest number in the first n numbers
    of the given sequence of numbers.  If there is a tie for largest
    number, returns the smallest of the indices of the tied numbers.

    For example, if the arguments are:
      [90, 0, 100, -5, 100, -10, 15]    and    3
    the correct answer is 2 (because 100, at index 2,
    is the largest of the first 3 numbers in the list).

    Another example:  For the same list as above, but with n = 2,
    the correct answer is 0 (because 90, at index 0,
    is the largest of the first 2 numbers in the list).

    Yet another example:  For the same list as above, but with n = 7,
    the correct answer is 2 (because 100, at indices 2 and 4,
    is the largest of the first 7 numbers in the list, and we break
    the tie in favor of the smaller index).

    Preconditions: The first argument is a sequence of numbers,
                   the second argument is a positive integer,
                   and the length of the given sequence is at least
                   the given n.
    """
    # TODO: 7. Implement and test this function.
    #     The testing code is already written for you (above).
    index = 0
    for k in range(n):
        if numbers[0] < numbers[k]:
            numbers[0] = numbers[k]
            index = k
    return index


# ----------------------------------------------------------------------
# Some problems iterate (loop) through the sequence accessing TWO
# (or more) places in the sequence AT THE SAME ITERATION, like these:
# ----------------------------------------------------------------------
def test_number_of_stutters():
    """ Tests the   number_of_stutters   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   number_of_stutters   function:')
    print('--------------------------------------------------')

    answer1 = number_of_stutters('xhhbrrs')
    print('Returned, expected:', answer1, 2)

    answer2 = number_of_stutters('xxxx')
    print('Returned, expected:', answer2, 3)

    answer3 = number_of_stutters('xaxaxa')
    print('Returned, expected:', answer3, 0)

    answer4 = number_of_stutters('xxx yyy xxxx')
    print('Returned, expected:', answer4, 7)

    answer5 = number_of_stutters('xxxyyyxxxx')
    print('Returned, expected:', answer5, 7)


def number_of_stutters(string):
    """
    Returns the number of times a letter is repeated
        twice-in-a-row in the given string.
        For example:
            'xhhbrrs'   returns 2
            'xxxx'      returns 3
            'xaxaxa'    returns 0
            'xxx yyy xxxx'    returns 7
            'xxxyyyxxxx'      returns 7
        Precondition: The argument is a string.
    """
    # TODO: 8. Implement and test this function.
    #     The testing code is already written for you (above).
    total = 0
    for k in range(len(string) - 1):
        if string[k] == string[k + 1]:
            k = k + 1
            total = total + 1
    return total



def test_is_palindrome():
    """ Tests the   is_palindrome   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   is_palindrome   function:')
    print('--------------------------------------------------')

    # Five tests.
    answer1 = is_palindrome('bob')
    answer2 = is_palindrome('obbo')
    answer3 = is_palindrome('nope')
    answer4 = is_palindrome('almosttxomla')
    answer5 = is_palindrome('abbz')

    # The next would normally be written:
    #      Murder for a jar of red rum
    # It IS a palindrome (ignoring spaces and punctuation).
    answer6 = is_palindrome('murderforajarofredrum')

    print('Test is_palindrome: ',
          answer1, answer2, answer3, answer4, answer5, answer6)
    print('The above should be: True True False False False True')

    # Explicit checks, to help students who return STRINGS that LOOK
    # like    True    False.
    if answer1 is not True:
        print('Your code failed the 1st test for   is_palindrome.')
    if answer2 is not True:
        print('Your code failed the 2nd test for   is_palindrome.')
    if answer3 is not False:
        print('Your code failed the 3rd test for   is_palindrome.')
    if answer4 is not False:
        print('Your code failed the 4th test for   is_palindrome.')
    if answer5 is not False:
        print('Your code failed the 5th test for   is_palindrome.')
    if answer6 is not True:
        print('Your code failed the 6th test for   is_palindrome.')


def is_palindrome(word):
    """
    Returns True if the given word is a palindrome,
    i.e., reads the same backwards and forwards.

    For example:
      abba  reads backwards as   abba   so is a palindrome
    but
      abbz  reads backwards as   zbba   so is NOT a palindrome

    Precondition: In this simple version of the palindrome problem,
                  the given argument will always contain just
                  lower-case letters (no spaces, no punctuation).
    """
    # TODO: 9. Implement and test this function.
    #     The testing code is already written for you (above).
    for k in range(len(word)):
        if word[k] != word[len(word) - 1 - k]:
            return False
    return True




# ----------------------------------------------------------------------
# Some problems loop (iterate) through two or more sequences
#    IN PARALLEL, like this:
# ----------------------------------------------------------------------
def test_count_same():
    """ Tests the   count_same   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   count_same   function:')
    print('--------------------------------------------------')
    answer1 = count_same([1, 44, 55],
                         [0, 44, 77])
    print('Returned, expected:', answer1, 1)

    answer2 = count_same([1, 44, 55, 88, 44],
                         [0, 44, 77, 88, 44])
    print('Returned, expected:', answer2, 3)

    answer3 = count_same([1, 44, 55, 88, 44],
                         [0, 43, 77, 8, 4])
    print('Returned, expected:', answer3, 0)


def count_same(sequence1, sequence2):
    """
    Returns the number of indices at which the two given sequences
    have the same item at that index.
    For example, if the sequences are:
       (11, 33, 83, 18, 30, 55)
       (99, 33, 83, 19, 30, 44)
    then the function returns 3,
    since the two sequences have the same item at:
      -- index 1 (both are 33)
      -- index 2 (both are 83)
      -- index 4 (both are 30)

    Precondition: The sequences are the same length.
    """
    # TODO: 10. Implement and test this function.
    #     The testing code is already written for you (above).
    count = 0
    for k in range(len(sequence1)):
        if sequence1[k] == sequence2[k]:
            count = count + 1
    return count

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
