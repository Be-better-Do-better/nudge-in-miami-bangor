from Auxiliaries.utils import FOLDER_OF_SAMPLES, CS_LEVELS_OPTIONS
from Auxiliaries.sample import Sample
from Classes.corpus import Corpus

def collect_samples_by_utterances(corpus: Corpus) -> None:
	samples = {}
	for cs_level in CS_LEVELS_OPTIONS:
		samples[cs_level] = Sample(sample_title='Samples of ' + cs_level + ' utterances',
		                           sample_filename=cs_level + '_utterances.txt')

	for dialogue in corpus.dialogues:
		for cs_level in CS_LEVELS_OPTIONS:
			samples[cs_level].add_subtitle(dialogue.name)

		for utterance in dialogue.utterances:
			samples[utterance.cs_level].add_to_content(utterance.surface)

	for cs_level in CS_LEVELS_OPTIONS:
		samples[cs_level].save_sample()

def collect_samples_by_turns(corpus: Corpus) -> None:
	samples = {}
	for cs_level in CS_LEVELS_OPTIONS:
		samples[cs_level] = Sample(sample_title='Samples of ' + cs_level + ' utterances',
		                           sample_filename=cs_level + '_turns.txt')

	for dialogue in corpus.dialogues:
		for cs_level in CS_LEVELS_OPTIONS:
			samples[cs_level].add_subtitle(dialogue.name)

		for turn in dialogue.turns:
			samples[turn.cs_level].add_to_content(turn.surface)

	for cs_level in CS_LEVELS_OPTIONS:
		samples[cs_level].save_sample()
