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

def plotballfile(filename):
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
	return [s_hat, minus_beta_prime]
#print (minus_beta_prime)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

filelist = ['ballrho_90_shape.out', 'ballrho_91_shape.out', 'ballrho_92_shape.out','ballrho_93_shape.out', 'ballrho_94_shape.out', 
'ballrho_96_shape.out', 'ballrho_97_shape.out', 'ballrho_98_shapezoom.out',
'ballrho_99_shape.out']


s_hat = minus_beta_prime = []

for file in filelist:
	s_hat = plotballfile(file)[0]
	minus_beta_prime = plotballfile(file)[1]
	ax.plot(s_hat, minus_beta_prime, 'ko', ms = 7)
	
#ax.plot(s_hat,minus_beta_prime,'ro')
s_hat_eq = [-0.96, -0.54, -0.08, 0.41, 0.91, 2.04, 2.73, 3.62, 4.86]
beta_prime_eq = [-0.42, -0.39, -0.35, -0.32, -0.28, -0.2, -0.15, -0.11, -0.06]
minus_beta_prime_eq = [-1*x for x in beta_prime_eq]
ax.plot(s_hat_eq, minus_beta_prime_eq, 'b^', ms = 10)
s_hat_95 = [1.45]
beta_prime_95 = [.24]
plt.plot(s_hat_95, beta_prime_95, 'go', ms = 10)
s_hat = plotballfile('ballrho_95_shape.out')[0]
minus_beta_prime = plotballfile('ballrho_95_shape.out')[1]
ax.plot(s_hat, minus_beta_prime, 'ro', ms = 7)
x_ticks = np.arange(-10, 10, 1)
y_ticks = np.arange(0, 2, .25)
#plt.axis([min(s_hat),max(s_hat),-10,10])
plt.axis([-10,10,0,2])
plt.ylabel("-beta prime")
plt.title("-beta prime vs s_hat (rhoc from .90 to .99)")
plt.xlabel("s_hat")
ax.title.set_fontsize(24)
ax.xaxis.label.set_fontsize(24)
ax.yaxis.label.set_fontsize(24)
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.tick_params(axis='both', which='major', labelsize=20)
ax.tick_params(axis='both', which='minor', labelsize=20)

ax.grid()

plt.show()

