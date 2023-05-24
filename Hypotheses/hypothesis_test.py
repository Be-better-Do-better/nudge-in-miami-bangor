from Hypotheses.hypothesis import Hypothesis
from Classes.corpus_cs_levels_series_representation import CorpusCSSeries

class HypothesisTest(object):
	def __init__(self, hypothesis: Hypothesis, corpus_as_cs_levels_series: CorpusCSSeries, probability_of_sample_inclusion: float):
		self.hypothesis = hypothesis
		self.corpus_as_cs_levels_series = corpus_as_cs_levels_series
		self.probability_of_sample_inclusion = probability_of_sample_inclusion

		# Run the test on the data:
		self.hypothesis.test(self.corpus_as_cs_levels_series.list_of_series, self.probability_of_sample_inclusion)

		self.contingency_table = self.hypothesis.contingency_table.copy()
		self.odd_ratio = float(self.hypothesis.odd_ratio.copy())
		self.fisher_p_value = float(self.hypothesis.fisher_p_value.copy())
		self.chi2_p_value = float(self.hypothesis.chi2_p_value.copy())
		self.power = float(self.hypothesis.power.copy())
		self.contingency_table = self.hypothesis.contingency_table.copy()
		self.relative_risk = float(self.hypothesis.relative_risk)
		self.relative_risk_confidence_level = self.hypothesis.relative_risk_confidence_level
		self.accuracy = float(self.hypothesis.accuracy)


	def __str__(self):
		s = 'Hypothesis: ' + self.hypothesis.name + '\n'
		s += self.hypothesis.description + '\n'
		s += 'X: ' + self.hypothesis.x_description + '\n'
		s += 'Y: ' + self.hypothesis.y_description + '\n'

		if self.fisher_p_value is not None:
			s += 'fisher\'s p_value is : ' + str(self.fisher_p_value) + '\n'
		if self.chi2_p_value is not None:
			s += 'chi^2 p_value is : ' + str(self.chi2_p_value) + '\n'
		if self.odd_ratio is not None:
			s += 'odd ratio : ' + str(self.odd_ratio) + '\n'

		if self.power is not None:
			s += 'statistics power (1-beta): ' + str(self.power) + '\n'

		if self.relative_risk is not None:
			s += 'relative risk: ' + str(self.relative_risk) + '\n'

		if not None in self.relative_risk_confidence_level:
			s += 'relative risk 95%: ({}, {}) \n'.format(self.relative_risk_confidence_level[0],
			                                             self.relative_risk_confidence_level[1])
		if self.accuracy is not None:
			s += 'accuracy: ' + str(self.accuracy) + '\n'
		s += '\n'
		s += "X | Y | Frequency" + '\n'
		for x in [True, False]:
			for y in [True, False]:
				s += "{} | {} | {} \n".format(x, y, self.contingency_table[(x, y)])

		return s
