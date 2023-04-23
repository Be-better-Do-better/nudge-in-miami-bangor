import os
import matplotlib.pyplot as plt

from Classes.corpus import Corpus
from Classes.utterance import Utterance
from Auxiliaries.utils import FOLDER_OF_FIGURES, PURE_CS_LEVELS_OPTIONS

def tag_utterances(corpus: Corpus, tagging_function) -> list[list[str]]:
	return [[tagging_function(utterance) for utterance in dialogue.utterances]
							for dialogue in corpus.dialogues]

def get_list_of_tags(lists_of_list_of_tag_series: list[list[str]]) -> list:
	flat_list = [tag for sublist in lists_of_list_of_tag_series for tag in sublist]
	return list(set(flat_list))

def subsequences_lengths_extractor(tags_sequence_extracted: list[str]) -> list[(str, int)]:
	"""
	This function "squoshes" the sub-sequences of mono-lingual tags into pairs of (tag, length of sub-sequence).
	e.g.: the sequence: ['eng', 'eng', 'spa'] will be squoshed into [('eng', 2), ('spa', 1)]
	:param tags_sequence_extracted:
	:return: list of (tag, sub-sequence length)
	"""
	tags_sequence_squoshed = []
	i = 0
	current_subsequence_length = 0
	prev_tag = None
	while i < len(tags_sequence_extracted):
		curr_tag = tags_sequence_extracted[i]
		if (prev_tag is None) or (curr_tag == prev_tag):
			current_subsequence_length += 1
		else:
			tags_sequence_squoshed.append((prev_tag, current_subsequence_length))
			current_subsequence_length = 1
		prev_tag = curr_tag
		i += 1

	if not(current_subsequence_length == 0):
		tags_sequence_squoshed.append((prev_tag, current_subsequence_length))
	return tags_sequence_squoshed

def get_frequency_of_lengths_of_subsequences(lists_of_list_of_tag_series: list[list[str]]) -> dict:
	temp_relative_frequency_of_subsequences = {}

	found_tags = get_list_of_tags(lists_of_list_of_tag_series)
	for tag in found_tags:
		temp_relative_frequency_of_subsequences[tag] = {}

	for tag_list in lists_of_list_of_tag_series:
		squoshed_tag_list = subsequences_lengths_extractor(tag_list)
		for tag, subsequence_length in squoshed_tag_list:
			if subsequence_length in temp_relative_frequency_of_subsequences[tag].keys():
				temp_relative_frequency_of_subsequences[tag][subsequence_length] += 1
			else:
				temp_relative_frequency_of_subsequences[tag][subsequence_length] = 1

	relative_frequency_of_subsequences = {}
	for tag in found_tags:
		relative_frequency_of_subsequences[tag] = convert_to_frequency_vector(temp_relative_frequency_of_subsequences[tag])
	return relative_frequency_of_subsequences

def convert_to_frequency_vector(frequency_counter: dict) -> list:
	max_key = max(frequency_counter.keys())
	frequency_vector = [0 for _ in range(max_key+1)]
	for i, frequency in frequency_counter.items():
		frequency_vector[i] = frequency
	return frequency_vector

def get_sorted_list_of_tags(frequency_of_lengths_of_subsequences: dict) -> list[str]:
	list_of_tag_sum_tuples = []
	for tag, tag_freq in frequency_of_lengths_of_subsequences.items():
		list_of_tag_sum_tuples.append((tag, sum([i*tag_freq[i] for i in range(len(tag_freq))])))
	list_of_tag_sum_tuples.sort(key=(lambda x: x[1]), reverse=True) # sort by second
	return [item[0] for item in list_of_tag_sum_tuples]

