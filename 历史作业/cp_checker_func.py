# coding=utf-8
#CP=&&RtdInterval=30&&
def check_cp(cp_str):
    cp_v=cp_str.split("=")
    try:
        if(cp_v[1]=="&&&&"):
            raise ValueError("CP正确无参数")
        if(cp_v[1].find('&')!=-1 and cp_v[1].find('&&')==-1):
            raise ValueError("CP缺1个左&")
        if(cp_v[1].find('&&')==-1):
            raise ValueError("CP缺2个左&")
        if (cp_v[2].find('&') != -1 and cp_v[2].find('&&') == -1):
         raise ValueError("CP缺1个右&")
        if (cp_v[2].find('&&') == -1):
            raise ValueError("CP缺2个右&")
    except Exception as e:
        raise (e)