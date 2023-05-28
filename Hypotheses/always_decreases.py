import math
import random
from random import randint
from Classes.hypothesis import Hypothesis


class AlwaysDecrease(Hypothesis):
	"""This function returns True if the c0<c1<c2<c3 condition holds and False otherwise"""
	def __init__(self):
		super().__init__(name='Always Decrease', n=3, relevant_indexes=[0, 1, 2, 3])

	def check_condition(self, c: list[int]) -> bool:
		return (c[0] < c[1]) and (c[1] < c[2]) and (c[2] < c[3])

