from Classes.corpus import Corpus
from Classes.corpus_cs_levels_series_representation import CorpusCSSeries
from Auxiliaries.utils import CS_LEVELS_DECODE
from Hypotheses.random_cs_sequences_generation import generate_random_list_of_series
from CorpusAnalyses.corpus_analyses import get_cs_levels_distribution, get_dialogues_length


def generate_utterances_corpora_representations(corpus: Corpus) -> list[CorpusCSSeries]:
	list_of_cs_series_of_utterances = []
	for dialogue in corpus.dialogues:
		series_of_cs_levels_in_utterances = [CS_LEVELS_DECODE[utterance.cs_level] for utterance in dialogue.utterances]
		list_of_cs_series_of_utterances.append(series_of_cs_levels_in_utterances)

	list_of_random_cs_series_of_with_utterances_distribution = generate_random_list_of_series(
		get_cs_levels_distribution(corpus, utterances=True),
		get_dialogues_length(corpus, utterances=True))
	cs1 = CorpusCSSeries('utterances', list_of_cs_series_of_utterances)
	cs2 = CorpusCSSeries('random_utterances',
	                     list_of_random_cs_series_of_with_utterances_distribution)

	cs = [cs1, cs2]
	return cs


def generate_turns_corpora_representations(corpus: Corpus):
	list_of_cs_series_of_turns = []

	for dialogue in corpus.dialogues:
		series_of_cs_levels_in_turns = [CS_LEVELS_DECODE[turn.cs_level] for turn in dialogue.turns]
		list_of_cs_series_of_turns.append(series_of_cs_levels_in_turns)

	list_of_random_cs_series_of_with_turns_distribution = generate_random_list_of_series(
		get_cs_levels_distribution(corpus, utterances=False), get_dialogues_length(corpus, utterances=False))

	cs1 = CorpusCSSeries('turns', list_of_cs_series_of_turns)
	cs2 = CorpusCSSeries('random_turns',
	                     list_of_random_cs_series_of_with_turns_distribution)
	cs = [cs1, cs2]
	return cs