def get_random_expected_values(frequency_of_lengths_of_subsequences: dict) -> dict:
	"""This function returns the expected # of relative sub-sequences of a specific language tag,
	if the distribution was completely random"""
	# Get total sum of utterances/turns:
	total_sum = 0
	sum_of_tag = {}

	for current_tag, frequency_of_lengths_of_subsequences_of_current_tag in frequency_of_lengths_of_subsequences.items():
		sum_of_current_tag =\
			sum([i*frequency_of_lengths_of_subsequences_of_current_tag[i] for i in range(len(frequency_of_lengths_of_subsequences_of_current_tag))])
		sum_of_tag[current_tag] = sum_of_current_tag

		total_sum += sum_of_current_tag

	# Calc probability of each language tag:
	if total_sum > 0:
		probability_of_tags = {}
		for current_tag, current_sum_of_tag in sum_of_tag.items():
			probability_of_tags[current_sum_of_tag] = sum_of_current_tag / total_sum

	# Calculate Results:
	res = {}
	for current_tag, frequency_of_lengths_of_subsequences_of_current_tag in frequency_of_lengths_of_subsequences.items():
		p = probability_of_tags[current_sum_of_tag]
		sum_of_current_tag = sum_of_tag[current_tag]
		# normalization_factor = sum([(1-p)*p**(s-1)*s for s in range(1, len(frequency_of_lengths_of_subsequences_of_current_tag)+1)])
		normalization_factor = sum([(1-p)*p**(s-1)*s for s in range(1, len(frequency_of_lengths_of_subsequences_of_current_tag))])
		if normalization_factor > 0:
			# r = [sum_of_current_tag/normalization_factor*(1-p)*p**(s-1) for s in range(1, len(frequency_of_lengths_of_subsequences_of_current_tag)+1)]
			r = [sum_of_current_tag/normalization_factor*(1-p)*p**(s-1) for s in range(1, len(frequency_of_lengths_of_subsequences_of_current_tag))]
			# r.insert(0, 0)
			res[current_tag] = r.copy()

	# Check validity:
	after_sum_of_tags = {}
	for current_tag, frequency_of_lengths_of_subsequences_of_current_tag in res.items():
		sum_of_current_tag =\
			sum([i*frequency_of_lengths_of_subsequences_of_current_tag[i] for i in range(len(frequency_of_lengths_of_subsequences_of_current_tag))])
		after_sum_of_tags[current_tag] = sum_of_current_tag

	return res

def plot_frequency_of_lengths_of_subsequences(frequency_of_lengths_of_subsequences: dict,
											  title: str, figure_name: str) -> None:
	fig, ax = plt.subplots()
	sorted_list_of_tags = get_sorted_list_of_tags(frequency_of_lengths_of_subsequences)

	# for tag in frequency_of_lengths_of_subsequences.keys():
	for tag in sorted_list_of_tags:
		x = [i for i in range(0, len(frequency_of_lengths_of_subsequences[tag]))]
		ax.loglog(x, frequency_of_lengths_of_subsequences[tag], linestyle="None", marker='.', label=tag)

	# ax.autoscale(False, axis="x")
	# ax.autoscale(False, axis="y")
	# Expected results:
	expected_results = get_random_expected_values(frequency_of_lengths_of_subsequences)
	for tag in sorted_list_of_tags:
		x = [i for i in range(1, len(frequency_of_lengths_of_subsequences[tag]))]
		ax.loglog(x, expected_results[tag], linestyle="dashed", marker='_', label=tag+' randomly expected')

	ax.set_xlim(0.5, 5000)
	ax.set_ylim(0.5, 5000)
	plt.ylabel('# of occurances')
	plt.xlabel('sub-sequence length')
	plt.ylabel('Frequency')
	ax.legend()
	plt.title(title)

	plt.savefig(os.path.join(FOLDER_OF_FIGURES, figure_name))
	plt.show()

def tag_function_eng_spa_cs(utterance: Utterance) -> str:
	if utterance.cs_level in PURE_CS_LEVELS_OPTIONS:
		return 'CS'
	else:
		return utterance.major_lang

def analyse_frequency_of_lengths_of_subsequences(corpus: Corpus) -> None:
	
	# Analyse by major language (English/Spanish):
	lists_of_list_of_tag_series = tag_utterances(corpus, tagging_function=(lambda u: u.major_lang))
	frequency_of_lengths_of_subsequences = get_frequency_of_lengths_of_subsequences(lists_of_list_of_tag_series)
	plot_frequency_of_lengths_of_subsequences(frequency_of_lengths_of_subsequences,
											  title='Sub-Sequence Length Analysis',
											  figure_name='mono_lingual_major_subsequences_lengths_histogram.png')

	# Analyse by general language type (English/Spanish/CS):
	lists_of_list_of_tag_series = tag_utterances(corpus, tagging_function=tag_function_eng_spa_cs)
	frequency_of_lengths_of_subsequences = get_frequency_of_lengths_of_subsequences(lists_of_list_of_tag_series)
	plot_frequency_of_lengths_of_subsequences(frequency_of_lengths_of_subsequences,
											  title='Sub-Sequence Length Analysis',
											  figure_name='eng_spa_cs_subsequences_lengths_histogram.png')

	# Analyse by CS level (EN/ET/EL/EP/SP/SL/ST/SN):
	lists_of_list_of_tag_series = tag_utterances(corpus, tagging_function=(lambda u: u.cs_level))
	frequency_of_lengths_of_subsequences = get_frequency_of_lengths_of_subsequences(lists_of_list_of_tag_series)
	plot_frequency_of_lengths_of_subsequences(frequency_of_lengths_of_subsequences,
											  title='Sub-Sequence Length Analysis',
											  figure_name='cs_levels_subsequences_lengths_histogram.png')
