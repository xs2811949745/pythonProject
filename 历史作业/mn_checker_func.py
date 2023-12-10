# coding=utf-8

#6-6
size=24
def check_mn(mn_str):
    mn_v=mn_str.split("=")[1]
    try:
        if(len(mn_v)>size):
            raise ValueError("MN长度多")
        if (len(mn_v) < size):
            raise ValueError("MN长度缺")
    except Exception as e:
        raise (e)