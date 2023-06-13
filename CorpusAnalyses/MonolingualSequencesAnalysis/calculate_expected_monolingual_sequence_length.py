def calculate_expected_monolingual_sequence_length(p_L: float) -> float:
	expected_monolingual_sequence_length = -1
	if (0 < p_L) and (p_L < 1):
		expected_monolingual_sequence_length = 1/(1-p_L)
	return expected_monolingual_sequence_length
