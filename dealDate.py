import csv
from collections import defaultdict
from sklearn import cluster
import numpy as np
f=csv.reader(open("data.csv"))
mydict=defaultdict(int)
tag=0
for line in f:
    tag += 1
    if tag==1:
        continue
    mydict[line[1]]+=1
print(sorted(mydict.items(),key=lambda item:item[1],reverse=True))
'''
scipy
'''
from scipy.optimize import fsolve
def f(x):
    x1=x[0]
    x2=x[1]
    return [x1-x2,x1+x2]
result=fsolve(f,[1,1])
print result