import os
os.chdir('../..')

from CorpusAnalyses.MonolingualSequencesAnalysis.extract_monolingual_subsequences_lengths import extract_monolingual_subsequences_lengths


def test_extract_monolingual_subsequences_lengths():
	tag_sequence = ['eng', 'eng', 'spa']
	# will be squoshed into [('eng', 2), ('spa', 1)]
	expected_result = [('eng', 2), ('spa', 1)]
	un_expected_result = [('eng', 2)]
	res = extract_monolingual_subsequences_lengths(tag_sequence)
	print(res)
	assert (res == expected_result)


if __name__ == '__main__':
	test_extract_monolingual_subsequences_lengths()
	print("Test passed successfully!")

