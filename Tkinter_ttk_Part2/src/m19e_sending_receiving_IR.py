"""
This module demonstrates SENDING IR and RECEIVING IR.

Authors: David Mutchler, Chandan Rupakheti and their colleagues,
         April 2013.
"""

import new_create


def main():
    """ Calls the   TEST   functions in this module. """

    # The simulator does NOT simulate IR.  Use a REAL robot to test!
    port = 'sim'
    robot = new_create.Create(port)

    # Attach the RED wire of the "hat" device to either of the two
    # +5V holes.  Attach the BLACK wire to the LD1 hole.  Maybe turn
    # off the overhead lights.  The little red light on the device
    # blinks when it is sending a signal.

    # To SEND an IR signal, use the   startIR  method (NOT sendIR):
    number = 57  # IR signals can be between 0 and 254
    robot.startIR(number)

    # To RECEIVE an IR signal, use the usual   getSensor  method
    # with the   ir_byte   sensor type.  A result of  255  means
    # "nothing received".
    # IMPORTANT: Be sure you understand why a LOOP is necessary below.
    #            Discuss with your instructor!
    ir_sensor = new_create.Sensors.ir_byte
    while True:
        number_heard = robot.getSensor(ir_sensor)
        if number_heard != 255:
            break

    print(number_heard)

    # To STOP a  startIR  method from sending, use   stopIR   method.
    robot.stopIR()

    # WHAT YOU SHOULD DO TO TRY THIS OUT:
    # In tkinter, make:
    #   Button:  When pressed, starts sending a number (say, 57).
    #   Button:  When pressed, stops the IR sending.
    #   Button:  When pressed, prints whatever it currently hears
    #            (maybe 255).

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
