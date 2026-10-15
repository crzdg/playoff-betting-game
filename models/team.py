from dataclasses import dataclass


@dataclass
class Team:
    name: str
    odds_sb: float
    seed: int
    conference: str
    wins: int = 0
    sb_wins: int = 0
    current_wins: int = 0
    points: int = 0

    def reset_current_wins(self) -> None:
        self.current_wins = 0

    def reset(self) -> None:
        self.current_wins = 0
        self.wins = 0
        self.sb_wins = 0
        self.points = 0
