import operator
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

from constants import SUB_PLOTS
from lvii.preparation import MY, MY_2, SB_WINS, WINS
from lvii.schedule import get_schedule
from models.bet import Bet
from models.matchup import Matchup
from models.schedule import Schedule
from models.team import Team
from simulation import Simulation
from utils import print_header, print_row, print_table


def _simulate_bet(
    bet: Bet, sims: int, schedule: Callable[[], Schedule], **simulation_kwargs
) -> list[int]:
    sums = []
    simulation = Simulation(schedule, bet=bet, **simulation_kwargs)
    for _ in range(sims):
        simulation.simulate()
        sum = 0
        for team in simulation.teams:
            sum += team.points * team.current_wins
        sums.append(sum)
    return sums


def simulate_bets(
    bets: list[Bet],
    schedule: Callable[[], Schedule],
    sims: int,
    plot: bool = True,
    log: bool = True,
    **simulation_kwargs
) -> None:
    if log:
        header = ["Team", "Mean", "Median", "std", "max", "min", "q60", "q80"]
        print_header(header)

    for i, bet in enumerate(bets):
        if plot:
            plt.subplot(*SUB_PLOTS[len(bets)], i + 1)

        sums = _simulate_bet(bet, sims, schedule, **simulation_kwargs)

        if log:
            bet_stats = [
                bet.name,
                round(np.mean(sums), 2),
                round(np.median(sums), 2),
                round(np.std(sums), 2),
                np.max(sums),
                np.min(sums),
                round(np.percentile(sums, 60), 2),
                round(np.percentile(sums, 80), 2),
            ]
            bet_stats = [str(stat) for stat in bet_stats]
            print_row(bet_stats)

        if plot:
            plt.hist(sums, bins=152)
            plt.title(bet.name)
            plt.xlim(40, 152)


def simulate_sbs(
    schedule: Callable[[], Schedule],
    sims: int,
    log: bool = True,
    sort_by_wins: bool = False,
    **simulation_kwargs
) -> None:
    simulation = Simulation(schedule, **simulation_kwargs)
    for _ in range(sims):
        simulation.simulate()

    if log:

        header = ["Team", "SBs", "Ws", "pSB%", "aSB%"]

        def get_team_simulation_stats(team: Team) -> list[str]:
            team_stats = [
                team.name,
                team.sb_wins,
                team.wins,
                round(team.odds_sb * 100, 2),
                round(team.sb_wins / sims * 100, 2),
            ]
            team_stats_str = [str(stat) for stat in team_stats]
            return team_stats_str

        if sort_by_wins:
            print_table(
                simulation.teams,
                get_team_simulation_stats,
                header,
                sort=True,
                sort_key="wins",
            )
        else:
            print_table(
                simulation.teams,
                get_team_simulation_stats,
                header,
                sort=True,
                sort_key="sb_wins",
            )
