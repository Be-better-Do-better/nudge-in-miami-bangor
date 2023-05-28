
from scipy.stats import ttest_1samp


def t_test(sample, expected_population_mean) -> tuple[float, float]:
	result = ttest_1samp(sample, popmean=expected_population_mean, alternative='two-sided')
	# lower_bound_of_95_confidence_level = result.confidence_interval().low
	# higher_bound_of_95_confidence_level = result.confidence_interval().high
	t_stat, p_value = result.statistic, result.pvalue
	return t_stat, p_value

