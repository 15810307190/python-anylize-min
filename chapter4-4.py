#-*-coding:utf-8-*-
import pandas as pd
inputfile='electricity_data.xls'
outputfile='electricity_data_out.xls'
data=pd.read_excel(inputfile)
data[u'线损率']=(data[u'供入电量']-data[u'供出电量'])/data[u'供入电量']
data.to_excel(outputfile,index=False)