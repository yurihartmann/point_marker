

class Game:

    id: int
    score: int
    minimum_season_score = int
    maximum_season_score = int
    minimum_record_breaking = int
    maximum_record_breaking = int

    def __init__(self, id: int,
                 score: int,
                 minimum_season_score: int,
                 maximum_season_score: int,
                 minimum_record_breaking: int,
                 maximum_record_breaking: int) -> None:
        self.id = id
        self.score = score
        self.minimum_season_score = minimum_season_score
        self.maximum_season_score = maximum_season_score
        self.minimum_record_breaking = minimum_record_breaking
        self.maximum_record_breaking = maximum_record_breaking
