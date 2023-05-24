from Classes.corpus import Corpus
from CorpusAnalyses.corpus_analyses import analyse_corpus_for_inter_sentential_cs, analyse_corpus_for_intra_sentential_cs, analyse_langid_results, analyse_raw_cs_levels_distribution, analyses_cs_bigrams_distribution
from CorpusAnalyses.mono_tag_series_analysis import analyse_frequency_of_lengths_of_subsequences
from CorpusAnalyses.analyse_nudge_proportion import analyse_nudge_proportion
from CorpusAnalyses.analyse_hypotheses_proportions import analyse_always_0_or_7_proportion, analyse_always_decreases_proportion


def analyse_corpus(corpus: Corpus):

	# distances between IntRA-Sentential CS
	analyse_corpus_for_intra_sentential_cs(corpus)

	# distances between IntER-Sentential CS
	analyse_corpus_for_inter_sentential_cs(corpus)

	# Sub-sequences Lengths
	analyse_frequency_of_lengths_of_subsequences(corpus)

	# langid analysis:
	analyse_langid_results(corpus)

	# cs levels distribution in corpus
	analyse_raw_cs_levels_distribution(corpus)

	# Finding cs-levels bigrams in corpus
	analyses_cs_bigrams_distribution(corpus)

	# Analyse nudge proportion
	analyse_nudge_proportion(corpus)

	# Analyse always 0 or 7 proportion
	analyse_always_0_or_7_proportion(corpus)

	# Analyse always decreases proportion
	analyse_always_decreases_proportion(corpus)
