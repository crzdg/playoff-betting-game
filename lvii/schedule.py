from constants import AFCn, NFCn
from models.matchup import Matchup
from models.schedule import Schedule
from models.team import Team


def get_schedule() -> Schedule:
    # pylint: disable=invalid-name, too-many-locals
    KC = Team("KC", 0.2326, 0.334, 1, AFCn)
    BUF = Team("BUF", 0.2025, 0.31, 2, AFCn)
    CIN = Team("CIN", 0.1127, 0.164, 3, AFCn)
    JAX = Team("JAX", 0.0206, 0.043, 4, AFCn)
    LAC = Team("LAC", 0.0426, 0.082, 5, AFCn)
    BAL = Team("BAL", 0.0426, 0.047, 6, AFCn)
    MIA = Team("MIA", 0.0132, 0.029, 7, AFCn)

    PHI = Team("PHI", 0.1649, 0.323, 1, NFCn)
    SF = Team("SF", 0.1739, 0.317, 2, NFCn)
    MIN = Team("MIN", 0.0323, 0.068, 3, NFCn)
    TB = Team("TB", 0.0354, 0.081, 4, NFCn)
    DAL = Team("DAL", 0.069, 0.148, 5, NFCn)
    NJG = Team("NJG", 0.0178, 0.034, 6, NFCn)
    SEA = Team("SEA", 0.0131, 0.029, 7, NFCn)

    AFC = [KC, BUF, CIN, JAX, LAC, BAL, MIA]
    NFC = [PHI, SF, MIN, TB, DAL, NJG, SEA]

    SEA_SF = Matchup(1, SF, SEA, NFCn, 0.806, 0.194)
    NJG_MIN = Matchup(1, MIN, NJG, NFCn, 0.599, 0.401)
    DAL_TB = Matchup(1, TB, DAL, NFCn, 0.447, 0.553)

    LAC_JAX = Matchup(1, JAX, LAC, AFCn, 0.429, 0.571)
    BAL_CIN = Matchup(1, CIN, BAL, AFCn, 0.77, 0.23)
    MIA_BUF = Matchup(1, BUF, MIA, AFCn, 0.862, 0.132)

    AFC_R1 = [LAC_JAX, BAL_CIN, MIA_BUF]
    NFC_R1 = [SEA_SF, NJG_MIN, DAL_TB]

    AFC_R2_TEAMS = [KC]
    NFC_R2_TEAMS = [PHI]

    return Schedule(AFC_R1, AFC_R2_TEAMS, NFC_R1, NFC_R2_TEAMS, AFC, NFC)
