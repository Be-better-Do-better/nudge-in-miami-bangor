import os
os.chdir('..')
from Auxiliaries.artificial_generation import generate_token

t1 = generate_token()
print(t1)
print(os.getcwd())