import os
import matplotlib.pyplot as plt

from Classes.corpus import Corpus
from Classes.utterance import Utterance
from Auxiliaries.utils import FOLDER_OF_FIGURES, PURE_CS_LEVELS_OPTIONS, WELL_DEFINED_LANGUAGE_OPTIONS


def tag_utterances(corpus: Corpus, tagging_function) -> list[list[str]]:
	return [[tagging_function(utterance) for utterance in dialogue.utterances] for dialogue in corpus.dialogues]


def tag_turns(corpus: Corpus, tagging_function) -> list[list[str]]:
	return [[tagging_function(turn) for turn in dialogue.turns] for dialogue in corpus.dialogues]


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
	list_of_tag_sum_tuples.sort(key=(lambda x: x[1]), reverse=True)  # sort by second
	return [item[0] for item in list_of_tag_sum_tuples]


def get_random_expected_frequencies(frequency_of_lengths_of_subsequences: dict) -> dict:
	"""This function returns the expected # of relative sub-sequences of a specific language tag,
	if the distribution was completely random"""

	def get_p_L(f: dict) -> dict:
		"""f = frequency_of_lengths_of_subsequences (dict)
		has the format:
			f[L] = [0, f(1, L), f(2, L), ... ,f(n_L, L)]
			(list of ints which starts with 0, since the frequency of 0-length subsequence is 0)
			where L might be 'eng' or 'spa'
		and we return
		p['eng'] = probability of an English utterance/turn
		p['spa'] = probability of a Spanish utterance/turn
		"""
		# Get total sum of utterances/turns:
		total_sum = 0
		sum_of_tag = {}

		for current_tag, frequency_of_lengths_of_subsequences_of_current_tag in f.items():
			sum_of_current_tag =\
				sum([i*frequency_of_lengths_of_subsequences_of_current_tag[i] for i in range(len(frequency_of_lengths_of_subsequences_of_current_tag))])
			sum_of_tag[current_tag] = sum_of_current_tag

			total_sum += sum_of_current_tag

		# Calc probability of each language tag:
		if total_sum > 0:
			p_L = {}
			for current_tag, current_sum_of_tag in sum_of_tag.items():
				p_L[current_tag] = current_sum_of_tag / total_sum

		return p_L

	def get_N_L(f: dict) -> dict:
		"""This function returns the total number of sub-sequences
		WARNING: This is not equal to the number of utterances/turns!!!
		(every sub-sequence is counted only once!)
		e.g.:
		f['eng'] = [0, f(s=1, L='eng')=4, f(s=2, L='eng')=2, f(s=3, L='eng')=0, f(s=4, L='eng')=1]
		f['spa'] = [0, f(s=1, L='spa')=2, f(s=2, L='spa')=1]
		returns:
		N_L['eng'] = 7
		N_L['spa'] = 3
		"""
		N_L = {}
		for current_tag, frequency_of_lengths_of_subsequences_of_current_tag in f.items():
			sum_of_current_tag =\
				sum([frequency_of_lengths_of_subsequences_of_current_tag[i] for i in range(len(frequency_of_lengths_of_subsequences_of_current_tag))])
			N_L[current_tag] = sum_of_current_tag
		return N_L

	def get_n_L(f: dict) -> dict:
		"""This function returns the max length sub-sequence for each language tag
		WARNING: This is not equal to N_L (The total # of subsequences of any length for language L)
		e.g.:
		f['eng'] = [0, f(s=1, L='eng')=4, f(s=2, L='eng')=2, f(s=3, L='eng')=0, f(s=4, L='eng')=1]
		f['spa'] = [0, f(s=1, L='spa')=2, f(s=2, L='spa')=1]
		returns:
		n_L['eng'] = 4
		n_L['spa'] = 2
		"""
		n_L = {}
		for current_tag, frequency_of_lengths_of_subsequences_of_current_tag in f.items():
			n_L[current_tag] = len(frequency_of_lengths_of_subsequences_of_current_tag)-1
		return n_L

	def get_sigma_L(p_L: dict, n_L:dict) -> dict:
		sigma_L = {}

		for tag in p_L.keys():
			p = p_L[tag]
			n = n_L[tag]
			sigma_L[tag] = sum([(1-p)*p**s for s in range(1, n+1)])
		return sigma_L

	def get_infinite_sum_probability(p_L: dict, n_L:dict) -> dict[list]:
		"""
		This function returns a vector for each language tag.
		p(s, L) = p_L**(s-1)*(1-p_L) for s=1, 2, ..., n_L
		for L = 'eng', 'spa'
		:return:
		"""
		p_s_L = {}
		for tag in p_L.keys():
			p = p_L[tag]
			n = n_L[tag]
			p_s_L[tag] = [p**(s-1)*(1-p) for s in range(n)]
		return p_s_L

	def get_finite_sum_probability(sigma_L: dict, p_s_L: dict) -> dict:
		p_s_L_tilde = {}
		for tag in sigma_L.keys():
			sigma = sigma_L[tag]
			p_s_L_vector = p_s_L[tag]
			if sigma > 0:
				p_s_L_tilde[tag] = [p_s_L_vector[i]/sigma for i in range(len(p_s_L_vector))]

		return p_s_L_tilde

	def get_expected_values(p_s_L_tilde: dict, N_L:dict) -> dict:
		expected_frequency = {}
		for tag in p_s_L_tilde.keys():
			N_L_value = N_L[tag]
			p_s_L_tilde_values = p_s_L_tilde[tag]
			expected_frequency[tag] = [N_L_value*val for val in p_s_L_tilde_values]
		return expected_frequency

	p_L = get_p_L(frequency_of_lengths_of_subsequences)
	N_L = get_N_L(frequency_of_lengths_of_subsequences)
	n_L = get_n_L(frequency_of_lengths_of_subsequences)
	sigma_L = get_sigma_L(p_L, n_L)
	p_s_L = get_infinite_sum_probability(p_L, n_L)
	p_s_L_tilde = get_finite_sum_probability(sigma_L, p_s_L)

	return get_expected_values(p_s_L_tilde, N_L)


