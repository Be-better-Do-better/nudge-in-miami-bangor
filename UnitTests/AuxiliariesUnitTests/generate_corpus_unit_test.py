import os
os.chdir('..')
from Auxiliaries.artificial_generation import generate_corpus

corpus = generate_corpus()
print(corpus)