# coding=utf-8

#1000-9999
def check_cn(cn_str):
    cn_v=cn_str.split("=")[1]
    # print(len(cn_v))
    try:
        if(len(cn_v)==0):
            raise ValueError("CN无值")
        if(int(cn_v)<1000 or int(cn_v)>9999):
            raise ValueError("CN值域错误")
    except ValueError as e:
        raise (e)
