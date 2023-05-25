import os
import numpy as np

os.chdir('../..')
from Auxiliaries.data_loaders import collect_corpus
from Auxiliaries.t_test import t_test
from Classes.hypothesis import Hypothesis
from CorpusAnalyses.corpus_analyses import collect_languages, langid_classify, analyse_langid_results, analyse_cs_level_classifier, analyses_cs_bigrams_distribution
from CorpusAnalyses.distances_between_events_in_boolean_sequences_analysis import extract_distances, calc_frequency, calc_relative_frequency, calc_hazards, generate_series, relative_frequency_comparison, plot_relative_frequency
from CorpusAnalyses.run_analysis import analyse_corpus
from CorpusAnalyses.analyse_hypotheses_proportions import analyse_hypothesis_proportion, calc_expected_proportion, calc_actual_proportions, extract_cs_levels_frequency, collect_cs_levels
from Hypotheses.always_0_or_7 import Always_0_or_7
from Hypotheses.always_decreases import AlwaysDecrease

REDUCED_MIAMI_BANGOR_CORPUS = collect_corpus(corpus_name='Reduced-Miami-Bangor',
										 root_dir=os.path.join(os.getcwd(), 'Data', 'bangor_raw_reduced'))


def test_calc_expected_proportion():
	pass

def test_calc_actual_proportion():
	pass

def test_analyse_hypothesis_proportion():
	hypothesis = Always_0_or_7()
	corpus = REDUCED_MIAMI_BANGOR_CORPUS

	corpus_as_cs_levels_series = collect_cs_levels(corpus, utterances=True)
	dict_of_frequencies = extract_cs_levels_frequency(corpus_as_cs_levels_series)
	# print(dict_of_frequencies)
	p_expected = calc_expected_proportion(dict_of_frequencies, hypothesis)
	print("p_expected = {}".format(p_expected))
	proportions_sample = calc_actual_proportions(corpus_as_cs_levels_series, hypothesis)
	print('Sample: ', proportions_sample)
	print(f"# of samples = {len(proportions_sample)}")
	print(f"Max of samples = {max(proportions_sample)}")
	print(f"Min of samples = {min(proportions_sample)}")
	print(f"Mean of samples = {np.mean(proportions_sample)}")
	print(f"STD of samples = {np.std(proportions_sample)}")
	t_stat, p_value = t_test(proportions_sample, p_expected)
	print("test_stat = {}".format(t_stat))
	# Output the p-value of the test statistic (right tailed test)
	print("p_value = {}".format(p_value))


def run_tests():
	test_calc_actual_proportion()
	test_calc_expected_proportion()
	test_analyse_hypothesis_proportion()

if __name__ == '__main__':
	run_tests()