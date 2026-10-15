import pandas as pd

from models.bet import Bet

data = pd.read_csv("/home/rb/git/playoff-betting-game/lviii/game.csv")

BETS = []

for index, row in data.iterrows():
    BETS.append(
        Bet(
            name=row["Name"],
            points={
                "BAL": row["Ravens"],
                "BUF": row["Bills"],
                "KC": row["Chiefs"],
                "HOU": row["Texans"],
                "CLE": row["Browns"],
                "MIA": row["Dolphins"],
                "PIT": row["Steelers"],
                "SF": row["49ers"],
                "DAL": row["Cowboys"],
                "DET": row["Lions"],
                "TB": row["Bucs"],
                "PHI": row["Eagles"],
                "LA": row["Rams"],
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
