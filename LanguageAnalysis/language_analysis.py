import os
from Auxiliaries.utils import PUNCTUATION_MARK_TAG, WELL_DEFINED_LANGUAGE_OPTIONS, CS_LEVELS_OPTIONS, CS_LEVELS_DECODE, PURE_CS_LEVELS_OPTIONS, MAJOR_LANGUAGE_ENCODE, load_most_common_words_list
from Auxiliaries.utils import MOST_COMMON_WORDS_IN_ENGLISH_FILE, MOST_COMMON_WORDS_IN_SPANISH_FILE
from Auxiliaries.utils import MOST_COMMON_BIGRAMS_IN_ENGLISH_FILE, MOST_COMMON_BIGRAMS_IN_SPANISH_FILE
from Auxiliaries.utils import MOST_COMMON_TRIGRAMS_IN_ENGLISH_FILE, MOST_COMMON_TRIGRAMS_IN_SPANISH_FILE

DIR_OF_MOST_COMMON_N_GRAMS = os.path.join('Data', 'common_n_grams')

LIST_OF_MOST_COMMON_WORDS_IN_SPANISH = load_most_common_words_list(MOST_COMMON_WORDS_IN_SPANISH_FILE)
LIST_OF_MOST_COMMON_WORDS_IN_ENGLISH = load_most_common_words_list(MOST_COMMON_WORDS_IN_ENGLISH_FILE)

LIST_OF_MOST_COMMON_BIGRAMS_IN_SPANISH = load_most_common_words_list(MOST_COMMON_BIGRAMS_IN_SPANISH_FILE)
LIST_OF_MOST_COMMON_BIGRAMS_IN_ENGLISH = load_most_common_words_list(MOST_COMMON_BIGRAMS_IN_ENGLISH_FILE)

LIST_OF_MOST_COMMON_TRIGRAMS_IN_SPANISH = load_most_common_words_list(MOST_COMMON_TRIGRAMS_IN_SPANISH_FILE)
LIST_OF_MOST_COMMON_TRIGRAMS_IN_ENGLISH = load_most_common_words_list(MOST_COMMON_TRIGRAMS_IN_ENGLISH_FILE)


def find_first_well_defined_label_in(label_seq):
	for label in label_seq:
		if label in WELL_DEFINED_LANGUAGE_OPTIONS:
			return label
	return None

def apply_well_defined_lang_label_to_all_ambiguous_tokens(tokens):
	good_tokens = [token for token in tokens if token.is_a_word]
	utterance_language_labels = [token.lang for token in tokens if token.is_a_word]

	for ind in range(len(good_tokens)):
		token = good_tokens[ind]
		current_token_label = token.lang

		if current_token_label in WELL_DEFINED_LANGUAGE_OPTIONS:
			token.well_defined_lang = token.lang

		else:  # 1) Look backward in the sequence to find the closest well-defined label
			sequence_before_reversed = utterance_language_labels[0:ind].copy()
			sequence_before_reversed.reverse()
			best_label_before = find_first_well_defined_label_in(sequence_before_reversed)
			if best_label_before is not None:  # well-defined language label was found before
				# token.well_defined_lang = best_label_before
				token.set_well_defined_lang(best_label_before)

			else:  # 2) Look forward in the sequence to find the closest well-defined label
				best_label_after = \
					find_first_well_defined_label_in(utterance_language_labels[ind:])
				if best_label_after is not None:  # well-defined language label was found after
					# token.well_defined_lang = best_label_after
					token.set_well_defined_lang(best_label_after)

def get_end_indices_of_longest_sequence(sequence_of_labels, lang):
	count = 0
	prev = 0
	indexend = 0
	for i in range(len(sequence_of_labels)):
		current_lang_label = sequence_of_labels[i]
		if current_lang_label == lang:
			count += 1
		else:
			if count > prev:
				prev = count
				indexend = i
				count = 0

	start_index, end_index = indexend - prev, indexend - 1
	# print("The longest sequence of lang is " + str(prev))
	# print("index start at: " + str(indexend - prev))
	# print("index ends at: " + str(indexend - 1))
	return start_index, end_index

def apply_well_defined_lang_label_to_all_ambiguous_tokens(tokens):
	good_tokens = [token for token in tokens if not token.lang == PUNCTUATION_MARK_TAG]
	utterance_language_labels = [token.lang for token in tokens if not token.lang == PUNCTUATION_MARK_TAG]
	for ind in range(len(good_tokens)):
		token = good_tokens[ind]
		current_token_label = token.lang

		if current_token_label in WELL_DEFINED_LANGUAGE_OPTIONS:
			token.set_well_defined_lang(current_token_label)

		else:  # 1) Look backward in the sequence to find the closest well-defined label
			sequence_before_reversed = utterance_language_labels[0:ind].copy()
			sequence_before_reversed.reverse()
			best_label_before = find_first_well_defined_label_in(sequence_before_reversed)
			if best_label_before is None:
			# 2) Look forward in the sequence to find the closest well-defined label
				best_label_after = find_first_well_defined_label_in(utterance_language_labels[ind:])
				if best_label_after is not None:
					token.set_well_defined_lang(best_label_after)  # Well-defined language label was found after
			else:  # well-defined language label was found before
				token.set_well_defined_lang(best_label_before)

