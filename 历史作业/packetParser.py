# coding=gbk
# import sys
#
# #if __name__ == "__main__":
# #     print(f"Arguments count: {len(sys.argv)}")
# #     for i, arg in enumerate(sys.argv):
# #         print(f"Argument {i:>6}: {arg}")
#
# src_str = "##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
#
# ## 尝试打印从包头往后的数据包
# print(src_str[2:])
#
# # 按 ; 号 将字符串用split 切分
# src_list = src_str.split(";")
# # 分别打印每个src_list内的元素
# print(src_list[0])
# print(src_list[1])
# print(src_list[2])
# print(src_list[3])
# print(src_list[4])
# print(src_list[5])
# print(src_list[6])
# # print(src_list[7])
#
# ## 处理包头分别取 长度 和 QN
# tmp = src_list[0]
# left = tmp.split("=")
# print(left)
# print(left[0][2:-2])
# print(left[1])


### python
# ref:   https://realpython.com/python-command-line-arguments/

# main.py
# import sys
# # argv.py
# import sys
#
# print(f"Name of the script      : {sys.argv[0]=}")
# print(f"Arguments of the script : {sys.argv[1:]=}")
# # if __name__ == "__main__":
# #     print(f"Arguments count: {len(sys.argv)}")
# #     for i, arg in enumerate(sys.argv):
# #         print(f"Argument {i:>6}: {arg}")

'''
python main.py Python Command Line Arguments
Arguments count: 5
Argument      0: main.py
Argument      1: Python
Argument      2: Command
Argument      3: Line
Argument      4: Arguments
'''

# str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
# str1=str.split(";")
# str1=str.split("=")
# print(str)
#
# print(str1[0][0:2])
# print(str1[0][2:6])
# print(str1[1][:-3])
# print(str1[2][:-3])
# print(str1[3][:-3])
# print(str1[4][:-3])
# print(str1[5][:-5])
# print(str1[6][:-3])
# print(str1[7])




### python
# ref:   https://realpython.com/python-command-line-arguments/

# main.py
import sys

# if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
# print(f"Arguments count: {len(sys.argv)}")
# print(sys.argv)
# print(sys.argv[1])

# src_str = sys.argv[1]
# 此行以下是v1.0的程序
i=0
flag=0
src_str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
# 按 ; 号 将字符串用split 切分
src_list = src_str.split(";")
src_equal = src_str.split("=")
print(src_list)
print(src_equal)
    ## 尝试打印从包头往后的数据包
print(f"打印包头往后的数据",src_str[2:])
if src_str[0:2]!='##':
    i+=1
    print("缺包头")
if src_equal[0][-6:-2]!="0101" and src_list[0][2:6]!="0101" and src_equal[0]!="0101":
    i+=1
    print("缺长度")
if src_equal[0][-2:]!="QN":
    i+=1
    print("缺请求码QN")
if src_list[1][0:2]!="ST":
    i+=1
    print("缺系统编码ST")
if src_list[2][0:2]!="CN":
    i+=1
    print("缺命令编码CN")
if src_list[3][0:2]!="PW":
    i+=1
    print("缺访问密码PW")
if src_list[4][0:2]!="MN":
    i+=1
    print("缺设备标识MN")
if src_list[5][0:4]!="Flag":
    i+=1
    print("缺拆分包及应答标签Flag")
if src_list[6][0:2]!="CP":
    i+=1
    print("缺指令参数CP")
if src_equal[-1][4:9]!="1C80" and src_list[-1][-2:]!="\r\n":
    i+=1
    flag+=1
    print("缺CRC校验和包尾")
if src_equal[-1][-2:]!="\r\n" and src_list[-1][-2:]!="\r\n"and flag==0:
    i+=1
    print("缺包尾")
if i==0:
    print(f"包头:"+src_str[0:2])  # 输出包头
    print(f"数据端长度:"+src_equal[0][2:-2])  # 输出数据端长度
    print(f"请求码 QN"+src_equal[1].split(";")[0])  # 输出请求码QN
    print(f"系统编码 ST:"+src_equal[2].split(";")[0])  # 输出系统编码ST
    print(f"命令编码 CN:"+src_equal[3].split(";")[0])  # 输出命令编码CN
    print(f"访问密码 PW:"+src_equal[4].split(";")[0])  # 访问密码 PW
    print(f"设备标识 MN:"+src_equal[5].split(";")[0])  # 设备标识 MN
    print(f"拆分包及应答标志 Flag:"+src_equal[6].split(";")[0])  # 拆分包及应答标志Flag
    print(f"指令参数 CP:"+src_equal[7].split(";")[0])  # 指令参数 CP
    print(f"CRC校验:"+src_equal[8][-6:-2])  # CRC校验
    print("包尾：" + str(hex(int(ord((src_str[-2:-1]))))) + str(hex(int(ord((src_str[-1]))))))


"""    
# 分别打印每个src_list内的元素
print(src_list[0])
print(src_list[1])
print(src_list[2])
print(src_list[3])
print(src_list[4])
print(src_list[5])
print(src_list[6])
    ##print(src_list[7])

    ## 处理包头分别取 长度 和 QN
tmp = src_list[0]
left = tmp.split("=")
print(left)
print(left[0][2:-2])
print(left[1])
"""
'''
python main.py Python Command Line Arguments
Arguments count: 5
Argument      0: main.py
Argument      1: Python
Argument      2: Command
Argument      3: Line
Argument      4: Arguments'''







