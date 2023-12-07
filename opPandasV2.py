import time
from datetime import datetime
import pandas as pd
#打开文件
file = pd.read_csv('221040100213胡焮铭.csv',encoding='utf-8')

#将NaN值填充为0 分组要求时考虑填充其他平均数、中位数等数值
filefull=file.fillna(value=0)
# print("filefull set 0 :\n",filefull)


#将数据转换为二维DataFrame数据格式
fileDF = pd.DataFrame(filefull)
#print(fileDF)
#提取表头和 列数
header = fileDF.head(0)
cntHeader = len(list(header))
#print(cntHeader)
#
# #获取 QN 列的行数


# for i in range(cntRow) :
#     file_row = fileDF.iloc[i,-3:]
#     print("row\n",file_row)
#     print("w01001-Rtd",file_row["w01001-Rtd"])
#     print("w01012-Rtd", file_row["w01012-Rtd"])
#     file_row_sum = file_row[["w01001-Rtd","w01012-Rtd"]].sum()
#     print('累加和', file_row_sum)
#     file_row_max = file_row[["w01001-Rtd","w01012-Rtd"]].max()
#     print('最大值',file_row_max)
#     file_row_min = file_row[["w01001-Rtd","w01012-Rtd"]].min()
#     print('最小值',file_row_min)
#     file_row_mean = file_row[["w01001-Rtd","w01012-Rtd"]].mean()
#     print('平均值',file_row_mean)
#     file_row_var = file_row[["w01001-Rtd","w01012-Rtd"]].var()
#     print('方差', file_row_var)
#     file_row_std = file_row[["w01001-Rtd","w01012-Rtd"]].std()
#     print('标准差', file_row_std)
#     print('%' * 20)
#
# print('' * 20)
# print('#' * 20)

for x in fileDF.index:
    if fileDF.loc[x,"w01001-Rtd"]<=0:
        fileDF.loc[x, "w01001-Rtd"] = fileDF["w01001-Rtd"].mean()
    if fileDF.loc[x,"w01012-Rtd"]<=0:
        fileDF.loc[x, "w01012-Rtd"] = fileDF["w01012-Rtd"].mean()
# 查询到 某个列符合某个或者某几个条件的数据
# newFileDF= fileDF.loc[(fileDF["w01001-Rtd"]>0) & (fileDF["w01012-Rtd"]>0) ]
# print("符合条件的新DataFrame",newFileDF)
#
# print("*******************")
#按列计算值
# for j in range(cntHeader-2,cntHeader) :
#     coldata = newFileDF.loc[:, list(header)[j]]
#     #print(coldata)
#     #print(fileDF.columns[j])
#     lineone_sum = coldata.sum()
#     print(newFileDF.columns[j],'列 总和',lineone_sum)
#     lineone_mean = coldata.mean()
#     print(newFileDF.columns[j], '列 平均值', lineone_mean)
#     lineone_max = coldata.max()
#     print(newFileDF.columns[j], '列 最大值', lineone_max)
#     lineone_min = coldata.min()
#     print(newFileDF.columns[j], '列 最小值', lineone_min)
#     lineone_std = coldata.std()
#     print(newFileDF.columns[j], '列 标准差值', lineone_std)
#     lineone_var = coldata.var()
#     print(newFileDF.columns[j], '列 方差', lineone_var)
#     print('#' * 20)

current_col_list = list(fileDF['DataTime'])
cntRow = len(current_col_list)
#下面对日期进行剔除
format = "%Y%m%d%H%M%S"
for x in fileDF.index:
   try:
       d =datetime.strptime(str(fileDF.loc[x,'DataTime']),format)
       a=time.localtime()#获取当前时间
       a=time.mktime(a)#转化为时间戳
       a=datetime.fromtimestamp(a)#转化为format格式

       if(d>a or a.year>d.year):
           fileDF.drop(x, inplace=True)
   except:
       fileDF.drop(x,inplace=True)

max_w1=0
max_w2=0
fileDF["w01001-Rtd"] = fileDF["w01001-Rtd"].astype(float)
fileDF["w01012-Rtd"] = fileDF["w01012-Rtd"].astype(float)
print("w01001传感器的最大值为：",fileDF["w01001-Rtd"].max())
#此时计算的是 删除日期非法后的，季度数据
#季度数据在日期剔除前剔除后进行？
# newFileDF= fileDF.loc[(fileDF["w01001-Rtd"]>0) & (fileDF["w01012-Rtd"]>0) ]
# for x in fileDF.index:
#     newFileDF_w1=fileDF.loc[(datetime.strptime(str(fileDF.loc[x,'DataTime']),format).month>=4 & datetime.strptime(
#         str(fileDF.loc[x,'DataTime']),format).month<=6)]
#
#     newFileDF_w2 = (datetime.strptime(str(fileDF.loc[x, 'DataTime']), format).month >= 4 & datetime.strptime(
#         str(fileDF.loc[x, 'DataTime']), format).month <= 6)

# 差，将第二季度存到新dataframe数据中，进行w01001-Rtd的中位数统计比较【cy】
max_ww=max(max_w1,max_w2)
print("第二季度中w01001和w01012中的中位数最大值为"+max_ww)