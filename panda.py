# coding=utf-8
import pandas as pd
import numpy as s
import matplotlib as a
data =[['Gool',10],['runoob',13],['wikl',12]]
# df = pd.DataFrame(data,columns=['Site','Age'],dtype=float)
# df = pd.DataFrame(data,columns=['Site','Age'])
# df['Age']=df['Age'].astype('float')
# df['Site']=df['Site'].astype('string')
# data={'a':['123','s','saas'],'b':['a','b','111']}
#
# df=pd.DataFrame(data)
#
# print(df)
# data1=[{'a':1,'b':2,'c':3},{'d':56}]
# df=pd.DataFrame(data1)
# print(df)


#data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# # 数据载入到 DataFrame 对象
# df = pd.DataFrame(data)
# print(df)
# print(df.loc[0])
# print(df.loc[1])
# print(df.loc[2])

import pandas as pd
import json
# df = pd.read_csv('nba.csv')
# import pandas as pd
#
# df = pd.read_csv('nba.csv')

# print(df)
# print(df.to_string())
# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# # 数据载入到 DataFrame 对象
# df = pd.DataFrame(data)
#
# # 返回第一行和第二行
# print(df.loc[[0, 1]])

# name=['google','taobao','runoob','wiki']
# st=['www.google.com','www.taobao.com','www.runoob.com','www.wiki.com']
# ag=['12','13','14','15']
# dict={'name':name,'site':st,'age':ag}
# df=pd.DataFrame(dict)
# df.to_csv('test1.csv')
# ad=pd.read_csv('test1.csv')
# print(ad.to_string())
# print(df)

# import pandas as pd

# df = pd.read_json('sites.json')
#
# print(df.to_string())



#import pandas as pd
#
# data =[
#     {
#       "id": "A001",
#       "name": "菜鸟教程",
#       "url": "www.runoob.com",
#       "likes": 61
#     },
#     {
#       "id": "A002",
#       "name": "Google",
#       "url": "www.google.com",
#       "likes": 124
#     },
#     {
#       "id": "A003",
#       "name": "淘宝",
#       "url": "www.taobao.com",
#       "likes": 45
#     }
# ]
# df = pd.DataFrame(data)
#
# print(df)
# 字典格式的 JSON
# s = {
#     "col1":{"row1":1,"row2":2,"row3":3},
#     "col2":{"row1":"x","row2":"y","row3":"z"}
# }
#
# # 读取 JSON 转为 DataFrame
# df = pd.DataFrame(s)
# print(df)



# import pandas as pd
#
# df = pd.read_csv('property-data.csv')
#
# print (df['NUM_BEDROOMS'])
# print (df['NUM_BEDROOMS'].isnull())

# import pandas as pd
#
# df = pd.read_csv('property-data.csv')
#
# new_df = df.dropna(inplace=True)
#
# print(new_df.to_string())

import pandas as pd
#打开文件
#file = pd.read_csv('OpD.csv',encoding='utf-8')
file = pd.read_csv('OpD.csv',encoding='gbk')
print(file)
#将NaN值填充为0
filefull=file.fillna(value=0)
print("filefull set 0 :\n",filefull)
#将数据转换为二维DataFrame数据格式
fileDF = pd.DataFrame(filefull)
print(fileDF)
#提取表头和 列数
header = fileDF.head(1)
n = len(list(header))
#获取 行数
rowall = list(fileDF['ID'])
m = len(rowall)
print(m)
#按行计算值
for i in range(m) :
    print('第',i+1,'号 产品销量信息')
    file_row = fileDF.iloc[i,4:]
    file_row_sum = file_row.sum()
    print('总销量', file_row_sum)
    file_row_max = file_row.max()
    print('最大值',file_row_max)
    file_row_min = file_row.min()
    print('最小值',file_row_min)
    file_row_mean = file_row.mean()
    print('平均值',file_row_mean)
    file_row_var = file_row.var()
    print('方差', file_row_var)
    file_row_std = file_row.std()
    print('标准差', file_row_std)
    print('%' * 20)
print('' * 20)
print('#' * 20)
#按列计算值
for j in range(4,n) :
    print('第',j - 3,'月 数据')
    lineone = fileDF.loc[:,list(header)[j]]
    print(lineone)
    lineone_sum = lineone.sum()
    print('第',j - 3,'月 销量总和',lineone_sum)
    lineone_mean = lineone.mean()
    print('第', j - 3, '月 销量平均值', lineone_mean)
    lineone_max = lineone.max()
    print('第', j - 3, '月 销量最大值', lineone_max)
    lineone_min = lineone.min()
    print('第', j - 3, '月 销量最小值', lineone_min)
    lineone_std = lineone.std()
    print('第', j - 3, '月 销量标准差值', lineone_std)
    lineone_var = lineone.var()
    print('第', j - 3, '月 销量方差', lineone_var)
    print('#' * 20)
