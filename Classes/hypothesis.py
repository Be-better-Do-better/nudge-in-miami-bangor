from abc import ABC, abstractmethod


class Hypothesis(ABC):
	def __init__(self, name: str, n: int, relevant_indexes: list[int]):
		self.name = name  # name of hypothesis
		self.n = n  # maximal relevant history
		self.relevant_indexes = relevant_indexes  # indexes actually used in hypothesis

	@abstractmethod
	def check_condition(self, c: list[int]) -> bool:
		pass

