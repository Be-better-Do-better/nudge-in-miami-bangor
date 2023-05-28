from Classes.hypothesis import Hypothesis


class TitForTat(Hypothesis):
	"""This function returns True if the c0==c1 and False otherwise"""
	def __init__(self):
		super().__init__(name='Tit-for-Tat', n=1, relevant_indexes=[0, 1])

	def check_condition(self, c: list[int]) -> bool:
		return c[0] == c[1]
