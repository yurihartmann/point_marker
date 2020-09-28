import sys
from typing import List

from app.game import Game


class PointTable:

    __games: List[Game] = []

    def get_games(self) -> List[Game]:
        return self.__games

    def add_game(self, score: int) -> None:
        if not isinstance(score, int):
            raise ValueError('Score is not a integer!')
        if score < 0:
            raise ValueError('Score should not be a negative value!')
        if score > 1000:
            raise ValueError('Score should not be bigger than 1000!')

        minimum_record_breaking = self.get_minimum_record_breaking() + 1 if self.is_minimum_record_breaking(score) else self.get_minimum_record_breaking()
        maximum_record_breaking = self.get_maximum_record_breaking() + 1 if self.is_maximum_record_breaking(score) else self.get_maximum_record_breaking()

        new_game = Game(id=len(self.__games) + 1,
                        score=score,
                        minimum_season_score=self.discovery_new_minimum_season_score(score),
                        maximum_season_score=self.discovery_new_maximum_season_score(score),
                        minimum_record_breaking=minimum_record_breaking,
                        maximum_record_breaking=maximum_record_breaking)

        self.__games.append(new_game)

    def discovery_new_minimum_season_score(self, score: int) -> int:
        minimum_season_score = self.get_minimum_season_score()
        return score if score < minimum_season_score else minimum_season_score

    def get_minimum_season_score(self) -> int:
        minimum_season_score = sys.maxsize
        for game in self.__games:
            if game.score < minimum_season_score:
                minimum_season_score = game.score
        return minimum_season_score

    def discovery_new_maximum_season_score(self, score: int) -> int:
        maximum_season_score = self.get_maximum_season_score()
        return score if score > maximum_season_score else maximum_season_score

    def get_maximum_season_score(self) -> int:
        maximum_season_score = 0
        for game in self.__games:
            if game.score > maximum_season_score:
                maximum_season_score = game.score
        return maximum_season_score

    def is_minimum_record_breaking(self, score: int) -> bool:
        if self.__games and score < self.get_minimum_season_score():
            return True
        return False

    def is_maximum_record_breaking(self, score: int) -> bool:
        if self.__games and score > self.get_maximum_season_score():
            return True
        return False

    def get_minimum_record_breaking(self) -> int:
        if self.__games:
            return self.__games[-1].minimum_record_breaking
        return 0

    def get_maximum_record_breaking(self) -> int:
        if self.__games:
            return self.__games[-1].maximum_record_breaking
        return 0
