import os
from abc import ABC
from Auxiliaries.utils import FOLDER_OF_REPORTS

class Report(ABC):
	def __init__(self, report_title, report_filename=None, report_content=''):
		self.report_title = report_title
		self.report_filename = report_filename
		self.report_content = report_content

		self.__save_report()

	def __save_report(self):
		if self.report_filename is not None:
			with open(os.path.join(FOLDER_OF_REPORTS, self.report_filename), 'w') as f:
				f.write(self.report_title)
				f.write('\n'*2)
				f.write(self.report_content)