#-*-coding:utf-8-*-#
import pandas as pd
'''
catering_sale = 'catering_sale.xls'
data = pd.read_excel(catering_sale)
data = data[(data[u'销量']>400)&(data[u'销量']<5000)]
statistics = data.describe()
'''
dish_profile='catering_dish_profit.xls'
data=pd.read_excel(dish_profile,index_col=u'菜品名')
data=data[u'盈利'].copy()
data.sort(ascending = False)

import matplotlib.pyplot as plt #导入图像库
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利(元)')
p = 1.0*data.cumsum()/data.sum()#累计的曲线图
p.plot(color='r',secondary_y=True,style='-o',linewidth=2)
#第一个是值，第二个是目标位置，第三个是标记位置，最后一个是箭头的样式
plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #添加注释，即85%处的标记。这里包括了指定箭头样式。
plt.ylabel(u'盈利（比例）')
plt.show()