import os
from collections import Counter
from CorpusAnalyses.MonolingualSequencesAnalysis.convert_counter_to_frequency_vector import convert_counter_to_frequency_vector

os.chdir('../..')


def test_convert_counter_to_frequency_vector():
	counter = Counter({1: 7, 3: 2})
	print(counter)
	res = convert_counter_to_frequency_vector(counter)
	expected_result = [0, 7, 0, 2]
	print(res)
	assert res == expected_result


if __name__ == '__main__':
	test_convert_counter_to_frequency_vector()
	print("Test passed successfully!")

