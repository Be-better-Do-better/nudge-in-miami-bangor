# http://powerandsamplesize.com/Calculators/Test-Odds-Ratio/Equality
import numpy as np
from scipy.stats import norm

class StatisticsPower(object):
	def __init__(self, nTT: int, nTF: int, nFT: int, nFF: int):
		"""
		For verifying the hypothesis: X->Y (where X & Y are some Boolean conditions).

		Group A: is X==T
		Group B (Control Group) is X==F

		:param nTT: # of occasions where X is True, Y is True
		:param nTF: # of occasions where X is True, Y is False
		:param nFT: # of occasions where X is False, Y is True
		:param nFF: # of occasions where X is False, Y is False
		"""
		self.nTT, self.nTF, self.nFT, self.nFF = nTT, nTF, nFT, nFF

		self.nA = self.nTT + self.nTF # First Group is X==T
		self.nB = self.nFT + self.nFF # Second Group is X==F

		self.pA = None
		if self.nA > 0:
			self.pA = self.nTT/self.nA # First Group is X==T

		self.pB = None
		if self.nB > 0:
			self.pB = self.nFT/self.nB # Second Group is X==F

		self.relative_risk = None
		self.relative_risk_95_CI = (None, None) # 95% confidence level


	def __calc_odds_ratio(self):
		if None in [self.pA, self.pB]:
			return None
		elif not 0 in [self.pB, 1-self.pA]:
			return self.pA*(1 - self.pB)/(self.pB * (1 - self.pA))
		else:
			return None

	def __calc_k(self):
		if self.nB>0:
			return self.nA/self.nB
		else:
			return None

	def __calc_z(self):
		if None in [self.pA, self.pB, self.odds_ratio, self.nA, self.nB]:
			return None
		elif self.odds_ratio == 0:
			return None
		elif self.nB < 0:
			return None

		num = np.log(self.odds_ratio) * np.sqrt(self.nB)
		den = 0
		if not 0 in [self.pA, 1-self.pA, self.pB, 1-self.pB, self.k]:
			val = 1/(self.k*self.pA*(1-self.pA))+1/(self.pB*(1-self.pB))
			den = np.sqrt(val)
		if den > 0:
			return num/den
		else:
			return None

	def __calc_power(self, alpha=0.05):
		self.odds_ratio = self.__calc_odds_ratio()
		self.k = self.__calc_k()
		self.z = None
		z_one_minus_half_alpha = None
		if not None in [self.k, self.odds_ratio]:
			self.z = self.__calc_z()
			z_one_minus_half_alpha = norm.cdf(1-alpha/2)

		if not None in [self.z, z_one_minus_half_alpha]:
			return norm.cdf(self.z-z_one_minus_half_alpha)+norm.cdf(-self.z-z_one_minus_half_alpha)
		else:
			return None

	def calc_power(self, alpha=0.05):
		return self.__calc_power(alpha)

	def calc_odds_ratio(self):
		return self.__calc_odds_ratio()

	def __calc_relative_risk(self):
		""" https://www.statology.org/relative-risk-confidence-interval/ """
		a, b, c, d = self.nTT, self.nTF, self.nFT, self.nFF
		if (a+b)*c > 0:
			self.relative_risk = (a*(c+d))/((a+b)*c)

	def calc_relative_risk(self):
		self.__calc_relative_risk()
		return self.relative_risk

	def __calc_relative_risk_confidence_level(self):
		""" https://www.statology.org/relative-risk-confidence-interval/ """
		a, b, c, d = self.nTT, self.nTF, self.nFT, self.nFF
		if not self.relative_risk is None:
			if 0 not in [a, c, a+b, c+d]:
				value_under_sqrt = 1/a+1/c-1/(a+b)-1/(c+d)
				if value_under_sqrt >= 0:
					lower_95_CI = np.e**(np.log(self.relative_risk)-1.96*np.sqrt(value_under_sqrt))
					upper_95_CI = np.e**(np.log(self.relative_risk)+1.96*np.sqrt(value_under_sqrt))
					self.relative_risk_95_CI = (lower_95_CI, upper_95_CI)

	def calc_relative_risk_confidence_level(self):
		self.__calc_relative_risk_confidence_level()
		return self.relative_risk_95_CI
