#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
'''
catering_sale='catering_sale_all.xls'
data=pd.read_excel(catering_sale)
print data.corr(method='spearman')
print data.corr()[u'百合酱蒸凤爪']
print data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺'])
'''
data=pd.DataFrame(np.random.randn(6,5))
data2=pd.DataFrame([range(0,7),range(1,8)])
print data
print data2
s1=data2.loc[0]
s2=data2.loc[1]
print s1.corr(s2)

'''
cumsum
rolling_sum
'''
data=pd.Series(range(0,10))
print data
print data.cumsum()
print pd.rolling_sum(data,2)

#x=range(0,10)
x=np.linspace(0,10)
y=np.sin(x)
'''
plot
'''
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.figure(1)
plt.plot(x,y,'b*--')
plt.show()
'''
pie
'''
plt.figure(2)
labels='Frogs','Hogs','Dogs','Logs'#标签
sizes=[15,30,45,10]#每块大小
colors=['yellowgreen','gold','lightskyblue','lightcoral']#每块颜色
explode=[0,0.1,0,0]#突出显示

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')#显示为圆，避免压缩显示为椭圆
plt.show()

plt.figure(3)
x=np.random.randn(1000)
plt.hist(x,10)#第二个参数为间隔
plt.show()

plt.figure(4)
x=np.random.randn(1000)
D=pd.DataFrame([x,x+1]).T
D.plot(kind='box')
plt.show()

plt.figure(5)
x=pd.Series(np.exp(np.arange(200)))
x.plot(label=u'原始数据',legend=True)
plt.show()
x.plot(logy=True,label=u'对数数据图',legend=True)
plt.show()

plt.figure(6)
error = np.random.randn(10)
y=pd.Series(np.sin(np.arange(10)))
print 'error:',error,'y:',y
y.plot(yerr = error)
plt.show()