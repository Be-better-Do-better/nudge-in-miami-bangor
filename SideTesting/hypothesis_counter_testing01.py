# Check Always Decrease:
print("Always Decrease")
s = [1, 0, 2, 3, 4, 5, 6]
relevant_indexes = [0, 1, 2, 3]
hypothesis_n = 3

hypothesis_condition_counter = 0
n_series = len(s)
for c0_index in range(hypothesis_n, n_series):
	c = [s[c0_index-i] for i in range(hypothesis_n+1)]
	print(c)

# Check Always 0 or 7:
print("Always 0 or 7")
s = [1, 0, 2, 3, 4, 5, 6]
relevant_indexes = [0]
hypothesis_n = 0

hypothesis_condition_counter = 0
n_series = len(s)
for c0_index in range(hypothesis_n, n_series):
	c = [s[c0_index-i] for i in range(hypothesis_n+1)]
	print(c)
