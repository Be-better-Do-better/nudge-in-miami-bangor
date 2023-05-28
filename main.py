import os

from Auxiliaries.data_loaders import collect_corpus
from CorpusAnalyses.run_analysis import analyse_corpus
from LanguageAnalysis.collect_samples import collect_samples_by_utterances

MIAMI_BANGOR_CORPUS_NAME = "Miami-Bangor"
MIAMI_BANGOR_CORPUS_ROOT_DIR = os.path.join(os.getcwd(), 'Data', 'bangor_raw_without_maria')


def main():
	miami_bangor_corpus = collect_corpus(corpus_name=MIAMI_BANGOR_CORPUS_NAME, root_dir=MIAMI_BANGOR_CORPUS_ROOT_DIR)
	print(miami_bangor_corpus)
	analyse_corpus(miami_bangor_corpus)

	# compare_predictors_on_corpus(miami_bangor_corpus)
	# run_test_hypothesis(miami_bangor_corpus)
	# nudge_occurrence_testing(miami_bangor_corpus)
	# tit_for_tat_occurrence_testing(miami_bangor_corpus)
	# analyse_cs_level_classifier(miami_bangor_corpus)

	# collect samples of Utterances for each CS level:
	# collect_samples_by_utterances(miami_bangor_corpus)


if __name__ == '__main__':
	main()
	print("Finished!")
