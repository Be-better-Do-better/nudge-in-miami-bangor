import math
import scipy.stats as stats
import random
import numpy as np

from Auxiliaries.utils import CS_LEVELS_DECODE
from Auxiliaries.artificial_generation import generate_corpus
from Classes.corpus import Corpus
from Classes.corpus_cs_levels_series_representation import CorpusCSSeries
from Hypotheses.nudge import nudge
from CorpusAnalyses.extract_cs_levels_frequency import extract_cs_levels_frequency
from Auxiliaries.t_test import t_test


def collect_cs_levels(corpus: Corpus, utterances=True) -> CorpusCSSeries:
	list_of_cs_series_of_utterances = []
	for dialogue in corpus.dialogues:

		if utterances:
			series_of_cs_levels_in_utterances = [CS_LEVELS_DECODE[utterance.cs_level] for utterance in dialogue.utterances]
		else:
			series_of_cs_levels_in_utterances = [CS_LEVELS_DECODE[turn.cs_level] for turn in dialogue.turns]

		list_of_cs_series_of_utterances.append(series_of_cs_levels_in_utterances)

	if utterances:
		return CorpusCSSeries('utterances', list_of_cs_series_of_utterances)
	else:
		return CorpusCSSeries('turns', list_of_cs_series_of_utterances)


def calc_expected_proportion(dict_of_frequencies):
	proportion = 0
	cs_levels_options = CS_LEVELS_DECODE.values()
	for c0 in cs_levels_options:
		for c1 in cs_levels_options:
			for c2 in cs_levels_options:
				for c3 in cs_levels_options:
					if nudge(c0, c1, c2, c3):
						proportion += \
							dict_of_frequencies[c0]*dict_of_frequencies[c1]*dict_of_frequencies[c2]*dict_of_frequencies[c3]
	return proportion


def calc_actual_proportions(cs_levels: CorpusCSSeries) -> list[float]:
	proportions = []

	for dialogue_as_cs_levels in cs_levels.list_of_series:
		total_counter = 0
		nudge_condition_counter = 0
		n = len(dialogue_as_cs_levels)
		for i in range(3, n):
			c0 = dialogue_as_cs_levels[i-0]
			c1 = dialogue_as_cs_levels[i-1]
			c2 = dialogue_as_cs_levels[i-2]
			c3 = dialogue_as_cs_levels[i-3]
			total_counter += 1
			if nudge(c0, c1, c2, c3):
				nudge_condition_counter += 1

		if total_counter > 0:
			proportion = nudge_condition_counter / total_counter

		proportions.append(proportion)

	return proportions


def generate_equivalent_random_corpus(original_corpus: CorpusCSSeries, cs_levels_frequencies: dict) -> CorpusCSSeries:
	collected_output_series = []
	cs_levels = [i for i in range(len(CS_LEVELS_DECODE))]
	cs_levels_frequency = [cs_levels_frequencies[i] for i in cs_levels]
	for original_cs_levels_series in original_corpus.list_of_series:
		collected_output_series.append(random.choices(cs_levels, cs_levels_frequency, k=len(original_cs_levels_series)))

	return CorpusCSSeries('random', collected_output_series)


def analyse_nudge_proportion(corpus: Corpus) -> None:
	corpus_as_cs_levels_series = collect_cs_levels(corpus, utterances=True)
	dict_of_frequencies = extract_cs_levels_frequency(corpus_as_cs_levels_series)
	# print(dict_of_frequencies)
	p_expected = calc_expected_proportion(dict_of_frequencies)
	print("p_expected = {}".format(p_expected))
	proportions_sample = calc_actual_proportions(corpus_as_cs_levels_series)
	print('Sample: ', proportions_sample)
	print(f"# of samples = {len(proportions_sample)}")
	print(f"Max of samples = {max(proportions_sample)}")
	print(f"Min of samples = {min(proportions_sample)}")
	print(f"Mean of samples = {np.mean(proportions_sample)}")
	print(f"STD of samples = {np.std(proportions_sample)}")
	t_stat, p_value = t_test(proportions_sample, p_expected)
	print("test_stat = {}".format(t_stat))
	print("p_value = {}".format(p_value))

	"""
	results = []
	# test on random
	for _ in range(1000):
		random_corpus_as_cs_levels_series = generate_equivalent_random_corpus(corpus_as_cs_levels_series, dict_of_frequencies)
		p_measured, sample_size = calc_actual_proportion(random_corpus_as_cs_levels_series)
		# print("p_measured@random = {}".format(p_measured))
		results.append(p_measured)
	print("At the randomly generated series:")
	print("mean = {}, std = {}".format(np.mean(results), np.std(results)))
	"""


def test_generate_equivalent_random_corpus():
	corpus = generate_corpus()
	cs_levels = collect_cs_levels(corpus, utterances=True)
	proportions = calc_actual_proportions(cs_levels)
