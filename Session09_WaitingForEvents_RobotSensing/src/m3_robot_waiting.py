"""
This module lets you practice the WAIT-UNTIL-EVENT pattern:
   while True:
       ...
       if <event has occurred>:
           break
       ...
in the context of waiting for a robot sensor to reach a given threshold.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  December 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time
import random


def main():
    """ Calls the   TEST   functions in this module. """
#     test_go_until_black()
#     test_go_distance_until_time()
    test_go_distance_until_sensor()


def test_go_until_black():
    """ Tests the    go_until_black    function. """
    # TODO: Implement this WITH YOUR INSTRUCTOR.
    port = 'sim'
    robot = new_create.Create(port)
    reading_when_stop = go_until_black(robot, 100)
    print(reading_when_stop)
    time.sleep(2)

    robot.shutdown()


def go_until_black(robot, threshold):
    """
    Start a robot moving at a slow speed, straight forward.
    Stops the robot when its front left cliff sensor
    gets a value LESS than the given threshold.

    Preconditions: The arguments satisfy:
      :type robot: new_create.Create
      :type threshold: int
    with the threshold being between 0 and 4095.
    """
    # TODO: Implement this WITH YOUR INSTRUCTOR.
    robot.driveDirect(5, 5)
    sensor_name = new_create.Sensors.cliff_front_left_signal
    while True:
        reading = robot.getSensor(sensor_name)
        print(reading)
        if reading < threshold:
            break
        time.sleep(0.05)
    robot.stop()
    return reading


def test_go_distance(function_to_test):
    """ Tests the given    go_distance_until...    function. """
    # TODO: Do your testing in the simulator.
    #       If time permits, ALSO test with a REAL robot,
    #       replacing   'sim'   by YOUR port number when doing so.
    port = 'sim'
    robot = new_create.Create(port)

    number_of_tests = 5
    for _ in range(number_of_tests):

        # Go a random distance that ranges from 10 to 100 cm.
        # Use a random speed that ranges from slow (5) to fast (50).
        centimeters = random.randrange(10, 101)
        speed = random.randrange(5, 51)

        message1 = 'Going {} cm at {} cm per second.'
        print(message1.format(centimeters, speed))
        reported_distance = function_to_test(robot, centimeters, speed)

        message2 = '   The robot thinks it went {} cm.'
        print(message2.format(reported_distance))

        # Pause between each movement to be able to see them separately.
        time.sleep(2)

    robot.shutdown()

    # Pause briefly in case we are about to make another connection to
    # this robot.  There needs to be a short pause between connections.
    time.sleep(1)


def test_go_distance_until_time():
    """ Tests the   go_distance_until_time    function. """
    test_go_distance(go_distance_until_time)



def go_distance_until_time(robot, centimeters, centimeters_per_second):
    """
    Makes the given robot go straight the given number of centimeters
    at the given speed (in centimeters per second), then stop.
      Positive centimeters means go forward;
      negative centimeters means go backwards.

    Returns the number of centimeters that the robot reports
    that it went (positive if it went forward, negative otherwise).

    IMPLEMENTATION REQUIREMENT:  Use this algorithm
       (which we'll call the   "time"   algorithm):

         0. Compute the TIME the robot must move to achieve the
              requested DISTANCE at the requested SPEED.
         1. Start the robot moving at the requested speed.
         2. Sleep the computed time.
         3. Stop the robot.

    Preconditions: The arguments satisfy:
      :type robot: new_create.Create
      :type centimeters: float
      :type centimeters_per_second: float
          with centimeters_per_second being positive.
    """
    # The following helps ensure that you get the arguments correct.
    assert(isinstance(robot, new_create.Create))
    assert(isinstance(centimeters, (int, float)))
    assert(isinstance(centimeters_per_second, (int, float)))
    assert(centimeters_per_second > 0)

    # TODO: 2b. Implement and test this function.
    #
    # NOTE: Use the REQUIRED ALGORITHM TO IMPLEMENT,
    #       per the specification, with the required restrictions on
    #       the arguments (in particular, centimeters_per_second > 0).
    #
    # HINT: ** First solve this problem BY HAND on an example! **

    robot.go(centimeters_per_second, 0)
    time1 = float(centimeters / centimeters_per_second)
    time.sleep(time1)
    robot.stop()
    sensor_n = new_create.Sensors.distance
    reading1 = robot.getSensor(sensor_n)
    return (reading1 / 10)

    robot.shutdown()



def test_go_distance_until_sensor():
    """ Tests the   go_distance_until_sensor    function. """
    test_go_distance(go_distance_until_sensor)


def go_distance_until_sensor(robot, centimeters, centimeters_per_second):
    """
    NOTE: This function has the same specification as the
             go_distance_until_time
          function, except that it requires a DIFFERENT IMPLEMENTATION.
          See details in the following specification.

    Makes the given robot go straight the given number of centimeters
    at the given speed (in centimeters per second), then stop.
      Positive centimeters means go forward;
      negative centimeters means go backwards.

    Returns the number of centimeters that the robot reports
    that it went (positive if it went forward, negative otherwise).

    IMPLEMENTATION REQUIREMENT:  Use this algorithm
       (which we'll call the   "sensor"   algorithm):

         0. Ask the robot to do a DISTANCE sensor reading.
              (but ignore the returned value).
         1. Tell the robot to start moving in the specified direction
              at the specified speed.
         2. Repeatedly:
              a. Ask the robot to do a DISTANCE sensor reading.
              b. See if the TOTAL distance traveled so far is greater
                   than or equal to the requested distance to go.
                   If so, BREAK out of the loop.
              c. Sleep a small amount of time (try 0.01).
                   This is necessary for real robots for reasons
                   we will discuss later.
         3. Stop the robot.

    Preconditions: The arguments satisfy:
      :type robot: new_create.Create
      :type centimeters: float
      :type centimeters_per_second: float
          with centimeters_per_second being positive.
    """
    # The following helps ensure that you get the arguments correct.
    assert(isinstance(robot, new_create.Create))
    assert(isinstance(centimeters, (int, float)))
    assert(isinstance(centimeters_per_second, (int, float)))
    assert(centimeters_per_second > 0)

    # TODO: 2b. Implement and test this function.
    #
    # NOTE: Use the REQUIRED ALGORITHM TO IMPLEMENT,
    #       per the specification, with the required restrictions on
    #       the arguments (in particular, centimeters_per_second > 0).
    #
    # HINT: ** First solve this problem BY HAND on an example! **
    robot.go(centimeters_per_second, 0)
    sensor_n = new_create.Sensors.distance
    distance = robot.getSensor(sensor_n)
    time.sleep(float(centimeters / centimeters_per_second))

    return (distance / 10)
    while True:
        centimeters < distance
        break
    time.sleep(0.01)

    robot.shutdown()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
