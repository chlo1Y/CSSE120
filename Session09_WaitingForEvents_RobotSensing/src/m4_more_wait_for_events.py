"""
This module lets you practice the WAIT-UNTIL-EVENT pattern:
   while True:
       ...
       if <event has occurred>:
           break
       ...
in the context of waiting for an accumulator to exceed a value.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import random


def main():
    """ Calls the   TEST   functions in this module. """
    test_wait_for_sum_of_cubes()
    test_random_walk()


def test_wait_for_sum_of_cubes():
    """ Tests the   wait_for_sum_of_cubes    function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_sum_of_cubes   function:')
    print('--------------------------------------------------')
    a1 = wait_for_sum_of_cubes(100)
    print(a1)
    a2 = wait_for_sum_of_cubes(35)
    print(a2)

def wait_for_sum_of_cubes(x):
    """
    Returns the smallest n such that the sum
      1 cubed  +  2 cubed  +  3 cubed  +  ...  + n cubed
    is greater than or equal to x.

    Some examples:
      -- if x is 1 or less, this function returns 1.
      -- if x is bigger than 1 but less than or equal to 9,
            this function returns 2.
      -- if x is 12 (or any number in the range (9, 36]),
            this function returns 3.
      -- if x is 100, this function returns 4.
      -- if x is 1000, this function returns 8 because:
             1 + 8 + 27 + 64 + ... + (7**3) = 784
           but
             1 + 8 + 27 + 64 + ... + (8**3) = 1296

    Precondition: x is a number.
    """
    # TODO: 2b. Implement and test this function.
    #    Implementation requirement:
    #       -- Solve this using the   wait-until-event   pattern.
    #       -- But there is a mathematical formula that you
    #            can look up or figure out, that you could use
    #            as an oracle for your testing, if you wish.
    total = 0
    n = 1
    while True:
        total = total + n ** 3
        n = n + 1
        if total >= x:
            return n - 1
            break



def test_random_walk():
    """ Tests the   random_walk    function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   random_walk   function:')
    print('--------------------------------------------------')

    window1 = rg.RoseWindow(400, 400)
    center1 = rg.Point(200, 200)
    circle1 = rg.Circle(center1, 20)
    circle1.fill_color = 'blue'
    probability_up1 = 0.4
    pixels_to_move1 = 1
    print(random_walk(window1, circle1, probability_up1, pixels_to_move1))

    center2 = rg.Point(250, 200)
    circle2 = rg.Circle(center2, 20)
    circle2.fill_color = "purple"
    probability_up2 = 0.7
    pixels_to_move2 = 1
    print(random_walk(window1, circle2, probability_up2, pixels_to_move2))

    center3 = rg.Point(300, 200)
    circle3 = rg.Circle(center3, 20)
    circle3.fill_color = 'pink'
    probability_up3 = 0.6
    pixels_to_move3 = 3
    print(random_walk(window1, circle3, probability_up3, pixels_to_move3))

    window1.close_on_mouse_click()




def random_walk(window, circle, probability_up, pixels_to_move):
    """
    See the    RandomWalkExample.mp4    movie to see this function
    in action.  The movie shows THREE calls to this function:
       -- Blue circle  with probability_up = 0.4 and pixels_to_move =  1
       -- Green circle with probability_up = 0.5 and pixels_to_move = 10
       -- Red circle   with probability_up = 0.5 and pixels_to_move = 10

    Attaches the given rg.Circle to the initial canvas of
    the given rg.RoseWindow.

    Then repeatedly:
      -- Flips a weighted coin
           -- using random.randrange(100)
           -- HEADS are (by definition) numbers
                strictly less than probability_up * 100
           -- TAILS otherwise
      -- Moves the given rg.Circle:
           -- If the coin is HEADS, moves the circle UP
                the given number of pixels.
           -- If the coin is TAILS, moves the circle DOWN
                the given number of pixels.
       -- Draws (renders) the given rg.Circle at its current position,
            pausing a small amount of time after each render
            (to make the animation look good).

    Stops when the circle's center is no longer within
    the given rg.RoseWindow.

    RETURNs the number of movements.

    Preconditions: the first argument is a rg.RoseWindow,
      the second argument is a rg.Circle,
      the third argument is a number between 0 and 1, and
      the fourth argument is a small positive number.
       :type window: rg.RoseWindow
       :type circle: rg.Circle
       :type probability_up: float
       :type pixels_to_move: int
    with   probability_up   between 0 and 1
    and   pixels_to_move   a small integer (typically less than 10).
    """
    # TODO: 3b. Implement and test this function.

    circle.attach_to(window.initial_canvas)
    total = 0
    while True:
        circle_y = circle.center.y
        a = random.randrange(100)
        if float(probability_up) * 100 > a:
            circle.move_by(0, pixels_to_move)
        else:
            circle.move_by(0, -pixels_to_move)
        window.render(0.01)
        total = total + 1

        if circle_y > window.height  or circle_y < 0:
            return total
            break







# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
