import math
import random
from random import randint
from Classes.hypothesis import Hypothesis


class AlwaysDecrease(Hypothesis):
	"""This function returns True if the c0<c1 condition holds and False otherwise"""
	def __init__(self):
		super().__init__(name='Always Decrease', n=1, relevant_indexes=[0, 1])

	def check_condition(self, c: list[int]) -> bool:
		return c[0] < c[1]
