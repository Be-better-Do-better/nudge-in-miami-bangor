import math

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    return (x**3 - 1)  # only one real root at x = 1

def d2(theta):
	th1, th2 = theta[0], theta[1]
	return np.array((2+3*math.cos(th1)+0.5*math.sin(th1))**2+(2+3*math.cos(th2)+0.5*math.sin(th2))**2)

root = optimize.newton(f, 1.5)
print(root)

theta0 = [1.5, 0.5]
print(theta0)
print(d2(theta0))

r2 = optimize.newton(d2, theta0)
print(r2)
print(d2(r2))