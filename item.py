"""
Everything shared by all note items is placed in this class.
All note items (the stem, the oval, the lines, and accidentals)
subclass from the Item class.

Gregary C. Zweigle

2019

"""

import random


class Item:
    def __init__(self, shared, x, y):
        # x-y dynamics are [location, velocity, and acceleration].
        # It is intentional that every item gets a different random value.
        if shared.test_mode:
            self.x = [x, shared.note_speed, -0.02*random.random()]
            self.y = [y, 0, -0.75*random.random()]
        else:
            self.x = [x, shared.note_speed, shared.x_accel*random.random()]
            self.y = [y, 0, shared.y_accel*random.random()]
        self.min_percent = shared.min_percent
        self.color = shared.color
        self.x_staff_start = shared.x_staff_start
        self.note_speed = shared.note_speed
        self.active = True
        self.floating = False

    def move(self):
        if self.active:
            if self.floating:
                # After exiting the score, the notes float away.
                self.x[0] = round(self.x[0] + self.x[1])
                self.y[0] = round(self.y[0] + self.y[1])
                # Update x-velocity by deceleration but never allow
                # slower than a percent of starting speed (this also prevents
                # note items from changing x-velocity direction).
                if self.x[1] < self.min_percent * self.note_speed:
                    self.x[1] += self.x[2]
                self.y[1] += self.y[2]
            else:
                # While in the score, the notes move along the x-axis only.
                self.x[0] += self.note_speed
                if self.x[0] < self.x_staff_start:
                    self.floating = True

    def write_to_array(self, frame, x_start, x_end, y_start, y_end):

        if self.active:

            # Matrix is transposed compared to visual x,y perspective.
            x_max = frame.shape[1]
            y_max = frame.shape[0]

            # When only a single value is written, the calling function sets
            # start and end to the same value. However, writing a single value
            # with a range requires end = start + 1 as the range written is
            # {start, start + 1, ... end - 1}.
            if x_start == x_end:
                x_end = x_start + 1
            if y_start == y_end:
                y_end = y_start + 1

            # If attempt to write out of the video display range,
            # ignore the write and disable the note.
            # This is normal and happens when a note exits the video
            # display range.
            if (0 <= x_start < x_max and 0 < x_end <= x_max and
               0 <= y_start < y_max and 0 < y_end <= y_max):
                frame[y_start:y_end, x_start:x_end, 0] = self.color[0]
                frame[y_start:y_end, x_start:x_end, 1] = self.color[1]
                frame[y_start:y_end, x_start:x_end, 2] = self.color[2]
            else:
                self.active = False
