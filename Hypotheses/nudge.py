import math
import random
from Classes.hypothesis import Hypothesis


def avg(c1: int, c2: int, c3: int):
	return (c1+c2+c3)/3


class Nudge(Hypothesis):
	"""This function returns True if the nudge condition holds and False otherwise"""
	def __init__(self):
		super().__init__(name='Nudge', n=3, relevant_indexes=[0, 1, 2, 3])

	def check_condition(self, c: list[int]) -> bool:
		if (c[1] < c[2]-1) or (c[1]+c[3] < c[2]):
		# print('backoff')
		# print("c0 = {}".format(c0))
		# print("expected = {}".format(max(0, c1-1)))
			return c[0] == max(0, c[1]-1)
		else:
			# print('non-backoff')
			floor_avg = math.floor(avg(c[1], c[2], c[3]))
			# print("c0 = {}".format(c0))
			# print("min = {}".format(floor_avg))
			# print("max = {}".format(min(floor_avg+3, 7)))
			return (floor_avg <= c[0]) and (c[0] <= min(floor_avg+3, 7))
