from Classes.hypothesis import Hypothesis
from Hypotheses.nudge import Nudge
from Hypotheses.tit_for_tat import TitForTat
from Hypotheses.major_language_tit_for_tat import MajorLanguageTitForTat
from Hypotheses.close_to_previous import CloseToPrevious
from Hypotheses.always_0_or_7 import Always_0_or_7
from Hypotheses.always_decreases import AlwaysDecrease

from Hypotheses.boolean_conditions import backoff_condition, retreat, non_backoff_condition, nudge, cs_level_changed_c1_to_c0, cs_level_changed_c2_to_c1, cs_level_changed_c3_to_c2, cs_level_changed_c4_to_c3, cs_level_changed_c21_to_c20, cs_level_changed_c51_to_c50, cs_level_changed_c101_to_c100, last_is_zero, last_belongs_to, previous_belongs_to


def generate_hypotheses():
	hypotheses = [Nudge(), TitForTat(), MajorLanguageTitForTat(), CloseToPrevious(), Always_0_or_7(), AlwaysDecrease()]
	return hypotheses
