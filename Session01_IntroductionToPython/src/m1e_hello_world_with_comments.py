"""
The classic first program in any introduction to software development.

Authors: Many, many people over many, many years.
         David Mutchler, Amanda Stouder, Chandan Rupakheti,
         and Claude Anderson wrote this version.  December 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do here.  Just use it as an example to see:
#   0. The two kinds of comments:
#        -- Green, multi-line "docstrings".
#        -- Pink, one-line internal comments.
#   1. The  ** definition **   of the   main   function.
#   2. The   IF statement    at the bottom that CALLS main
#        (which makes  main  run).
#   3. How  main  PRINTS a STRING.
#        -- A STRING is a sequence of characters.
#        -- Literal strings are notated with single or double quotes,
#             e.g.    'I don't like eggs!'   "I love oranges"
#-----------------------------------------------------------------------


def main():
    """ Prints a welcoming message on the console. """
    print('I like apples')

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
