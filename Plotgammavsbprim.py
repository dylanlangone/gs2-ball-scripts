"""
Plots gamma vs bprim or some other independent variable, will later be generalized

@author: Dylan Langone

"""

import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
import numpy as np
import csv
import sys

# variable declarations
gamma  = []
delta_min = float(sys.argv[2])
delta_max = float(sys.argv[3])
delta_step = float(sys.argv[4])
filelistname = sys.argv[1]
plotname = filelistname[:-9] + '.png' 

fields = open(filelistname, "r")
with fields:
	plots = csv.reader(fields, delimiter = ' ')
	newrows = []
	for row in plots:  # for each .out file: 
		# print (row)
		fields2 = open(str(row)[2:-2], "r")
		with fields2:  # go inside each .out file:
			plots2 = csv.reader(fields2, delimiter = ' ') 
			newrows = []
			# filter rows of each .out file
			for row2 in plots2:
				#print (row2)
				newrow = []
				for e in row2:
					if e != '':
						newrow.append(e)
				#print (newrow)
				newrows.append(newrow)
			
			#print (newrows)
		
		fields2.close()

		#calculate max time
		maxTime = 0
		for row in newrows:
			if row[0] == 't=':
				if float(row[1]) > maxTime:
					maxTime = float(row[1])
					
		# print ("The max time is ", maxTime)

		#fill in gamma list
		for row in newrows:
			if (row[0] == 't=' and row[2] == 'aky='):
				if (abs(float(row[1]) - maxTime) < .00001 or float(row[1]) > 500):  # make sure we don't encounter numerical instabilities
					print (row[9])
					gamma.append(float(row[11]))
					break
		

	
delta = np.arange(delta_min, delta_max + .001, delta_step)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
print (gamma)
ax.plot(delta, gamma, 'ro')
#plt.title("gamma vs bprim/bprim_eq for ky = 0.001, N_theta = 212, rho_c = 0.95")
#plt.xlabel("bprim/bprim_eq")
#plt.ylabel("gamma")

ax.xaxis.label.set_fontsize(48)
ax.yaxis.label.set_fontsize(48)
ax.tick_params(axis='both', which='major', labelsize=20)
ax.tick_params(axis='both', which='minor', labelsize=20)
plt.grid(True)
plt.savefig(plotname)
