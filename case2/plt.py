import matplotlib.pyplot as plt
import csv
x=[]
y=[]

# 打开待画图数据
with open('csvfile1.csv', 'r') as csvfile:
    # 读文件中的数据
    plots= csv.reader(csvfile, delimiter=',')
    # 按行取出
    for row in plots:
        # 获取第一列数据
        x.append(int(row[0]))
        # 获取第二列数据        
        y.append(int(row[1]))

# 设置x，y轴和点类型数据到画图对象中
plt.plot(x,y, marker='o')

# 设置标题
plt.title('Data from the CSV File: Month and Cost')
# 设置X轴
plt.xlabel('month')
# 设置Y轴
plt.ylabel('cost')

# 保存成指定名称的图片到运行目录
plt.savefig('myplot.png')

# 显示一下，根据情况不调用则不显示
plt.show()
