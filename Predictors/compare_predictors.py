import time
import random


from Predictors.only_english_predictor import OnlyEnglishPredictor
from Predictors.only_spanish_predictor import OnlySpanishPredictor
from Predictors.random_predictor import RandomPredictor
from Predictors.tit_for_tat_predictor import TitForTatPredictor
from Predictors.goldfish_predictor import GoldfishPredictor
from sklearn.model_selection import KFold


def compare_predictors(predictors, train_data, test_data):
    for predictor in predictors:
        start_time = time.time()
        predictor.train(train_data)
        accuracy = predictor.eval(test_data)
        end_time = time.time()
        print(f'{predictor.name} predictor took {end_time - start_time:.2f} seconds and had an accuracy of {accuracy:.2f}')


def compare_predictors_on_corpus(corpus):
    full_data = [dialogue for dialogue in corpus.dialogues]
    random.shuffle(full_data)
    kf = KFold(n_splits=3)
    kf.get_n_splits(full_data)

    for i, (train_index, test_index) in enumerate(kf.split(full_data)):
        print(f"Fold {i}:")
        print(f"  Train: index={train_index}")
        print(f"  Test:  index={test_index}")
        train_data = [full_data[i] for i in train_index]
        test_data = [full_data[i] for i in test_index]
        predictor_1 = OnlyEnglishPredictor()
        predictor_2 = OnlySpanishPredictor()
        predictor_3 = RandomPredictor()
        predictor_4 = TitForTatPredictor()
        predictor_5 = GoldfishPredictor()
        predictors = [predictor_1, predictor_2, predictor_3, predictor_4, predictor_5]
        compare_predictors(predictors, train_data, test_data)
