import numpy as np
str_arr = np.loadtxt("OpD.csv",delimiter=",", dtype=str)
num_arr=np.genfromtxt('OpD.csv',delimiter=',')
num_arr[np.isnan(num_arr)]=0
output_arr=num_arr[1:,3:]
print(output_arr.shape)
month1_arr=num_arr[1:,3]
month2_arr=num_arr[1:,4]
month3_arr=num_arr[1:,5]

print("month1 sum:\n",month1_arr.sum())
print("month2 sum:\n",month2_arr.sum())
print("month3 sum:\n",month3_arr.sum())

print("output sum:\n",output_arr.sum())

sum_product=np.sum(output_arr, axis=1)
print("sum_max_product:\n",sum_product.max())
print("sum_min_product:\n",sum_product.min())
print("var_product:\n",output_arr.var())

mean_product=np.mean(output_arr, axis=1)
max_product=np.max(output_arr, axis=1)
min_product=np.min(output_arr, axis=1)
sum_product=np.sum(output_arr, axis=1)
for i in range(len(str_arr)):
    if i==0:
        print(str_arr[i])
    else:
        print(str_arr[i],'本月最大值为：',max_product[i-1],'本月平均值为:',mean_product[i-1],'本月最小值为：',min_product[i-1],'本月总计销售值为：',sum_product[i-1])
