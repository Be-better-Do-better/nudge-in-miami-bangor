from Predictors.predictor import Predictor, LIST_OF_LANGUAGES


class OnlyEnglishPredictor(Predictor):
    def __init__(self):
        self.name = 'onlyEnglish'
        self.lang_probabilities = {}
        for lang in LIST_OF_LANGUAGES:
            self.lang_probabilities[lang] = 0
        self.lang_probabilities['eng'] = 1.0

    def train(self, training_set: list) -> None:
        pass

    def predict(self, label='eng', history=None, next_speaker=None):
        return self.lang_probabilities[label]

    def eval(self, test_set: list) -> float:
        m = 0
        probability_sum = 0
        for dialogue in test_set:
            for n in range(len(dialogue.utterances)):
                true_label = dialogue.utterances[n].lang
                speaker = dialogue.utterances[n].speaker
                history = dialogue.utterances[0:n]
                probability_sum += self.predict(true_label, history, speaker)
                m += 1
        if m > 0:
            return probability_sum / m
        else:
            return 0
