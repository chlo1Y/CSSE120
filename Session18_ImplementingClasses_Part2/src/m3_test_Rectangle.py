"""
Tests the   Rectangle  class
that is defined in the imported   m3_Rectangle   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Zesun Yang.  October 2014.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE

import m1e_Point as pt
import m2_Circle as cir
import m3_Rectangle as rect



def main():
    """
    Tests the   Rectangle   class defined in the imported  rect module.
    """
    # TODO: Add code below (at the appropriate places)
    #       to test your   Rectangle   class as you implement it.
    #       Be sure that your tests print the EXPECTED results of the
    #       tests as well as the ACTUAL results from the function calls.
    print('------------------------------------')
    print('Testing __init__:')

    rect1 = rect.Rectangle(pt.Point(20, 50), pt.Point(80, 0))
    print(rect1.corner1)
    print(rect1.corner2)

    print('\n------------------------------------')
    print('Testing __repr__:')

    print(rect1.__repr__())

    print('\n------------------------------------')
    print('Testing clone:')
    print(rect1.clone())

    print('\n------------------------------------')
    print('Testing move_by:')
    print(rect1.move_by(10, 15))

    print('\n------------------------------------')
    print('Testing corners:')
    print(rect1.corners())

    print('\n------------------------------------')
    print('Testing contains:')
    print(rect1.contains(pt.Point(42, 23)))

    print('\n------------------------------------')
    print('Testing intersects:')
    another_rect = rect.Rectangle(pt.Point(40, 60), pt.Point(80, 0))
    print(rect1.intersects(another_rect))

    print('\n------------------------------------')
    print('Testing sub_circle:')
    print(rect1.sub_circle())

    print('\n------------------------------------')
    print('Testing super_rectangle:')
    rect3 = rect.Rectangle(pt.Point(70, 50), pt.Point(20, 15))
    rect4 = rect.Rectangle(pt.Point(12, 15), pt.Point(70, 40))
    print(rect1.super_rectangle([rect1, another_rect, rect3, rect4]))



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
