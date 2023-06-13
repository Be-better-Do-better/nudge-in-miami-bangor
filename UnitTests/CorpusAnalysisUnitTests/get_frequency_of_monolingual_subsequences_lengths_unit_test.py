import os
os.chdir('../..')

from CorpusAnalyses.MonolingualSequencesAnalysis.get_frequency_of_monolingual_subsequences_lengths import get_frequency_of_monolingual_subsequences_lengths


def test_get_frequency_of_monolingual_subsequences_lengths():
	frequency_of_monolingual_subsequences_lengths = [('eng', 2), ('spa', 1), ('eng', 3), ('eng', 2)]
	res = get_frequency_of_monolingual_subsequences_lengths(frequency_of_monolingual_subsequences_lengths)
	print(res)


if __name__ == '__main__':
	test_get_frequency_of_monolingual_subsequences_lengths()
	print("Test passed successfully!")

