import sys

if __name__ == "__main__":
    ###print(f"Arguments count: {len(sys.argv)}")
    ###print (sys.argv)
    ###print (sys.argv[1])

    src_str = sys.argv[1]
    # 此行以下是v1.0的程序
    src_list = src_str.split(";")
    tmp = src_list[0]
    left = tmp.split("=")
    
    i=0
    if left[0].find("##")==-1:
        print("缺包头")
        i+=1
    
    if src_list[0].find("0101")==-1:
        print("缺长度")
        i+=1
    if src_str.find("QN")==-1:
        print("缺QN")
        i+=1
    ###if src_list[0].find("20160801085857223")==-1:
    ###    print("缺请求码")
    ###   i+=1
    if  src_str.find("ST")==-1:
        print("缺ST")
        i+=1
    ###if  src_list[1].split("=")[1].find("32")==-1:
    ###    print("缺系统编码")
    ###    i+=1
    if  src_str.find("CN")==-1:
        print("缺CN")
        i+=1
    ###if  src_list[2].split("=")[1].find("1062")==-1:
    ###    print("缺命令编码")
    ###    i+=1
    if  src_str.find("PW")==-1:
        print("缺PW")
        i+=1
    ###if  src_list[3].split("=")[1].find("100000")==-1:
    ###    print("缺访问密码")
    ###    i+=1
    if  src_str.find("MN")==-1:
        print("缺MN")
        i+=1
    ###if  src_list[4].split("=")[1].find("010000A8900016F000169DC0")==-1:
    ###    print("缺设备标识")
    ###    i+=1
    if  src_str.find("Flag")==-1:
        print("缺Flag")
        i+=1
    ###if  src_list[5].split("=")[1].find("5")==-1:
    ###    print("缺拆分包及应答标志")
    ###    i+=1
    if  src_str.find("CP")==-1:
        print("缺CP")
        i+=1
    ###if  tmpstr.find("&&RtdInterval")==-1:
    ### print("缺指令参数")
    ###    i+=1
    if  src_str.find("30&&")==-1:
        print("缺30&&")
        i+=1
    if  src_str.find("1C80")==-1:
        print("缺CRC校验")
        i+=1
    if  src_str.find("\r\n")==-1:
        print("缺包尾")
        i+=1

    ###"##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;
    #   MN=010000A8900016F000169DC0;Flag=5;
    #   CP=&&RtdInterval=30&&1C80`r`n"
    if i==0:
        tmpstr= src_list[6].split("=")[1] +src_list[6].split("=")[2][:-6]
        print("包头:"+src_list[0][0:2])
        print("数据段长度:"+src_list[0].split("=")[0][2:-2])
        print("请求码 QN:"+src_list[0].split("=")[1])
        print("系统编码 ST:"+src_list[1].split("=")[1])
        print("命令编码 CN:"+src_list[2].split("=")[1])
        print("访问密码 PW:"+src_list[3].split("=")[1])
        print("设备标识 MN:"+src_list[4].split("=")[1])
        print("拆分包及应答标志Flag:"+src_list[5].split("=")[1])

        ###tmpstr= src_list[6].split("=")[1] +src_list[6].split("=")[2][:-6]
        print("指令参数 CP:"+tmpstr)
        print("CRC校验:"+src_list[6].split("=")[2][-6:])
        print("包尾:"+str(hex(int(ord((src_str[-2:-1])))))+str(hex(int(ord((src_str[-1]))))))

   
