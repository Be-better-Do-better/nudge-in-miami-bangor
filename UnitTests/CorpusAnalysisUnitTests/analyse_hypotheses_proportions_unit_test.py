import os
import numpy as np

os.chdir('../..')
from Auxiliaries.t_test import t_test
from CorpusAnalyses.NextLevelPredition.analyse_hypotheses_proportions import calc_expected_proportion, calc_actual_proportions, extract_cs_levels_frequency, collect_cs_levels
from Hypotheses.always_EN_or_SN import Always_EN_or_SN
from Hypotheses.always_decreases import AlwaysDecrease

"""
REDUCED_MIAMI_BANGOR_CORPUS = collect_corpus(corpus_name='Reduced-Miami-Bangor',
										 root_dir=os.path.join(os.getcwd(), 'Data', 'bangor_raw_reduced'))
"""


def test_calc_expected_proportion():
	hypothesis = AlwaysDecrease()
	dict_of_frequencies = {0: 0.3, 1: 0.1, 2: 0.05, 3: 0.05, 4: 0, 5: 0, 6: 0.1, 7: 0.4}
	p = calc_expected_proportion(dict_of_frequencies, hypothesis)
	print(p)
	s = 0
	for c1 in range(8):
		s += dict_of_frequencies[c1] * sum([dict_of_frequencies[c2] for c2 in dict_of_frequencies.keys() if c2>c1])
	print(s)


def test_calc_actual_proportion():
	pass


def test_analyse_hypothesis_proportion():
	hypothesis = Always_EN_or_SN()
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
	#  test_calc_actual_proportion()
	test_calc_expected_proportion()
	# test_analyse_hypothesis_proportion()

if __name__ == '__main__':
	run_tests()
