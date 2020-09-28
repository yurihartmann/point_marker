import sys
from typing import List

from app.game import Game


class PointTable:

    __games: List[Game] = []

    def get_games(self) -> List[Game]:
        return self.__games

    def add_game(self, score: int) -> None:
        score = int(score) if str(score).isdigit() else None
        if not isinstance(score, int):
            raise ValueError('Score is not a integer!')
        if score < 0:
            raise ValueError('Score should not be a negative value!')
        if score > 1000:
            raise ValueError('Score should not be bigger than 1000!')

        new_game = Game(id=len(self.__games) + 1,
                        score=score,
                        minimum_season_score=self.__discovery_new_minimum_season_score(score),
                        maximum_season_score=self.__discovery_new_maximum_season_score(score),
                        minimum_record_breaking=self.__discovery_if_minimum_record_breaking(score),
                        maximum_record_breaking=self.__discovery_if_maximum_record_breaking(score))

        self.__games.append(new_game)

    def __discovery_new_minimum_season_score(self, score: int) -> int:
        minimum_season_score = self.__get_minimum_season_score()
        return score if score < minimum_season_score else minimum_season_score

    def __get_minimum_season_score(self) -> int:
        minimum_season_score = sys.maxsize
        for game in self.__games:
            if game.score < minimum_season_score:
                minimum_season_score = game.score
        return minimum_season_score

    def __discovery_new_maximum_season_score(self, score: int) -> int:
        maximum_season_score = self.__get_maximum_season_score()
        return score if score > maximum_season_score else maximum_season_score

    def __get_maximum_season_score(self) -> int:
        maximum_season_score = 0
        for game in self.__games:
            if game.score > maximum_season_score:
                maximum_season_score = game.score
        return maximum_season_score

    def __discovery_if_minimum_record_breaking(self, score: int) -> int:
        if self.__games and score < self.__get_minimum_season_score():
            return self.__games[-1].minimum_record_breaking + 1
        return self.__games[-1].minimum_record_breaking if self.__games else 0

    def __discovery_if_maximum_record_breaking(self, score: int) -> int:
        if self.__games and score > self.__get_maximum_season_score():
            return self.__games[-1].maximum_record_breaking + 1
        return self.__games[-1].maximum_record_breaking if self.__games else 0
