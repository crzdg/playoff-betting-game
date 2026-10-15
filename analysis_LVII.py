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
from lvii.preparation import BETS
from lvii.schedule import get_schedule
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (20,10)

# %%
sims = 10000

# %%
# Chances to win the Super Bowl for each Team by Vegas Odds
schedule = get_schedule()
schedule.normalize_sb_odds()
schedule.print_sb_odds()

# %%
# Chances to win the their Conference for each Team by Vegas Odds
schedule.print_cf_odds()

# %%
# Prepare ourselvs by simulating path to Super Bowl
simulate_sbs(get_schedule, sims)

# %%
# Compare our prepeared bets against some baseline
from lvii.preparation import BETS
simulate_bets(BETS, get_schedule, sims, adjust_r1_odds=False)

# %%
# Compare our prepeared bets against some baseline
from lvii.game import BETS, get_sb_odds
simulate_bets(BETS, get_schedule, sims, adjust_r1_odds=False)

# %%
simulate_sbs(get_schedule, sims, odds=get_sb_odds(), use_cf_odds=False)

# %%
simulate_bets(BETS, get_schedule, sims, odds=get_sb_odds(), use_cf_odds=False)


# %%
# First game is played SEA@SF : SEA 25 : 41 SF
def schedule(schedule_):
    for matchup in schedule_.nfc_r1:
        if matchup.home.name == "SF":
            matchup.odds_away = 0
            matchup.odds_home = 1
        if matchup.away.name == "NJG" or matchup.away.name == "DAL":
            matchup.odds_away = 1
            matchup.odds_home = 0
    for matchup in schedule_.afc_r1:
        if matchup.home.name == "JAX" or matchup.home.name == "BUF" or matchup.home.name == "CIN":
            matchup.odds_away = 0
            matchup.odds_home = 1
    return schedule_


# %%
sims = 10000

# %%
simulate_bets(BETS, get_schedule, sims, schedule_adjuster=schedule, adjust_r1_odds=False, plot=False)

# %%
simulate_bets(BETS, get_schedule, sims, odds=get_sb_odds(), use_cf_odds=False, schedule_adjuster=schedule, plot=False)

# %%
