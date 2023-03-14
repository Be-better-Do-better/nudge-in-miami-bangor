import os
os.chdir('..')
from LanguageAnalysis.language_analysis import MOST_COMMON_WORDS_IN_ENGLISH_FILE, load_most_common_words_list, find_first_well_defined_label_in, WELL_DEFINED_LANGUAGE_OPTIONS, get_end_indices_of_longest_sequence, apply_well_defined_lang_label_to_all_ambiguous_tokens, calc_cs_level
from Auxiliaries.artificial_generation import generate_utterance


def test_load_most_common_words_list():
	file_of_most_common_words = MOST_COMMON_WORDS_IN_ENGLISH_FILE
	dir_of_most_common_words = os.path.join('../Data', 'common_n_grams')
	list_of_common_words = load_most_common_words_list(file_of_most_common_words, dir_of_most_common_words)
	print(list_of_common_words)
	print(len(list_of_common_words))


def test_find_first_well_defined_label_in():
	label_seq = ['eng&spa', 'eng', 'spa']
	res = find_first_well_defined_label_in(label_seq)
	print(res)

def test_get_end_indices_of_longest_sequence():
	utterance = generate_utterance()
	# major_lang = find_major_language(utterance)
	major_lang = utterance.major_lang
	major_lang_index = WELL_DEFINED_LANGUAGE_OPTIONS.index(major_lang)
	print(major_lang_index)
	minor_lang = WELL_DEFINED_LANGUAGE_OPTIONS[major_lang_index-1] # select other language than major lang
	print("minor_lang")
	print(minor_lang)
	get_end_indices_of_longest_sequence(utterance.tokens, minor_lang)

def are_all_tokens_ambiguous(tokens) -> bool:
	for token in tokens:
		if token.lang in WELL_DEFINED_LANGUAGE_OPTIONS:
					return False
	return True

def test_are_all_tokens_ambiguous():
	utterance = generate_utterance()
	res = are_all_tokens_ambiguous(utterance.tokens)
	print(res)


def test_apply_well_defined_lang_label_to_all_ambiguous_tokens():
	utterance = generate_utterance()
	apply_well_defined_lang_label_to_all_ambiguous_tokens(utterance.tokens)
	for token in utterance.tokens:
		print(token.surface)
		print(token.well_defined_lang)


def test_calc_cs_level():
	utterance = generate_utterance()
	apply_well_defined_lang_label_to_all_ambiguous_tokens(utterance.tokens)
	cs_level = calc_cs_level(utterance.tokens, utterance.minor_lang, utterance.major_lang)
	print(utterance)
	print('cs_level = ' + cs_level)


def run_tests():
	test_get_end_indices_of_longest_sequence()
	test_load_most_common_words_list()
	test_are_all_tokens_ambiguous()
	test_apply_well_defined_lang_label_to_all_ambiguous_tokens()
	test_calc_cs_level()

if __name__ == '__main__':
	run_tests()
	print("Finished!")