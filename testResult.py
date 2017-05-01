#-*-coding:utf-8-*-
result=[0]+[2]+[3]#list相加是扩展
list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
print [list1[i]+list2[i] for i in range(len(list2))]
print result