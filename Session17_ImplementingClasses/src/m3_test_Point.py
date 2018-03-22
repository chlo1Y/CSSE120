"""
Tests the   Point  class
that is defined in the imported   m3_Point   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import m3_Point as pt


def main():
    """
    Tests the   Point   class defined in the imported   pt  module.
    """
    # TODO: Add code below (at the appropriate places)
    #       to test your   Point   class as you implement it.
    print('------------------------------------')
    print('Testing __init__:')
    point1 = pt.Point(200, 100)
    point2 = pt.Point(50, 25)
    print(point1.x, point1.y)
    print(point2.x, point2.y)

    print('\n------------------------------------')
    print('Testing __repr__:')
    point1 = pt.Point(200, 100)
    point2 = pt.Point(50, 25)
    print(point1.__repr__())
    print(point2.__repr__())

    print('\n------------------------------------')
    print('Testing move_to:')
    point1.move_to(75, 80)
    print(point1)
    point2.move_to(90, 100)
    print(point2)

    print('\n------------------------------------')
    print('Testing move_by:')
    point1.move_by(3, 5)
    print(point1)
    point2.move_by(15, 29)
    print(point2)

    print('\n------------------------------------')
    print('Testing distance_from:')
    test_point = pt.Point(90, 50)
    print(point1.distance_from(test_point))
    print(point2.distance_from(test_point))

    print('\n------------------------------------')
    print('Testing closer_to:')
    p1 = pt.Point(50, 78)
    p2 = pt.Point(60, 70)
    print(point1.closer_to(p1, p2))


    print('\n------------------------------------')
    print('Testing halfway_to:')
    p1 = pt.Point(70, 80)
    print(point1.halfway_to(p1))
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
