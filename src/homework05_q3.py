# this file runs PROBLEM 3

import numpy as np
import math
import sympy as sym
import csv

e = 0.100 #ecentricity
M = np.deg2rad(5) #mean anomoly
E0 = [np.deg2rad(5)]

while True:
    En = E0[-1] - e * sym.sin(E0[-1]) - M
    En_prime = 1 - e * sym.cos(E0[-1])
    En_2prime = e * sym.sin(E0[-1])
    En_3prime = e * sym.cos(E0[-1])
    Ex1 = -(En/En_prime)
    Ex2 = -(En/(En_prime + 1/2 * Ex1 * En_2prime))
    Ex3 = -(En/(En_prime + 1/2 * Ex2 * En_2prime + 1/6 * Ex2**2 * En_3prime))
    Ex = E0[-1] + Ex3
    if abs(E0[-1] - Ex) < np.deg2rad(0.000001):
        break
    E0.append(Ex)

with open("module05-prob03-output.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(E0)

print(E0)

