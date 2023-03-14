from Predictors.predictor import Predictor, LIST_OF_LANGUAGES
from CorpusAnalyses.categorial_subsequences_length_analysis import collect_subsequence_frequencies, \
    unite_subsequence_frequencies, calc_relative_frequency_of_tags, hazard_function_calculation


class GoldfishPredictor(Predictor):
    def __init__(self):
        self.name = 'goldfish'
        self.lang_probabilities = {}
        self.sub_sequences_lengths = {}
        self.relative_frequency_of_tags = {}
        self.hazards_for_tags = {}
        self.previous_lang_tag = None
        self.current_sub_sequence_length = 1

        for lang in LIST_OF_LANGUAGES:
            self.lang_probabilities[lang] = 0.5
            self.sub_sequences_lengths[lang] = []

    def train(self, training_set: list) -> None:
        for dialogue in training_set:
            language_tags_in_dialogue = [utterance.lang for utterance in dialogue.utterances]

            found_sub_seq_len_freq = collect_subsequence_frequencies(language_tags_in_dialogue)
            self.sub_sequences_lengths = \
                unite_subsequence_frequencies(found_sub_seq_len_freq, self.sub_sequences_lengths)

        self.relative_frequency_of_tags = calc_relative_frequency_of_tags(self.sub_sequences_lengths)
        for lang in LIST_OF_LANGUAGES:
            self.hazards_for_tags[lang] = hazard_function_calculation(self.relative_frequency_of_tags[lang])

        print(self.relative_frequency_of_tags)


    def predict(self, label='eng', history=None, next_speaker=None):
        # 1) if no history (return majority baseline)

        if len(history) <= 0:
            self.previous_lang_tag = label
            return self.lang_probabilities[label]

        # 2) if history exists - select result according to previous language label

        if len(history) > 0:
            self.previous_lang_tag = history[-1].lang
            p_change = 1.0  # in case current sub-sequence is larger than found in training set
            if self.current_sub_sequence_length < len(self.hazards_for_tags[self.previous_lang_tag]):
                p_change = self.hazards_for_tags[self.previous_lang_tag][self.current_sub_sequence_length]
            p_dont_change = 1-p_change
            if label == history[-1].lang:  # No Change
                self.current_sub_sequence_length += 1
                return p_dont_change
            else:  # Change
                self.current_sub_sequence_length = 1
                return p_change

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
