import os
os.chdir('../..')


from CorpusAnalyses.MonolingualSequencesAnalysis.analyse_monolingual_sequences import analyse_monolingual_sequences
from Auxiliaries.data_loaders import collect_corpus
from Auxiliaries.utils import WELL_DEFINED_LANGUAGE_OPTIONS

# root_dir = os.path.join(os.getcwd(), 'Data', 'bangor_raw_reduced')
# REDUCED_MIAMI_BANGOR_CORPUS = collect_corpus(corpus_name='Reduced-Miami-Bangor', root_dir=root_dir)
root_dir = os.path.join(os.getcwd(), 'Data', 'bangor_raw_without_maria')
MIAMI_BANGOR_CORPUS = collect_corpus(corpus_name='Miami-Bangor', root_dir=root_dir)


def test_analyse_monolingual_sequences():
	# analyse_monolingual_sequences(corpus=REDUCED_MIAMI_BANGOR_CORPUS)
	for lang in WELL_DEFINED_LANGUAGE_OPTIONS:
		for by_utterances in [True, False]:
			# analyse_monolingual_sequences(corpus=MIAMI_BANGOR_CORPUS, by_utterances=by_utterances, lang=lang)
			s_measured, lower_bound_of_95_confidence_level, upper_bound_of_95_confidence_level, s_expected, p_value = \
				analyse_monolingual_sequences(corpus=MIAMI_BANGOR_CORPUS, by_utterances=by_utterances, lang=lang)
			print(f"s_measured = {s_measured :3.3f}")
			print(f"CI = [{lower_bound_of_95_confidence_level :3.3f}, {upper_bound_of_95_confidence_level :3.3f}]")
			print(f"s_expected = {s_expected :3.3f}")
			print(f"p_value = {p_value :3.3f}")


if __name__ == '__main__':
	test_analyse_monolingual_sequences()
	print("Test passed successfully!")

