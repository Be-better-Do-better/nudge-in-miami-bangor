from Classes.hypothesis import Hypothesis


class CloseToPrevious(Hypothesis):
	"""This function returns True if the |c0-c1|<=1 and False otherwise"""
	def __init__(self):
		super().__init__(name='Close by 1 to Previous', n=1, relevant_indexes=[0, 1])

	def check_condition(self, c: list[int]) -> bool:
		return abs(c[0]-c[1]) <= 1
