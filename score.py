"""
Draw the score lines.

Gregary C. Zweigle

2019

"""

import accidental


class Score:

    def __init__(self, shared):
        self.x_staff_start = shared.x_staff_start
        self.x_staff_sig_end = shared.x_staff_sig_end
        self.y_lower_staff_start = shared.y_lower_staff_start
        self.y_spacing = shared.y_spacing
        self.color = shared.color

        # The music has key-signature b-flat. Place these flat symbols
        # at the appropriate place along the musical score.
        self.sig0 = accidental.Accidental(shared, self.x_staff_sig_end - 20,
                                          shared.y_lower_staff_start -
                                          2*self.y_spacing, "flat", 0)
        self.sig1 = accidental.Accidental(shared, self.x_staff_sig_end - 10,
                                          shared.y_lower_staff_start -
                                          5*self.y_spacing, "flat", 0)
        self.sig2 = accidental.Accidental(shared, self.x_staff_sig_end - 20,
                                          shared.y_lower_staff_start -
                                          16*self.y_spacing, "flat", 0)
        self.sig3 = accidental.Accidental(shared, self.x_staff_sig_end - 10,
                                          shared.y_lower_staff_start -
                                          19*self.y_spacing, "flat", 0)

    def draw(self, frame):
        for x in range(self.x_staff_start, self.x_staff_sig_end):
            for y_ind in range(0, 11):  # 11 lines in a grand staff.
                if y_ind != 5:  # No line in between upper and lower staff.
                    y_offset = y_ind * (2*self.y_spacing)  # 2 notes / staff.
                    for color in range(3):
                        frame[self.y_lower_staff_start-y_offset, x, color] = \
                            self.color[color]
                        frame[self.y_lower_staff_start-y_offset-1, x, color] = \
                            self.color[color]

        # Draw the key signature.
        self.sig0.draw(frame)
        self.sig1.draw(frame)
        self.sig2.draw(frame)
        self.sig3.draw(frame)
