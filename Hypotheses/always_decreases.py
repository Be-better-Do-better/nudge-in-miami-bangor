import math
import random
from random import randint
from Classes.hypothesis import Hypothesis


class AlwaysDecrease(Hypothesis):
	"""This function returns True if the c0<c1<c2<c3 condition holds and False otherwise"""
	def __init__(self):
		super().__init__(name='always decrease', n=3, relevant_indexes=[0, 1, 2, 3])

	def check_condition(self, c: list[int]) -> bool:
		return (c[0] < c[1]) and (c[1] < c[2]) and (c[2] < c[3])


def test_always_decrease():
	h = AlwaysDecrease()
	c = random.sample(range(0, 7), h.n)
	if h.check_condition(c):
		print(h.check_condition(c))
		print(c)
		print('*')


if __name__ == '__main__':
	for _ in range(1000):
		test_always_decrease()
