from Classes.corpus import Corpus
from Classes.hypothesis import Hypothesis
from Classes.corpus_cs_levels_series_representation import CorpusCSSeries
from Auxiliaries.report import Report
from Hypotheses.hypotheses import generate_hypotheses
from CorpusAnalyses.analyse_hypotheses_proportions import analyse_hypothesis_proportion
from Auxiliaries.utils import SIGNIFICANCE_LEVEL

def generate_hypotheses_testing_report(corpus: Corpus, by_utterances: bool = True) -> Report:
	def generate_report_head():
		report_content = ''
		report_content += '\\begin{table}\n'
		report_content += '\\begin{center}\n'
		report_content += '\\begin{tabular}{|c|c|c|c|}\n'
		report_content += '\\hline\n'
		report_content += '\\hline\n'
		# report_content += '\\multirow{2}{*}{Hypotheses} & \\multicolumn{2}{c|}{Accuracy} & c \\\\\n'
		# report_content += '\\cline{2-3}\n'
		# report_content += '& Corpus & Random \\\\\n'
		report_content +=  'Hypothesis & $p_{measured}$ (95\%CI) & $p_{expected}$ & p-value \\\\\n'
		report_content += '\\hline \\hline\n'

		return report_content

	report_content = generate_report_head()

	hypotheses = generate_hypotheses()

	for hypothesis in hypotheses:
		p_measured, lower_bound_of_95_confidence_level, upper_bound_of_95_confidence_level, p_expected, p_value = \
			analyse_hypothesis_proportion(corpus, hypothesis, utterances=by_utterances)

		report_content += hypothesis.name + f" & {p_measured :3.3f} ({lower_bound_of_95_confidence_level :3.3f}, " \
		                                    + f"{upper_bound_of_95_confidence_level :3.3f}) & {p_expected: 3.3f} & {p_value: 2.2e}"
		if p_value < SIGNIFICANCE_LEVEL:
			report_content += "*"
		report_content += ' \\\\\n'  # between different hypotheses
		report_content += '\\hline\n'

	report_content += '\\end{tabular}\n'
	report_content += '\\end{center}\n'

	if by_utterances:
		report_content += '\\caption{Hypotheses Testing by Utterances}\n'
		report_content += '\\label{table:hypotheses-testing-table-by-utterances}\n'
	else:
		report_content += '\\caption{Hypotheses Testing by Turns}\n'
		report_content += '\\label{table:hypotheses-testing-table-by-turns}\n'
	report_content += '\\end{table}\n'

	report_title = 'Hypotheses Testing Results'
	if by_utterances:
		report_filename = 'hypotheses_testing_by_utterances.txt'
	else:
		report_filename = 'hypotheses_testing_by_turns.txt'
	Report(report_title, report_filename, report_content)
