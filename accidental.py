"""
Draw sharps, flats, and naturals.
In order for the symbols to appear a specific way
there are lots of numerical constants in this class.

Gregary C. Zweigle

2019

"""

import item


class Accidental(item.Item):
    def __init__(self, shared, x, y, value, a):
        x = x - 2*round(a)  # Put to the left of the note.
        item.Item.__init__(self, shared, x, y)
        self.line_thickness = shared.line_thickness
        self.value = value

    def draw(self, frame):
        if self.value == "flat":
            self.__draw_a_flat(frame)
        elif self.value == "natural":
            self.__draw_a_natural(frame)
        elif self.value == "sharp":
            self.__draw_a_sharp(frame)

    def __draw_a_flat(self, frame):
        for k in range(self.line_thickness):
            # Vertical stem.
            self.write_to_array(frame, self.x[0]-5-k, self.x[0]-5-k,
                                self.y[0]-25, self.y[0]+5)
            # Horizontal segment.
            self.write_to_array(frame, self.x[0]-5, self.x[0]+5,
                                self.y[0]-5+k, self.y[0]-5+k)
            # Diagonal segment.
            for x in range(10):
                self.write_to_array(frame, self.x[0]+x-5, self.x[0]+x-5,
                                    self.y[0]-x+5+k, self.y[0]-x+5+k)

    def __draw_a_natural(self, frame):
        self.__draw_natural_and_sharp_vertical_lines(frame, True)
        for k in range(self.line_thickness):
            # Two diagonal segments.
            for x in range(7):
                y_lower = self.y[0]+x+k
                y_upper = self.y[0]+x-13+k
                self.__draw_natural_and_sharp_points(frame, x, y_lower, y_upper)

    def __draw_a_sharp(self, frame):
        self.__draw_natural_and_sharp_vertical_lines(frame, False)
        for k in range(self.line_thickness):
            # Two diagonal segments.
            for x in range(-3, 12):
                y_lower = self.y[0]+x+1+k
                y_upper = self.y[0]+x-12+k
                self.__draw_natural_and_sharp_points(frame, x, y_lower, y_upper)

    def __draw_natural_and_sharp_vertical_lines(self, frame, is_a_natural):
        if is_a_natural:
            shorten_it = 10
        else:
            shorten_it = 0
        for k in range(self.line_thickness):
            self.write_to_array(frame, self.x[0]-k, self.x[0]-k,
                                self.y[0]-(20-shorten_it), self.y[0]+20)
            self.write_to_array(frame, self.x[0]-7-k, self.x[0]-7-k,
                                self.y[0]-20, self.y[0]+(20-shorten_it))

    def __draw_natural_and_sharp_points(self, frame, x, y_lower, y_upper):
        self.write_to_array(frame, self.x[0]-x, self.x[0]-x,
                            y_upper, y_upper)
        self.write_to_array(frame, self.x[0]-x, self.x[0]-x,
                            y_lower, y_lower)
