# -*- coding: utf-8 -*-
"""
Created on Thu Jun 7 21:08:51 2018
@author: Dylan Langone
READ: This code is used for plotting the stability boundary of a configuration given
by an input file to the ballooning code.
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

def plotballfile(filename = input('Enter ball output file to plot: ')):
	boundary = open(filename)
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
		#print (points)
		for line in points:
			#print (line)
			if (line != []):
				if (not(line[0][0].isalpha()) or line[0][0] == 's'):
					clean_points.append(line)
		#for line in clean_points:
			#print(line)
		potential_s_hat = 0.0
		for x in range(0, len(clean_points) - 1):
			if (clean_points[x][0] == 's_hat' or clean_points[x][0] == 's_hat_input'):
				potential_s_hat = float(clean_points[x][2])
			else:
				#print(clean_points[x])
				if (clean_points[x][1] == '0' and clean_points[x+1][1] != '0' and (clean_points[x+1][0] != 's_hat')): # change all instances of s_hat_input to s_hat
					print(clean_points[x+1][0])
					s_hat.append(potential_s_hat)
					beta_prime.append(float(clean_points[x][2]))
					# print (clean_points[x][2])
				elif ((clean_points[x][1] != '0') and (clean_points[x+1][1] == '0') and (clean_points[x+1][0] != 's_hat' or clean_points[x+1][0] != 's_hat_input')):
					print(clean_points[x+1][0])
					s_hat.append(potential_s_hat)
					beta_prime.append(float(clean_points[x][2]))
					# print (clean_points[x][2])
					
	minus_beta_prime = [-1*x for x in beta_prime]
	return s_hat, minus_beta_prime
#print (minus_beta_prime)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
s_hat, minus_beta_prime = plotballfile()
ax.plot(s_hat,minus_beta_prime,'ro')
# ax.plot([-4.65], [.58], 'bo')
x_ticks = np.arange(-10, 10, 1)
y_ticks = np.arange(0, 2, .25)
#plt.axis([min(s_hat),max(s_hat),-10,10])
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)

plt.title("-beta prime vs s_hat (rhoc = .95)")
plt.xlabel("s_hat")
ax.grid()
plt.ylabel("-beta prime")
ax.title.set_fontsize(24)
ax.xaxis.label.set_fontsize(24)
ax.yaxis.label.set_fontsize(24)
ax.tick_params(axis='both', which='major', labelsize=20)
ax.tick_params(axis='both', which='minor', labelsize=20)
plt.show()
