from Auxiliaries.utils import WELL_DEFINED_LANGUAGE_OPTIONS
from LanguageAnalysis.language_analysis import get_end_indices_of_longest_sequence

class LanguageUsageData(object):
	def __init__(self, tokens):
		self.tokens = tokens
		self.language_usage_data = []

		self.__collect_language_usage_data()
		self.__sort_language_usage_data()

	def __str__(self):
		s = ''
		for datum in self.language_usage_data:
			lang, num_of_tokens, index_diff, position_of_last_token = datum
			s += "lang: " + lang
			s += ", # of tokens: " + str(num_of_tokens)
			s += ", index diff: " + str(index_diff)
			s += ", pos of last token:" + str(position_of_last_token)
			s += '\n'
		return s

	def __get_position_of_last_token(self, lang):
		if lang in [token.well_defined_lang for token in self.tokens]:  # at least 1 token is from that language
			return max([i for i in range(len(self.tokens)) if (self.tokens[i].well_defined_lang == lang)])
		else:  # a token with this language was not found in the utterance
			return -1

	def __get_num_of_tokens(self, lang):
		return sum([1 for token in self.tokens if (token.well_defined_lang == lang)])

	def __sort_language_usage_data(self):
		self.language_usage_data.sort(key=lambda row: row[3], reverse=True)  # sort by position of last token
		self.language_usage_data.sort(key=lambda row: row[2], reverse=True)  # sort by longest sequence of language
		self.language_usage_data.sort(key=lambda row: row[1], reverse=True)  # sort by number of tokens

	def __collect_language_usage_data(self):
		for lang in WELL_DEFINED_LANGUAGE_OPTIONS:
			num_of_tokens = self.__get_num_of_tokens(lang)
			position_of_last_token = self.__get_position_of_last_token(lang)
			start_index, end_index = get_end_indices_of_longest_sequence(self.tokens, lang)
			datum = (lang, num_of_tokens, end_index-start_index, position_of_last_token)
			self.language_usage_data.append(datum)

	def select_major_lang(self):
		return self.language_usage_data[0][0]

	def select_minor_lang(self):
		if self.language_usage_data[1][1] > 0:
			return self.language_usage_data[1][0]
		else:
			return None
