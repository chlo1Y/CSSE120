"""
Tests the   Circle  class
that is defined in the imported   m2_Circle   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Zesun Yang.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import m1e_Point as pt
import m2_Circle as cir


def main():
    """
    Tests the   Circle   class defined in the imported   cir  module.
    """
    # TODO: Add code below (at the appropriate places)
    #       to test your   Circle   class as you implement it.
    #       Be sure that your tests print the EXPECTED results of the
    #       tests as well as the ACTUAL results from the function calls.
    print('------------------------------------')
    print('Testing __init__:')
    circle1 = cir.Circle(pt.Point(50, 60), 25)
    circle2 = cir.Circle(pt.Point(10, 30), 50)
    print(circle1.center, circle1.radius)
    print(circle2.center, circle2.radius)

    print('\n------------------------------------')
    print('Testing __repr__:')
    print(circle1.__repr__())
    print(circle2.__repr__())

    print('\n------------------------------------')
    print('Testing clone:')
    print(circle1.clone())

    print('\n------------------------------------')
    print('Testing move_by:')
    circle1.move_by(5, 10)
    print(circle1)
    circle2.move_by(20, 14)
    print(circle2)

    print('\n------------------------------------')
    print('Testing intersects:')
    circle_test = cir.Circle(pt.Point(70, 60), 40)
    print(circle1.intersects(circle_test))
    print(circle2.intersects(circle_test))

    print('\n------------------------------------')
    print('Testing closer_to_origin:')
    circle_test1 = cir.Circle(pt.Point(60, 40), 40)
    print(circle1.closer_to_origin(circle_test1))
    print(circle2.closer_to_origin(circle_test1))

    print('\n------------------------------------')
    print('Testing super_circle:')
    ft_circle = cir.Circle(pt.Point(40, 80), 20)
    print(circle1.super_circle(ft_circle))


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
