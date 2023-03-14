from Auxiliaries.artificial_generation import generate_corpus
from compare_predictors import compare_predictors_on_corpus

corpus = generate_corpus()

compare_predictors_on_corpus(corpus)

print(corpus)
for dialogue in corpus.dialogues:
    print(dialogue)