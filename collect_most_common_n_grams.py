import os

from Auxiliaries.common_n_grams_collection import get_most_common_n_grams, save_most_common_n_grams
from Auxiliaries.utils import WELL_DEFINED_LANGUAGE_OPTIONS
from Auxiliaries.data_loaders import collect_corpus

MIAMI_BANGOR_CORPUS_NAME = "Miami-Bangor"
MIAMI_BANGOR_CORPUS_ROOT_DIR = os.path.join(os.getcwd(), 'Data', 'bangor_raw_without_maria')

NGRAMS_ROOT_DIR = os.path.join(os.getcwd(), 'Data', 'common_n_grams')

NGRAM_NAME = {1: 'unigram', 2: 'bigram', 3: 'trigram'}

miami_bangor_corpus = collect_corpus(corpus_name=MIAMI_BANGOR_CORPUS_NAME, root_dir=MIAMI_BANGOR_CORPUS_ROOT_DIR)
k = 1000  # required num of n-grams in most common list

for lang in WELL_DEFINED_LANGUAGE_OPTIONS:
	for n in [1, 2, 3]:
		filename = 'most_common_{}_'.format(k) + NGRAM_NAME[n] + 's_in_'.format(n) + lang + '.txt'
		most_common_n_grams = get_most_common_n_grams(miami_bangor_corpus, lang=lang, n=n)
		save_most_common_n_grams(most_common_n_grams, path=NGRAMS_ROOT_DIR, filename=filename)
