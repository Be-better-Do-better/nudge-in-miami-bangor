from collections import Counter
from Auxiliaries.utils import WELL_DEFINED_LANGUAGE_OPTIONS


def get_frequency_of_monolingual_subsequences_lengths(list_monolingual_tags_sequences_lengths: list[str]) -> dict:
	frequency_of_monolingual_subsequences_lengths = {}
	for lang in WELL_DEFINED_LANGUAGE_OPTIONS:
		frequency_of_monolingual_subsequences_lengths[lang] = Counter()

	for current_lang, current_sub_sequence_length in list_monolingual_tags_sequences_lengths:
		frequency_of_monolingual_subsequences_lengths[current_lang].update([current_sub_sequence_length])

	return frequency_of_monolingual_subsequences_lengths
