import os
import langid
import json

LANGUAGES = ['en', 'es']
langid.set_languages(LANGUAGES)
MAJOR_LANGUAGE_CODES = {'en': 'E', 'es': 'S'}

from Auxiliaries.utils import load_words
"""
COMMON_WORDS = {'en': ['hi', 'bye', 'hello'],
                  'es': ['hola', 'adiós', 'hola']}

UNCOMMON_WORDS = {'en': ['lion', 'bear', 'edge', 'butterfly'],
                  'es': ['león', 'oso', 'borde', 'mariposa']}
"""


COMMON_WORDS = {'en': load_words('most_common_en_words_without_shared.txt'),
                  'es': load_words('most_common_es_words_without_shared.txt')}

UNCOMMON_WORDS = json.loads(open(os.path.join('Data', 'common_n_grams', 'translation_pairs.json'), 'r').read())


def test_classify():
		str = '¿Cómo se llega a la capital?'
		c = langid.classify(str)
		print(c)

def get_other_lang(lang):
	major_lang_index = LANGUAGES.index(lang)
	return LANGUAGES[major_lang_index-1]


def test_get_other_lang():
	lang = 'en'
	other_lang = get_other_lang(lang)
	print(lang + ": " + other_lang)
	lang = 'es'
	other_lang = get_other_lang(lang)
	print(lang + ": " + other_lang)

def check_phrasal_cs_presence(sentence, minor_lang):
	tokens = sentence.split()
	if len(tokens)<=2:
		return False
	else:
		for n in range(len(tokens)-2):
			triplet = ' '.join(tokens[n:n+3])
			if langid.classify(triplet)[0] == minor_lang:
				return True
	return False


def check_lexical_cs_presence(sentence, minor_lang):
	tokens = sentence.split()
	for token in tokens:
		if token in UNCOMMON_WORDS[minor_lang]:
			return True
	return False


def check_frozen_expression_cs_presence(sentence, minor_lang):
	tokens = sentence.split()
	for token in tokens:
		if token in COMMON_WORDS[minor_lang]:
			return True
	return False


def test_check_phrasal_cs_presence():
	sentence='quiero saltar y cantar de joy'
	minor_lang='eng'
	res = check_phrasal_cs_presence(sentence, minor_lang)


def calc_cs_level_for_str(sentence):
	major_lang = langid.classify(sentence)[0]
	major_lang_code = MAJOR_LANGUAGE_CODES[major_lang]
	minor_lang = get_other_lang(major_lang)
	if check_phrasal_cs_presence(sentence, minor_lang):
		minor_lang_code = 'P'
	elif check_lexical_cs_presence(sentence, minor_lang):
		minor_lang_code = 'L'
	elif check_frozen_expression_cs_presence(sentence, minor_lang):
		minor_lang_code = 'T'
	else:
		minor_lang_code = 'N'
	return major_lang_code+minor_lang_code


def test_calc_cs_level_for_str():
	sentence = '¿Cómo se llega a la capital?'
	cs_level = calc_cs_level_for_str(sentence)
	print(sentence + " (" + cs_level + ")")

	sentence = 'tambien hay una una tienda en colombia que se llama azucar which translates to sugar'
	cs_level = calc_cs_level_for_str(sentence)
	print(sentence + " (" + cs_level + ")")

	sentence = 'entonces ya para cerrar la conversacion que como tu te sientes con tu familia'
	cs_level = calc_cs_level_for_str(sentence)
	print(sentence + " (" + cs_level + ")")


	sentence = 'well i love spending time with you guys you know'
	cs_level = calc_cs_level_for_str(sentence)
	print(sentence + " (" + cs_level + ")")

def run_tests():
	test_classify()
	test_calc_cs_level_for_str()
	test_get_other_lang()
	test_check_phrasal_cs_presence()

if __name__ == '__main__':
	run_tests()
	print("Finished!")