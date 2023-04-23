import codecs
import os.path

from Classes.corpus import Corpus
from collections import Counter


def get_most_common_1_grams(corpus: Corpus, lang: str, k=1000) -> list[str]:
	"""
	:param corpus: Corpus to analyse
	:param lang: language to analyse
	:param k: length of required list (default = 1000)
	:return: list of most common unigrams
	"""
	unigram_counter = Counter()
	for dialogue in corpus.dialogues:
		for utterance in dialogue.utterances:
			for token in utterance.tokens:
				if token.well_defined_lang == lang:
					unigram_counter.update([token.surface])

	list_of_most_common = unigram_counter.most_common(n=k)
	return [x[0] for x in list_of_most_common]


def get_most_common_bigrams(corpus: Corpus, lang: str, k=1000) -> list[str]:
	"""
	:param corpus: Corpus to analyse
	:param lang: language to analyse
	:param k: length of required list
	:return: list of most common bigrams
	"""
	bigrams_counter = Counter()
	for dialogue in corpus.dialogues:
		for utterance in dialogue.utterances:
			for i in range(len(utterance.tokens)-1):
				t1 = utterance.tokens[i]
				t2 = utterance.tokens[i+1]
				if (t1.well_defined_lang == lang) and (t2.well_defined_lang == lang):
					bigrams_counter.update([t1.surface + ' ' + t2.surface])

	list_of_most_common = bigrams_counter.most_common(n=k)
	return [x[0] for x in list_of_most_common]


def get_most_common_trigrams(corpus: Corpus, lang: str, k=1000) -> list[str]:
	"""
	:param corpus: Corpus to analyse
	:param lang: language to analyse
	:param k: length of required list
	:return: list of most common bigrams
	"""
	trigrams_counter = Counter()
	for dialogue in corpus.dialogues:
		for utterance in dialogue.utterances:
			for i in range(len(utterance.tokens)-2):
				t1 = utterance.tokens[i]
				t2 = utterance.tokens[i+1]
				t3 = utterance.tokens[i+1]
				if (t1.well_defined_lang == lang) and (t2.well_defined_lang == lang) and (t3.well_defined_lang == lang):
					trigrams_counter.update([t1.surface + ' ' + t2.surface + ' ' + t3.surface])

	list_of_most_common = trigrams_counter.most_common(n=k)
	return [x[0] for x in list_of_most_common]


def get_most_common_n_grams(corpus: Corpus, lang: str, n: int, k=1000) -> list[str]:
	"""
	:param corpus: Corpus to analyse
	:param lang: language to analyse
	:param n: n-gram (1=unigram, 2=bigram, 3=trigram)
	:param k: length of required list
	:return: a list of k-most common tokens types in the corpus
	"""

	if n == 1:
		return get_most_common_1_grams(corpus, lang, k)
	elif n == 2:
		return get_most_common_bigrams(corpus, lang, k)
	elif n == 3:
		return get_most_common_trigrams(corpus, lang, k)
	else:
		return []


def save_most_common_n_grams(most_common_n_grams: list[str], path: str, filename: str) -> None:
	f = codecs.open(os.path.join(path, filename), 'w', encoding='utf-8')
	f.write('\n'.join(most_common_n_grams))
	f.close()

