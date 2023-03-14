import os
os.chdir('../..')
from Auxiliaries.data_loaders import collect_corpus
from CorpusAnalyses.corpus_analyses import collect_languages, langid_classify, analyse_langid_results, analyse_cs_level_classifier, analyses_cs_bigrams_distribution
from CorpusAnalyses.distances_between_events_in_boolean_sequences_analysis import extract_distances, calc_frequency, calc_relative_frequency, calc_hazards, generate_series, relative_frequency_comparison, plot_relative_frequency
from CorpusAnalyses.run_analysis import analyse_corpus


REDUCED_MIAMI_BANGOR_CORPUS = collect_corpus(corpus_name='Reduced-Miami-Bangor',
										 root_dir=os.path.join(os.getcwd(), 'Data', 'bangor_raw_reduced'))

def test_collect_languages():
	all_found_languages = collect_languages(REDUCED_MIAMI_BANGOR_CORPUS)
	print(all_found_languages)

def test_langid_classify():
	t1 = 'Hello to you all...'
	r1 = langid_classify(t1)
	print(r1)
	t2 = 'Quién es el tonto que escribió todas estas tonterías.'
	r2 = langid_classify(t2)
	print(r2)

def test_analyse_langid_results():
	analyse_langid_results(REDUCED_MIAMI_BANGOR_CORPUS)


def test_analyse_corpus():
	analyse_corpus(REDUCED_MIAMI_BANGOR_CORPUS)

def test_analyse_cs_level_classifier():
	analyse_cs_level_classifier(REDUCED_MIAMI_BANGOR_CORPUS)

def test_analyses_cs_bigrams_distribution():
	analyses_cs_bigrams_distribution(REDUCED_MIAMI_BANGOR_CORPUS)

def test_extract_distances():
	boolean_series = [True, False, True, True, False, True]
	distances_between_true = extract_distances(boolean_series)

def test_calc_frequency():
	d = [1, 2, 1, 3, 1]
	f = calc_frequency(d)
	print(f)

def test_calc_relative_frequency():
	print("test_calc_relative_frequency:")
	distances = [1, 1, 3]
	print(distances)
	f = calc_frequency(distances=distances)
	r = calc_relative_frequency(frequency_counter=f)
	print(r)

def test_calc_hazard():
	print("test_calc_hazard")
	r = [0.0, 0.6666666666666666, 0.0, 0.3333333333333333]
	print(r)
	h = calc_hazards(r)
	print(h)

def test_generate_series():
	print("test_generate_series")
	f = [0, 3, 2, 1, 0, 1]
	r = calc_relative_frequency(f)
	h = calc_hazards(r)
	s = generate_series(h, n=10, d=1)
	print(s)

def test_relative_frequency_comparison():
	r1 = [0, 4, 3, 2, 1, 0]
	r2 = [0, 5, 2, 3, 0, 1]
	relative_frequency_comparison(r1, r2)

def test_plot_relative_frequency():
	f = [0, 4, 3, 2, 1, 0]
	r = calc_relative_frequency(f)
	plot_relative_frequency(r)

def test_full_cycle():
	s0 = [True, False, False, True, True, False]
	d0 = extract_distances(s0)
	f0 = calc_frequency(d0)
	r0 = calc_relative_frequency(f0)
	h0 = calc_hazards(r0)
	s1 = generate_series(h0, n=100000, d=1)
	d1 = extract_distances(s1)
	f1 = calc_frequency(d1)
	r1 = calc_relative_frequency(f1)
	relative_frequency_comparison(r0, r1)

def run_tests():
	test_analyse_corpus()
	test_collect_languages()
	test_langid_classify()
	test_analyse_langid_results()
	test_analyse_cs_level_classifier()

	test_analyses_cs_bigrams_distribution()

	test_extract_distances()
	test_calc_frequency()
	test_calc_relative_frequency()
	test_calc_hazard()
	test_generate_series()
	test_relative_frequency_comparison()
	test_plot_relative_frequency()
	test_full_cycle()

if __name__ == '__main__':
	run_tests()