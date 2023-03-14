from Classes.corpus import Corpus
from Hypotheses.hypothesis_test import HypothesisTest
from Hypotheses.hypothesis import Hypothesis
from Hypotheses.corpus_cs_levels_series_representation import CorpusCSSeries
from Hypotheses.corpora_representations import generate_utterances_corpora_representations, generate_turns_corpora_representations
from Hypotheses.hypotheses import generate_hypotheses
from Hypotheses.reports_generation import generate_hypothesis_test_per_corpus_report, generate_all_hypotheses_reports

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
	list_of_sample_inclusion_probabilities = [1.0] # [0.01, 0.1, 1.0]
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
	generate_all_hypotheses_reports(dict_of_hypothesis_tests_for_turns)
