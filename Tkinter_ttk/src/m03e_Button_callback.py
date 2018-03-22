"""
Example showing for tkinter and ttk:
  -- How to CONSTRUCT and DISPLAY a WIDGET
       (in this case, a ttk.Button)

  -- How to associate a widget (here, a ttk.Button)
       with a CALLBACK function

Authors: David Mutchler, Mark Hays, and their colleagues
         at Rose-Hulman Institute of Technology. October 2014.
"""

import tkinter
from tkinter import ttk
import random


def main():
    root = tkinter.Tk()
    root.title('Hello!')
    root.minsize(300, 0)

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    change_title_button = ttk.Button(main_frame,
                                     text='Change the Title (above)')
    change_title_button.grid()
    change_title_button['command'] = lambda: change_title(root)

    root.mainloop()


def change_title(root):
    """ Make the given root have 10 random letters as its title. """
    random_letters = []
    for _ in range(10):
        random_letters.append(chr(ord('A') + random.randrange(26)))

    random_word = ''.join(random_letters)

    root.title('This title is: {}'.format(random_word))

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
