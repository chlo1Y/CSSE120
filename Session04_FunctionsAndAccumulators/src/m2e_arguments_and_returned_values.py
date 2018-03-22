"""
This module demonstrates:
  -- ARGUMENTs in function CALLs,
  -- PARAMETERs in function DEFINITIONs, and
  -- RETURNING a value from a function.

When a function is CALLED:

  a. The ARGUMENTs given in the function CALL are sent
       TO the PARAMETERs in the function DEFINITION.
       That is, the parameters are ASSIGNED values,
       just like in an assignment statement (with an = sign)).

  b. The function runs.

  c. When the function reaches a RETURN statement, the value of the
       expression after the RETURN keyword is sent BACK to the caller
       (as if it replaced the function call itself).

       If the function reaches its end without encountering a RETURN
       statement, it returns the special value    None.

  d. When the function returns to the caller (either via a RETURN
        statement or by reaching the end of the function), execution
        continues from the point at which the function was called.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
# ----------------------------------------------------------------------
# Students: PREDICT what this program will print when you run it,
# then run it to check your prediction.  Before you leave this example:
#
#   *** MAKE SURE YOU UNDERSTAND HOW THE
#          ** actual arguments  **
#       ARE ASSIGNED TO THE
#          ** formal parameters **
#       WHEN A FUNCTION IS CALLED.
#
#       Additionally, be sure that YOU understand how to
#          ** CAPTURE A RETURNED VALUE IN A VARIABLE. **
#
#   There is nothing for you to turn in from this file.
# ----------------------------------------------------------------------


def main():
    """
    An example of CALLING functions, sending them arguments.
    Here, the returned value is ignored.
    """
    example1(1234)

    print()
    example2(98765)


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


def example1(n):
    """
    Takes an integer n and prints various things about it.
    In particular, this is an example that shows how to:
      -- CALL a function (here,   sum_of_digits   is called three times)
      -- SEND it information in ARGUMENTS
            (here,  73922  in the 1st call and  8301  in the 2nd call
            and n**99 in the 3rd call, where n is the PARAMETER
            (whose value is established by the CALLER) for this function
      -- CAPTURE the returned value in a VARIABLE
            (here, the   sum1   and   sum2   and   sum3   variables)
    """
    # Demonstrates calling a function, sending it an argument,
    # and capturing the returned value in a variable:
    sum1 = sum_of_digits(73922)
    sum2 = sum_of_digits(8301)
    sum3 = sum_of_digits(n ** 99)

    print('The sum of the digits of 73922 is', sum1)
    print('The sum of the digits of 8301 is', sum2)

    print(n, 'raised to the 99th power is', n ** 99)
    print('The sum of the digits in that number is', sum3)


def example2(m):
    """
    Takes an integer m and prints various things about it.
    In particular, this example is like example1, but it does more
    with the returned values from sum_of_digits than just print them.
    """
    sum1 = sum_of_digits(m ** 99)
    sum2 = sum_of_digits(m ** 42)

    sum3 = sum_of_digits(sum1 * sum2)

    print('The given number (call is X) is', m)
    print('Let Y stand for the sum of the digits in')
    print('(X raised to the 99th power), and let Z stand for')
    print('the sum of the digits in (X raised to the 42nd power).')
    print('Then the sum of the digits in Y * Z is', sum3)
    print('and the sum of the digits in Y ** Z is',
          sum_of_digits(sum1 ** sum2))
    # Students: Note how I chose to use a variable for sum3, but to do
    #   the computation "inline" for the next sum of digits.  Be sure
    #   to understand both approaches; use whichever you prefer for now.

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
