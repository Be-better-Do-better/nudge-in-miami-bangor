import os
os.chdir('..')
from Auxiliaries.artificial_generation import generate_turn

turn = generate_turn()
print(turn)
print(os.getcwd())