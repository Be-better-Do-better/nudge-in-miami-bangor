import math
from random import randint



def always_decreases(c0: int, c1: int, c2: int, c3: int) -> bool:
	"""
	This function returns True if the levels decreases holds and False otherwise
	:param c0: current CS level
	:param c1: previous CS level
	:param c2: CS level before two time periods
	:param c3: CS level before three time periods
	:return:
	"""

	return (c0 < c1) and (c1 < c2) and (c2 < c3)


def test_always_decreases():
	c0, c1, c2, c3 = 3, 4, 2, 1
	c0, c1, c2, c3 = randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7)
	res = always_decreases(c0, c1, c2, c3)
	if res:
		print(c0, c1, c2, c3)
		print('*'*3)


if __name__ == '__main__':
	for _ in range(3000):
		test_always_decreases()
