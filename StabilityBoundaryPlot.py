# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:56:55 2018

@author: Dylan
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
boundary = open('StabilityBoundary.csv')
s_hat = []
beta_prime = []
firstrow = True
with boundary:
    plots = csv.reader(boundary, delimiter = ',')
    for row in plots:
        if firstrow:
            firstrow = False
            continue
        s_hat.append(float(row[0]))
        beta_prime.append(float(row[1]))


minus_beta_prime = [-1*x for x in beta_prime]
#print (minus_beta_prime)

plt.plot(s_hat,minus_beta_prime,'ro')
plt.axis([-10,10,0,2])
plt.title("-beta prime vs s_hat")
plt.xlabel("s_hat")
plt.grid()
plt.ylabel("-beta prime")
plt.show()
