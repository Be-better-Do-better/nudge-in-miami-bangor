from Predictors.predictor import Predictor, LIST_OF_LANGUAGES
from collections import Counter


class TitForTatPredictor(Predictor):
    def __init__(self):
        self.name = 'titForTat'
        self.lang_probabilities = {}
        for lang in LIST_OF_LANGUAGES:
            self.lang_probabilities[lang] = 0.5

    def train(self, training_set: list) -> None:
        lang_label_counter = Counter()
        for dialogue in training_set:
            lang_label_counter.update([utterance.lang for utterance in dialogue.utterances])

        total_sum = sum(lang_label_counter.values())
        if total_sum > 0:
            for lang, counts in lang_label_counter.items():
                self.lang_probabilities[lang] = lang_label_counter[lang] / total_sum

    def predict(self, label='eng', history=None, next_speaker=None):
        # 1) if no history (return majority baseline)
        if len(history) <= 0:
            return self.lang_probabilities[label]
        # 2) if history exists - select result according to previous language label
        if len(history) > 0:
            if label == history[-1].lang:
                return 1.0
            else:
                return 0.0

    def eval(self, test_set: list):
        m = 0  # prediction counter
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
