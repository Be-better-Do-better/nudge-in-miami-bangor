def nudge_condition(history):
	c1 = history[-1]
	c2 = history[-2]
	c3 = history[-3]
	# nudge condition: c1<c2-1 | c1+c3<c2
	if c3 == 0:
		print('c1, c2, c3')
		print(c1, c2, c3)
		return c2 <= c1
	else:
		return c2 <= c1 + 1

def nudge_policy(c0, history):
	c1 = history[-1]
	print((c0 == 0 and c1 == 0))
	if c0 < c1 | (c0 == 0 and c1 == 0): # Backoff = stay @ 0 or decay
		print('backoff action:')
		print("c0 = {}".format(c0))
		return False
	else:
		print('nudge action:')
		print("c0 = {}".format(c0))
		return True


def init_results():
	results = {}
	for condition in [True, False]:
		for policy in [True, False]:
			results[(condition, policy)] = 0
	return results

def check_hypothesis(list_of_series: list):
	results = init_results()

	for s in list_of_series:
		for n in range(len(s)-1):
			print("n = {}".format(n))
			print(s[:n+1])
			if len(s[0:n+1])>=3:
				c = nudge_condition(s[0:n+1])
				a = nudge_policy(s[n+1], s[0:n+1])
				print("Cond = {}".format(c))
				print("Act = {}".format(a))
				results[(c, a)] += 1

	display_results(results)

def display_results(results):
	print("Condition | Action | Counter")
	for condition in [True, False]:
		for action in [True, False]:
			print("{} | {} | {}".format(condition, action, results[(condition, action)]))

def run_tests():
	# s1 = [0, 1, 2, 4, 2, 5, 7]
	# s2 = [3, 4, 2, 1, 2, 1, 6]
	s1 = [0, 1, 2, 3]
	s2 = [2, 3, 4, 0]
	list_of_series = [s1, s2]
	check_hypothesis(list_of_series)

if __name__ == '__main__':
	run_tests()
	print('Success!')

