import os
os.chdir('..')
from Auxiliaries.artificial_generation import generate_dialogue

dialogue = generate_dialogue()
print(dialogue)
