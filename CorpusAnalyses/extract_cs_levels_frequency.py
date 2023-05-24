from collections import Counter
from Classes.corpus_cs_levels_series_representation import CorpusCSSeries


def extract_cs_levels_frequency(cs_levels_series: CorpusCSSeries) -> dict:
	c = Counter()
	for dialogue_as_ints in cs_levels_series.list_of_series:
		c.update(dialogue_as_ints)

	cs_levels = set(c.keys())
	total_num = sum(c.values())
	d = {}
	for cs_level in cs_levels:
		d[cs_level] = c[cs_level] / total_num
	return d
