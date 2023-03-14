import os
from abc import ABC
from Auxiliaries.utils import FOLDER_OF_SAMPLES

class Sample(ABC):
	def __init__(self, sample_title, sample_filename=None):
		self.sample_title = sample_title
		self.sample_filename = sample_filename

		self.sample_content = self.sample_title + '\n'*2

	def save_sample(self):
		if self.sample_filename is not None:
			with open(os.path.join(FOLDER_OF_SAMPLES, self.sample_filename), 'w') as f:
				f.write(self.sample_content)
				f.close()

	def add_to_content(self, addition):
		self.sample_content += addition + '\n'

	def add_subtitle(self, subtitle: str):
		self.sample_content += '\n*' + subtitle + '*'+ '\n'