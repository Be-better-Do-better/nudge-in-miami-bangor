from Classes.corpus import Corpus
from Hypotheses.hypothesis_test import HypothesisTest
from Hypotheses.hypothesis import Hypothesis
from Hypotheses.corpus_cs_levels_series_representation import CorpusCSSeries
from Hypotheses.corpora_representations import generate_utterances_corpora_representations, \
	generate_turns_corpora_representations
from Hypotheses.hypotheses import generate_hypotheses
from Hypotheses.reports_generation import generate_hypothesis_test_per_corpus_report, generate_all_hypotheses_reports, generate_accuracy_hypothesis_test_per_corpus_report
from Hypotheses.nudge_testing import test_nudge, test_tit_for_tat
from Auxiliaries.report import Report


def collect_dict_of_hypotheses_tests(list_of_sample_inclusion_probabilities: list[float],
                                     corpora: list[CorpusCSSeries],
                                     hypotheses: list[Hypothesis]):
	dict_of_hypothesis_tests = {}
	for sample_inclusion_probability in list_of_sample_inclusion_probabilities:
		for corpus_as_list_of_cs_series in corpora:
			for hypothesis in hypotheses:
				dict_of_hypothesis_tests[(hypothesis, corpus_as_list_of_cs_series, sample_inclusion_probability)] = \
					HypothesisTest(hypothesis, corpus_as_list_of_cs_series, sample_inclusion_probability)

	return dict_of_hypothesis_tests


def run_test_hypothesis(corpus: Corpus):
	list_of_sample_inclusion_probabilities = [1.0]  # [0.01, 0.1, 1.0]
	hypotheses_for_utterances = generate_hypotheses()

	# Utterances:
	corpora_for_utterances = generate_utterances_corpora_representations(corpus)
	dict_of_hypothesis_tests_for_utterances = collect_dict_of_hypotheses_tests(list_of_sample_inclusion_probabilities,
	                                                                           corpora_for_utterances,
	                                                                           hypotheses_for_utterances)

	generate_hypothesis_test_per_corpus_report(hypotheses_for_utterances,
	                                           corpora_for_utterances,
	                                           [1.0],
	                                           dict_of_hypothesis_tests_for_utterances,
	                                           by_utterances=True)

	generate_accuracy_hypothesis_test_per_corpus_report(hypotheses_for_utterances,
                                           corpora_for_utterances,
                                           [1.0],
                                           dict_of_hypothesis_tests_for_utterances,
                                           by_utterances=True)
	generate_all_hypotheses_reports(dict_of_hypothesis_tests_for_utterances)

	# Turns:
	hypotheses_for_turns = generate_hypotheses()
	corpora_for_turns = generate_turns_corpora_representations(corpus)

	dict_of_hypothesis_tests_for_turns = collect_dict_of_hypotheses_tests(list_of_sample_inclusion_probabilities,
	                                                                      corpora_for_turns,
	                                                                      hypotheses_for_turns)
	generate_hypothesis_test_per_corpus_report(hypotheses_for_turns,
	                                           corpora_for_turns,
	                                           [1.0],
	                                           dict_of_hypothesis_tests_for_turns,
	                                           by_utterances=False)

	generate_accuracy_hypothesis_test_per_corpus_report(hypotheses_for_turns,
	                                       corpora_for_turns,
	                                       [1.0],
	                                       dict_of_hypothesis_tests_for_turns,
	                                       by_utterances=False)
	generate_all_hypotheses_reports(dict_of_hypothesis_tests_for_turns)


def nudge_occurrence_testing(corpus: Corpus):
	# Utterances:
	name = 'Nudge on utterances'
	report_content = ''
	report_content += '\\begin{table}\n'
	report_content += '\\begin{center}\n'
	report_content += '\\begin{tabular}{|c||c|c|c|c|}\n'
	report_content += '\\hline\n'
	report_content += name + ' & True & False & Total & \% \\\\\n'
	report_content += '\\hline \\hline\n'

	corpora_for_utterances = generate_utterances_corpora_representations(corpus)
	for corpus_as_cs_levels_series in corpora_for_utterances:
		num_of_true_results, num_of_false_results = test_nudge(corpus_as_cs_levels_series)
		total = num_of_true_results + num_of_false_results
		report_content += corpus_as_cs_levels_series.name + ' & {} & {} & {} & {:2.2f}\\\\\n'.format(num_of_true_results,
		                                                                                        num_of_false_results,
		                                                                                        total,
		                                                                                        num_of_true_results/total*100)
		report_content += '\\hline \n'

	name_of_table = name.lower().replace('_', ' ')
	report_content += '\\end{tabular}\n'
	report_content += '\\end{center}\n'
	report_content += '\\caption{Testing ' + name_of_table + '}\n'

	report_content += '\\label{table:' + name.lower().replace(' ', '-') + '}\n'
	report_content += '\\end{table}\n'
	report_title = 'general_nudge_testing'
	report_filename = 'general_nudge_testing.txt'
	Report(report_title, report_filename, report_content)


	# Turns:
	corpora_for_turns = generate_turns_corpora_representations(corpus)
	name = 'Nudge on turns'
	report_content = ''
	report_content += '\\begin{table}\n'
	report_content += '\\begin{center}\n'
	report_content += '\\begin{tabular}{|c||c|c|c|c|}\n'
	report_content += '\\hline\n'
	report_content += name + ' & True & False & Total & \% \\\\\n'
	report_content += '\\hline \\hline\n'

	for corpus_as_cs_levels_series in corpora_for_turns:
		num_of_true_results, num_of_false_results = test_nudge(corpus_as_cs_levels_series)
		total = num_of_true_results + num_of_false_results
		report_content += corpus_as_cs_levels_series.name + ' & {} & {} & {} & {:2.2f}\\\\\n'.format(num_of_true_results,
		                                                                                        num_of_false_results,
		                                                                                        total,
		                                                                                        num_of_true_results/total*100)
		report_content += '\\hline \n'

	name_of_table = name.lower().replace('_', ' ')
	report_content += '\\end{tabular}\n'
	report_content += '\\end{center}\n'
	report_content += '\\caption{Testing ' + name_of_table + '}\n'

	report_content += '\\label{table:' + name.lower().replace(' ', '-') + '}\n'
	report_content += '\\end{table}\n'
	report_title = 'general_nudge_testing'
	report_filename = 'general_nudge_testing_on_turns.txt'
	Report(report_title, report_filename, report_content)


def tit_for_tat_occurrence_testing(corpus: Corpus):
	# Utterances:
	corpora_for_utterances = generate_utterances_corpora_representations(corpus)
	for corpus_as_cs_levels_series in corpora_for_utterances:
		test_tit_for_tat(corpus_as_cs_levels_series)

	# Utterances:
	corpora_for_turns = generate_turns_corpora_representations(corpus)
	for corpus_as_cs_levels_series in corpora_for_turns:
		test_tit_for_tat(corpus_as_cs_levels_series)