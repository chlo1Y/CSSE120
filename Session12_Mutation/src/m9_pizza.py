"""
This module lets you practice:
  -- ITERATING (i.e. LOOPING) thru a SEQUENCE
  -- Using OBJECTS
  -- DEFINING functions
  -- CALLING functions

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Zesun Yang.  January 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_draw_points_on_circle()
    test_pizza()
    test_polygon()
    test_fancy_polygon()


# ----------------------------------------------------------------------
# Students: You MUST use this   generate_points_on_circle   function
#           in the exercises that follow.
#           It is ALREADY DONE - you must NOT modify it or add to it.
# ----------------------------------------------------------------------
def generate_points_on_circle(circle, number_of_points_to_generate):
    """
    Returns a list containing the given number of rg.Points,
    where the rg.Points:
      -- all lie on the circumference of the given rg.Circle,
      -- are equally distant from each other, and
      -- go clockwise around the circumference of the given rg.Circle,
            starting at the rightmost point on the rg.Circle.

    See the 'draw_points_on_circle' pictures  in the   pizza.pdf
    file attached, with the points shown on those pictures.

    Preconditions:
      :type circle: rg.Circle
      :type number_of_points_to_generate: int
    where number_of_points_to_generate is nonnegative.
    """
    radius = circle.radius
    center_x = circle.center.x
    center_y = circle.center.y

    # ------------------------------------------------------------------
    # Each point is   delta_degrees   from the previous point,
    # along the circumference of the given circle.
    # ------------------------------------------------------------------
    delta_degrees = 360 / number_of_points_to_generate

    points = []
    degrees = 0
    for _ in range(number_of_points_to_generate):

        # --------------------------------------------------------------
        # Compute x and y of the point on the circumference of the
        # circle by using a polar representation.
        # --------------------------------------------------------------
        angle = math.radians(degrees)
        x = radius * math.cos(angle) + center_x
        y = radius * math.sin(angle) + center_y

        # --------------------------------------------------------------
        # Construct the point and append it to the list.
        # --------------------------------------------------------------
        point_on_circumference = rg.Point(x, y)
        points.append(point_on_circumference)

        # --------------------------------------------------------------
        # The next point will be    delta_degrees    from this point,
        # along the circumference of the given circle.
        # --------------------------------------------------------------
        degrees = degrees + delta_degrees

    return points


def test_draw_points_on_circle():
    """ Tests the   draw_points_on_circle   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    window = rg.RoseWindow(400, 400, 'testing_draw_points ')

    circle1 = rg.Circle(rg.Point(200, 200), 150)
    draw_points_on_circle(window, circle1, 7, 'yellow')
    window.continue_on_mouse_click()
    circle1.detach_from(window.initial_canvas)

    circle2 = rg.Circle(rg.Point(200, 150), 100)
    draw_points_on_circle(window, circle2, 11, 'blue')

    window.close_on_mouse_click()



def draw_points_on_circle(window, circle, number_of_points, color):
    """
    See the 'draw_points_on_circle' pictures in   pizza.pdf   in this
    project; they may help you better understand the following
    specification:

    1. Attaches the given rg.Circle to the initial_canvas
         of the given rg.RoseWindow.
    2. Constructs the given number of rg.Point objects on the given
          rg.Circle's circumference, spaced equally from each other.
    3. For each of those rg.Point objects:
       a. Constructs an rg.Circle centered at that point,
            filled with the given color and with a radius of 10.
       b. Attaches the new rg.Circle to the initial_canvas
            of the given rg.RoseWindow.
       c. Attaches the rg.Point object to the initial_canvas
            of the given rg.RoseWindow.
    4. Renders the given rg.RoseWindow.

    Note that the rg.Point objects will generally be visible
    since they are on TOP of the zg.Circle objects.

    Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_points: int
      :type color: (str, rg.Color)
    where the number_of_points is nonnegative and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 2b. With your instructor:
    #   -- READ and UNDERSTAND the   generate_points_on_circle  function
    #         (defined above).
    #   -- Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate the points to draw.
    points = generate_points_on_circle(circle, number_of_points)
#     print(points)
    circle.attach_to(window.initial_canvas)
    for k in range(len(points)):
        dot = rg.Circle(points[k], 10)
        dot.fill_color = color
        dot.attach_to(window.initial_canvas)
        points[k].attach_to(window.initial_canvas)

    window.render()


def test_pizza():
    """ Tests the   pizza   function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    window1 = rg.RoseWindow(800, 800, 'testing pizza')
    circle1 = rg.Circle(rg.Point(400, 400), 300)
    pizza(window1, circle1, 5, 'blue')


