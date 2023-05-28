import math
import scipy.stats as stats
import random
import numpy as np

from Auxiliaries.utils import CS_LEVELS_DECODE
from Auxiliaries.artificial_generation import generate_corpus
from Classes.corpus import Corpus
from Classes.corpus_cs_levels_series_representation import CorpusCSSeries
from Hypotheses.always_decreases import AlwaysDecrease
from CorpusAnalyses.extract_cs_levels_frequency import extract_cs_levels_frequency
from Auxiliaries.t_test import t_test
from Auxiliaries.get_all_permutations import get_all_permutations
from Classes.hypothesis import Hypothesis
from Hypotheses.always_0_or_7 import Always_0_or_7
from Hypotheses.nudge import Nudge
from Hypotheses.hypotheses import generate_hypotheses

P_VALUE_LIMIT = 0.05

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


def calc_expected_proportion(dict_of_frequencies, hypothesis: Hypothesis):
	proportion = 0
	cs_levels_options = CS_LEVELS_DECODE.values()

	all_permutations_options = get_all_permutations(hypothesis.relevant_indexes, cs_levels_options)

	for permutation in all_permutations_options:
		c = [-1 for _ in range(hypothesis.n+1)]
		for i, value in zip(hypothesis.relevant_indexes, permutation):
			c[i] = value
		if hypothesis.check_condition(c):
			probabilities = [dict_of_frequencies[c[i]] for i in hypothesis.relevant_indexes]
			proportion += np.prod(probabilities)
	return proportion


def calc_actual_proportions(cs_levels: CorpusCSSeries, hypothesis) -> list[float]:
	proportions = []
	for dialogue_as_cs_levels in cs_levels.list_of_series:
		total_counter = 0
		hypothesis_condition_counter = 0
		n = len(dialogue_as_cs_levels)
		for c0_index in range(hypothesis.n, n):
			c = [dialogue_as_cs_levels[c0_index-i] for i in range(hypothesis.n+1)]
			total_counter += 1
			if hypothesis.check_condition(c):
				hypothesis_condition_counter += 1
		if total_counter > 0:
			proportions.append(hypothesis_condition_counter / total_counter)

	return proportions


def generate_equivalent_random_corpus(original_corpus: CorpusCSSeries, cs_levels_frequencies: dict) -> CorpusCSSeries:
	collected_output_series = []
	cs_levels = [i for i in range(len(CS_LEVELS_DECODE))]
	cs_levels_frequency = [cs_levels_frequencies[i] for i in cs_levels]
	for original_cs_levels_series in original_corpus.list_of_series:
		collected_output_series.append(random.choices(cs_levels, cs_levels_frequency, k=len(original_cs_levels_series)))

	return CorpusCSSeries('random', collected_output_series)


def analyse_hypothesis_proportion(corpus: Corpus, hypothesis: Hypothesis, utterances: bool=True) -> None:
	print("Hypothesis: " + hypothesis.name)
	corpus_as_cs_levels_series = collect_cs_levels(corpus, utterances)
	dict_of_frequencies = extract_cs_levels_frequency(corpus_as_cs_levels_series)
	# print(dict_of_frequencies)
	p_expected = calc_expected_proportion(dict_of_frequencies, hypothesis)
	print("p_expected = {}".format(p_expected))
	proportions_sample = calc_actual_proportions(corpus_as_cs_levels_series, hypothesis)
	print(f"p_measured = {np.mean(proportions_sample)} +- {np.std(proportions_sample)}")
	"""
	print('Sample: ', proportions_sample)
	print(f"# of samples = {len(proportions_sample)}")
	print(f"Max of samples = {max(proportions_sample)}")
	print(f"Min of samples = {min(proportions_sample)}")
	print(f"Mean of samples = {np.mean(proportions_sample)}")
	print(f"STD of samples = {np.std(proportions_sample)}")
	"""
	t_stat, p_value = t_test(proportions_sample, p_expected)

	if P_VALUE_LIMIT > p_value: # significant!
	# Output the p-value of the test statistic (right tailed test)
		print(f"test_stat = {t_stat}, p_value = {p_value} *")
	else:
		print(f"test_stat = {t_stat}, p_value = {p_value} (Insignificant)")


def analyse_hypotheses_proportion(corpus: Corpus):
	hypotheses = generate_hypotheses()
	for utterances in [True, False]:
		if utterances:
			print("Utterances:")
		else:
			print("Turns:")
		for hypothesis in hypotheses:
			analyse_hypothesis_proportion(corpus, hypothesis, utterances)
