class Corpus(object):
	def __init__(self, name, dialogues):
		self.name = name
		self.dialogues = dialogues

	def __str__(self):
		s = "The corpus " + self.name + " has {} dialogues".format(len(self.dialogues))
		return s
