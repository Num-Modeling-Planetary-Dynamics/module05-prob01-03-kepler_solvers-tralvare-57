# this file runs PROBLEM 2

import numpy as np
import math
import sympy as sym

e = 0.100 #ecentricity
M = np.deg2rad(5) #mean anomoly
E0 = [np.deg2rad(5)]

while True:
    En = E0[-1] - e * sym.sin(E0[-1]) - M
    En_prime = 1 - e * sym.cos(E0[-1])
    Ex = E0[-1] - (En/En_prime)
    if abs(E0[-1] - Ex) < np.deg2rad(0.000001):
        break
    E0.append(Ex)

print(E0)
