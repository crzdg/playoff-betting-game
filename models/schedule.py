from dataclasses import dataclass

import numpy as np

from models.bet import Bet
from models.matchup import Matchup
from models.team import Team
from utils import normalize_odds, print_table


@dataclass
class Schedule:
    afc_r1: list[Matchup]
    afc_r2_teams: list[Team]
    nfc_r1: list[Matchup]
    nfc_r2_teams: list[Team]
    afc_teams: list[Team]
    nfc_teams: list[Team]

    @property
    def teams(self) -> list[Team]:
        return [*self.afc_teams, *self.nfc_teams]

    @property
    def r1(self) -> list[Matchup]:
        return [*self.afc_r1, *self.nfc_r1]

    def normalize_sb_odds(self) -> None:
        sum_ = np.sum([team.odds_sb for team in self.teams])
        for team in self.teams:
            team.odds_sb = team.odds_sb / sum_

    def calculate_r1_odds(self) -> None:
        for matchup in self.r1:
            matchup.calculate_matchup_odds()

    def assign_bet(self, bet: Bet) -> None:
        for team in self.teams:
            team.points = bet.points[team.name]

    def apply_sb_odds(self, odds: dict) -> None:
        for team in self.teams:
            team.odds_sb = odds[team.name]

    def print_sb_odds(self) -> None:
        print_table(
            self.teams,
            lambda team: [team.name, str(round(team.odds_sb, 2))],
            ["Team", "%SB"],
            sort=True,
            sort_key="odds_sb",
        )

    def print_cf_odds(self) -> None:
        print("***** AFC ******")
        self.print_afc_odds()
        print("***** NFC ******")
        self.print_nfc_odds()

    def print_afc_odds(self) -> None:
        print_table(
            self.afc_teams,
            lambda team: [team.name, str(team.odds_cf)],
            ["Team", "%CF"],
            sort=True,
            sort_key="odds_sb",
        )

    def print_nfc_odds(self) -> None:
        print_table(
            self.nfc_teams,
            lambda team: [team.name, str(team.odds_cf)],
            ["Team", "%CF"],
            sort=True,
            sort_key="odds_sb",
        )
