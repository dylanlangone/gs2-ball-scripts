# -*- coding: utf-8 -*-
"""
Created on Mar 20 22:46:24 2018

@author: Dylan Langone

READ: This code is for plotting the real and imaginary parts of phi or the 
eigenfunctions vs the z coordinate for .fields or .eigenfunc file generated
by a gs2 run.  

"""
import matplotlib.pyplot as plt
import numpy as np
import csv

#edit to specify filename
fileName = input('Enter .fields or .eigenfunc file: \n')
fields = open(fileName, 'r')


xIndex = int(input('Enter column number for x-axis parameter: \n')) - 1
yIndex = int(input('Enter column number for y-axis parameter: \n')) - 1


x = []
y = []

#fill in data for x, y arrays
with fields:
    plots = csv.reader(fields, delimiter = ' ')
    for row in plots:
        if not row == []:
            newRow = []
            for e in row:
                if not e == '':
                    newRow.append(e)
                
            #print (newRow)
            x.append(newRow[xIndex])
            y.append(newRow[yIndex])
            
        
        

fields.close()
plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')        
plt.plot(x, y)
plt.show()

