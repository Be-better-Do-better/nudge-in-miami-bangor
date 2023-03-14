import os
from collections import Counter

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import langid
langid.set_languages(['en', 'es'])

from LanguageAnalysis.str_cs_level_analysis import calc_cs_level_for_str
from CorpusAnalyses.distances_between_events_in_boolean_sequences_analysis import extract_distances, calc_frequency, calc_relative_frequency, plot_relative_frequency
from CorpusAnalyses.categorial_subsequences_length_analysis import collect_subsequence_frequencies, unite_subsequence_frequencies, plot_relative_frequency_comparison, calc_relative_frequency_of_tags
from Auxiliaries.report import Report
from Auxiliaries.utils import LANGID_CODES, WELL_DEFINED_LANGUAGE_OPTIONS, CS_LEVELS_OPTIONS, PURE_CS_LEVELS_OPTIONS, CS_LEVELS_DECODE

from Classes.corpus import Corpus

def collect_languages(corpus):
	all_found_languages = []
	for dialogue in corpus.dialogues:
		for utterance in dialogue.utterances:
			for token in utterance.tokens:
				lang = token.lang
				if (lang not in all_found_languages) and (lang in WELL_DEFINED_LANGUAGE_OPTIONS):
					all_found_languages.append(lang)

	return all_found_languages

def analyse_corpus_for_intra_sentential_cs(corpus):
	distances_between_intra_sentential_cs = []
	for dialogue in corpus.dialogues:
		does_utterance_contain_intra_sentential_cs = [u.contains_intra_sentential_cs for u in dialogue.utterances]
		distances_between_utterances_with_intra_sentential_cs_in_current_dialogue = \
			extract_distances(does_utterance_contain_intra_sentential_cs)
		distances_between_intra_sentential_cs.extend(
			distances_between_utterances_with_intra_sentential_cs_in_current_dialogue)

	frequency_of_intra_sentential_cs = calc_frequency(distances_between_intra_sentential_cs)
	relative_frequency_of_intra_sentential_cs = calc_relative_frequency(frequency_of_intra_sentential_cs)
	plot_title = "Relative Frequency for " + corpus.name + " IntRA-Sentential CS distances"
	plot_relative_frequency(relative_frequency_of_intra_sentential_cs, title=plot_title)

def analyse_corpus_for_inter_sentential_cs(corpus):
	language_tag_types_in_corpus = []
	language_tags_subsequence_length_frequency_in_corpus = {}
	for dialogue in corpus.dialogues:
		language_tags_of_utterances = [utterance.lang for utterance in dialogue.utterances if utterance.lang in WELL_DEFINED_LANGUAGE_OPTIONS]

		language_tags_subsequence_length_frequency_in_current_dialogue = \
			collect_subsequence_frequencies(language_tags_of_utterances)

		language_tags_subsequence_length_frequency_in_corpus = \
			unite_subsequence_frequencies(language_tags_subsequence_length_frequency_in_corpus,
										  language_tags_subsequence_length_frequency_in_current_dialogue)

	language_tags_subsequence_length_relative_frequency_in_corpus = calc_relative_frequency_of_tags(
		language_tags_subsequence_length_frequency_in_corpus)
	plot_relative_frequency_comparison(language_tags_subsequence_length_frequency_in_corpus,
									   title='Relative Comparison in Corpus',
									   required_tags=['eng', 'spa'])

def analyse_langid_results(corpus):
	lang_analysis_results = {}
	for l1 in ['eng', 'spa']:
		for l2 in ['eng', 'spa']:
			lang_analysis_results[l1, l2] = 0

	for dialogue in corpus.dialogues:
		for utterance in dialogue.utterances:
			utterance_as_text = str(utterance)
			major_lang = utterance.lang
			langid_identified_lang = langid_classify(utterance_as_text)
			lang_analysis_results[major_lang, langid_identified_lang] += 1
			if not(major_lang == langid_identified_lang):
				print("major: " + major_lang)
				print("langid: " + langid_identified_lang)
				print(utterance)
				print("*"*5)

	print(lang_analysis_results)

def langid_classify(text):
	classifier_result = langid.classify(text)
	return LANGID_CODES[classifier_result[0]]

def analyse_cs_level_classifier(corpus: Corpus) -> None:
	y_true = []
	y_pred = []
	for dialogue in corpus.dialogues:
		for utterance in dialogue.utterances:
			ground_truth_cs_level = utterance.cs_level
			cs_level_by_classifier = calc_cs_level_for_str(utterance.surface)

			y_true.append(ground_truth_cs_level)
			y_pred.append(cs_level_by_classifier)

			if not(ground_truth_cs_level == cs_level_by_classifier):
				print(utterance.surface)
				print("has cs level:" + ground_truth_cs_level)
				print("cs level by classifier:" + cs_level_by_classifier)

	cm = confusion_matrix(y_true, y_pred, labels=CS_LEVELS_OPTIONS)
	print(cm)
	disp = ConfusionMatrixDisplay(cm, display_labels=CS_LEVELS_OPTIONS)
	disp.plot()
	plt.savefig(os.path.join('Products', 'Figures', 'cs_labels_confusion_matrix.png'))
	# plt.show()

