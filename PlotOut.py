# -*- coding: utf-8 -*-
"""
Created on Mar 22 15:01:17 2018

@author: Dylan Langone

READ: This code is used for plotting the growth rate gamma or eigenfrequency omegan vs 
the ky or kx wave number from a .out file generated by a gs2 run

Look below for where to specify the parameters to be plotted
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

def whatToPlot(k, om):
    result = ['','']
    if (k == 'ky'):
        result[0] = 3
    if (k == 'kx'):
        result[0] = 5
    if (om == 'omegan'):
        result[1] = 10
    if (om == 'gamma'):
        result[1] = 11
    if (result[0] == '' or result[1] == ''):
        raise ValueError('Enter \'ky\', \'kx\', \'omegan\', or \'gamma\'')
    return result


fileNames = input('Enter .out filenames\n').split(' ')

#edit to specify which columns of .out file to plot
xLabel = input('Enter x-axis parameter: ky or kx\n')
yLabel = input('Enter y-axis parameter: omegan or gamma\n')
xIndex, yIndex = whatToPlot(xLabel, yLabel)


#print (xIndex, ' ', yIndex)
x = []
y = []

for fileName in fileNames:
    fields = open(fileName, 'r')
    #create parsed array of data
    with fields:
        plots = csv.reader(fields, delimiter = ' ')
        newrows = []
        for row in plots:
            #print (row)
            newrow = []
            for e in row:
                if e != '':
                    newrow.append(e)
            #print (newrow)
            newrows.append(newrow)
        
        #print (newrows)
        
    fields.close()
    
    #calculate max time
    maxTime = 0
    for row in newrows:
        if row[0] == 't=':
            if float(row[1]) > maxTime:
                maxTime = float(row[1])
                
    print ("The max time is ", maxTime)
    
    #fill the x and y arrays
    for row in newrows:
        if (row[0] == 't=' and row[2] == 'aky='):
            if abs(float(row[1]) - maxTime) < .00001:
                x.append(float(row[xIndex]))
                y.append(float(row[yIndex]))
        
plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
plt.rcParams.update({'font.size': 32})
plt.grid(True)
plt.title(yLabel + " vs " + xLabel)
plt.xlabel(xLabel, fontsize = 32)
plt.ylabel(yLabel, fontsize = 32)
xMax = x[len(x) - 1]
yMin = min(y)
yMax = max(y)       
plt.plot(x, y, '-')
plt.axis([0, xMax, yMin, yMax]) 
plt.show()

    