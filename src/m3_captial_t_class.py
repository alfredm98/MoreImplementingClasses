"""
A   CapitalT   class and methods that use the Cross class.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Alfred Mustafa.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the test functions. As you implement CapitalT method uncomment the appropriate tests. """
    # --------------------------------------------------------------
    #   Uncomment only 1 test at a time as you develop your code.
    # --------------------------------------------------------------
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    # run_test_simple_t()
    # run_test_set_colors()
    # run_test_move_by()
    run_test_clone()


def run_test_simple_t():
    """ Tests for the __init__ method and attach_to method. See the simple_t PDF for expected output. """
    print()
    print('--------------------------------------------------')
    print('Testing    __init__    and    attach_to ')
    print('--------------------------------------------------')
    window = rg.RoseWindow(600, 400, 'Test 1 - Simple Ts')
    t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
    print("Expected: Point(250.0, 40.0) Point(350.0, 60.0)")
    print("Actual:  ", t1.h_rect.get_upper_left_corner(), t1.h_rect.get_lower_right_corner())
    print("Expected: Point(290.0, 40.0) Point(310.0, 240.0)")
    print("Actual:  ", t1.v_rect.get_upper_left_corner(), t1.v_rect.get_lower_right_corner())
    t1.attach_to(window)
    t2 = CapitalT(rg.Point(150, 150), 100, 150, 40)
    t2.attach_to(window)
    t3 = CapitalT(rg.Point(450, 150), 10, 15, 4)
    t3.attach_to(window)
    window.render()
    print("See graphics window and compare to the simple_t PDF")
    window.close_on_mouse_click()


def run_test_set_colors():
    """ Tests for the set_colors method.  See the set_colors PDF for expected output. """
    window = rg.RoseWindow(600, 400, 'Test 2 - Colorful Ts')
    t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
    t1.set_colors('red', 'magenta')
    t1.attach_to(window)
    t2 = CapitalT(rg.Point(150, 150), 100, 150, 40)
    t2.set_colors('green', 'purple')
    t2.attach_to(window)
    t3 = CapitalT(rg.Point(450, 150), 10, 15, 4)
    t3.set_colors('blue', 'gray')
    t3.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def run_test_move_by():
    """ Tests for the move_by method.  See the move_by PDF for expected output. """
    window = rg.RoseWindow(600, 400, 'Test 3 - Moving T')
    little_red_t = CapitalT(rg.Point(300, 50), 60, 80, 5)
    little_red_t.set_colors('red', 'gray')
    little_red_t.attach_to(window)
    window.render(0.5)
    little_red_t.move_by(0, 100)
    window.render(0.5)
    little_red_t.move_by(0, 100)
    window.render(0.5)
    for k in range(40):
        little_red_t.move_by(5, -2)
        window.render(0.05)
    window.close_on_mouse_click()


def run_test_clone():
    """ Tests for the clone method.  See the clone PDF for expected output. """
    window = rg.RoseWindow(650, 400, 'Test 4 - Cloning Ts')
    first_t = CapitalT(rg.Point(75, 50), 80, 80, 40)
    first_t.set_colors('blue', 'cyan')
    for k in range(6):
        t = first_t.clone()
        if k < 2:
            t.set_colors('white', 'black')
        t.move_by(100 * k, 20 * k)
        t.attach_to(window)
    first_t.move_by(0, 200)
    first_t.attach_to(window)
    window.render()
    window.close_on_mouse_click()


########################################################################
# The   CapitalT   class (and its methods) begins here.
########################################################################


