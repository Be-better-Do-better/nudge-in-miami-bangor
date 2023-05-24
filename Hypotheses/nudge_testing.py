from Hypotheses.boolean_conditions import general_nudge, same_cs_level
from Classes.corpus_cs_levels_series_representation import CorpusCSSeries


def test_nudge(corpus_as_cs_levels_series: CorpusCSSeries) -> tuple[int, int]:
	num_of_true_results = 0
	num_of_false_results = 0
	total = 0
	for series in corpus_as_cs_levels_series.list_of_series:
		if len(series) > 0:
			for n in range(len(series) - 1):
				if len(series[0:n + 1]) >= 4:
					res = general_nudge(series[0:n + 1])
					if res:
						num_of_true_results += 1
					else:
						num_of_false_results += 1
				total += 1
	if total > 0:
		str_to_print = f'Nudge occurred in {num_of_true_results} out of {total} ({num_of_true_results / total * 100:2.2f}%) @' + corpus_as_cs_levels_series.name
	else:
		str_to_print = "Nudge tested on an empty corpus"
	print(str_to_print)
	return num_of_true_results, num_of_false_results


def test_tit_for_tat(corpus_as_cs_levels_series: CorpusCSSeries):
	num_of_true_results = 0
	total = 0
	for series in corpus_as_cs_levels_series.list_of_series:
		if len(series) > 0:
			for n in range(len(series) - 1):
				if len(series[0:n + 1]) >= 2:
					res = same_cs_level(series[0:n + 1])
					if res:
						num_of_true_results += 1
				total += 1

	if total > 0:
		str_to_print = f'Tit-for-Tat occurred in {num_of_true_results} out of {total} ({num_of_true_results / total * 100:2.2f}%) @' + corpus_as_cs_levels_series.name
	else:
		str_to_print = "Tit-for-Tat tested on an empty corpus"
	print(str_to_print)
