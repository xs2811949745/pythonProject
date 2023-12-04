import pandas as pd
#打开文件
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
    file_row = fileDF.iloc[i,3:-1]
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
   