class CapitalT(object):
    """ Manages a CapitalT graphics object which is made up of two rectangles. """

    def __init__(self, intersection_center, width, height, letter_thickness):
        """
        What comes in:
           -- self
           -- an rg.Point for the intersection center of the CapitalT
              -- This point is also center of the horizontal rectangle.
           -- a int for the width of the CapitalT (the width of the horizontal rectangle)
           -- a int for the height of the CapitalT (the height of the vertical rectangle)
           -- a int for the thickness of each rectangle (the letter's thickness)
        What goes out:  Nothing (i.e., None).
        Side effects: Sets two instance variables named:
          -- h_rect  (to represent the horizontal rectangle in the T, the top bar)
          -- v_rect  (to represent the vertical rectangle in the T, the | part of the T)

           *** See the dimensions PDF for the exact placement of the rectangles in the T. ***

        Each rectangle is an rg.Rectangle. Unlike prior modules you are NOT
            allowed to make any other instance variables. You may only use
            exactly these two and must figure out how to do the problem with ONLY
            those two instance variables.

        Example:
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
                -- t1.h_rect would have an upper left corner of (250, 40)
                -- t1.h_rect would have an lower right corner of (350, 60)
                -- t1.v_rect would have an upper left corner of (290, 40)
                -- t1.v_rect would have an lower right corner of (310, 240)

        Type hints:
          :type intersection_center: rg.Point
          :type width:   int
          :type height:   int
          :type letter_thickness:   int
        """
        # --------------------------------------------------------------
        # DONE: 3.
        #   READ the above specification, including the Example.
        #   Implement this method
        #   Note: you will need to also implement attach_to before testing
        # --------------------------------------------------------------
        corner_1 = rg.Point(intersection_center.x + width/2, intersection_center.y - letter_thickness/2)
        corner_2 = rg.Point(intersection_center.x - width/2, intersection_center.y + letter_thickness/2)
        self.h_rect = rg.Rectangle(corner_1, corner_2)
        corner_3 = rg.Point(intersection_center.x + letter_thickness/2, intersection_center.y + letter_thickness/2)
        corner_4 = rg.Point(intersection_center.x - letter_thickness/2, intersection_center.y + height - letter_thickness/2)
        self.v_rect = rg.Rectangle(corner_3, corner_4)

        self.h_rect2 = rg.Rectangle(self.h_rect.corner_2, self.h_rect.corner_1)
        self.v_rect2 = rg.Rectangle(self.v_rect.corner_2, self.v_rect.corner_1)

    def attach_to(self, window):
        """
        What comes in:
           -- self
           -- an rg.RoseWindow
        What goes out:  Nothing (i.e., None).
        Side effects:
          -- Attaches both instance rectangles to the given window.
          -- Hint: Attach h_rect second to make it draw in front of v_rect

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.attach_to(window)

        Type hints:
          :type window: rg.RoseWindow
        """
        # --------------------------------------------------------------
        # DONE: 4.
        #   READ the above specification, including the Example.
        #   Implement and test this method by looking at the console and
        #     the graphics window (compare it to simple_t.pdf)
        # --------------------------------------------------------------
        self.v_rect.attach_to(window)
        self.h_rect.attach_to(window)

    def set_colors(self, fill_color, outline_color):
        """
        What comes in:
          -- self
          -- a string that represents a valid rosegraphics color
          -- a string that represents a valid rosegraphics color
        What goes out:  Nothing (i.e., None).
        Side effects:
          -- sets the fill_color of both rectangles to the given fill color
          -- sets the outline_color of both rectangles to the given outline color

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.set_color('red', 'blue')

        Type hints:
          :type fill_color: str
          :type outline_color: str
        """
        # --------------------------------------------------------------
        # DONE: 5.
        #   READ the above specification, including the Example.
        #   Implement and test this method by uncommenting the appropriate
        #     run_test method in main. Compare the graphics window to
        #     set_colors.pdf.
        # --------------------------------------------------------------
        self.h_rect.fill_color = fill_color
        self.v_rect.fill_color = fill_color
        self.h_rect.outline_color = outline_color
        self.v_rect.outline_color = outline_color

    def move_by(self, dx, dy):
        """
        What comes in:
           -- self
           -- an int amount to move in the x direction
           -- an int amount to move in the y direction
        What goes out:  Nothing (i.e., None).
        Side effects:
          -- Moves both h_rect and v_rect the specified dx and dy amounts.

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.attach_to(window)
            window.render(0.5)
            t1.move_by(100, 200) # Moves the T 100 pixels right and 200 down.
            window.render()  # necessary to see the change

        Type hints:
          :type dx: int
          :type dy: int
        """
        # --------------------------------------------------------------
        # DONE: 6.
        #   READ the above specification, including the Example.
        #   Implement and test this method by uncommenting the appropriate
        #     run_test method in main. Compare the graphics window to
        #     move_by.pdf. Note: the pdf shows the different locations
        #     that the T moves through, but there is only 1 T at any moment.
        # --------------------------------------------------------------
        self.h_rect.corner_1.x = self.h_rect.corner_1.x + dx
        self.h_rect.corner_1.y = self.h_rect.corner_1.y + dy
        self.h_rect.corner_2.x = self.h_rect.corner_2.x + dx
        self.h_rect.corner_2.y = self.h_rect.corner_2.y + dy
        self.v_rect.corner_1.x = self.v_rect.corner_1.x + dx
        self.v_rect.corner_1.y = self.v_rect.corner_1.y + dy
        self.v_rect.corner_2.x = self.v_rect.corner_2.x + dx
        self.v_rect.corner_2.y = self.v_rect.corner_2.y + dy
        return self

    def clone(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns a new CapitalT that is located in the same position as
               this CapitalT with the same colors for the rectangles.
        Side effects:
          -- None

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.set_color('red', 'blue')
            t2 = t1.clone() # t2 is at the same location WITH THE SAME COLORS

        Type hints:
          :rtype: CapitalT
        """
        # --------------------------------------------------------------
        # DONE: 7.
        #   READ the above specification, including the Example.
        #   Implement and test this method by uncommenting the appropriate
        #     run_test method in main. Compare the graphics window to
        #     clone.pdf.
        # --------------------------------------------------------------
        #self.h_rect.fill_color = self.h_rect.fill_color
        #self.v_rect.fill_color = self.v_rect.fill_color
        h_rect2 = self.h_rect2
        v_rect2 = self.v_rect2
        self.second = CapitalT(h_rect2.get_center(), h_rect2.get_width(), h_rect2.get_width() , v_rect2.get_width())
        self.second.set_colors(self.h_rect.fill_color, self.h_rect.outline_color)
        return self.second

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
