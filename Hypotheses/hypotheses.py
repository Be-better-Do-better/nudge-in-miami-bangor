from Hypotheses.nudge import Nudge
from Hypotheses.replication import Replication
from Hypotheses.major_language_replication import MajorLanguageReplication
from Hypotheses.close_to_previous import CloseToPrevious
from Hypotheses.always_EN_or_SN import Always_EN_or_SN
from Hypotheses.always_decreases import AlwaysDecrease


def generate_hypotheses():
	hypotheses = [Replication(), MajorLanguageReplication(), CloseToPrevious(), Always_EN_or_SN(), AlwaysDecrease(), Nudge()]
	return hypotheses
