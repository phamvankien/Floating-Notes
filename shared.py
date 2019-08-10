"""
Being art, many items are exactly positioned or with specific dynamics.
Most of constants are in this one location. In a few classes I kept
the constants local because I rarely (never) change them and because
they are so unique it complicates the code to move them into this class.

Gregary C. Zweigle

2019

"""


class Shared:

    def __init__(self, y_max, test_mode):

        self.test_mode = test_mode

        self.color = [48, 48, 48]
        self.y_spacing = 10  # Vertical spacing between notes.
        self.x_staff_start = 1200
        self.x_staff_sig_end = 1750
        self.x_staff_end = 1700
        self.line_thickness = 3

        self.oval_a = 1.5  # Horizontal ratio for the note oval shape.

        if self.test_mode:
            self.note_speed = -10
        else:
            self.note_speed = -5
        self.x_accel = 0.01
        self.y_accel = -0.1
        self.min_percent = 0.02  # x-velocity is never < this % of note_speed.

        # The white keys are ordered from 1 (lowest A) to 52 (highest C).
        # The following define when stem direction changes and when stem
        # stops while above or below the staff lines.
        # Just following the rules of music notation.
        self.key_lower_stem_start = 11
        self.key_upper_stem_start = 37
        self.key_middle_c = 24
        self.stem_up_endpoints = (17, 24, 29)

        # These are derived values from the above constants.
        self.y_lowest_note_location = y_max - 2*self.y_spacing
        self.y_lower_staff_start = self.y_lowest_note_location - 14*self.y_spacing
        self.stem_height = 6*self.y_spacing
        self.note_oval_radius = round(0.8 * self.y_spacing)
