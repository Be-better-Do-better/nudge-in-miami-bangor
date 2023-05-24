
from scipy.stats import ttest_1samp


def t_test(sample, expected_population_mean) -> tuple[float, float]:
	res = ttest_1samp(sample, popmean=expected_population_mean, alternative='greater')
	t_stat, p_value = ttest_1samp(sample, popmean=expected_population_mean, alternative='greater')
	print(f"df = { res.df }")
	print(f" confidence interval [{ res.confidence_interval().low}" f", { res.confidence_interval().high}]")
	return t_stat, p_value

