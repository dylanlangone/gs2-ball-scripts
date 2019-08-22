import csv
import pandas as pd
import sys

df2 = pd.read_csv(sys.argv[2])
df3 = pd.read_csv(sys.argv[3])
s_hat = 4*[df2['s_hat'][4]] + 4*[df2['s_hat'][9]] + 4*[df2['s_hat'][8]]
b_prim = 4*[df2['b_prim'][4]] + 4*[df2['b_prim'][9]] + 4*[df2['b_prim'][8]]
beta = 4*[df3['beta'][0]] + 4*[df3['beta'][1]] + 4*[df3['beta'][2]]
tprim1 = [0.0, .5*df3['gradeq'][0], .6666*df3['gradeq'][0], df3['gradeq'][0]]
fprim1 = [df3['gradeq'][0], .5*df3['gradeq'][0], .3333*df3['gradeq'][0], 0.0]
tprim2 = [0.0, .5*df3['gradeq'][1], .6666*df3['gradeq'][1], df3['gradeq'][1]]
fprim2 = [df3['gradeq'][1], .5*df3['gradeq'][1], .3333*df3['gradeq'][1], 0.0]
tprim3 = [0.0, .5*df3['gradeq'][2], .6666*df3['gradeq'][2], df3['gradeq'][2]]
fprim3 = [df3['gradeq'][2], .5*df3['gradeq'][2], .3333*df3['gradeq'][2], 0.0]
tprim = tprim1 + tprim2 + tprim3
fprim = fprim1 + fprim2 + fprim3
#print s_hat
rho = [.5, .5, .5, .5, .75, .75, .75, .75, .9, .9, .9, .9]
df = pd.DataFrame(rho, columns = ['rho'])
df['s_hat'] = s_hat
df['b_prim'] = b_prim
df['beta'] = beta
df['tprim'] = tprim
df['fprim'] = fprim
#print df
df.to_csv(sys.argv[1])
