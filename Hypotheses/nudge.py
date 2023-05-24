import math
from random import randint


def avg(c1: int, c2: int, c3: int):
	return (c1+c2+c3)/3


def nudge(c0: int, c1: int, c2: int, c3: int) -> bool:
	"""
	This function returns True if the nudge condition holds and False otherwise
	:param c0: current CS level
	:param c1: previous CS level
	:param c2: CS level before two time periods
	:param c3: CS level before three time periods
	:return:
	"""

	if (c1 < c2-1) or (c1+c3 < c2):
		# print('backoff')
		# print("c0 = {}".format(c0))
		# print("expected = {}".format(max(0, c1-1)))
		return c0 == max(0, c1-1)
	else:
		# print('non-backoff')
		floor_avg = math.floor(avg(c1, c2, c3))
		# print("c0 = {}".format(c0))
		# print("min = {}".format(floor_avg))
		# print("max = {}".format(min(floor_avg+3, 7)))
		return (floor_avg <= c0) and (c0 <= min(floor_avg+3, 7))


def test_nudge():
	c0, c1, c2, c3 = 3, 4, 2, 1
	c0, c1, c2, c3 = randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7)
	print(c0, c1, c2, c3)
	res = nudge(c0, c1, c2, c3)
	print(res)
	print('*'*3)


if __name__ == '__main__':
	for _ in range(3):
		test_nudge()