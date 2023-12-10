# coding=gbk
src_str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
tem=src_str.split(";")
if src_str[-2:]!='\r\n':
    print("仅缺包尾")
else:
    print("包头：" + tem[0][0] + tem[0][1])
    print("数据端长度：" + src_str.split("=")[0][-6:-2])
    print("请求码QN：" + src_str.split("=")[1][:-3])
    print("系统编码 ST：" + tem[1][3:])
    print("命令编码 CN：" + tem[2][3:])
    print("访问密码：" + tem[3][3:])
    print("设备标识MN：" + tem[4][3:])
    print("拆分包及应答标志Flag：" + tem[5][5:])
    print("指令参数 CP：" + tem[6].split("=")[1][0:] + tem[6].split("=")[2][:-6])
    print("CRC校验：" + tem[6].split("=")[2][4:-1])
    print("包尾：" + str(hex(int(ord((src_str[-2:-1]))))) + str(hex(int(ord((src_str[-1]))))))
