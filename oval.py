"""
Draw the oval portion of a note.

Gregary C. Zweigle

2019

"""

import item


class Oval(item.Item):
    def __init__(self, shared, x, y, timing):
        item.Item.__init__(self, shared, x, y)
        self.radius = shared.note_oval_radius
        self.a = shared.oval_a*self.radius
        self.b = self.radius
        self.timing = timing
        self.line_thickness = shared.line_thickness

    def draw(self, frame):
        # Add one so oval covers full +/- 2*radius.
        for x in range(-2*self.radius, 2*self.radius + 1):
            for y in range(-2*self.radius, 2*self.radius + 1):
                # Fill in all points within the oval unless a whole type timing.
                if x*x/(self.a*self.a) + y*y/(self.b*self.b) < 1:
                    if ((self.timing != "half" and self.timing != "half-dot" and
                       self.timing != "whole") or
                       x*x/(self.a*self.a) + y*y/(self.b*self.b) > 1/3):
                        self.write_to_array(frame, x+self.x[0], x+self.x[0],
                                            y+self.y[0], y+self.y[0])

        # Add the dot timing value.  Its 3x line_thickness to make more visible.
        if (self.timing == "sixteenth-dot" or self.timing == "eighth-dot" or
           self.timing == "quarter-dot" or self.timing == "half-dot"):
            for x in range(3*self.line_thickness):
                for y in range(3*self.line_thickness):
                    # Move the dot out an extra 1.5 times the 'a' oval parameter.
                    x_loc = self.x[0] + round(1.5*self.a) + x
                    y_loc = self.y[0] - round(self.b) + y
                    self.write_to_array(frame, x_loc, x_loc, y_loc, y_loc)

    def get_oval_width(self):
        return self.a
