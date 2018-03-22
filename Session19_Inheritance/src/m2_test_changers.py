"""
Tests the various   Ball  classes
that are defined in the imported   m2_changers   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Zesun Yang.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import simulator as sim
import m2_changers as changers
import rosegraphics as rg
import random



# ----------------------------------------------------------------------
# TODO: Modify this module as needed to test your   Changer   classes
#       as you implement them.  We have supplied some tests for you.
# ----------------------------------------------------------------------
def main():
    """
    Calls the   TEST   functions in this module to get
    lists of Changers that are good for testing the Changer classes.
    Constructs a Simulator, sending the Changers to the Simulator.
    As such, this provides a VISUAL test of the Changer classes.
    """
    # If you add your own classes, add to the following list.
    testers = [test_Dud, test_Mover, test_Randomizer, test_Jiggler,
               test_Follower, test_Grower, test_MoverGrower,
               test_Exploder]

    changers_to_test = []
    for tester in testers:
        changers = tester()
        if changers:
            changers_to_test = changers_to_test + changers

    sim.Simulator(changers_to_test)


def test_Dud():
    """ Returns a list of   Dud   instances good for testing. """
    dud1 = changers.Dud(rg.Point(100, 100))
    dud2 = changers.Dud(rg.Point(150, 80))

    return [dud1, dud2]


def test_Mover():
    """ Returns a list of   Mover   instances good for testing. """
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = 'green'
    mover1 = changers.Mover(circle, 15, 5)
    rectangel = rg.Rectangle(rg.Point(200, 40), 50, 20)
    rectangel.fill_color = 'black'
    mover2 = changers.Mover(rectangel, -6, 20)

    return [mover1, mover2]



def test_Randomizer():
    """ Returns a list of   Randomizer   instances good for testing. """
    # TODO: Implement and test this method.
    rect1 = rg.Rectangle(rg.Point(70, 50), 70, 40)
    rect1.fill_color = 'red'
    randomizer1 = changers.Randomizer(rect1)
    return [randomizer1]

def test_Jiggler():
    """ Returns a list of   Jiggler   instances good for testing. """
    # TODO: Implement and test this method.
    circle1 = rg.Circle(rg.Point(400, 120), 30)
    circle1.fill_color = 'pink'
    range1 = 4
    jiggler1 = changers.Jiggler(circle1, range1)
    return [jiggler1]





def test_Follower():
    """ Returns a list of   Follower   instances good for testing. """
    # TODO: Implement and test this method.
#     circle1 = rg.Circle(rg.Point(60, 120), 30)
#     circle1.fill_color = 'violet'
#     follower = changers.Follower(circle1)
#     return [follower]



def test_Grower():
    """ Returns a list of   Grower   instances good for testing. """
    # TODO: Implement and test this method.


def test_MoverGrower():
    """ Returns a list of   MoverGrower   instances good for testing. """
    # TODO: Implement and test this method.


def test_Exploder():
    """ Returns a list of   Exploder   instances good for testing. """
    # TODO: Implement and test this method.


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
