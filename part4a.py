import csv
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], names=['gradeq', 'beta'])
df2 = pd.read_csv(sys.argv[2])
df3 = pd.read_csv(sys.argv[3], names=['s_hat_avg'])
rho = ['0.5', '0.75', '0.9']
s_hat = [df3['s_hat_avg'][0], df3['s_hat_avg'][1], df3['s_hat_avg'][2]]
b_prim = [df2['b_prim'][5], df2['b_prim'][9], df2['b_prim'][8]]
df['rho'] = rho
df['s_hat'] = s_hat
df['b_prim'] = b_prim
df.to_csv(sys.argv[1])
