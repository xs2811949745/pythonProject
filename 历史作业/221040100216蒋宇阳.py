def check_cn(cn_str,b):
    try:
        cn_v = (cn_str.split("=")[1])
        if cn_v=="":
            b.append(1)
            raise ValueError("CN无值")
        if int(cn_v)<1000 or int(cn_v)>9999:
            b.append(1)
            raise ValueError("CN值域错误")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
        raise ValueError("CN格式不合法")
    except Exception as e:
        print(e)
        raise ValueError(str(e))

def check_mn(mn_str,b):
    try:
        mn_v = mn_str.split("=")[1]
        if len(mn_v)>24 :
            b.append(1)
            raise ValueError("MN长度多")
        if len(mn_v) < 24 :
            b.append(1)
            raise ValueError("MN长度缺")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
        raise ValueError("MN格式不合法")
    except Exception as e:
        print(e)
        raise ValueError(str(e))
def check_cp(cp_str,b):
    try:
        if cp_str.split("CP=")[1][0:2] !="&&" and cp_str.split("CP=")[1][0:1]=="&" :
            b.append(1)
            raise ValueError("CP缺1个左&")
        if cp_str.split("CP=")[1][0:2] != "&&" and cp_str.split("CP=")[1][0:1] != "&":
            b.append(1)
            raise ValueError("CP缺2个左&")
        if cp_str.split("CP=")[1][-2:] !="&&" and cp_str.split("CP=")[1][-1:]=="&" :
            b.append(1)
            raise ValueError("CP缺1个右&")
        if cp_str.split("CP=")[1][-2:] != "&&" and cp_str.split("CP=")[1][-1:] != "&":
            b.append(1)
            raise ValueError("CP缺2个右&")
        if cp_str.split("&&")[1]=="":
            b.append(1)
            raise ValueError("CP正确无参数")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
        raise ValueError("CP格式不合法")
    except Exception as e:
        print(e)
        raise ValueError(str(e))

def check_flag(flag_str,b):
    try:
        flag_v = int(flag_str.split("=")[1])
        if int(flag_v)>255:
            b.append(1)
            raise ValueError("Flag值域错误1")
        if int(flag_v)<0:
            b.append(1)
            raise ValueError("Flag值域错误2")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
        raise ValueError("Flag格式不合法")
    except Exception as e:
        print(e)
        raise ValueError(str(e))
def check_pw(pw_str,b):
    try:
        pw_v = pw_str.split("=")[1]
        if len(pw_v)>6 :
            b.append(1)
            raise ValueError("PW长度多")
        if len(pw_v) < 6 :
            b.append(1)
            raise ValueError("PW长度缺")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
        raise ValueError("PW格式不合法")
    except Exception as e:
        print(e)
        raise ValueError(str(e))

def check_qn(qn_str,b):
    try:
        qn_v = qn_str.split("=")[1]
        if len(qn_v)>17 and qn_v!="":
            b.append(1)
            raise ValueError("QN长度多")
        if len(qn_v) < 17 and qn_v!="" and qn_v.isdigit()==True:
            b.append(1)
            raise ValueError("QN长度缺")
        if qn_v.isdigit()==False and qn_v!="":
            b.append(1)
            raise ValueError("QN不是日期")
        if  qn_v=="":
            b.append(1)
            raise ValueError("QN无值")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
        raise ValueError("QN格式不合法")
    except Exception as e:
        print(e)
        raise ValueError(str(e))

def check_st(st_str,b):
    try:
        st_v = st_str.split("=")[1]
        st_target_list = ["21", "22", "23", "24", "25", "26", "27", "31", "32", "33", "34", "35", "36", "37", "38",
                          "39", "41", "51", "52", "91"]
        if st_v == "":
            b.append(1)
            raise ValueError("ST无值")
        if st_v not in st_target_list:
            b.append(1)
            raise ValueError("ST值域错误")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
        raise ValueError("ST格式不合法")
    except Exception as e:
        print(e)
        raise ValueError(str(e))

import sys
if __name__ == "__main__":
    a = 0
    b=[0]
    data_section = sys.argv[1].split(";")
    for item in data_section:
        if item.find("QN") != -1:
            check_qn(item,b)

        elif item.find("ST") != -1:
            check_st(item,b)

        elif item.find("CN") != -1:
            check_cn(item,b)

        elif item.find("PW") != -1:
            check_pw(item,b)

        elif item.find("MN") != -1:
            check_mn(item,b)

        elif item.find("Flag") != -1:
            check_flag(item,b)

        elif item.find("CP") != -1:
            check_cp(item,b)

    if "ST" not in sys.argv[1]:
        print("数据段缺ST")
        a = a + 1
    if "CN" not in sys.argv[1]:
        print("数据段缺CN")
        a = a + 1
    if "MN" not in sys.argv[1]:
        print("数据段缺MN")
        a = a + 1
    if "PW" not in sys.argv[1]:
        print("数据段缺PW")
        a = a + 1
    if "Flag" not in sys.argv[1]:
        print("数据段缺Flag")
        a = a + 1
    if "CP" not in sys.argv[1]:
        print("数据段缺CP")
        a = a + 1
    if len(data_section) == 8 and sys.argv[1][-1:] != ";" and "" not in data_section:
        print("数据段多字段")
        a = a + 1
    if len(data_section) == 8 and sys.argv[1][-1:] == ";" and "''" not in data_section:
        print("数据段尾部多;号")
        a = a + 1
    if len(data_section) == 8 and sys.argv[1][-1:] != ";" and "" in data_section:
        print("数据段中部多;号")
        a = a + 1
    if a==0 and b==[0] :
        print("数据段完整")
