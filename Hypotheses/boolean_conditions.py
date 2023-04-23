import math

def decrease_at_prev(history, constants=None):
	# c0 = history[-1]
	c1 = history[-2]
	c2 = history[-3]
	return c1-c2 < 0

def decrease_at_last_or_zero(history, constants=None):
	c0 = history[-1]
	c1 = history[-2]
	return (c0-c1<0) or (c0==0)

def increase_at_prev(history, constants=None):
	# c0 = history[-1]
	c1 = history[-2]
	c2 = history[-3]
	return c1-c2>0

def increase_at_last_or_seven(history, constants={}):
	c0 = history[-1]
	c1 = history[-2]
	return (c0-c1>0) or (c0==7)

def previous_cs_level_is(history, constants=None):
	if constants is None:
		constants = {'required_cs_level': 0}
	# c0 = history[-1]
	c1 = history[-2]
	return c1 == constants['required_cs_level']

def previous_cs_levels_are(history, constants=None):
	if constants is None:
		constants = {'required_cs_levels': [0, 1]}
	required_cs_levels = constants['required_cs_levels']
	n = len(required_cs_levels)
	last_n_elements = history[-n-1:-1] # without actually the last one!!!
	return last_n_elements == required_cs_levels

def cs_level_changed_c1_to_c0(history, constants=None):
	c0 = history[-1]
	c1 = history[-2]
	return not (c0 == c1)

def cs_level_changed_c2_to_c1(history, constants=None):
	c1 = history[-2]
	c2 = history[-3]
	return not (c1 == c2)

def cs_level_changed_c3_to_c1(history, constants=None):
	c1 = history[-2]
	# c2 = history[-3]
	c3 = history[-4]
	return not (c3 == c1)

def cs_level_changed_c3_to_c2(history, constants=None):
	# c1 = history[-2]
	c2 = history[-3]
	c3 = history[-4]
	return not (c3 == c2)

def cs_level_changed_c4_to_c3(history, constants=None):
	# c1 = history[-2]
	# c2 = history[-3]
	c3 = history[-4]
	c4 = history[-5]
	return not (c4 == c3)

def cs_level_changed_c21_to_c20(history, constants=None):
	c20 = history[-21]
	c21 = history[-22]
	return not (c20 == c21)

def cs_level_changed_c51_to_c50(history, constants=None):
	c50 = history[-51]
	c51 = history[-52]
	return not (c50 == c51)

def cs_level_changed_c101_to_c100(history, constants=None):
	c100 = history[-101]
	c101 = history[-102]
	return not (c100 == c101)

def same_cs_level(history, constants=None):
	c0 = history[-1]
	c1 = history[-2]
	return c0 == c1

def changed_at_previous(history, constants={}):
	c1 = history[-2]
	c3 = history[-4]
	return not c3 == c1

def changed_at_last(history, constants={}):
	c0 = history[-1]
	c2 = history[-3]
	return not c0 == c2

def confinement(history, constants=None):
	if constants is None:
		constants = {'previous_cs_levels': [0]}
	c0 = history[-1]
	return (min(constants['previous_cs_levels']) <= c0) and (c0 <= max(constants['previous_cs_levels']))

def backoff_condition(history, constants={}):
	# c0 = history[-1]
	c1 = history[-2]
	c2 = history[-3]
	c3 = history[-4]
	return (c1 < c2-1) or (c1+c3<c2)

def non_backoff_condition(history, constants={}):
	# c0 = history[-1]
	c1 = history[-2]
	c2 = history[-3]
	c3 = history[-4]
	backoff = (c1 < c2-1) or (c1+c3<c2)
	return not backoff

def retreat(history, constants=None):
	c0 = history[-1]
	c1 = history[-2]
	return c0 == max(0, c1-1)


def nudge(history, constants=None) -> bool:
	if constants is None:
		constants = {'max_allowed_raise': 3}
	c0, c1, c2, c3 = history[-1], history[-2], history[-3], history[-4]
	max_allowed_raise = constants['max_allowed_raise']
	avg = (c1+c2+c3)/3
	avg_floor = math.floor(avg)
	return (avg_floor <= c0) and (c0 <= min(avg_floor+max_allowed_raise, 7))

def last_is_zero(history, constants=None) -> bool:
	c0 = history[-1]
	return c0 == 0

def last_belongs_to(history, constants=None) -> bool:
	if constants is None:
		constants = {'last_set': [0]}
	c0 = history[-1]
	return c0 in constants['last_set']

def previous_belongs_to(history, constants=None) -> bool:
	if constants is None:
		constants = {'previous_set': [0]}
	# c0 = history[-1]
	c1 = history[-2]
	return c1 in constants['previous_set']


def general_nudge(history, constants=None) -> bool:
	def __avg(c1, c2, c3):
		return (c1+c2+c3)/3

	def __get_lower_limit(c1: int, c2:int, c3:int):
		if (c1 < c2-1) and (c1+c3 < c2):
			return max(0, c1-1)
		else:
			return min(math.floor(__avg(c1, c2, c3)), 7)
	def __get_upper_limit(c1: int, c2:int, c3:int):
		if (c1 < c2-1) and (c1+c3 < c2):
			return max(0, c1-1)
		else:
			return min(math.floor(__avg(c1, c2, c3)+3), 7)

	c0, c1, c2, c3 = history[-1], history[-2], history[-3], history[-4]
	lower_limit = __get_lower_limit(c1, c2, c3)
	upper_limit = __get_upper_limit(c1, c2, c3)
	return (lower_limit <= c0) and (c0 <= upper_limit)