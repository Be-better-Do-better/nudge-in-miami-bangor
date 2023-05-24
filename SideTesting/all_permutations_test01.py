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


def get_all_options(args, C):
	opt = []
	for _ in range(len(args)):
		if len(opt) == 0:
			opt = [[c] for c in C]
		else:
			opt = recursively_add(opt, C)
	return opt


if __name__ == '__main__':
	args = ['c0', 'c1']
	C = [c for c in range(7)]
	# n_list = [[3], [4]]
	# n_plus1_list = recursively_add(n_list, C)
	# print(n_plus1_list)
	opts = get_all_options(args, C)
	print(opts)
	print(len(opts))