import os
os.chdir('../..')

from CorpusAnalyses.MonolingualSequencesAnalysis.extract_raw_languages_probabilities import extract_raw_languages_probabilities


def test_extract_raw_languages_probabilities():
	tag_sequence1 = ['eng', 'eng', 'spa', 'eng']
	tag_sequence2 = ['eng', 'eng', 'eng', 'spa']
	tag_sequences = [tag_sequence1, tag_sequence2]

	expected_result = {'eng': 0.75, 'spa': 0.25}

	res = extract_raw_languages_probabilities(tag_sequences)
	print(res)
	assert (res == expected_result)


if __name__ == '__main__':
	test_extract_raw_languages_probabilities()
	print("Test passed successfully!")

