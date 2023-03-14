from abc import ABC, abstractmethod
LIST_OF_LANGUAGES = ['eng', 'spa']


class Predictor(ABC):
    @abstractmethod
    def train(self, training_set: list) -> None:
        pass

    @abstractmethod
    def predict(self, label: str, history: list, next_speaker: str) -> float:
        pass

    @abstractmethod
    def eval(self, test_set: list) -> float:
        pass
