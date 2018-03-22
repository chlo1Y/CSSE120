"""
This module is a VERY BASIC introduction to the Create robot.
We'll use it to:
  -- Help you figure out the mechanics of establishing and using
       a Bluetooth connection to the robot.
  -- Serve as a basic example.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         Dave Fisher and their colleagues. December 2013.
"""

import new_create
import time


def main():
    # ------------------------------------------------------------------
    # Set the port to whatever COM number YOUR laptop is using
    # for its connection to the BAM on the Create robot.
    # Then connect to a Create via that port.
    # Put the robot in "full mode" so that sensors don't stop the robot.
    # ------------------------------------------------------------------
    port = 3  # Use YOUR laptop's COM number
    robot = new_create.Create(port)
    robot.toFullMode()

    # ------------------------------------------------------------------
    # Start moving:
    #   -- left wheel at 30 centimeters per second forwards,
    #   -- right wheel at 25 centimeters per second forwards.
    # (so forward but veering to the right).
    # Sleep for 4 seconds (while doing the above motion),
    # then stop.
    # ------------------------------------------------------------------
    robot.driveDirect(30, 25)
    time.sleep(4.0)
    robot.stop()

    # ------------------------------------------------------------------
    # All sensor data is obtained by the   getSensor   method.
    # The  Sensors  class has constants for all sensor names available.
    # ------------------------------------------------------------------
    sensor = new_create.Sensors.cliff_front_left_signal
    reflectance = robot.getSensor(sensor)
    print('Current value of the front left cliff sensor:', reflectance)

    # ------------------------------------------------------------------
    # ALWAYS execute the following before your program ends.  Otherwise,
    # your robot may be left in a funky state and on the NEXT run,
    # it might fail to connect or it might run incorrectly.
    # ------------------------------------------------------------------
    robot.shutdown()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
