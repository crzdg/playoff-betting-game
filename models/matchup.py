from dataclasses import dataclass

import numpy as np

from models.team import Team
from utils import normalize_odds


@dataclass
class Matchup:
    round: int
    home: Team
    away: Team
    conference: str
    odds_home: float = 0.0
    odds_away: float = 0.0

    def calculate_matchup_odds(self) -> tuple[float, float]:
        home_odds = []
        away_odds = []

        home_, away_ = normalize_odds(self.home.odds_sb, self.away.odds_sb)
        home_odds.append(home_)
        away_odds.append(away_)

        self.odds_home = float(np.mean(home_odds))
        self.odds_away = float(np.mean(away_odds))