def plot_frequency_of_lengths_of_subsequences(frequency_of_lengths_of_subsequences: dict,
											  title: str, figure_name: str) -> None:
	def get_tag_first_letter(tag: str) -> str:
		""" This function replaces:
			eng -> E
			spa -> S
			as in paper
		"""
		return tag[0].upper()

	def get_measured_tag_label(tag: str) -> str:
		""" This replaces:
		eng -> f(s, E) - measured
		spa -> f(s, S) - measured
		as in paper
		or:
		EN -> f(s, EN) - measured
		ET -> f(s, ET) - measured
		...
		SN -> f(s, SN) - measured
		"""
		if tag in WELL_DEFINED_LANGUAGE_OPTIONS:
			letter = get_tag_first_letter(tag)
			return r'f(s, '+letter+') - measured'
		else:
			return r'f(s, '+tag+') - measured'

	def get_expected_tag_label(tag):
		""" This replaces:
		eng -> $\hat{f}$(s, E) - expected
		spa -> $\hat{f}$(s, S) - expected
		as in paper
		or:
		EN -> $\hat{f}$(s, EN) - expected
		ET -> $\hat{f}$(s, ET) - expected
		...
		SN -> $\hat{f}$(s, SN) - expected
		"""
		if tag in WELL_DEFINED_LANGUAGE_OPTIONS:
			letter = get_tag_first_letter(tag)
			return r'$\hat{f}$(s, '+letter+') - expected'
		else:
			return r'$\hat{f}$(s, '+tag+') - expected'

	fig, ax = plt.subplots()
	sorted_list_of_tags = get_sorted_list_of_tags(frequency_of_lengths_of_subsequences)
	print("sorted_list_of_tags")
	print(sorted_list_of_tags)
	# for tag in frequency_of_lengths_of_subsequences.keys():
	for tag in sorted_list_of_tags:
		x = [i for i in range(0, len(frequency_of_lengths_of_subsequences[tag]))]
		# ax.loglog(x, frequency_of_lengths_of_subsequences[tag], linestyle="None", marker='.', label=tag)
		ax.loglog(x, frequency_of_lengths_of_subsequences[tag], linestyle="None", marker='.', label=get_measured_tag_label(tag))
	# ax.autoscale(False, axis="x")
	# ax.autoscale(False, axis="y")
	# Expected results:
	expected_results = get_random_expected_frequencies(frequency_of_lengths_of_subsequences)

	for tag in sorted_list_of_tags:
		x = [i for i in range(1, len(frequency_of_lengths_of_subsequences[tag]))]
		# ax.loglog(x, expected_results[tag], linestyle="dashed", marker='_', label=tag+' randomly expected')
		ax.loglog(x, expected_results[tag], linestyle="dashed", marker='_', label=get_expected_tag_label(tag))

	ax.set_xlim(0.5, 50000)
	ax.set_ylim(0.5, 10000)
	plt.ylabel('# of occurances')
	plt.xlabel('sub-sequence length')
	plt.ylabel('Frequency')
	ax.legend()
	plt.title(title)
	prev_dir = os.getcwd()
	os.chdir(FOLDER_OF_FIGURES)
	plt.savefig(figure_name)
	os.chdir(prev_dir)
	plt.show()


def tag_function_eng_spa_cs(utterance: Utterance) -> str:
	if utterance.cs_level in PURE_CS_LEVELS_OPTIONS:
		return 'CS'
	else:
		return utterance.major_lang


def analyse_frequency_of_lengths_of_subsequences(corpus: Corpus) -> None:
	
	# Analyse Utterances by major language (English/Spanish):
	lists_of_list_of_tag_series = tag_utterances(corpus, tagging_function=(lambda u: u.major_lang))
	frequency_of_lengths_of_subsequences = get_frequency_of_lengths_of_subsequences(lists_of_list_of_tag_series)
	plot_frequency_of_lengths_of_subsequences(frequency_of_lengths_of_subsequences,
											  title='Sub-Sequence Length Analysis of Utterances',
											  figure_name='mono_lingual_major_subsequences_lengths_utterances_histogram.png')

	# Analyse Turns by major language (English/Spanish):
	lists_of_list_of_tag_series = tag_turns(corpus, tagging_function=(lambda u: u.major_lang))
	frequency_of_lengths_of_subsequences = get_frequency_of_lengths_of_subsequences(lists_of_list_of_tag_series)
	plot_frequency_of_lengths_of_subsequences(frequency_of_lengths_of_subsequences,
											  title='Sub-Sequence Length Analysis of Turns',
											  figure_name='mono_lingual_major_subsequences_lengths_turns_histogram.png')

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
