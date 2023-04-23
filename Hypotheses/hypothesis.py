import scipy.stats as stats
import random
from Hypotheses.hypothesis_power_calculations import StatisticsPower

ALPHA = 0.05 # Probability of type I error

class Hypothesis(object):
	def __init__(self, name, description, x_description, y_description, f_x, f_y, f_x_required_context_length=0,
	             f_y_required_context_length=0, constants={}):
		self.name = name
		self.description = description
		self.x_description = x_description
		self.y_description = y_description
		self.conditions = {'X': f_x, 'Y': f_y}
		self.f_x_context_length = f_x_required_context_length
		self.f_y_context_length = f_y_required_context_length

		self.constants = constants

		self.odd_ratio = None
		self.fisher_p_value = None
		self.chi2_p_value = None
		self.power = None
		self.relative_risk = None
		self.relative_risk_confidence_level = (None, None)
		self.accuracy = None

		self.contingency_table = {}
		self.init_contingency_table()

	def __str__(self):
		s = 'Hypothesis: ' + self.name + '\n'
		s += self.description + '\n'
		s += 'X: ' + self.x_description + '\n'
		s += 'Y: ' + self.y_description + '\n'
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

		s += '\n'
		s += "X | Y | Frequency" + '\n'
		for x in [True, False]:
			for y in [True, False]:
				s += "{} | {} | {} \n".format(x, y, self.contingency_table[(x, y)])

		return s

	def init_contingency_table(self):
		for x in [True, False]:
			for y in [True, False]:
				self.contingency_table[(x, y)] = 0

	def display_contingency_table(self):
		print("X | Y | Frequency")
		for x in [True, False]:
			for y in [True, False]:
				print("{} | {} | {}".format(x, y, self.contingency_table[(x, y)]))


	def test(self, list_of_series:list[list[int]], probability_of_sample_inclusion:float=0.05):
		for series in list_of_series:
			if len(series) > 0:
				for n in range(len(series)-1):
					if (len(series[0:n+1])>=self.f_x_context_length) and (len(series[0:n+1])>=self.f_y_context_length):
						x = self.conditions['X'](series[0:n+1], self.constants)
						y = self.conditions['Y'](series[0:n+1], self.constants)
						to_include = random.choices([True, False],
						                            [probability_of_sample_inclusion,
						                             1-probability_of_sample_inclusion],k=1)[0]
						if to_include:
							self.contingency_table[(x, y)] += 1

		self.calc_statistics()

	def calc_accuracy(self):
		"""
		This function calculates the value of the accuracy from the contingency table
		:return: accuracy [float]
		"""
		accuracy = None
		total_sum = 0
		for x in [True, False]:
			for y in [True, False]:
				total_sum += self.contingency_table[(x, y)]

		if total_sum > 0:
			accuracy = (self.contingency_table[(True, True)] + self.contingency_table[(False, False)]) / total_sum

		return accuracy


	def calc_statistics(self):
		data = [[0, 0], [0, 0]]
		data[0][0] = self.contingency_table[(False, False)]
		data[0][1] = self.contingency_table[(False, True)]
		data[1][0] = self.contingency_table[(True, False)]
		data[1][1] = self.contingency_table[(True, True)]

		# performing fishers exact test on the data
		self.odd_ratio, self.fisher_p_value = stats.fisher_exact(data)
		try:
			chi_val, self.chi2_p_value, dof, expected = stats.chi2_contingency(data)
		except ValueError:
			print("a row/column of zeros was found in the contingency matrix :(")
		except:
			print("Something else went wrong")

		sp = StatisticsPower(nTT=data[1][1], nTF=data[1][0], nFT=data[0][1], nFF=data[0][0])
		self.power = sp.calc_power(ALPHA)

		self.relative_risk = sp.calc_relative_risk()
		self.relative_risk_confidence_level = sp.calc_relative_risk_confidence_level()

		self.accuracy = self.calc_accuracy()


