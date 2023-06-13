from CorpusAnalyses.MonolingualSequencesAnalysis.calculate_expected_monolingual_sequence_length import calculate_expected_monolingual_sequence_length

def test_calculate_expected_monolingual_sequence_length():
	p_E = 0.80
	s_E = calculate_expected_monolingual_sequence_length(p_L=p_E)
	print(fr"with p_E = {p_E}, s_E = {s_E}")


if __name__ == '__main__':
	test_calculate_expected_monolingual_sequence_length()
	print("Test passed successfully!")
