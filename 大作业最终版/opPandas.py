import time
from datetime import datetime
import pandas as pd
#打开文件
file = pd.read_csv('221040100213胡焮铭.csv',encoding='utf-8')

#将NaN值填充为0 分组要求时考虑填充其他平均数、中位数等数值
filefull=file.fillna(value=0)
#表格去重
df = pd.read_csv('221040100213胡焮铭.csv')
df = df.dropna(how='all')

duplicates = df.duplicated()
df = df[~duplicates]
df.to_csv('221040100213胡焮铭.csv', index=False)




#将数据转换为二维DataFrame数据格式
fileDF = pd.DataFrame(filefull)
#print(fileDF)
#提取表头和 列数
header = fileDF.head(0)
cntHeader = len(list(header))
#去重
fileDF= fileDF.drop_duplicates()
aver1= fileDF["w01001-Rtd"].mean()
aver2= fileDF["w01012-Rtd"].mean()
for x in fileDF.index:
    if fileDF.loc[x,"w01001-Rtd"]<=0:
        fileDF.loc[x, "w01001-Rtd"] = aver1
    if fileDF.loc[x,"w01012-Rtd"]<=0:
        fileDF.loc[x, "w01012-Rtd"] = aver2


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
print("查询所有w01001传感器的最大值为：",fileDF["w01001-Rtd"].max())
#此时计算的是 删除日期非法后的，季度数据
#季度数据在日期剔除前剔除后进行？
# newFileDF= fileDF.loc[(fileDF["w01001-Rtd"]>0) & (fileDF["w01012-Rtd"]>0) ]

newDF=pd.DataFrame(columns=["QN","ST","CN","PW","MN","Flag","DataTime","w01001-Rtd","w01012-Rtd"])

for x in fileDF.index:
    current_time=datetime.strptime(str(fileDF.loc[x,'DataTime']),format)
    if 4<=current_time.month<=6:
        newDF=newDF._append(fileDF.loc[x])

# 差，将第二季度存到新dataframe数据中，进行w01001-Rtd的中位数统计比较【cy】
max_w1=newDF["w01001-Rtd"].median()
max_w2=newDF["w01012-Rtd"].median()
max_ww=max(max_w1,max_w2)
print("查询第二季度的w01001和w01012中的中位数最大值为",max_ww)