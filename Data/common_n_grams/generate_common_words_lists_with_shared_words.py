import codecs

def load_words(filename):
	with open(filename) as f:
		txt_str = f.read()
		list_of_words = txt_str.split()
		print(list_of_words)
	f.close()
	return list_of_words

def save_words(list_of_words, filename):
	text_to_write = '\n'.join(list_of_words)
	with codecs.open(filename, 'w', "utf-8") as f:
		f.write(text_to_write)
	f.close()

def test_save_words():
	list_of_words = ['hi', 'bye']
	filename = 'check.txt'
	save_words(list_of_words, filename)

def test_load_words():
	filename = 'most_common_1000_eng_words.txt'
	load_words(filename)

def create_word_lists_of_words_without_shared_words():
	words_in_english = load_words('most_common_1000_eng_words.txt')
	words_in_spanish = load_words('most_common_1000_spa_words.txt')

	words_in_english_without_shared = []
	for word in words_in_english:
		if word not in words_in_spanish:
			words_in_english_without_shared.append(word)

	save_words(words_in_english_without_shared, 'most_common_en_words_without_shared.txt')

	words_in_spanish_without_shared = []
	for word in words_in_spanish:
		if word not in words_in_english:
			words_in_spanish_without_shared.append(word)
	save_words(words_in_spanish_without_shared, 'most_common_es_words_without_shared.txt')

	print("# of words in English without shared = {}".format(len(words_in_english_without_shared)))
	print("# of words in Spanish without shared = {}".format(len(words_in_spanish_without_shared)))
	print(words_in_english_without_shared)
	print(words_in_spanish_without_shared)

def run_tests():
	test_save_words()
	test_load_words()

if __name__ == '__main__':
	create_word_lists_of_words_without_shared_words()
	print("success!")
