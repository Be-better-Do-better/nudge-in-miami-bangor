import math
import random
from random import randint
from Classes.hypothesis import Hypothesis


class Always_0_or_7(Hypothesis):
	"""This function returns True if the c0 is either 0 or 7 condition holds and False otherwise"""
	def __init__(self):
		super().__init__(name='Always 0 or 7', n=0, relevant_indexes=[0])

	def check_condition(self, c: list[int]) -> bool:
		return c[0] in [0, 7]
