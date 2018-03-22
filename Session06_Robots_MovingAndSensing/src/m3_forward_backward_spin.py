"""
This module lets you practice making the Create robot MOVE,
with multiple motions.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and Zesun Yang, Songyu Wang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time


def main():
    """
    1. Prompts for and inputs a speed and number of seconds
         to move at that speed.  (The user should enter speeds that
         are between 0 and 50 and seconds between 0.5 and 5.0 or so).

         For example, where the user's input is shown to the right
         of the colons:
           Enter the speed: 25
           Enter the number of seconds to move at that speed: 3.2

    2. Constructs (and hence connects to) a Create robot.
         Puts the robot in full mode.

    3. Moves the robot FORWARD (in a straight line) at the requested
         speed for the requested time (and then stops the robot).

    4. Moves the robot BACKWARDS (in a straight line) at the requested
         speed for the requested time (and then stops the robot).

    5. Makes the robo SPIN (turns in place) CLOCKWISE
         for the requested time (and then stops the robot).
         To spin, make both wheels go at the requested speed,
         but with one wheel going forwards and the other backwards.

    6. Makes the robo SPIN (turns in place) COUNTER-CLOCKWISE
         for the requested time (and then stops the robot).
         To spin, make both wheels go at the requested speed,
         but with one wheel going forwards and the other backwards.

    7. Shuts down the robot.
    """
    # TODO: 2. Implement and test this function.
    #
    # IMPORTANT: Do your work using what is called
    #    an ITERATIVE ENHANCEMENT PLAN, here:
    #      Step 1: Implement and test just the FORWARD motion.
    #                Get that to work before continuing.
    #      Step 2: THEN implement and test the backward motion.
    #      Step 3: THEN implement and test clockwise spinning.
    #      Step 4: THEN implement and test counter-clockwise spinning.
    #
    # CAUTION: Do NOT use   'time'   as a VARIABLE since it is
    #      the name of a MODULE that you need.  Instead, consider
    #      using something like   'seconds'   for the seconds to move.
    port = 3
    robot = new_create.Create(port)
    speed = float(input('give me the speed'))
    time1 = float(input('give me a time'))
    robot.toFullMode()

    robot.go(speed, 0)
    time.sleep(time1)
    robot.stop()

    robot.go(-speed, 0)
    time.sleep(time1)
    robot.stop()

    robot.driveDirect(speed, -speed)
    time.sleep(time1)
    robot.stop()

    robot.driveDirect(-speed, speed)
    time.sleep(time1)
    robot.stop()

    robot.shutdown()






# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
