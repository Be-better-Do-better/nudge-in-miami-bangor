import math
from random import randint


def always_0_or_7(c0: int, c1: int, c2: int, c3: int) -> bool:
	"""
	This function returns True if the c0 is either 0 or 7 condition holds and False otherwise
	:param c0: current CS level
	:param c1: previous CS level
	:param c2: CS level before two time periods
	:param c3: CS level before three time periods
	:return: True if c0 is 0 or 7 (False otherwise)
	"""
	return c0 in [0, 7]


def test_always_0_or_7():
	c0, c1, c2, c3 = 3, 4, 2, 1
	c0, c1, c2, c3 = randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7)
	print(c0, c1, c2, c3)
	res = always_0_or_7(c0, c1, c2, c3)
	print(res)
	print('*'*3)


if __name__ == '__main__':
	for _ in range(10):
		test_always_0_or_7()
