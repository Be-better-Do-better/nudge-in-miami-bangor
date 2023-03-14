from Auxiliaries.report import Report
from Hypotheses.hypotheses import generate_hypotheses

def test_hypotheses(list_of_series, probability_of_sample_inclusion=0.05, report_title='title', report_filename=None):
	hypotheses = generate_hypotheses(probability_of_sample_inclusion)
	what_to_write = ''
	for h in hypotheses:
		h.test(list_of_series, probability_of_sample_inclusion)
		print(h)
		what_to_write += str(h)
		what_to_write += '\n'*3
		# h.display_contingency_table()
		print('*'*10)

	Report(report_title=report_title, report_filename=report_filename, report_content=what_to_write)
