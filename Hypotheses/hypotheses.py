from Hypotheses.nudge import Nudge
from Hypotheses.tit_for_tat import TitForTat
from Hypotheses.major_language_tit_for_tat import MajorLanguageTitForTat
from Hypotheses.close_to_previous import CloseToPrevious
from Hypotheses.always_EN_or_SN import Always_EN_or_SN
from Hypotheses.always_decreases import AlwaysDecrease


def generate_hypotheses():
	hypotheses = [TitForTat(), MajorLanguageTitForTat(), CloseToPrevious(), Always_EN_or_SN(), AlwaysDecrease(), Nudge()]
	return hypotheses
