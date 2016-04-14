import unittest
import bowling

class BowlingTest(unittest.TestCase):
    def setUp(self):
        self.frames = [(0,0)] * 10

    def test_score__returns_zero_for_all_gutter_balls(self):
        score = bowling.score(self.frames)
        self.assertEquals(score, 0, "All gutter balls should result in a score of 0.")

    def test_score__each_no_spare_or_strike_frame_adds_pin_total_to_score(self):
        self.frames[0] = (5, 3)
        score = bowling.score(self.frames)
        self.assertEquals(score, 8, "Five and three should result in a score of 8.")

    def test_score__adds_two_frames_together(self):
        self.frames[0] = (5, 3)
        self.frames[1] = (8, 1)
        score = bowling.score(self.frames)
        self.assertEquals(score, 17, "Two frames should be added together.")

    def test_score__adds_the_first_throw_from_the_next_frame_to_the_current_frame_total_if_spare(self):
        self.frames[0] = (9, 1)
        self.frames[1] = (5, 3)
        score = bowling.score(self.frames)
        self.assertEquals(score, 23, "Spare frame should add next throw to total.")
