#-*-coding:utf-8-*-#
from scipy.optimize import fsolve
#get result
def f(x):
    x1=x[0]
    x2=x[1]
    return [x1-x2-1,x1+x2-1]
result=fsolve(f,[1,1])
#zero is 5.55111512e-17
print result

'''
Scipy----matrix
Numpy----array
Matplotlib----make picture
Pandas----date analyze
'''
'''
numpy
'''
import numpy as np
a=np.array([[2,0,1,5],[3,2,4,1]])
print(a*a)
'''
matplot
'''
import matplotlib.pyplot as plt
x=np.linspace(0,10,1000)
y=np.sin(x)
z=np.cos(x)

plt.figure(figsize=(8,4))#resize picture
plt.plot(x,y,label='$\sinx$',color='red',linewidth=2)
plt.plot(x,z,'b--',label='$\cosx$',color='blue')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('A simple examples')
plt.ylim(-2.2,2.2)
plt.legend()
plt.show()

import pandas as pd
s=pd.Series([1,2,3],index=['a','b','c'])
d=pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])
d2=pd.DataFrame(s)

print d
print d2

print d.head()
print d.describe()

#pd.read_excel('data.xls')
p=pd.read_csv('data.csv',encoding='utf-8')
print p

'''
   a  b  c
0  1  2  3
1  4  5  6
   0
a  1
b  2
c  3
   a  b  c
0  1  2  3
1  4  5  6
             a        b        c
count  2.00000  2.00000  2.00000
mean   2.50000  3.50000  4.50000
std    2.12132  2.12132  2.12132
min    1.00000  2.00000  3.00000
25%    1.75000  2.75000  3.75000
50%    2.50000  3.50000  4.50000
75%    3.25000  4.25000  5.25000
max    4.00000  5.00000  6.00000
   id name  time
0   1    a    11
1   2    a    12
2   3    b    11
3   4    b    12
4   5    b    13
5   6    d    11
6   7    c    11
'''
'''
statsmodels
'''
from statsmodels.tsa.stattools import adfuller as ADF
print ADF(np.random.rand(100))
