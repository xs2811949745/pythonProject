import time
from datetime import datetime
import pandas as pd
#打开文件
file = pd.read_csv('221040100213胡焮铭.csv',encoding='utf-8')
print(file)

#将NaN值填充为0 分组要求时考虑填充其他平均数、中位数等数值
filefull=file.fillna(value=0)
print("filefull set 0 :\n",filefull)


#将数据转换为二维DataFrame数据格式
fileDF = pd.DataFrame(filefull)
#print(fileDF)
#提取表头和 列数
header = fileDF.head(1)
cntHeader = len(list(header))
#print(cntHeader)
#
# #获取 QN 列的行数
current_col_list = list(fileDF['DataTime'])
format = "%Y%m%d%H%M%S%f"

for x in fileDF.index:

   try:
       d=datetime.strptime(str(fileDF.loc[x,'DataTime']),format)
   except:
       fileDF.drop(x,inplace=True)




cntRow = len(current_col_list)
#print(cntRow)
#按行计算值
#print(fileDF["MN"])


for i in range(cntRow) :
    file_row = fileDF.iloc[i,-3:]
    print("row\n",file_row)
    #print("LA1-Rtd",file_row["LA1-Rtd"])
    #print("LA2-Rtd", file_row["LA2-Rtd"])

    file_row_sum = file_row[["LA1-Rtd","LA2-Rtd"]].sum()
    print('累加和', file_row_sum)
    file_row_max = file_row[["LA1-Rtd","LA2-Rtd"]].max()
    print('最大值',file_row_max)
    file_row_min = file_row[["LA1-Rtd","LA2-Rtd"]].min()
    print('最小值',file_row_min)
    file_row_mean = file_row[["LA1-Rtd","LA2-Rtd"]].mean()
    print('平均值',file_row_mean)
    file_row_var = file_row[["LA1-Rtd","LA2-Rtd"]].var()
    print('方差', file_row_var)
    file_row_std = file_row[["LA1-Rtd","LA2-Rtd"]].std()
    print('标准差', file_row_std)
    print('%' * 20)
print('' * 20)
print('#' * 20)


# 查询到 某个列符合某个或者某几个条件的数据
newFileDF= fileDF.loc[(fileDF["LA1-Rtd"]>0) & (fileDF["LA2-Rtd"]>0) ]
print("符合条件的新DataFrame",newFileDF)

print("*******************")
#按列计算值
for j in range(cntHeader-2,cntHeader) :
    coldata = newFileDF.loc[:, list(header)[j]]
    #print(coldata)
    #print(fileDF.columns[j])
    lineone_sum = coldata.sum()
    print(newFileDF.columns[j],'列 总和',lineone_sum)
    lineone_mean = coldata.mean()
    print(newFileDF.columns[j], '列 平均值', lineone_mean)
    lineone_max = coldata.max()
    print(newFileDF.columns[j], '列 最大值', lineone_max)
    lineone_min = coldata.min()
    print(newFileDF.columns[j], '列 最小值', lineone_min)
    lineone_std = coldata.std()
    print(newFileDF.columns[j], '列 标准差值', lineone_std)
    lineone_var = coldata.var()
    print(newFileDF.columns[j], '列 方差', lineone_var)
    print('#' * 20)
