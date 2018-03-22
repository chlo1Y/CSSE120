"""
A    BallSimulation   object simulates a world of Balls
(of various kinds).

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, and their colleagues.
         October 2014.
"""

import rosegraphics as rg
import time


# ----------------------------------------------------------------------
# The BallSimulation appears below here.
# Students - you probably do NOT want to change anything in here.
# ----------------------------------------------------------------------

class Simulator:
    """ Simulates a world of Changers (of various kinds). """

    def __init__(self, changers=[], width=1200, height=800,
                 msecs_per_frame=50):
        """
        Constructs a RoseWindow for the simulation's window,
        with the given width and height.
        """
        self.changers = changers
        self.width = width
        self.height = height
        self.msecs_per_frame = msecs_per_frame

        title = 'World of Changers'
        self.window = rg.RoseWindow(self.width, self.height, title)

        for changer in self.changers:
            changer.shape.attach_to(self.window.initial_canvas)

        rg._master_Tk.after(self.msecs_per_frame, self.run_one_frame)

        rg._master_Tk.mainloop()


#         self.is_time_to_stop = False
#         self.is_paused = False
#         self.highlighted_ball = None
#         self.selected_ball = None
#         self.rectangle_for_highlighting = None

    def run_one_frame(self):
        for changer in self.changers:
            changer.change()

        self.window.render()
        rg._master_Tk.after(self.msecs_per_frame, self.run_one_frame)


    def add_ball(self, ball):
        """
        Adds the given Ball to the simulation.
        Each Ball starts in the "not stopped" state.
        """
        self.balls.append(ball)
        ball.is_stopped = False

        # On the fly, add two new instance variables to the Ball:
        ball._window = self.window
        ball._simulation = self

    def remove_ball(self, ball):
        """
        Removes the given Ball from the simulation.
        """
        self.balls.remove(ball)

    def draw_balls(self):
        """
        Draws each Ball's circle,
        plus the highlighting rectangle if it exists.
        """
        if not self.window:
            return

        for ball in self.balls:
            c = ball.circle
            c.draw(self.window)

        if self.rectangle_for_highlighting:
            self.rectangle_for_highlighting.draw(self.window)

    def undraw_balls(self):
        """
        Un-draws each Ball's circle,
        plus the highlighting rectangle if it exists.
        """
        if not self.window:
            return

        for ball in self.balls:
            c = ball.circle
            c.undraw()

        if self.rectangle_for_highlighting:
            self.rectangle_for_highlighting.undraw()

    def change_balls(self):
        """
        Calls each Ball's   change  method,
        unless the Ball is in the   stopped  state.
        """
        for ball in self.balls:
            if not ball.is_stopped:
                ball.change()

    def start(self):
        """
        Constructs a GraphWin for the simulation.
        Repeatedly draws, then undraws, each Ball's circle,
        then calls each Ball's   change   method.
        Stops when the   stop   method returns True.
        """

        while True:
            self.draw_balls()
            time.sleep(0.001)
            self.undraw_balls()

            if not self.is_paused:
                self.change_balls()

            self.handle_events()
            if self.is_time_to_stop:
                break

        # Get one last look at the Balls.
        self.draw_balls()
        time.sleep(2)

    def handle_events(self):
        """
        Handle mouse and key events, as follows:
        
        Handle key events:
          q - quit the simulation after a brief pause
          p - pause the simulation
          r - resume the simulation
                (and unhighlight any highlighted Ball)
          b - pause the simulation and highlight the best Ball
          w - pause the simulation and highlight the worst Ball
          c - pause the simulation and highlight the closest Ball
                to the NEXT mouse-click
          s - stop the most recently-highlighted Ball,
                i.e., no longer call its   change  method
          k - kill the most recently-highlighted Ball
                i.e., remove it from the list of simulated Balls.
              
        Upper and lower-case letters are treated the same.
        
        Handle mouse events:
          -- Immediately after a c key-press, selects closest Ball
             to the mouse-click for highlighting
          -- Otherwise quits the simulation after a brief pause.
        """
        key = self.window.checkKey()

        if key:
            if key.lower() == 'q':
                self.is_time_to_stop = True
            elif key.lower() == 'p':
                self.is_paused = True
            elif key.lower() == 'r':
                if self.rectangle_for_highlighting:
                    self.rectangle_for_highlighting.undraw()
                    self.rectangle_for_highlighting = None
                self.is_paused = False
            elif key.lower() == 'b':
                self.is_paused = True
                self.highlight(self.best_ball())
            elif key.lower() == 'w':
                self.is_paused = True
                self.highlight(self.worst_ball())
            elif key.lower() == 'c':
                self.is_paused = True
                self.draw_balls()
                mouse_point = self.window.getMouse()
                self.highlight(self.closest_ball(mouse_point))
                self.undraw_balls()
            elif key.lower() == 's':
                if self.selected_ball:
                    self.selected_ball.is_stopped = True
            elif key.lower() == 'k':
                if self.selected_ball:
                    self.remove_ball(self.selected_ball)

        if self.window.checkMouse():
            self.is_time_to_stop = True

    def closest_ball(self, point):
        """
        Returns the closest Ball to the given Point,
        or None if there are no Balls in the simulation at this time.
        """
        if len(self.balls) == 0:
            return None

        closest = self.balls[0]
        for k in range(1, len(self.balls)):
            if self.balls[k].distance_from(point) < closest.distance_from(point):
                closest = self.balls[k]

        return closest

    def best_ball(self):
        """
        Returns the best Ball in the simulation,
        or None if there are no Balls in the simulation at this time.
        """
        if len(self.balls) == 0:
            return None

        best = self.balls[0]
        for k in range(1, len(self.balls)):
            best = best.better(self.balls[k])

        return best

    def worst_ball(self):
        """
        Returns the w0rst Ball in the simulation,
        or None if there are no Balls in the simulation at this time.
        """
        if len(self.balls) == 0:
            return None

        worst = self.balls[0]
        for k in range(1, len(self.balls)):
            better = worst.better(self.balls[k])
            if better is worst:
                worst = self.balls[k]

        return worst

    def highlight(self, ball):
        """
        Highlights the given Ball by drawing a rectangle around it,
        and marks that Ball as the   selected   Ball.
        Does nothing, however, if the given Ball is None.
        """
        if not ball:
            return

        self.rectangle_for_highlighting = zg.Rectangle(ball.circle.p1, ball.circle.p2)
        self.rectangle_for_highlighting.setWidth(3)
        self.rectangle_for_highlighting.draw(self.window)
        self.selected_ball = ball
