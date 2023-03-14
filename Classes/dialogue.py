class Dialogue(object):
	def __init__(self, name, turns, utterances, list_of_speakers):
		self.name = name
		self.turns = turns
		self.utterances = utterances
		self.list_of_speakers = list_of_speakers

	def __str__(self):
		s = ''
		for turn in self.turns:
			s += str(turn)
		return s