def get_list_of_minor_language_common_tokens(minor_lang):
	if minor_lang == 'spa':  # Major language = English, Minor_language = Spanish
		# return load_most_common_words_list(MOST_COMMON_WORDS_IN_SPANISH_FILE)
		return LIST_OF_MOST_COMMON_WORDS_IN_SPANISH
	elif minor_lang == 'eng':  # Major language = Spanish, Minor_language = English
		# return load_most_common_words_list(MOST_COMMON_WORDS_IN_ENGLISH_FILE)
		return LIST_OF_MOST_COMMON_WORDS_IN_ENGLISH
	else:
		# return load_most_common_words_list(MOST_COMMON_WORDS_IN_ENGLISH_FILE)
		return LIST_OF_MOST_COMMON_WORDS_IN_ENGLISH

def get_list_of_minor_language_common_bigrams(minor_lang):
	if minor_lang == 'spa':  # Minor_language = Spanish
		return LIST_OF_MOST_COMMON_BIGRAMS_IN_SPANISH
	elif minor_lang == 'eng':
		return LIST_OF_MOST_COMMON_BIGRAMS_IN_ENGLISH
	else:  # Default
		return LIST_OF_MOST_COMMON_BIGRAMS_IN_ENGLISH

def get_list_of_minor_language_common_trigrams(minor_lang):
	if minor_lang == 'spa':  # Minor_language = Spanish
		return LIST_OF_MOST_COMMON_TRIGRAMS_IN_SPANISH
	elif minor_lang == 'eng':
		return LIST_OF_MOST_COMMON_TRIGRAMS_IN_ENGLISH
	else:  # Default
		return LIST_OF_MOST_COMMON_TRIGRAMS_IN_ENGLISH

def are_all_tokens_are_common(list_of_tokens_to_check, list_of_all_common_words):
	for token in list_of_tokens_to_check:
		if token.lower() not in list_of_all_common_words:  # an un-common token was found
			return False
	return True

def is_this_bigram_common(bigram_to_check, list_of_all_common_bigrams):
	bigram_to_check_in_lower_case = [token.lower() for token in bigram_to_check]
	if tuple(bigram_to_check_in_lower_case) not in list_of_all_common_bigrams:
		return False
	return True

def calc_cs_level(tokens, minor_lang, major_lang):
	tokens = [token for token in tokens if token.lang is not PUNCTUATION_MARK_TAG]
	clean_utterance_language_labels = [token.well_defined_lang for token in tokens]

	clean_utterance_tokens = [token.surface.lower() for token in tokens]

	start_index, end_index = get_end_indices_of_longest_sequence(clean_utterance_language_labels, minor_lang)

	len_of_longest_minor_lang_sequence = end_index - start_index + 1

	if len_of_longest_minor_lang_sequence <= 0:  # absence of minor language in sentence
		minor_language_level = 'N'

	elif len_of_longest_minor_lang_sequence > 3:  # more than 3 tokens of minor language
		minor_language_level = 'P'

	elif len_of_longest_minor_lang_sequence == 3:  #3 tokens of the minor language
		longest_minor_language_sequence = clean_utterance_tokens[start_index: end_index + 1]
		list_of_all_common_trigrams = get_list_of_minor_language_common_trigrams(minor_lang)
		if longest_minor_language_sequence in list_of_all_common_trigrams:
			minor_language_level = 'T'
		else:
			minor_language_level = 'P'

	elif 1 <= len_of_longest_minor_lang_sequence <= 2:  # one or two tokens of the minor language
		longest_minor_language_sequence = clean_utterance_tokens[start_index: end_index + 1]
		list_of_all_common_words = get_list_of_minor_language_common_tokens(minor_lang)
		list_of_all_common_bigrams = get_list_of_minor_language_common_bigrams(minor_lang)

		# unigram / bigram
		if are_all_tokens_are_common(longest_minor_language_sequence, list_of_all_common_words):
			minor_language_level = 'T'
		else:
			minor_language_level = 'L'

		# for bigram only
		if len_of_longest_minor_lang_sequence == 2:  # bigram
			if is_this_bigram_common(longest_minor_language_sequence, list_of_all_common_bigrams):
				minor_language_level = 'T'

	else:
		print("an error occurred in the function find_cs_level")
		minor_language_level = 'X'

	cs_level = MAJOR_LANGUAGE_ENCODE[major_lang] + minor_language_level

	return cs_level
