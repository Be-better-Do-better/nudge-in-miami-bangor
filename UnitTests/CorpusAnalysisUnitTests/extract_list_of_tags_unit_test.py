import os
os.chdir('../..')

from Auxiliaries.data_loaders import collect_corpus
from CorpusAnalyses.MonolingualSequencesAnalysis.extract_list_of_tags import extract_list_of_tags


root_dir = os.path.join(os.getcwd(), 'Data', 'bangor_raw_reduced')
REDUCED_MIAMI_BANGOR_CORPUS = collect_corpus(corpus_name='Reduced-Miami-Bangor', root_dir=root_dir)



def test_extract_list_of_tags():
	list_of_utterances_tags = extract_list_of_tags(corpus=REDUCED_MIAMI_BANGOR_CORPUS, tagging_function=(lambda u: u.major_lang), use_utterances=True)
	print(list_of_utterances_tags)


if __name__ == '__main__':
	test_extract_list_of_tags()
