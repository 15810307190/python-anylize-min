#-*- coding:utf-8 -*-
import pandas as pd
from scipy.interpolate import lagrange

inputfile = 'catering_sale.xls'
outputfile= 'sales.xls'

data = pd.read_excel(inputfile)#读取excel
data[u'销量'][(data[u'销量']<400)|(data[u'销量']>5000)]=None#异常值变为空值

def ployinterp_column(s,n,k=5):
    tem=list(range(n-k,n))+list(range(n+1,n+1+k))
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    y=y[y.notnull()]
    teml=lagrange(y.index,list(y))
    return lagrange(y.index,list(y))(n)
for i in data.columns:
    if i==u'日期':
        continue
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)
data.to_excel(outputfile)