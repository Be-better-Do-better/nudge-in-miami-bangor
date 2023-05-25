import os
os.chdir('..\..')

from Hypotheses.random_cs_sequences_generation import generate_random_list_of_series
from Hypotheses.hypothesis_testing import generate_hypotheses  # retreat, nudge, test_hypotheses
from Hypotheses.corpora_representations import CorpusCSSeries
from Hypotheses.hypothesis_power_calculations import StatisticsPower
from Hypotheses.hypothesis_test import HypothesisTest


def test_test_hypotheses():
	hypotheses = generate_hypotheses()
	h0 = hypotheses[0]
	list_of_series = generate_random_list_of_series()
	cscorpus = CorpusCSSeries('random', list_of_series)
	probability_of_sample_inclusion = 1.0

	ht = HypothesisTest(h0, cscorpus, probability_of_sample_inclusion)

def test_calc_power():
	sp=StatisticsPower(nTT=11, nTF=1000, nFT=3, nFF=4)
	print("Odds Ratio: {}".format(sp.calc_odds_ratio()))
	p = sp.calc_power(alpha=0.05)
	print("Power: 1-beta = {}".format(p))
	p = sp.calc_power(alpha=0.01)
	print("Power: 1-beta = {}".format(p))

def test_relative_risk():
	sp=StatisticsPower(nTT=34, nTF=16, nFT=39, nFF=11)
	print("Odds Ratio: {}".format(sp.calc_odds_ratio()))
	rr = sp.calc_relative_risk()
	print("Relative Risk = {}".format(rr))
	rr_95_CI = sp.calc_relative_risk_confidence_level()
	print("Relative Risk 95% Confidence level = ({}, {})".format(rr_95_CI[0], rr_95_CI[1]))

	sp=StatisticsPower(nTT=110653, nTF=51705, nFT=51761, nFF=46590)
	print("Odds Ratio: {}".format(sp.calc_odds_ratio()))
	rr = sp.calc_relative_risk()
	print("Relative Risk = {}".format(rr))
	rr_95_CI = sp.calc_relative_risk_confidence_level()
	print("Relative Risk 95% Confidence level = ({}, {})".format(rr_95_CI[0], rr_95_CI[1]))


def run_tests():
	test_test_hypotheses()
	test_calc_power()
	test_relative_risk()


if __name__ == '__main__':
	run_tests()
	print('Success!')
