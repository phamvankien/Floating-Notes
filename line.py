"""
Draw horizontal and vertical line segments when a note is
above the top score or below the bottom score.

Gregary C. Zweigle

2019

"""

import item


class Line(item.Item):
    def __init__(self, shared, x, y, timing, stem_up, oval_width):
        item.Item.__init__(self, shared, x, y)
        self.width = round(1.5*oval_width)  # Width of the horizontal line.
        self.timing = timing
        self.stem_up = stem_up
        # Using as an array index so round to make sure its an integer.
        if stem_up:
            self.oval_width = round(oval_width)
        else:
            self.oval_width = -round(oval_width)
        self.staff_inc = 2*shared.y_spacing
        self.line_thickness = shared.line_thickness

    def draw(self, frame):
        # Draw the horizontal lines.
        for k in range(self.line_thickness):
            self.write_to_array(frame, self.x[0] - self.width, self.x[0] +
                                self.width, self.y[0] + k, self.y[0] + k)
        # Draw the stem segments.
        if self.timing != "whole":
            if self.stem_up:
                for k in range(self.line_thickness):
                    self.write_to_array(frame, self.x[0] + self.oval_width + k,
                                        self.x[0] + self.oval_width + k,
                                        self.y[0] - self.staff_inc, self.y[0])
            else:
                for k in range(self.line_thickness):
                    self.write_to_array(frame, self.x[0] + self.oval_width + k,
                                        self.x[0] + self.oval_width + k,
                                        self.y[0], self.y[0] + self.staff_inc)
