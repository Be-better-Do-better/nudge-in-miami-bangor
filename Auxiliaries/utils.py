import os
import codecs

LANGID_CODES = {'en': 'eng', 'es': 'spa'}

FOLDER_OF_PRODUCTS = os.path.join(os.getcwd(), 'Products')
FOLDER_OF_FIGURES = os.path.join(FOLDER_OF_PRODUCTS, 'Figures')
FOLDER_OF_REPORTS = os.path.join(FOLDER_OF_PRODUCTS, 'Reports')
FOLDER_OF_SAMPLES = os.path.join(FOLDER_OF_PRODUCTS, 'Samples')

PUNCTUATION_MARK_TAG = '999'
WELL_DEFINED_LANGUAGE_OPTIONS = ['eng', 'spa']

CS_LEVELS_OPTIONS = ['EN', 'ET', 'EL', 'EP', 'SP', 'SL', 'ST', 'SN']
PURE_CS_LEVELS_OPTIONS = ['ET', 'EL', 'EP', 'SP', 'SL', 'ST']
CS_LEVELS_DECODE = {'EN': 0, 'ET': 1, 'EL': 2, 'EP': 3, 'SP': 4, 'SL': 5, 'ST': 6, 'SN': 7}
MAJOR_LANGUAGE_ENCODE = {'eng': 'E', 'spa': 'S'}

MOST_COMMON_WORDS_IN_ENGLISH_FILE = 'most_common_1000_unigrams_in_eng.txt'
MOST_COMMON_WORDS_IN_SPANISH_FILE = 'most_common_1000_unigrams_in_spa.txt'

MOST_COMMON_BIGRAMS_IN_ENGLISH_FILE = 'most_common_1000_bigrams_in_eng.txt'
MOST_COMMON_BIGRAMS_IN_SPANISH_FILE = 'most_common_1000_bigrams_in_spa.txt'

MOST_COMMON_TRIGRAMS_IN_ENGLISH_FILE = 'most_common_1000_trigrams_in_eng.txt'
MOST_COMMON_TRIGRAMS_IN_SPANISH_FILE = 'most_common_1000_trigrams_in_spa.txt'

DIR_OF_MOST_COMMON_N_GRAMS = os.path.join('Data', 'common_n_grams')


def load_most_common_words_list(file_of_most_common_words, dir_of_most_common_words=DIR_OF_MOST_COMMON_N_GRAMS):
	list_of_common_words = []
	path_to_most_common_words = os.path.join(os.getcwd(), dir_of_most_common_words, file_of_most_common_words)
	splitting_delimiters = '|'  # '|'
	f = codecs.open(path_to_most_common_words, "r", "utf-8")
	temp_all_common_words_as_a_list = f.readlines()
	f.close()

	for a_word_or_two in temp_all_common_words_as_a_list:
		split_word = a_word_or_two.strip().split(splitting_delimiters)
		list_of_common_words.extend(split_word)

	return list_of_common_words


def load_words(filename):
	f = codecs.open(os.path.join('Data', 'common_n_grams', filename))
	t = f.read()
	f.close()
	s = t.split()
	return [w.lower() for w in s]