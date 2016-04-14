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

    def test_score__adds_the_next_throw_twice_if_spare(self):
        self.frames[0] = (9, 1)
        self.frames[1] = (5, 3)
        score = bowling.score(self.frames)
        self.assertEquals(score, 23, "Spare frame should add next throw to total.")

    def test_score__adds_the_next_two_throws_if_strike(self):
        self.frames[0] = (10, 0)
        self.frames[1] = (5, 3)
        score = bowling.score(self.frames)
        self.assertEquals(score, 26, "Strike frame should add next two throws to total.")

    def test_score__correctly_scores_perfect_game_as_300(self):
        frames = [(10,0)] * 13
        score = bowling.score(frames)
        self.assertEquals(score, 300, "Perfect game results in score of 300.")

