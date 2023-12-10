# coding=gbk
src_str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
tem=src_str.split(";")
a=0
if src_str[0:2]!="##":
    print("缺包头")
    a=1
elif  src_str[0:4]=="##QN":
    print("缺长度")
    a = 1
elif src_str[6:8]!="QN":
    print("缺请求码QN")
    a = 1
elif src_str[27:29]!="ST":
    print("缺系统编码 ST")
    a = 1
elif src_str[33:35]!="CN":
    print("缺命令编码 CN")
    a = 1
elif src_str[41:43]!="PW":
    print("缺访问密码PW")
    a = 1
elif src_str[51:53]!="MN":
    print("缺设备标识MN")
    a = 1
elif src_str[79:83]!="Flag":
    print("缺拆分包及应答标志Flag")
    a = 1
elif tem[6][0:2] != 'CP':
    print("缺指令参数")
    a = 1
elif tem[6][21:25] != '1C80':
    print("缺CRC校验")
    a = 1
elif  src_str[-2:]!='\r\n':
    print("缺包尾")
    a = 1
if a==0:
    print("包头：" + tem[0][0] + tem[0][1])
    print("数据端长度：" + src_str.split("=")[0][-6:-2])
    print("请求码QN：" + src_str.split("=")[1][:-3])
    print("系统编码 ST：" + tem[1][3:])
    print("命令编码 CN：" + tem[2][3:])
    print("访问密码：" + tem[3][3:])
    print("设备标识MN：" + tem[4][3:])
    print("拆分包及应答标志Flag：" + tem[5][5:])
    print("指令参数 CP：" + tem[6][3:-6])
    print("CRC校验：" + tem[6][-6:-2])
    print("包尾：" + str(hex(int(ord((src_str[-2:-1]))))) + str(hex(int(ord((src_str[-1]))))))
