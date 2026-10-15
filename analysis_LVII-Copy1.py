# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:hydrogen,ipynb
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from calculate import simulate_bets, simulate_sbs
from lviii.preparation import BETS
from lviii.schedule import get_schedule
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (40,20)
plt.rcParams['figure.constrained_layout.use'] = True

# %%
sims = 10000

# %%
# Chances to win the Super Bowl for each Team by Vegas Odds
schedule = get_schedule()
schedule.normalize_sb_odds()
schedule.print_sb_odds()

# %%
# Prepare ourselvs by simulating path to Super Bowl
simulate_sbs(get_schedule, sims)

# %%
# Compare our prepeared bets against some baseline
from lviii.preparation import BETS
simulate_bets(BETS, get_schedule, sims)

# %%
from lviii.game import BETS, get_sb_odds
simulate_bets(BETS, get_schedule, sims)

# %%
simulate_sbs(get_schedule, sims, odds=get_sb_odds())

# %%
simulate_bets(BETS, get_schedule, sims, odds=get_sb_odds())


# %%
# First game is played SEA@SF : SEA 25 : 41 SF
def schedule(schedule_):
    #for matchup in schedule_.nfc_r1:
        #if matchup.home.name == "SF":
        #    matchup.odds_away = 0
        #    matchup.odds_home = 1
        #if matchup.away.name == "NJG" or matchup.away.name == "DAL":
        #    matchup.odds_away = 1
        #    matchup.odds_home = 0
    for matchup in schedule_.afc_r1:
        if matchup.home.name == "HOU":
            matchup.odds_away = 0
            matchup.odds_home = 1
    return schedule_


# %%
sims = 10000

# %%
simulate_bets(BETS, get_schedule, sims, schedule_adjuster=schedule)

# %%
simulate_bets(BETS, get_schedule, sims, odds=get_sb_odds(), schedule_adjuster=schedule)


# %%
# First game is played SEA@SF : SEA 25 : 41 SF
def schedule(schedule_):
    #for matchup in schedule_.nfc_r1:
        #if matchup.home.name == "SF":
        #    matchup.odds_away = 0
        #    matchup.odds_home = 1
        #if matchup.away.name == "NJG" or matchup.away.name == "DAL":
        #    matchup.odds_away = 1
        #    matchup.odds_home = 0
    for matchup in schedule_.afc_r1:
        if matchup.home.name == "HOU" or matchup.home.name == "KC":
            matchup.odds_away = 0
            matchup.odds_home = 1
    return schedule_
