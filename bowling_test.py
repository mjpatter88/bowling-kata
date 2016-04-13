import unittest
import bowling

class BowlingTest(unittest.TestCase):

    def test_score_returns_zero_for_all_gutter_balls(self):
        balls = [0] * 10
        score = bowling.score(balls)
        self.asserEquals(score, 0, "All gutter balls should result in a score of 0.")
