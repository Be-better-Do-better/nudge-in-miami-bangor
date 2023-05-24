import os
os.chdir('..')

from Auxiliaries.t_test import t_test

import numpy as np
from scipy import stats
from numpy.random import seed
from numpy.random import randn
from numpy.random import normal

seed = 1
sample = normal(0.5, 0.1, 20)
print('Sample: ', sample)
expected_population_mean = 0.3

t_stat, p_value = t_test(sample, expected_population_mean)
print("T-statistic value: ", t_stat)
print("P-Value: ", p_value)