def analyse_raw_cs_levels_distribution(corpus: Corpus) -> None:
	c = Counter()
	for dialogue in corpus.dialogues:
		for utterance in dialogue.utterances:
			c.update([utterance.cs_level])
	total_sum = sum(c.values())
	text_to_write = ''
	for cs_level in CS_LEVELS_OPTIONS:
		text_to_write += cs_level + ': {} ({:.2f}%)\n'.format(c[cs_level], c[cs_level]/total_sum*100)

	Report(report_title='CS Levels Distribution in Utterances',
	           report_filename='cs_levels_distribution_in_utterances.txt',
	           report_content=text_to_write)

	total_sum = sum(c[cs_level] for cs_level in PURE_CS_LEVELS_OPTIONS)
	text_to_write = ''
	for cs_level in PURE_CS_LEVELS_OPTIONS:
		text_to_write += cs_level + ': {} ({:.2f}%)\n'.format(c[cs_level], c[cs_level]/total_sum*100)

	Report(report_title='Pure CS Levels Distribution in Utterances',
	       report_filename='pure_cs_levels_distribution_in_utterances.txt',
	       report_content=text_to_write)

	c = Counter()
	for dialogue in corpus.dialogues:
		for turn in dialogue.turns:
			c.update([turn.cs_level])

	total_sum = sum(c.values())
	sorted(c, key=c.get, reverse=True)
	text_to_write = ''
	for cs_level in c.keys():
		text_to_write += cs_level + ': {} ({:.2f}%)\n'.format(c[cs_level], c[cs_level]/total_sum*100)

	Report(report_title='CS Levels Distribution in Turns',
	       report_filename='cs_levels_distribution_in_turns.txt',
	       report_content=text_to_write)

def analyses_cs_bigrams_distribution(corpus: Corpus) -> None:
	c = Counter()
	for dialogue in corpus.dialogues:
		for n in range(len(dialogue.utterances)-1):
			c.update([(dialogue.utterances[n].cs_level, dialogue.utterances[n+1].cs_level)])

	total_sum = sum(c.values())
	text_to_write = '\\begin{table}\n'
	text_to_write += '\\begin{center}\n'
	text_to_write += '\\begin{tabular}{ |c||c|c|c|c|c|c|c|c| }\n'
	text_to_write += '\\hline\n'
	text_to_write += '1st / 2nd'

	for first_cs_level in CS_LEVELS_OPTIONS:
			text_to_write += ' & ' + first_cs_level
	text_to_write += '\\\\\n'
	text_to_write += '\\hline \\hline\n'
	for first_cs_level in CS_LEVELS_OPTIONS:
		text_to_write += first_cs_level
		for second_cs_level in CS_LEVELS_OPTIONS:
			text_to_write += ' & {} '.format(c[(first_cs_level, second_cs_level)])
		text_to_write += '\\\\\n'
		for second_cs_level in CS_LEVELS_OPTIONS:
			text_to_write += ' & ({:.2f}\%) '.format(c[(first_cs_level, second_cs_level)]/total_sum*100)
		text_to_write += '\\\\\n\\hline\n'

	text_to_write += '\n'
	text_to_write += '\\end{tabular}\n'
	text_to_write += '\\end{center}\n'
	text_to_write += '\\caption{CS Levels Bigrams Frequency}\n'
	text_to_write += '\\label{table:cs-levels-bigrams}\n'
	text_to_write += '\end{table}\n'



	Report(report_title='CS Levels Bigrams Distribution in Utterances',
	       report_filename='cs_levels_bigrams_distribution_in_utterances.txt',
	       report_content=text_to_write)

def get_cs_levels_distribution(corpus: Corpus, utterances=True) -> list[float]:
	cs_levels_distribution: list[int] = [0 for _ in CS_LEVELS_OPTIONS]

	for dialogue in corpus.dialogues:
		if utterances:
			for utterance in dialogue.utterances:
				cs_levels_distribution[CS_LEVELS_DECODE[utterance.cs_level]] += 1
		else: # in turns:
			for turn in dialogue.utterances:
				cs_levels_distribution[CS_LEVELS_DECODE[turn.cs_level]] += 1
	
	total_sum = sum(cs_levels_distribution)
	if total_sum > 0:
		for cs_level in range(len(CS_LEVELS_OPTIONS)):
			cs_levels_distribution[cs_level] = cs_levels_distribution[cs_level] / total_sum
	return cs_levels_distribution
