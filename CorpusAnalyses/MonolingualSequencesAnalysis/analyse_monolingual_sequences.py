import statistics
import numpy as np

from Auxiliaries.utils import WELL_DEFINED_LANGUAGE_OPTIONS, SIGNIFICANCE_LEVEL
from Auxiliaries.t_test import t_test
from Auxiliaries.report import Report
from Classes.corpus import Corpus
from CorpusAnalyses.MonolingualSequencesAnalysis.extract_list_of_tags import extract_list_of_tags
from CorpusAnalyses.MonolingualSequencesAnalysis.extract_raw_languages_probabilities import extract_raw_languages_probabilities
from CorpusAnalyses.MonolingualSequencesAnalysis.calculate_expected_monolingual_sequence_length import calculate_expected_monolingual_sequence_length
from CorpusAnalyses.MonolingualSequencesAnalysis.extract_monolingual_subsequences_lengths import extract_monolingual_subsequences_lengths
from CorpusAnalyses.MonolingualSequencesAnalysis.get_frequency_of_monolingual_subsequences_lengths import get_frequency_of_monolingual_subsequences_lengths


def analyse_monolingual_sequences(corpus: Corpus, by_utterances: bool, lang: str) -> tuple[float, float, float, float, float]:
	measured_average_monolingual_sequence_length = -1
	lower_bound_of_95_confidence_level = -1
	upper_bound_of_95_confidence_level = -1
	expected_sequence_length = -1
	p_value = -1

	list_language_tags_sequences = extract_list_of_tags(corpus=corpus, tagging_function=(lambda u: u.major_lang), by_utterances=by_utterances)
	# print(list_language_tags_sequences)

	language_tag_probabilities = extract_raw_languages_probabilities(list_language_tags_sequences)

	print("language_tag_probabilities:")
	print(language_tag_probabilities)

	p_L = language_tag_probabilities[lang]
	expected_monolingual_sequence_length = calculate_expected_monolingual_sequence_length(p_L)

	print("Expected monolingual sequence lengths:")
	print(expected_monolingual_sequence_length)

	measured_sequences_lengths = []

	for dialogue_tag_sequence in list_language_tags_sequences:
		list_monolingual_tags_sequences_lengths = extract_monolingual_subsequences_lengths(dialogue_tag_sequence)
		# print(list_monolingual_tags_sequences_lengths)
		frequency_of_monolingual_subsequences_lengths = get_frequency_of_monolingual_subsequences_lengths(list_monolingual_tags_sequences_lengths)
		# print(frequency_of_monolingual_subsequences_lengths)

		if len(frequency_of_monolingual_subsequences_lengths[lang].values()) > 0:
			measured_average_length = statistics.mean(frequency_of_monolingual_subsequences_lengths[lang].values())
			# print(f"Measured average {measured_average_length}")
			measured_sequences_lengths.append(measured_average_length)
		else:
			pass
			# print("0 points found")



	print("Results for lang: " + lang)
	sample = measured_sequences_lengths
	if len(sample) > 0:
		measured_average_monolingual_sequence_length = np.mean(sample)
		expected_sequence_length = expected_monolingual_sequence_length
		print(f"measured average monolingual sequence length = {measured_average_monolingual_sequence_length :3.3f} +- {np.std(sample) :3.3f}")
		print(f"expected length: {expected_sequence_length}")

		lower_bound_of_95_confidence_level, upper_bound_of_95_confidence_level, p_value = t_test(sample, expected_sequence_length)
		print(f"CI = [{lower_bound_of_95_confidence_level :3.3f}, {upper_bound_of_95_confidence_level :3.3f}]")
		if p_value < SIGNIFICANCE_LEVEL:  # significant!
			print(f"p_value = {p_value} *")
		else:
			print(f"p_value = {p_value} (Insignificant)")

		return measured_average_monolingual_sequence_length, lower_bound_of_95_confidence_level, upper_bound_of_95_confidence_level, expected_sequence_length, p_value



