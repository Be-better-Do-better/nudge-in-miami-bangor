from Classes.corpus_cs_levels_series_representation import CorpusCSSeries
from Auxiliaries.report import Report


def generate_hypothesis_test_per_corpus_report(hypotheses: list[Hypothesis],
                                               corpora: list[CorpusCSSeries],
                                               probabilities: list[float],
                                               dict_of_hts: dict,
                                               by_utterances: bool=True):
	required_values = [(lambda x: (x.relative_risk, x.relative_risk_confidence_level)),
	                   (lambda x: x.fisher_p_value),
	                   (lambda x: x.chi2_p_value)]
	required_values_names = ['relative risk', 'Fisher\'s p-value', 'chi-square p-value']

	report_content = ''
	report_content += '\\begin{table}\n'
	report_content += '\\begin{center}\n'
	report_content += '\\begin{tabular}{|c|c|c|c|c|c|c|}\n'
	report_content += '\\hline\n'
	report_content += '\\hline\n'
	report_content += '\\multirow{2}{*}{Hypotheses} & \\multicolumn{2}{c|}{Relative-Risk (95\\%CI)} & \multicolumn{2}{c|}{Fisher\'s p-value} & \multicolumn{2}{c|}{$\chi^2$ p-value} \\\\\n'
	report_content += '\\cline{2-7}\n'
	report_content += '& Corpus & Random & Corpus & Random & Corpus & Random \\\\\n'
	report_content += '\\hline \\hline\n'

	hypothesis_counter = 1

	get_name = (lambda x: x.name)
	# for corpus in corpora:
	#	report_content += get_name(corpus) + ' | '

	for hypothesis in hypotheses:
		# report_content += get_name(hypothesis) + ' | '
		report_content += "H{} ".format(hypothesis_counter)
		hypothesis_counter += 1

		for required_value_name, required_value in zip(required_values_names, required_values):
			# for required_value in required_values:
			for corpus in corpora:
				report_content += ''  # between results of different corpora:
				for p in probabilities:
					report_content += ''
					ht = dict_of_hts[(hypothesis, corpus, p)]
					val = required_value(ht)

					if type(val) is float:
						if val > 0.1:
							report_content += ' & {:2.2f}'.format(val)
						else:
							report_content += ' & {:1.2e}'.format(val)
					else:

						report_content += ' & {:2.2f} ({:2.2f}, {:2.2f})'.format(val[0], val[1][0], val[1][1])

		report_content += ' \\\\\n' # between different hypotheses
		report_content += '\\hline\n'

	report_content += '\\end{tabular}\n'
	report_content += '\\end{center}\n'
	if by_utterances:
		report_content += '\\caption{Hypotheses Testing by Utterances}\n'
		report_content += '\\label{table:hypotheses-table-by-utterances}\n'
	else:
		report_content += '\\caption{Hypotheses Testing by Turns}\n'
		report_content += '\\label{table:hypotheses-table-by-turns}\n'
	report_content += '\\end{table}\n'

	report_title = 'Corpora Comparison'
	if by_utterances:
		report_filename = 'corpora_comparison_by_utterances.txt'
	else:
		report_filename = 'corpora_comparison_by_turns.txt'
	Report(report_title, report_filename, report_content)


def generate_accuracy_hypothesis_test_per_corpus_report(hypotheses: list[Hypothesis],
                                               corpora: list[CorpusCSSeries],
                                               probabilities: list[float],
                                               dict_of_hts: dict,
                                               by_utterances: bool=True):
	required_values = [(lambda x: x.accuracy)]
	required_values_names = ['accuracy']

	report_content = ''
	report_content += '\\begin{table}\n'
	report_content += '\\begin{center}\n'
	report_content += '\\begin{tabular}{|c|c|c|}\n'
	report_content += '\\hline\n'
	report_content += '\\hline\n'
	report_content += '\\multirow{2}{*}{Hypotheses} & \\multicolumn{2}{c|}{Accuracy} \\\\\n'
	report_content += '\\cline{2-3}\n'
	report_content += '& Corpus & Random \\\\\n'
	report_content += '\\hline \\hline\n'

	hypothesis_counter = 1

	get_name = (lambda x: x.name)
	# for corpus in corpora:
	#	report_content += get_name(corpus) + ' | '

	for hypothesis in hypotheses:
		# report_content += get_name(hypothesis) + ' | '
		report_content += "H{} ".format(hypothesis_counter)
		hypothesis_counter += 1

		for required_value_name, required_value in zip(required_values_names, required_values):
			# for required_value in required_values:
			for corpus in corpora:
				report_content += ''  # between results of different corpora:
				for p in probabilities:
					report_content += ''
					ht = dict_of_hts[(hypothesis, corpus, p)]
					val = required_value(ht)

					if type(val) is float:
						if val > 0.1:
							report_content += ' & {:2.2f}'.format(val)
						else:
							report_content += ' & {:1.2e}'.format(val)
					else:

						report_content += ' & {:2.2f} ({:2.2f}, {:2.2f})'.format(val[0], val[1][0], val[1][1])

		report_content += ' \\\\\n' # between different hypotheses
		report_content += '\\hline\n'

	report_content += '\\end{tabular}\n'
	report_content += '\\end{center}\n'
	if by_utterances:
		report_content += '\\caption{Accuracy Testing by Utterances}\n'
		report_content += '\\label{table:accuracy-table-by-utterances}\n'
	else:
		report_content += '\\caption{Accuracy Testing by Turns}\n'
		report_content += '\\label{table:accuracy-table-by-turns}\n'
	report_content += '\\end{table}\n'

	report_title = 'Comparison of Accuracy in Corpora Comparison'
	if by_utterances:
		report_filename = 'accuracy_comparison_by_utterances.txt'
	else:
		report_filename = 'accuracy_comparison_by_turns.txt'
	Report(report_title, report_filename, report_content)
