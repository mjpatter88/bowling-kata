import unittest
import bowling

class BowlingTest(unittest.TestCase):
    def setUp(self):
        self.balls = [(0,0)] * 10

    def test_score__returns_zero_for_all_gutter_balls(self):
        score = bowling.score(self.balls)
        self.assertEquals(score, 0, "All gutter balls should result in a score of 0.")

    def test_score__each_no_spare_or_strike_frame_adds_pin_total_to_score(self):
        self.balls[0] = (5, 3)
        score = bowling.score(self.balls)
        self.assertEquals(score, 8, "Five and three should result in a score of 8.")
