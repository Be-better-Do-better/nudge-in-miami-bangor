def recursively_add(n_list: list[list], C: list) -> list:
	n_plus_1_list = []
	for c in C:
		if len(n_list) == 0:
			n_plus_1_list = [c for c in C]
		else:
			for element in n_list:
				temp = element.copy()
				temp.append(c)
				n_plus_1_list.append(temp)
	return n_plus_1_list


def get_all_permutations(args: list, C: list) -> list:
	options = []
	for _ in range(len(args)):
		if len(options) == 0:
			options = [[c] for c in C]
		else:
			options = recursively_add(options, C)
	return options
