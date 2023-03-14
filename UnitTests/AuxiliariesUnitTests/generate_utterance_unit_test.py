import os
os.chdir('..')
from Auxiliaries.artificial_generation import generate_utterance, generate_utterance2

utterance = generate_utterance()
print(utterance)

utterance = generate_utterance2()
print(utterance)
