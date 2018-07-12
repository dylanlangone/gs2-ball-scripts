# -*- coding: utf-8 -*-
"""
Created on July 12 2018

@author: Dylan Langone, University of Maryland

READ: This code is for plotting flux surfaces for .g files generated
by a gs2 run.  
"""
import matplotlib.pyplot as plt
import numpy as np
import csv
import math

fileName = input('Enter .g filename: \n')
fields = open(fileName, 'r')


#xIndex = int(input('Enter column number for x-axis parameter: \n')) - 1
#yIndex = int(input('Enter column number for y-axis parameter: \n')) - 1

# arrays for theta, r, z coordinates of points on the flux surface, 
# to be converted to Cartesian coordinates for plotting
theta = []
r = []
z = []

#fill in data for x, y arrays
with fields:
    plots = csv.reader(fields, delimiter = ' ')
    for row in plots:
        if not row[0] == '#':
            newRow = []
            for e in row:
                if not e == '':
                    newRow.append(e)
                
            #print (newRow)
            theta.append(float(newRow[0]))
            r.append(float(newRow[1]))
            z.append(float(newRow[2]))
            
        
# x = np.zeros(len(theta))
# for i in range(0, len(theta)):
	# x[i] = (r[i]*math.cos(theta[i]))


fields.close()

plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')   
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.grid(True)
plt.show()
