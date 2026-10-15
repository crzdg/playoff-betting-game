import pandas as pd

from models.bet import Bet

data = pd.read_csv("/home/rb/git/playoff-betting-game/lvix/game.csv")

BETS = []

for index, row in data.iterrows():
    BETS.append(
        Bet(
            name=row["Name"],
            points={
                "KC": row["Chiefs"],
                "BUF": row["Bills"],
                "BAL": row["Ravens"],
                "HOU": row["Texans"],
                "LAC": row["Chargers"],
                "PIT": row["Steelers"],
                "DEN": row["Broncos"],
                "DET": row["Lions"],
                "PHI": row["Eagles"],
                "TB": row["Bucs"],
                "LA": row["Rams"],
                "MIN": row["Vikings"],
                "WAS": row["WAS"],
                "GB": row["Packers"],
            },
        )
    )


def get_sb_odds() -> dict:
    from collections import defaultdict

    sums = defaultdict(lambda: 0)
    sum_points = 0
    for bet in BETS:
        sum_bet = 0
        for team, points in bet.points.items():
            sums[team] += points
            sum_bet += points
        assert sum_bet == 105
        sum_points += sum_bet
    odds = {}
    for team, points in sums.items():
        odds[team] = points / sum_points
    return odds
