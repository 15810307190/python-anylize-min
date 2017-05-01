#-*-coding:utf-8-*-
import pandas as pd
input_file="principal_component.xls"
output_file="principal_component_out.xls"

data=pd.read_excel(input_file,header=None)

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)
print pca.components_,len(pca.components_)#返回特征向量
print pca.explained_variance_ratio_#返回各个成分的方差百分比

pca=PCA(3)
pca.fit(data)
low_d = pca.transform(data)#降低纬度
pd.DataFrame(low_d).to_excel(output_file)#保存文件
print "================",pca.inverse_transform(low_d)#复原数据