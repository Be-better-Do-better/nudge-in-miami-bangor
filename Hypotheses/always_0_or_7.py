import math
import random
from random import randint
from Classes.hypothesis import Hypothesis


class Always_0_or_7(Hypothesis):
	"""This function returns True if the c0 is either 0 or 7 condition holds and False otherwise"""
	def __init__(self):
		super().__init__(name='always 0 or 7', n=0, relevant_indexes=[0])

	def check_condition(self, c: list[int]) -> bool:
		return c[0] in [0, 7]


def test_always_0_or_7():
	h = Always_0_or_7()
	print('name')
	print(h.name)
	c = [random.randint(0, 7)]
	if h.check_condition(c):
		print(c)
		print(h.check_condition(c))
		print('*')


if __name__ == '__main__':
	for _ in range(10):
		test_always_0_or_7()
