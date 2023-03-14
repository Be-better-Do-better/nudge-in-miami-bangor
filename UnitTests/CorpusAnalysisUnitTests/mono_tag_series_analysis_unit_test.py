import os
import random

os.chdir('../..')
from Auxiliaries.data_loaders import collect_corpus
from CorpusAnalyses.mono_tag_series_analysis import tag_utterances, get_list_of_tags, subsequences_lengths_extractor, analyse_frequency_of_lengths_of_subsequences, get_random_expected_values



REDUCED_MIAMI_BANGOR_CORPUS = collect_corpus(corpus_name='Reduced-Miami-Bangor',
										 root_dir=os.path.join(os.getcwd(), 'Data', 'bangor_raw_reduced'))


def test_tag_utterances():
	l2 = tag_utterances(corpus=REDUCED_MIAMI_BANGOR_CORPUS, tagging_function=(lambda u: u.major_lang))
	print(l2)
	tags = get_list_of_tags(l2)
	print(tags)
	l3 = tag_utterances(corpus=REDUCED_MIAMI_BANGOR_CORPUS, tagging_function=(lambda u: u.cs_level))
	print(l3)
	tags = get_list_of_tags(l3)
	print(tags)

def test_subsequences_lengths_extractor():
	tag_sequence = random.choices(['eng', 'spa'], weights=[0.6, 0.4], k=10)
	print(tag_sequence)
	res = subsequences_lengths_extractor(tag_sequence)
	print(res)

def test_analyse_frequency_of_lengths_of_subsequences():
	analyse_frequency_of_lengths_of_subsequences(REDUCED_MIAMI_BANGOR_CORPUS)

def test_get_random_expected_values():
	frequency_of_lengths_of_subsequences = {}
	frequency_of_lengths_of_subsequences['eng'] = [0, 2]
	frequency_of_lengths_of_subsequences['spa'] = [0, 3, 2, 1]
	get_random_expected_values(frequency_of_lengths_of_subsequences, tag='eng')

def run_tests():
	# test_tag_utterances()
	# test_subsequences_lengths_extractor()
	# test_analyse_frequency_of_lengths_of_subsequences()
	test_get_random_expected_values()

if __name__ == '__main__':
	run_tests()