def pizza(window, circle, number_of_slices, color):
    """
    See the 'pizza' pictures in   pizza.pdf   in this project;
    they may help you better understand the following specification:

    1. Draws the given rg.Circle in the given rg.RoseWindow.
    2. Constructs and draws rg.Line objects to make the picture
         look like a 'pizza pie' cut into the given number of 'slices'.
         Each line has the given color and width (thickness) 3.

     Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_slices: int
      :type color: (str, rg.Color)
    where the number_of_slices is at least 2 and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 3b. Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate points on the circle,
    #    then draw lines based in part on those points.
    points = generate_points_on_circle(circle, number_of_slices)
#     print(points)
    circle_x = circle.center.x
    circle_y = circle.center.y
    radius = circle.radius
    circle = rg.Circle(rg.Point(circle_x, circle_y), radius)
    circle.attach_to(window.initial_canvas)


    for k in range(len(points)):
        line = rg.Line(points[k], rg.Point(circle_x, circle_y))
        line.thickness = 3
        line.attach_to(window.initial_canvas)
        line.color = color

    window.render()
    window.close_on_mouse_click()



def test_polygon():
    """ Tests the   polygon   function. """
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    window1 = rg.RoseWindow(800, 800, 'polygon')
    circle1 = rg.Circle(rg.Point(400, 400), 300)
    polygon(window1, circle1, 7, 'red')


def polygon(window, circle, number_of_segments, color):
    """
    See the 'polygon' pictures in   pizza.pdf   in this project;
    they may help you better understand the following specification:

    1. Draws the given rg.Circle in the given rg.RoseWindow.
    2. Constructs and draws rg.Line objects to make the picture
         look like an inscribed regular polygon with the given
         number of segments.
         Each line has the given color and width (thickness) 3.

     Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_segments: int
      :type color: (str, rg.Color)
    where the number_of_segments is at least 3 and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 4b. Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate points on the circle,
    #    then draw lines based in part on those points.
    points = generate_points_on_circle(circle, number_of_segments)
#     print(points)
    circle_x = circle.center.x
    circle_y = circle.center.y
    radius = circle.radius
    circle = rg.Circle(rg.Point(circle_x, circle_y), radius)
    circle.attach_to(window.initial_canvas)


    for k in range(len(points) - 1):
        line1 = rg.Line(points[k], points[k + 1])
        line2 = rg.Line(points[k], points[k - 1])
        line1.thickness = 3
        line1.attach_to(window.initial_canvas)
        line1.color = color
        line2.thickness = 3
        line2.attach_to(window.initial_canvas)
        line2.color = color

    window.render()
    window.close_on_mouse_click()

def test_fancy_polygon():
    """ Tests the   polygon   function. """
    # TODO: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    # Indeed, try a variety of tests to get some really cool pictures.
    # Some that I especially like are:
    #    -- 20 segments, hops of length 7
    #    -- 50 segments, hops of length 25
    #    -- 100 segments, hops of length 30
    window1 = rg.RoseWindow(800, 800, 'polygon')
    circle1 = rg.Circle(rg.Point(400, 400), 300)
    fancy_polygon(window1, circle1, 5, 2, 'pink')

    window2 = rg.RoseWindow(800, 800, 'hihi')
    circle2 = rg.Circle(rg.Point(400, 400), 300)
    fancy_polygon(window2, circle2, 15, 10, 'red')

def fancy_polygon(window, circle, number_of_segments,
                  hops_to_next_point, color):
    """
    See the 'fancy_polygon' pictures in   pizza.pdf   in this project;
    they may help you better understand the following specification:

    1. Draws the given rg.Circle in the given rg.RoseWindow.
    2. Constructs and draws rg.Line objects to make the picture
         look like an inscribed regular polygon with the given
         number of segments, but with each rg.Line going from one point
         on the given zg.Circle to the point on the given zg.Circle
         that is the given number of 'hops' away (wrapping as needed).
         Each line has the given color and width (thickness) 3.

         For example, if hops_to_next_point is 1,
            then the picture is a regular polygon.
         Or, if hops_to_next_point is 2, the lines go:
           -- from point 0 to point 2
           -- from point 1 to point 3
           -- from point 2 to point 4
           -- etc.
         One more example:
           if  hops_to_next_point  is 3 and  number_of_segments  is 5,
           then the lines go:
           -- from point 0 to point 3
           -- from point 1 to point 4
           -- from point 2 to point 0 (note the 'wrap' effect)
           -- from point 3 to point 1
           -- from point 4 to point 2

     Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_segments: int
      :type hops_to_next_point: int
      :type color: (str, rg.Color)
    where the number_of_segments is at least 3,
    the hops_to_next_point is at least 1
    and less than number_of_segments, and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 5b. Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate points on the circle,
    #    then draw lines based in part on those points.
    #
    # HINT: One way to do "wrapping" is to use the  %  operator
    #       appropriately.  THIS REQUIRES SOME THOUGHT - ask as needed.
    points = generate_points_on_circle(circle, number_of_segments)
#     print(points)
    circle.attach_to(window.initial_canvas)

    n = hops_to_next_point
    for k in range(len(points)):

        line2 = rg.Line(points[k - n], points[k])
        line2.thickness = 3
        line2.attach_to(window.initial_canvas)
        line2.color = color

    window.render()
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
