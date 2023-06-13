
def extract_monolingual_subsequences_lengths(tags_sequence_extracted: list[str]) -> list[(str, int)]:
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
