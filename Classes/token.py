class Token(object):
	def __init__(self, surface, lang, speaker='OSE'):
		self.surface = surface
		self.lang = lang
		self.speaker = speaker
		self.well_defined_lang = None

	def __str__(self):
		s = "The token is: " + self.surface
		s += '\n'
		return s

	def set_well_defined_lang(self, selected_lang):
		self.well_defined_lang = selected_lang