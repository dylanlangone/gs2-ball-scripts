# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:28:51 2019

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

filelist = ['ballr90.out', 'ballr80.out', 'ballr70.out']


s_hat = minus_beta_prime = []

for file in filelist:
	s_hat = plotballfile(file)[0]
	minus_beta_prime = plotballfile(file)[1]
	if (file == 'ballr90.out'):
		s_hat = [x - .8 for x in s_hat]
		minus_beta_prime = [x - .375 for x in minus_beta_prime]
		ax.plot([-.422-.8], [-.849 - .375], 'bo', ms = 10)
	elif (file == 'ballr80.out'):
		s_hat = [x - .6 for x in s_hat]
		minus_beta_prime = [x - .3 for x in minus_beta_prime]
		ax.plot([-4.54-.6], [-.849 - .3], 'bo', ms = 10)
	elif (file == 'ballr70.out'):
		s_hat = [x - .2 for x in s_hat]
		minus_beta_prime = [x - .1 for x in minus_beta_prime]
		ax.plot([-5.16-.2], [-.36 - .1], 'bo', ms = 10)
		
	ax.plot(s_hat, minus_beta_prime, 'ko', ms = 2)
	
#ax.plot(s_hat,minus_beta_prime,'ro')



x_ticks = np.arange(-6, 5.0001, 1)
y_ticks = np.arange(0, 1.0001, .25)
#plt.axis([min(s_hat),max(s_hat),-10,10])
plt.axis([-1.5,5.01,0,1.01])
#plt.ylabel("-beta prime")
#plt.title("-beta prime vs s_hat (rhoc from .90 to .99)")
#plt.xlabel("s_hat")
#ax.title.set_fontsize(24)
ax.xaxis.label.set_fontsize(24)
ax.yaxis.label.set_fontsize(24)
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.tick_params(axis='both', which='major', labelsize=20)
ax.tick_params(axis='both', which='minor', labelsize=20)

ax.grid()

plt.show()

