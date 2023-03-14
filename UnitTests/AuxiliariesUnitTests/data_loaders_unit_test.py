import os
os.chdir('..')

from Auxiliaries.data_loaders import collect_all_utterances, aggregate_utterances_to_turns, collect_list_of_speakers, collect_dialogue, collect_corpus

def test_aggregate_utterances_to_turns():
    root_dir = os.path.join(os.getcwd(), 'Data', 'bangor_raw')
    filename = 'herring1.csv'
    list_of_utterances = collect_all_utterances(root_dir, filename)
    list_of_turns = aggregate_utterances_to_turns(list_of_utterances)
    print(filename + ' has {} turns'.format(len(list_of_turns)))

def test_collect_list_of_speakers():
    root_dir = os.path.join(os.getcwd(), 'Data', 'bangor_raw')
    filename = 'herring1.csv'
    list_of_utterances = collect_all_utterances(root_dir, filename)
    list_of_turns = aggregate_utterances_to_turns(list_of_utterances)
    list_of_speakers = collect_list_of_speakers(list_of_turns)
    print(filename + ' has {} turns'.format(len(list_of_turns)))
    print('list of speakers include:')
    print(list_of_speakers)

def test_collect_dialogue():
    root_dir = os.path.join(os.getcwd(), 'Data', 'bangor_raw_reduced')
    filename = 'herring1_cgwords.csv'
    dialogue = collect_dialogue(root_dir, filename)
    print(dialogue)

def test_collect_corpus():
    corpus_name = 'Miami-Bangor Reduced'
    root_dir = os.path.join(os.getcwd(), '../Data', 'bangor_raw_reduced')
    c1 = collect_corpus(corpus_name, root_dir)
    print(c1)

if __name__ == '__main__':
	test_collect_list_of_speakers()
	test_collect_corpus()
	test_collect_dialogue()
