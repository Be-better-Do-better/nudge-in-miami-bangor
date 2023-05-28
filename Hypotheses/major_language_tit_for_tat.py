from Classes.hypothesis import Hypothesis
from Auxiliaries.utils import CS_LEVELS_OPTIONS

class MajorLanguageTitForTat(Hypothesis):
	"""This function returns True if the major language of c0 is the same as the major language of c1 and False otherwise"""
	def __init__(self):
		super().__init__(name='Major Language Tit-for-Tat', n=1, relevant_indexes=[0, 1])

	def check_condition(self, c: list[int]) -> bool:
		major_lang_of_c0 = CS_LEVELS_OPTIONS[c[0]][0]  # first letter of CS_LEVELS_OPTIONS is either 'E' or 'S'
		major_lang_of_c1 = CS_LEVELS_OPTIONS[c[1]][0]  # second letter of CS_LEVELS_OPTIONS is either 'E' or 'S'
		return major_lang_of_c0 == major_lang_of_c1
