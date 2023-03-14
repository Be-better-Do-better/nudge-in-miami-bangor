from LanguageAnalysis.language_analysis import apply_well_defined_lang_label_to_all_ambiguous_tokens, calc_cs_level
from Classes.language_usage_data import LanguageUsageData

class Turn(object):
	def __init__(self, utterances, speaker):
		self.utterances = utterances
		self.speaker = speaker
		self.tokens = [token for utterance in self.utterances for token in utterance.tokens]

		self.surface = ' '.join([utterance.surface for utterance in self.utterances])
		self.lang = None
		self.contains_intra_sentential_cs = None
		self.major_lang = None
		self.minor_lang = None
		self.cs_level = None

		apply_well_defined_lang_label_to_all_ambiguous_tokens(self.tokens)
		self.language_usage_data = LanguageUsageData(self.tokens)
		self.major_lang = self.language_usage_data.select_major_lang()
		self.minor_lang = self.language_usage_data.select_minor_lang()
		self.cs_level = calc_cs_level(self.tokens, self.minor_lang, self.major_lang)

		self.lang = self.major_lang

	def __str__(self):
		s = ''
		for utterance in self.utterances:
			s += self.speaker + ': ' + str(utterance) + '\n'

		if self.cs_level is not None:
			s += 'Turn CS level: ' + self.cs_level + '\n'
		return s