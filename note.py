"""
The notes class builds a note out of all the pieces of the note.

Gregary C. Zweigle

2019

"""

import accidental
import line
import oval
import stem


class Note:

    def __init__(self, shared, value, timing, sharp_flat):

        x = shared.x_staff_end
        y = shared.y_lowest_note_location - value * shared.y_spacing

        # Instantiate the parts of each note: the oval, the stem,
        # the lines when above and below the staff, and any accidentals.

        self.oval = oval.Oval(shared, x, y, timing)

        self.accidental = accidental.Accidental(shared, x, y, sharp_flat,
                                                self.oval.get_oval_width())
        self.stem = None
        self.__instantiate_stem(shared, value, timing)

        self.lineList = list([])
        self.__instantiate_lines(shared, value, timing)

    def draw(self, frame):
        self.oval.draw(frame)
        self.stem.draw(frame)
        self.accidental.draw(frame)
        for lines in self.lineList:
            lines.draw(frame)

    def move(self):
        self.oval.move()
        self.stem.move()
        self.accidental.move()
        for lines in self.lineList:
            lines.move()

    def __instantiate_stem(self, shared, value, timing):
        x = shared.x_staff_end

        # Below and above the staff, the stem starts at a fixed location.
        if value <= shared.key_lower_stem_start:
            y_stem = shared.y_lowest_note_location - \
                     (shared.key_lower_stem_start+1) * shared.y_spacing
        elif value >= shared.key_upper_stem_start:
            y_stem = shared.y_lowest_note_location - \
                     (shared.key_upper_stem_start-1) * shared.y_spacing
        else:
            y_stem = shared.y_lowest_note_location - value * shared.y_spacing

        stem_up = self.__return_true_if_stem_is_up(value,
                                                   shared.stem_up_endpoints)

        self.stem = stem.Stem(shared, x, y_stem, timing,
                              stem_up, self.oval.get_oval_width())

    def __instantiate_lines(self, shared, value, timing):
        x = shared.x_staff_end
        stem_up = self.__return_true_if_stem_is_up(value,
                                                   shared.stem_up_endpoints)

        # Fill in the horizontal lines and the stem segments for
        # notes that are above and below the staff.
        if value <= shared.key_lower_stem_start + 1:
            for k in range(shared.key_lower_stem_start+1, value-1, -2):
                y_line = shared.y_lowest_note_location - k * shared.y_spacing
                self.lineList.append(line.Line(shared, x, y_line,
                                               timing, stem_up,
                                               self.oval.get_oval_width()))
        elif value >= shared.key_upper_stem_start - 1:
            for k in range(shared.key_upper_stem_start-1, value+1, 2):
                y_line = shared.y_lowest_note_location - k * shared.y_spacing
                self.lineList.append(line.Line(shared, x, y_line,
                                               timing, stem_up,
                                               self.oval.get_oval_width()))
        elif value == shared.key_middle_c:
            y_line = shared.y_lowest_note_location - value * shared.y_spacing
            self.lineList.append(line.Line(shared, x, y_line,
                                           timing, stem_up,
                                           self.oval.get_oval_width()))

    @staticmethod
    def __return_true_if_stem_is_up(value, stem_up_endpoints):
        if (value <= stem_up_endpoints[0] or
           stem_up_endpoints[1] <= value <= stem_up_endpoints[2]):
            stem_up = True
        else:
            stem_up = False
        return stem_up
