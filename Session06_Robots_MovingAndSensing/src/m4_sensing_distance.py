"""
This module lets you practice using Create SENSORS,
in particular the DISTANCE and ANGLE sensors.

The    getSensor   method is used for ALL sensor accesses, like this:
   sensor_value = robot.getSensor(...)

where the argument is a constant that indicates the sensor whose value
is sought:
  -- The   Sensors.distance   constant indicates LINEAR distance
       traveled ** SINCE you last asked for that sensor reading. **
  -- The   Sensors.angle   constant indicates ANGULAR distance
       traveled ** SINCE you last asked for that sensor reading. **

The former is in MILLIMETERS (NOT centimeters).
The latter is in DEGREES.
Each is returned as an INTEGER.

So, to obtain linear distance traveled, the usual approach is:
  1. Use getSensor(Sensors.distance) to get a DISTANCE sensor reading
       (but ignoring the value of that reading).
  2. Make the robot move, e.g. by:
       a. robot.driveDirect(..., ...)
       b. time.sleep(...)
       c. robot.stop()
  3. Use getSensor(Sensors.distance) to get ANOTHER DISTANCE sensor
       reading.  This NEW reading is the distance the robot traveled.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and Zesun Yang, Songyu Wang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time


def main():
    """
    1. Prompts for and inputs two speeds (one for each wheel)
         and the number of seconds to move at that speed.
         (The user should enter speeds that are between -50 and 50
         and seconds between 0.5 and 5.0 or so).

         For example, where the user's input is shown to the right
         of the colons:
           Enter the left wheel speed: -25
           Enter the right wheel speed:  18
           Enter the number of seconds to move at that speed: 1.2

    2. Constructs (and hence connects to) a Create robot.
         Puts the robot in full mode.

    3. Repeats the following 3 times:
       a. Moves the robot at the requested wheel speeds for the
          requested number of seconds (and then stops the robot).
       c. Prints the LINEAR distance traveled.
       d. Prints the ANGULAR distance traveled.
       e. Waits for the user to press the ENTER key.
            Implement this by using this statement:
               input('Press the Enter key):
            Note that this statement waits for input but ignores
            the actual input.  That is what we want here.

    3. Shuts down the robot.
    """
    # TODO: 2. Implement and test this function.
    #
    # IMPORTANT: Do your work using what is called
    #    an ITERATIVE ENHANCEMENT PLAN, here:
    #      Step 1: Implement and test just the speeds/seconds input
    #                and the motion ONE time (not yet 3 times).
    #      Step 2: Implement and test the printing
    #                of the linear and angular distances.
    #      Step 3: Implement the loop that does the movement/sensing
    #                THREE (not just 1) times.
    run()
    run()


def run():
    port = 3
    robot = new_create.Create(port)
    leftspeed = float(input('left speed:'))
    rightspeed = float(input('right speed:'))
    time1 = float(input('time:'))
    robot.toFullMode()

    robot.driveDirect(leftspeed, rightspeed)
    time.sleep(time1)
    sensor1 = new_create.Sensors.distance
    sensor2 = new_create.Sensors.angle
    v1 = robot.getSensor(sensor1)
    v2 = robot.getSensor(sensor2)
    input('Press the Enter key')
    print("distance:", v1)
    print('angle:', v2)
    robot.stop()

    robot.shutdown()

# TODO: 3.  After implementing the above, experiment to learn
#   a bit about the ACCURACY of the sensors and movement, as follows:
#     -- Run the program with just linear speed
#          (i.e., left and right wheel speeds are the same).
#     -- Do this with SEVERAL choices of speeds and times.
#     -- For each run, write (here in this file, below this comment):
#          -- How far SHOULD the robot have moved, if it really moved
#               at the requested speed for the requested time?
#          -- How far DID the robot move?
#               (Measure it, with a yardstick, converting units to cm.)
#          -- How far did the robot REPORT that it moved, in cm?

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
