import unittest

import pytest

from app.point_table import PointTable


class TestPointTable(unittest.TestCase):

    def setUp(self) -> None:
        self.point_table = PointTable()
        self.point_table.add_game(10)
        self.point_table.add_game(100)
        self.point_table.add_game(5)
        self.point_table.add_game(500)

    def test_add_game_stats(self):
        games = self.point_table.get_games()

        self.assertEqual(10, games[0].minimum_season_score)
        self.assertEqual(10, games[0].maximum_season_score)
        self.assertEqual(0, games[0].minimum_record_breaking)
        self.assertEqual(0, games[0].maximum_record_breaking)
        self.assertEqual(10, games[1].minimum_season_score)
        self.assertEqual(100, games[1].maximum_season_score)
        self.assertEqual(0, games[1].minimum_record_breaking)
        self.assertEqual(1, games[1].maximum_record_breaking)

    def test_add_game_score(self):
        games = self.point_table.get_games()

        self.assertEqual(10, games[0].score)
        self.assertEqual(100, games[1].score)

    def test_add_game_id(self):
        games = self.point_table.get_games()

        self.assertEqual(1, games[0].id)
        self.assertEqual(2, games[1].id)

    def test_add_game_with_score_none(self):
        point_table = PointTable()

        with pytest.raises(ValueError) as err:
            point_table.add_game(score=None)

        self.assertEqual("Score is not a integer!", str(err.value))

    def test_add_game_with_score_less_than_0(self):
        point_table = PointTable()

        with pytest.raises(ValueError) as err:
            point_table.add_game(score=-1)

        self.assertEqual("Score should not be a negative value!", str(err.value))

    def test_add_game_with_score_more_than_1000(self):
        point_table = PointTable()

        with pytest.raises(ValueError) as err:
            point_table.add_game(score=1001)

        self.assertEqual("Score should not be bigger than 1000!", str(err.value))

    def test_discovery_new_minimum_season_score(self):
        point_table = PointTable()
        point_table.add_game(100)
        point_table.add_game(10)

        self.assertEqual(5, point_table.discovery_new_minimum_season_score(5))

    def test_discovery_new_maximum_season_score(self):
        point_table = PointTable()
        point_table.add_game(100)
        point_table.add_game(10)

        self.assertEqual(500, point_table.discovery_new_maximum_season_score(500))

    def test_get_minimum_season_score(self):
        self.assertEqual(5, self.point_table.get_minimum_season_score())

    def test_get_maximum_season_score(self):
        self.assertEqual(500, self.point_table.get_maximum_season_score())
