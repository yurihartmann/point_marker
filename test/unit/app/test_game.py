import unittest

from app.game import Game


class TestPointTable(unittest.TestCase):

    def test_game_instance(self):
        game = Game(id=1,
                    score=10,
                    minimum_season_score=5,
                    maximum_season_score=50,
                    minimum_record_breaking=2,
                    maximum_record_breaking=4)

        self.assertEqual(1, game.id)
        self.assertEqual(10, game.score)
        self.assertEqual(5, game.minimum_season_score)
        self.assertEqual(50, game.maximum_season_score)
        self.assertEqual(2, game.minimum_record_breaking)
        self.assertEqual(4, game.maximum_record_breaking)