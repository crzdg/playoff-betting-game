from constants import AFCn, NFCn
from models.matchup import Matchup
from models.schedule import Schedule
from models.team import Team


def get_schedule() -> Schedule:
    # pylint: disable=invalid-name, too-many-locals
    KC = Team("KC", 0.1936, 1, AFCn)
    BUF = Team("BUF", 0.1233, 2, AFCn)
    BAL = Team("BAL", 0.1258, 3, AFCn)
    HOU = Team("HOU", 0.0103, 4, AFCn)
    LAC = Team("LAC", 0.0293, 5, AFCn)
    PIT = Team("PIT", 0.0098, 6, AFCn)
    DEN = Team("DEN", 0.0118, 7, AFCn)

    DET = Team("DET", 0.2185, 1, NFCn)
    PHI = Team("PHI", 0.1108, 2, NFCn)
    TB = Team("TB", 0.0304, 3, NFCn)
    LA = Team("LA", 0.0234, 4, NFCn)
    MIN = Team("MIN", 0.0525, 5, NFCn)
    WAS = Team("WAS", 0.0194, 6, NFCn)
    GB = Team("GB", 0.0411, 7, NFCn)

    AFC = [KC, BUF, BAL, HOU, LAC, PIT, DEN]
    NFC = [DET, PHI, TB, LA, MIN, WAS, GB]

    HOU_LAC = Matchup(1, HOU, LAC, AFCn, 0.0, 0.0)
    BAL_PIT = Matchup(1, BAL, PIT, AFCn, 0.0, 0.0)
    BUF_DEN = Matchup(1, BUF, DEN, AFCn, 0.0, 0.0)

    LA_MIN = Matchup(1, LA, MIN, NFCn, 0.0, 0.0)
    TB_WAS = Matchup(1, TB, WAS, NFCn, 0.0, 0.0)
    PHI_GB = Matchup(1, PHI, GB, NFCn, 0.0, 0.0)

    AFC_R1 = [HOU_LAC, BAL_PIT, BUF_DEN]
    NFC_R1 = [LA_MIN, TB_WAS, PHI_GB]

    AFC_R2_TEAMS = [KC]
    NFC_R2_TEAMS = [DET]

    return Schedule(AFC_R1, AFC_R2_TEAMS, NFC_R1, NFC_R2_TEAMS, AFC, NFC)
