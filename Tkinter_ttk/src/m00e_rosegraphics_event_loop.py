"""
This module demonstrates a simple EVENT LOOP
that uses POLLING (not an event queue) to get the events.

This is a RoseGraphics example, NOT a Tkinter example.

Functions:
  -- main: Contains the Event Loop
  -- mouse_handler: A handler for one kind of event
  -- key_handler: A handler for another kind of event
  -- make_window: Returns a window and rg.Text object for this example

Authors: David Mutchler, Mark Hays, and their colleagues
         at Rose-Hulman Institute of Technology. October 2014.
"""

import rosegraphics as rg


def main():
    """ Demonstrates a simple Event Loop that polls for events. """

    # ------------------------------------------------------------------
    # Make a window with messages on it.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400, 400, 'Simple Event Loop')

    keyboard_text = rg.Text(rg.Point(140, 30), '')
    keyboard_text.attach_to(window.initial_canvas)

    instructions = 'Click the mouse or press a key.\n Press q to quit.'
    instructions_text = rg.Text(rg.Point(200, 350), instructions)
    instructions_text.attach_to(window.initial_canvas)

    while True:
        # --------------------------------------------------------------
        # Update the window's events.
        # --------------------------------------------------------------
        window.update()

        # --------------------------------------------------------------
        # Poll the devices (mouse and keyboard) to learn the events.
        # If an event has occurred, respond to it.
        # --------------------------------------------------------------
        if window.mouse.mouse_was_pressed:
            mouse_handler(window, window.mouse.mouse_position)

        if window.keyboard.key_was_pressed:
            key_handler(window, window.keyboard.key_that_was_pressed,
                        keyboard_text)

        # --------------------------------------------------------------
        # Render the window.  Then sleep a bit
        # to allow time for other threads/processes to run
        # --------------------------------------------------------------
        window.render(1.0)  # Purposely set way too big, to make a point


def mouse_handler(window, point):
    """
    Draws a small, blue-filled circle on the given window
    at the given point.

    Preconditions:
      :type window: rg.RoseWindowq
      :type point: rg.Point
    """
    circle = rg.Circle(point, 10)
    circle.fill_color = 'blue'
    circle.attach_to(window.initial_canvas)


def key_handler(window, key, textbox):
    """
    Displays a message that indicates what key was pressed,
    putting the message in the given textbox in the given window.
    Also closes the window and exits the program if the key is 'q'.

    Preconditions:
      :type window: rg.RoseWindow
      :type key: str
      :type textbox: rg.Text
    """
    textbox.text = 'You pressed: ' + key
    window.render()

    if key == 'q':
        window.close()
        exit()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
