from Classes.corpus import Corpus
from Auxiliaries.utils import WELL_DEFINED_LANGUAGE_OPTIONS
from Auxiliaries.report import Report
from Hypotheses.hypotheses import generate_hypotheses
from CorpusAnalyses.NextLevelPredition.analyse_hypotheses_proportions import analyse_hypothesis_proportion
from Auxiliaries.utils import SIGNIFICANCE_LEVEL
from CorpusAnalyses.MonolingualSequencesAnalysis.analyse_monolingual_sequences import analyse_monolingual_sequences


def generate_monolingual_sequences_lengths_testing_report(corpus: Corpus, by_utterances: bool = True) -> Report:
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
		report_content +=  ' & $\\bar{s}_{measured}$ (95\%CI) & $s_{expected}$ & p-value \\\\\n'
		report_content += '\\hline \\hline\n'

		return report_content

	report_content = generate_report_head()

	for lang in WELL_DEFINED_LANGUAGE_OPTIONS:

		s_measured, lower_bound_of_95_confidence_level, upper_bound_of_95_confidence_level, s_expected, p_value = \
			analyse_monolingual_sequences(corpus, by_utterances=by_utterances, lang=lang)

		report_content += lang + f" & {s_measured :3.3f} ({lower_bound_of_95_confidence_level :3.3f}, " \
		                                    + f"{upper_bound_of_95_confidence_level :3.3f}) & {s_expected: 3.3f} & {p_value: 2.2e}"
		if p_value < SIGNIFICANCE_LEVEL:
			report_content += "*"
		report_content += ' \\\\\n'  # between different hypotheses
		report_content += '\\hline\n'

	report_content += '\\end{tabular}\n'
	report_content += '\\end{center}\n'

	if by_utterances:
		report_content += '\\caption{Monolingual Sequences Lengths Testing by Utterances}\n'
		report_content += '\\label{table:monolingual-sequences-lengths-testing-table-by-utterances}\n'
	else:
		report_content += '\\caption{Monolingual Sequences Lengths Testing by Turns}\n'
		report_content += '\\label{table:monolingual-sequences-lengths-testing-table-by-turns}\n'
	report_content += '\\end{table}\n'

	report_title = 'Monolingual Sequences Lengths Results'
	if by_utterances:
		report_filename = 'monolingual_sequences_length_testing_by_utterances.txt'
	else:
		report_filename = 'monolingual_sequences_length_testing_by_turns.txt'
	Report(report_title, report_filename, report_content)
