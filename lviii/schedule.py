from constants import AFCn, NFCn
from models.matchup import Matchup
from models.schedule import Schedule
from models.team import Team


def get_schedule() -> Schedule:
    # pylint: disable=invalid-name, too-many-locals
    BAL = Team("BAL", 0.2401, 1, AFCn)
    BUF = Team("BUF", 0.1359, 2, AFCn)
    KC = Team("KC", 0.0946, 3, AFCn)
    HOU = Team("HOU", 0.0185, 4, AFCn)
    CLE = Team("CLE", 0.0272, 5, AFCn)
    MIA = Team("MIA", 0.0469, 6, AFCn)
    PIT = Team("PIT", 0.007, 7, AFCn)

    SF = Team("SF", 0.3167, 1, NFCn)
    DAL = Team("DAL", 0.1157, 2, NFCn)
    DET = Team("DET", 0.0483, 3, NFCn)
    TB = Team("TB", 0.0140, 4, NFCn)
    PHI = Team("PHI", 0.0593, 5, NFCn)
    LA = Team("LA", 0.0214, 6, NFCn)
    GB = Team("GB", 0.0115, 7, NFCn)

    AFC = [BAL, BUF, KC, HOU, CLE, MIA, PIT]
    NFC = [SF, DAL, DET, TB, PHI, LA, GB]

    TB_PHI = Matchup(1, TB, PHI, NFCn, 0.0, 0.0)
    DET_LA = Matchup(1, DET, LA, NFCn, 0.0, 0.0)
    DAL_GB = Matchup(1, DAL, GB, NFCn, 0.0, 0.0)

    HOU_CLE = Matchup(1, HOU, CLE, AFCn, 0.0, 0.0)
    KC_MIA = Matchup(1, KC, MIA, AFCn, 0.0, 0.0)
    BUF_PIT = Matchup(1, BUF, PIT, AFCn, 0.0, 0.0)

    AFC_R1 = [HOU_CLE, KC_MIA, BUF_PIT]
    NFC_R1 = [TB_PHI, DET_LA, DAL_GB]

    AFC_R2_TEAMS = [BAL]
    NFC_R2_TEAMS = [SF]

    return Schedule(AFC_R1, AFC_R2_TEAMS, NFC_R1, NFC_R2_TEAMS, AFC, NFC)
