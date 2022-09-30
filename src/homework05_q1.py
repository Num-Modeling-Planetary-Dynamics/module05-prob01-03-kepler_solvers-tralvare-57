# this file runs PROBLEM 1

import numpy as np
import math

e = 0.100 #ecentricity
M = np.deg2rad(5) #mean anomoly
E0 = [np.deg2rad(5)]

while True:
    En = M + e * math.sin(E0[-1])
    if abs(E0[-1] - En) < np.deg2rad(0.000001):
        break
    E0.append(En)

print(E0)

    
