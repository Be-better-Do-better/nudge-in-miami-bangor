import re
from Auxiliaries.utils import PURE_CS_LEVELS_OPTIONS
from LanguageAnalysis.language_analysis import apply_well_defined_lang_label_to_all_ambiguous_tokens, calc_cs_level
from Classes.language_usage_data import LanguageUsageData


class Utterance(object):
	def __init__(self, tokens, speaker):
		self.tokens = tokens
		self.speaker = speaker

		self.surface = ' '.join([token.surface for token in tokens])

		self.lang = None
		self.contains_intra_sentential_cs = None
		self.language_usage_data = []
		self.major_lang = None
		self.minor_lang = None
		self.cs_level = None

		apply_well_defined_lang_label_to_all_ambiguous_tokens(self.tokens)
		self.language_usage_data = LanguageUsageData(self.tokens)
		self.major_lang = self.language_usage_data.select_major_lang()
		self.minor_lang = self.language_usage_data.select_minor_lang()
		self.cs_level = calc_cs_level(self.tokens, self.minor_lang, self.major_lang)

		self.contains_intra_sentential_cs = (self.cs_level in PURE_CS_LEVELS_OPTIONS)
		self.lang = self.major_lang

		self.__fix_utterance_surface_endings()
		self.__remove_sub_tokens_from_surface()

	def __str__(self):
		s = self.surface
		if self.cs_level is not None:
			s += ' (' + self.cs_level + ')'
		return s.strip()

	def __fix_utterance_surface_endings(self):
		if self.surface.endswith(' .'):
			self.surface = re.sub(' .$', '.', self.surface)
		elif self.surface.endswith(' ?'):
			self.surface = self.surface[0:-2]+'?'
		elif self.surface.endswith(' !'):
			self.surface = re.sub(' !$', '!', self.surface)

	def __remove_sub_tokens_from_surface(self):
		self.surface = self.surface.replace(" 's", "'s")
		self.surface = self.surface.replace(" n't", "n't")
		self.surface = self.surface.replace(" 'll", "'ll'")
		self.surface = self.surface.replace(" 'm", "'m'")
