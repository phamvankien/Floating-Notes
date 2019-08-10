"""
This program adds notes to a video according to a song I wrote and performed.
Intentionally, no pre-built drawings.

Gregary C. Zweigle

2019

"""


import data
import imageio
import note
import numpy as np
import score
import shared

test_mode = True  # Test with all notes, accents, timings.

if test_mode:
    reader = imageio.get_reader('data/test_video.mp4')
else:
    reader = imageio.get_reader('data/video.mp4')
meta = reader.get_meta_data()

if test_mode:
    writer = imageio.get_writer('data/test_video_edited.mp4', fps=meta['fps'])
    filename = 'data/test_notes.xlsx'
else:
    writer = imageio.get_writer('data/video_edited.mp4', fps=meta['fps'])
    filename = 'data/notes.xlsx'

y_max = meta['size'][1]
shared = shared.Shared(y_max, test_mode)

data = data.Data(filename)
score = score.Score(shared)

noteList = list([])
for video_index, image in enumerate(reader):

    video_frame = image.astype(np.float)

    data.get_music_data(video_index)

    # Notes are added but never removed when no longer displayed.
    # Technically.... this could be considered a memory leak.
    # But the file is finite length and there are only a few hundred notes.
    if data.left_hand_has_data:
        noteList.append(note.Note(shared, data.left_hand_value,
                                  data.left_hand_timing,
                                  data.left_hand_accidental))

    if data.right_hand_has_data:
        noteList.append(note.Note(shared, data.right_hand_value,
                                  data.right_hand_timing,
                                  data.right_hand_accidental))

    score.draw(video_frame)
    for note_values in noteList:
        note_values.draw(video_frame)
        note_values.move()

    writer.append_data(video_frame.astype(np.uint8))
