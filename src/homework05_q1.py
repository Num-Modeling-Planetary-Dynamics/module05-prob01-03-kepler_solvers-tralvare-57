# this file runs PROBLEM 1

import numpy as np
import math
import csv

e = 0.100 #ecentricity
M = np.deg2rad(5) #mean anomoly
E0 = [np.deg2rad(5)]

while True:
    En = M + e * math.sin(E0[-1])
    if abs(E0[-1] - En) < np.deg2rad(0.000001):
        break
    E0.append(En)

with open("module05-prob01-output.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(E0)

print(E0)

    
