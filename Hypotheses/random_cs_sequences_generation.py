import random
NUM_OF_SERIES = 30
SERIES_LENGTH = 2000
random.seed(1234)


def generate_random_list_of_series(cs_levels_weights: list[float]=[1, 1, 1, 1, 1, 1, 1, 1], dialogues_length=[]) \
		-> list[list[int]]:
	cs_levels_options = [0, 1, 2, 3, 4, 5, 6, 7]
	list_of_series = []
	if not dialogues_length:  # Does not resembles corpus dialogue's length
		for _ in range(NUM_OF_SERIES):
			series = random.choices(cs_levels_options, weights=cs_levels_weights, k=SERIES_LENGTH)
			list_of_series.append(series)
	else:  # Imitates the exact corpus size
		for dialogue_index in range(len(dialogues_length)):
			series = random.choices(cs_levels_options, weights=cs_levels_weights, k=dialogues_length[dialogue_index])
			list_of_series.append(series)
	return list_of_series
