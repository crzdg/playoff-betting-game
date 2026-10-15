import operator
import random
from copy import copy
from typing import Callable, Optional

import numpy as np

from constants import MATCH, AFCn, NFCn
from models.bet import Bet
from models.matchup import Matchup
from models.schedule import Schedule
from models.team import Team


def simulate_matchup(matchup: Matchup) -> Team:
    draw = random.uniform(0, 1)
    if draw > matchup.odds_home:
        winner = matchup.away
    else:
        winner = matchup.home
    winner.wins += 1
    winner.current_wins += 1
    return winner


def simulate_round(matchups: list[Matchup]) -> list[Team]:
    teams = []
    for matchup in matchups:
        teams.append(simulate_matchup(matchup))
    return teams


def create_matchup(
    home: Team, away: Team, conference: str, round_nr: int, use_sb_odds
) -> Matchup:
    matchup = Matchup(round_nr, home, away, conference)
    matchup.calculate_matchup_odds()
    return matchup


def create_round_matchups(
    round: list[Team],
    round_nr: int,
    conference: str,
    use_sb_odds: bool,
) -> list[Matchup]:
    seed_sorted: list[Team] = sorted(round, key=operator.attrgetter("seed"))
    len_ = len(seed_sorted) - 1
    matchups = []
    for i, _ in enumerate(range(MATCH[round_nr] // 2)):
        home = seed_sorted[i]
        away = seed_sorted[len_ - i]
        matchups.append(create_matchup(home, away, conference, round_nr, use_sb_odds))
    return matchups


class Simulation:
    def __init__(
        self,
        schedule: Callable[[], Schedule],
        normalize_sb=True,
        use_sb_odds=True,
        bet: Optional[Bet] = None,
        odds: Optional[dict] = None,
        schedule_adjuster: Optional[Callable[[Schedule], None]] = None,
    ) -> None:
        self._schedule = schedule()
        self._use_sb_odds = use_sb_odds

        if isinstance(odds, dict):
            self._schedule.apply_sb_odds(odds)
        if normalize_sb:
            self._schedule.normalize_sb_odds()

        self._schedule.calculate_r1_odds()

        if isinstance(bet, Bet):
            self._schedule.assign_bet(bet)
        if callable(schedule_adjuster):
            schedule_adjuster(self._schedule)

    @property
    def teams(self) -> list[Team]:
        return self._schedule.teams

    def simulate(self) -> None:
        for team in self.teams:
            team.reset_current_wins()

        # Copy R2 as we manipulate it and may simulate another time
        afc_r2_teams = copy(self._schedule.afc_r2_teams)
        nfc_r2_teams = copy(self._schedule.nfc_r2_teams)

        # Append the winners of R1 to the set Teams in R2
        for team in simulate_round(self._schedule.afc_r1):
            afc_r2_teams.append(team)
        for team in simulate_round(self._schedule.nfc_r1):
            nfc_r2_teams.append(team)

        # Create R2
        afc_r2 = create_round_matchups(afc_r2_teams, 2, AFCn, self._use_sb_odds)
        nfc_r2 = create_round_matchups(nfc_r2_teams, 2, NFCn, self._use_sb_odds)

        # Run R2
        afc_r3_teams = simulate_round(afc_r2)
        nfc_r3_teams = simulate_round(nfc_r2)

        # Create R3
        afc_r3 = create_round_matchups(afc_r3_teams, 3, AFCn, self._use_sb_odds)
        nfc_r3 = create_round_matchups(nfc_r3_teams, 3, NFCn, self._use_sb_odds)

        # Run R3
        afc_champ = simulate_round(afc_r3)[0]
        nfc_champ = simulate_round(nfc_r3)[0]

        # Create SB
        odds_sum = nfc_champ.odds_sb + afc_champ.odds_sb
        nfc_odds = nfc_champ.odds_sb / odds_sum
        afc_odds = afc_champ.odds_sb / odds_sum
        sb = Matchup(4, nfc_champ, afc_champ, "SB", nfc_odds, afc_odds)

        # Run SB
        sb_champ = simulate_round([sb])[0]
        sb_champ.sb_wins += 1
