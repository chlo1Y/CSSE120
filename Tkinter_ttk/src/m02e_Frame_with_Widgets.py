"""
Example showing for tkinter and ttk:
  -- How to CONSTRUCT and DISPLAY a WIDGET, in this case:
  -- ttk.Frame - a container for other Widgets
  -- ttk.Button - a button in the ttk style

Authors: David Mutchler, Mark Hays, and their colleagues
         at Rose-Hulman Institute of Technology. October 2014.
"""

import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=(30, 10), relief='raised')
    main_frame.grid()

    connect_button = ttk.Button(main_frame, text='Connect')
    example_label = ttk.Label(main_frame, text='Enter something here:')
    entry_box = ttk.Entry(main_frame, width=20)

    connect_button.grid()

    example_label.grid(row=1, column=0)
    entry_box.grid(row=1, column=1)

    root.mainloop()

# ----------------------------------------------------------------------
# The 6 statements in main (above) do the following, respectively:
#   1. Constructs a tkinter.Tk.
#        This is the top-level window, traditionally called 'root'.
#
#   2. Constructs a widget (here, a ttk.Frame) on the root.
#        Use Frame objects to group other items.  Best practice is
#        to make a Frame and put all other widgets on the Frame.
#
#        This frame has a "pad" of 30 pixels on two borders
#        and 10 pixels on the other two borders.
#
#   3. Displays the ttk.Frame, using a layout called 'grid'.
#         -- We'll learn more about controlling the layout later.
#         -- For now, simply apply the   grid   method to ANY widget
#            to make it appear on the screen.
#
#   4. Constructs a widget (here, a ttk.Button) from the main_frame.
#         Set its text to 'Connect'.
#
#   5. Displays the ttk.Button, again using the 'grid' layout.
#
#   6. Runs the Event Loop.  tkinter maintains that loop.
#         This is a LOOP -- the code STAYS in here until the root window
#         is closed (by the user, or by the program itself).
#
# When you run the program, note that:
#   -- A window appears.
#   -- The window has the usual minimize, maximize and close buttons.
#   -- Those buttons work as expected.
#   -- There is also a button whose label is   Connect.
#   -- Pressing the Connect button causes visual feedback in the usual
#        way, but nothing else happens.  That's because we haven't told
#        tkinter/ttk what to do when the Connect button is pressed.
#        You'll see how to do that in the next examples.
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
