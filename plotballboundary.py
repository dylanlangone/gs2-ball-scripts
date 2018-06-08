# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:08:51 2018

@author: Dylan


READ: This code is used for plotting the stability boundary of a configuration given
by an input file to the ballooning code.
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

boundary = open('ballrun.out')
s_hat = []
beta_prime = []

with boundary:
    total = csv.reader(boundary, delimiter = ' ')
    #cleaned up input file
    points = []
    for line in total:
        points.append([x for x in line if x != ''])
    #further cleaned up input file
    clean_points = []
    for line in points:
        if (not(line[0][0].isalpha()) or line[0][0] == 's'):
            clean_points.append(line)
    #for line in clean_points:
        #print(line)
    potential_s_hat = 0.0
    for x in range(0, len(clean_points) - 1):
        if (clean_points[x][0] == 's_hat'):
            potential_s_hat = float(clean_points[x][2])
        else:
            #print(clean_points[x])
            if (clean_points[x][1] == '0' and clean_points[x+1][1] != '0' and clean_points[x+1][0] != 's_hat'):
                s_hat.append(potential_s_hat)
                beta_prime.append(float(clean_points[x][2]))
            elif ((clean_points[x][1] != '0') and (clean_points[x+1][1] == '0') and clean_points[x+1][0] != 's_hat'):
                s_hat.append(potential_s_hat)
                beta_prime.append(float(clean_points[x][2]))
                
minus_beta_prime = [-1*x for x in beta_prime]
#print (minus_beta_prime)

plt.plot(s_hat,minus_beta_prime,'ro')
plt.axis([min(s_hat),max(s_hat),-10,10])
plt.title("-beta prime vs s_hat")
plt.xlabel("s_hat")
plt.grid()
plt.ylabel("-beta prime")
plt.show()

