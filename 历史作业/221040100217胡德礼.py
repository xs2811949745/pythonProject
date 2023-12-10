# coding=gbk

import sys
if __name__ == "__main__":

    src_str = sys.argv[1]src_list = src_str.split(";")
    tmp = src_list[0] left = tmp.split("=")
    tmpstr= src_list[6].split("=")[1] +src_list[6].split("=")[2][:-6]
    if   left[0][0:2].find("##")==-1:  print("缺包头")
    elif left[0][2:-2].find("0101")==-1:
        print("缺数据段?度")
    elif left[1].find("20160801085857223")==-1:
        print("缺请求码")
    elif src_list[1].split("=")[1].find("32")==-1:
        print("缺系统编码")
    elif src_list[2].split("=")[1].find("1062")==-1:
        print("缺命令编码")
    elif src_list[3].split("=")[1].find("100000")==-1:
        print("缺访问密码")
    elif src_list[4].split("=")[1].find("010000A8900016F000169DC0")==-1:
        print("缺设备标识")
    elif src_list[5].split("=")[1].find("5")==-1:
        print("缺拆分包及应答标志")
    elif tmpstr.find("&&RtdInterval")==-1:
        print("缺指令参数")
    elif src_list[6].split("=")[2][-6:].find("1C80")==-1:
        print("缺CRC校验")
    elif src_list[6].split("=")[2].find("\r\n")==-1:
        print("缺包尾")
    else:
        print("包头:"+left[0][0:2])
        print("数据段长度:"+left[0][2:-2])
        print("请求码 QN:"+left[1])
        print("系统编码 ST:"+src_list[1].split("=")[1])
        print("命令编码 CN:"+src_list[2].split("=")[1])
        print("访问密码 PW:"+src_list[3].split("=")[1])
        print("设备标识 MN:"+src_list[4].split("=")[1])
        print("拆分包及应答标志Flag:"+src_list[5].split("=")[1])
        tmpstr= src_list[6].split("=")[1] +src_list[6].split("=")[2][:-6]
        print("指令参数 CP:"+tmpstr)
        print("CRC校验:"+src_list[6].split("=")[2][-6:])
        print("包尾:"+str(hex(int(ord((src_str[-2:-1])))))+str(hex(int(ord((src_str[-1]))))))