"""
PLots gamma vs bprime or some other independent variable, will later be generalized

@author: Dylan Langone

"""

import matplotlib.pyplot as plt
import numpy as np
import csv
gamma  = []
filename = input("Enter filename\n")
fields = open(filename, "r")
with fields:
	gammas = csv.reader(fields)
	for row in gammas:
		gamma.append(row[0][:-1])
	fields.close()
for k in range(0, len(gamma)):
	gamma[k] = float(gamma[k])
	
bprim = np.arange(0.00, .496, .005)
plt.plot(bprim, gamma, 'ro')
plt.title("gamma vs bakdif for ky = 0.002, delta = 3.65, s_hat = 1.445 at rhoc = 0.95")
plt.xlabel("bakdif")
plt.ylabel("gamma")
plt.grid(True)
plt.show()