"""
Draw the note stem and the timing marks on the stem.

Gregary C. Zweigle

2019

"""

import item


class Stem(item.Item):
    def __init__(self, shared, x, y, timing, stem_up, a):
        item.Item.__init__(self, shared, x, y)
        self.timing = timing
        self.stem_up = stem_up
        self.stem_height = shared.stem_height
        self.a = round(a)  # Using as an index so make sure its an integer.
        self.timing_width = round(1.5*self.a)
        self.line_thickness = shared.line_thickness

    def draw(self, frame):
        if self.timing != "whole":
            for stem_width in range(self.line_thickness):
                if self.stem_up:
                    x_loc = self.x[0] + self.a
                    y_top = self.y[0] - self.stem_height
                    y_bottom = self.y[0]
                else:
                    x_loc = self.x[0] - self.a
                    y_top = self.y[0]
                    y_bottom = self.y[0] + self.stem_height
                self.__draw_stem(frame, x_loc+stem_width, y_top, y_bottom)
                self.__draw_timings_on_stem(frame, stem_width,
                                            x_loc, y_top, y_bottom)

    def __draw_stem(self, frame, x_loc, y_top, y_bottom):
        self.write_to_array(frame, x_loc, x_loc, y_top, y_bottom)

    def __draw_timings_on_stem(self, frame, stem_width, x_loc, y_top, y_bottom):
        for x in range(self.timing_width):
            if self.stem_up:
                y_loc = y_top + x + stem_width
            else:
                y_loc = y_bottom - x + stem_width
            if (self.timing == "sixteenth" or self.timing == "sixteenth-dot" or
               self.timing == "eighth" or self.timing == "eighth-dot"):
                self.write_to_array(frame, x_loc+x, x_loc+x, y_loc, y_loc)
            if self.timing == "sixteenth" or self.timing == "sixteenth-dot":
                # Add another timing mark but move it on the stem.
                if self.stem_up:
                    y_loc += 4*self.line_thickness
                else:
                    y_loc -= 4*self.line_thickness
                self.write_to_array(frame, x_loc+x, x_loc+x, y_loc, y_loc)
