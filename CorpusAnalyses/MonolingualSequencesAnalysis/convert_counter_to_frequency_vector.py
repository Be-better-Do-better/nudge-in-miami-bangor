from collections import Counter


def convert_counter_to_frequency_vector(frequency_counter: Counter) -> list[int]:
	"""
	This function receives a counter and returns a list with frequencies.
	for example: the counter = {1: 7, 3: 2} will be converted into:
	list = [0, 7, 0, 2]
	:param frequency_counter:
	:return:
	"""
	max_key = max(frequency_counter.keys())
	frequency_vector = [0 for _ in range(max_key+1)]
	for i, frequency in frequency_counter.items():
		frequency_vector[i] = frequency
	return frequency_vector
