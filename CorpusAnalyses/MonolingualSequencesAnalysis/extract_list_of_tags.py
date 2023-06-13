from Classes.corpus import Corpus


def extract_list_of_tags(corpus: Corpus, tagging_function: callable, by_utterances: bool = True) -> list[list[str]]:
	"""
	This function returns a list of tags for each dialogue in the corpus.
	:param corpus:
	:param tagging_function: for example: return major-language
	:param by_utterances: True if utterances, False if turns
	:return: a list of lists: a list for each dialogue
	"""
	if by_utterances:  # Use Utterances
		return [[tagging_function(utterance) for utterance in dialogue.utterances] for dialogue in corpus.dialogues]
	else:  # use Turns
		return [[tagging_function(turn) for turn in dialogue.turns] for dialogue in corpus.dialogues]
