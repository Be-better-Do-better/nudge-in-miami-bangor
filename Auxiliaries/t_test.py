import numpy as np
from scipy.stats import ttest_1samp


def t_test(sample, expected_population_mean) -> tuple[float, float, float]:
	result = ttest_1samp(sample, popmean=expected_population_mean, alternative='two-sided')
	lower_bound_of_95_confidence_level = result.confidence_interval().low
	upper_bound_of_95_confidence_level = result.confidence_interval().high
	# t_stat = result.statistic
	p_value = result.pvalue
	return lower_bound_of_95_confidence_level, upper_bound_of_95_confidence_level, p_value
