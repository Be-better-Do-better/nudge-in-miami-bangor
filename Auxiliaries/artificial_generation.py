from Classes.token import Token
from Classes.utterance import Utterance
from Classes.turn import Turn
from Classes.dialogue import Dialogue
from Classes.corpus import Corpus

def generate_token():
	return Token(surface='hi', lang='eng', speaker='NET')

def generate_utterance():
	"""
	speaker = 'NET'
	t1 = Token(surface='hi', lang='eng', speaker=speaker)
	t2 = Token(surface='amigo', lang='spa', speaker=speaker)
	t3 = Token(surface='adios', lang='spa', speaker=speaker)
	tokens = [t1, t2, t3]
	"""
	speaker = 'MOT'
	t1 = Token(surface='we', lang='eng', speaker=speaker)
	t2 = Token(surface='could', lang='eng', speaker=speaker)
	t3 = Token(surface='vamos', lang='spa', speaker=speaker)
	t4 = Token(surface='amigos', lang='eng&spa', speaker=speaker)
	t5 = Token(surface='?', lang='999', speaker=speaker)
	tokens = [t1, t2, t3, t4, t5]
	return Utterance(tokens=tokens, speaker=speaker)

def generate_utterance2():
	speaker = 'NET'
	t1 = Token(surface='entonces', lang='spa', speaker=speaker)
	t2 = Token(surface='ya', lang='spa', speaker=speaker)
	t3 = Token(surface='para', lang='spa', speaker=speaker)
	t4 = Token(surface='cerrar', lang='spa', speaker=speaker)
	t5 = Token(surface='la', lang='spa', speaker=speaker)
	t6 = Token(surface='conversacion', lang='spa', speaker=speaker)
	t7 = Token(surface='como', lang='spa', speaker=speaker)
	t8 = Token(surface='tu', lang='spa', speaker=speaker)
	t9 = Token(surface='te', lang='spa', speaker=speaker)
	t10 = Token(surface='sientes', lang='spa', speaker=speaker)
	t11 = Token(surface='con', lang='spa', speaker=speaker)
	t12 = Token(surface='tu', lang='spa', speaker=speaker)
	t13 = Token(surface='familia', lang='spa', speaker=speaker)

	tokens = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13]
	return Utterance(tokens=tokens, speaker=speaker)

def generate_turn():
	speaker = 'NET'
	utterances = []
	t1 = Token(surface='hi', lang='eng', speaker=speaker)
	t2 = Token(surface='adios', lang='spa', speaker=speaker)
	t3 = Token(surface='.', lang='999', speaker=speaker)
	tokens = [t1, t2, t3]
	utterances.append(Utterance(tokens=tokens, speaker=speaker))
	t1 = Token(surface='How', lang='eng', speaker=speaker)
	t2 = Token(surface='are', lang='spa', speaker=speaker)
	t3 = Token(surface='you', lang='eng', speaker=speaker)
	t4 = Token(surface='?', lang='999', speaker=speaker)
	tokens = [t1, t2, t3, t4]
	utterances.append(Utterance(tokens=tokens, speaker=speaker))

	return Turn(utterances=utterances, speaker=speaker)

def generate_dialogue():
	speaker1 = 'NET'
	speaker2 = 'ADV'

	all_utterances = []
	turns = []

	utterances = []
	t1 = Token(surface='Buenos', lang='spa', speaker=speaker1)
	t2 = Token(surface='d?as', lang='spa', speaker=speaker1)
	t3 = Token(surface='.', lang='999', speaker=speaker1)
	tokens = [t1, t2, t3]
	utterance1 = Utterance(tokens=tokens, speaker=speaker1)
	utterances.append(utterance1)
	all_utterances.append(utterance1)

	t1 = Token(surface='c?mo', lang='spa', speaker=speaker1)
	t2 = Token(surface='est?s', lang='spa', speaker=speaker1)

	tokens = [t1, t2]
	utterance2 = Utterance(tokens=tokens, speaker=speaker1)
	utterances.append(utterance2)
	all_utterances.append(utterance2)
	turn1 = Turn(utterances=utterances, speaker=speaker1)
	turns.append(turn1)

	utterances = []
	t1 = Token(surface='Hi', lang='eng', speaker=speaker2)
	t2 = Token(surface='there', lang='spa', speaker=speaker2)
	t3 = Token(surface='.', lang='999', speaker=speaker2)
	tokens = [t1, t2, t3]
	utterance3 = Utterance(tokens=tokens, speaker=speaker2)
	utterances.append(utterance3)
	all_utterances.append(utterance3)


	t1 = Token(surface='donde', lang='spa', speaker=speaker2)
	t2 = Token(surface='sigues', lang='spa', speaker=speaker2)
	t3 = Token(surface='ahora', lang='spa', speaker=speaker2)
	t4 = Token(surface='?', lang='999', speaker=speaker2)
	tokens = [t1, t2, t3, t4]
	utterance4 = Utterance(tokens=tokens, speaker=speaker1)
	utterances.append(utterance4)
	all_utterances.append(utterance4)
	turn2 = Turn(utterances=utterances, speaker=speaker2)
	turns.append(turn2)

	utterances = []
	t1 = Token(surface='looks', lang='eng', speaker=speaker1)
	t2 = Token(surface='great', lang='eng', speaker=speaker1)
	t3 = Token(surface='!', lang='999', speaker=speaker1)
	tokens = [t1, t2, t3]
	utterance4 = Utterance(tokens=tokens, speaker=speaker1)
	utterances.append(utterance4)
	all_utterances.append(utterance4)

	t1 = Token(surface='fine', lang='eng', speaker=speaker1)
	t2 = Token(surface='!', lang='999', speaker=speaker1)

	tokens = [t1, t2]
	utterance5 = Utterance(tokens=tokens, speaker=speaker1)
	utterances.append(utterance5)
	all_utterances.append(utterance5)
	turn3 = Turn(utterances=utterances, speaker=speaker1)
	turns.append(turn3)

	utterances = []
	t1 = Token(surface='good', lang='eng', speaker=speaker2)
	t2 = Token(surface='bye', lang='eng', speaker=speaker2)
	t3 = Token(surface='!', lang='999', speaker=speaker2)
	tokens = [t1, t2, t3]
	utterance6 = Utterance(tokens=tokens, speaker=speaker2)
	utterances.append(utterance6)
	all_utterances.append(utterance6)
	turn4 = Turn(utterances=utterances, speaker=speaker2)
	turns.append(turn4)

	list_of_all_speakers = [speaker1, speaker2]
	return Dialogue(name='test_dialogue', turns=turns, utterances=all_utterances, list_of_speakers=list_of_all_speakers)

def generate_corpus():
	corpus_name = 'artificial_corpus'
	dialogues = []
	num_of_dialogues = 3
	for _ in range(num_of_dialogues):
		dialogues.append(generate_dialogue())

	return Corpus(name=corpus_name, dialogues=dialogues)