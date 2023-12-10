import sys
src_str = sys.argv[1]
# 对样例进行分割
src_list = src_str.split(";")
tmp_0 = src_list[0]
left_0 = tmp_0.split("=")

# 对1进行分割
tmp_1 = src_list[1]
left_1 = tmp_1.split("=")

# 对2进行分割
tmp_2 = src_list[2]
left_2 = tmp_2.split("=")

# 对3进行分割
tmp_3 = src_list[3]
left_3 = tmp_3.split("=")

# 对4进行分割
tmp_4 = src_list[4]
left_4 = tmp_4.split("=")

# 对5进行分割
tmp_5 = src_list[5]
left_5 = tmp_5.split("=")

# 对6进行分割
tmp_6 = src_list[6]
left_6 = tmp_6.split("=", 1)

if src_str[0] != "#" or src_str[1] != "#":
    print("缺包头")
if src_list[6].split("=")[2][-4:] != "1C80" and src_list[6][-2:] != "\r\n":
    print("缺包尾和包校验")
if src_list[6].split("=")[2][-4:] == "1C80" and src_list[6][-2:] != "\r\n":
    print("缺包尾")
if left_0[0][-2:]!="QN":
    print("缺QN")
if left_1[0] != "ST":
    print("缺ST")
if left_2[0] != "CN":
    print("缺CN")
if left_3[0] != "PW":
    print("缺PW")
if left_4[0] != "MN":
    print("缺MN")
if left_5[0] != "Flag":
    print("缺Flag")
if left_6[0] != "CP":
    print("缺CP")
if src_str[0:2]=="##" and src_str[0:6]!="##0101":
    print("缺长度")
src_str_1 = "##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
if sys.argv[1] == src_str_1:
    print(f"包头:{src_str[0:2]}")  # 输出包头
    print(f"数据端长度:{left_0[0][2:-2]}")  # 输出数据端长度
    print(f"请求码 QN:{left_0[1]}")  # 输出请求码QN
    print(f"系统编码 ST:{left_1[1]}")  # 输出系统编码ST
    print(f"命令编码 CN:{left_2[1]}")  # 输出命令编码CN
    print(f"访问密码 PW:{left_3[1]}")  # 访问密码 PW
    print(f"设备标识 MN:{left_4[1]}")  # 设备标识 MN
    print(f"拆分包及应答标志 Flag:{left_5[1]}")  # 拆分包及应答标志Flag
    print(f"指令参数 CP:{left_6[1][0:18]}")  # 指令参数 CP
    print(f"CRC校验:{left_6[1][-6:-2]}")  # CRC校验
    print("包尾：" + str(hex(int(ord((src_str[-2:-1]))))) + str(hex(int(ord((src_str[-1]))))))