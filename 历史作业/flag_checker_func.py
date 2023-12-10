# coding=utf-8
def check_flag(flag_str):
    flag_v=flag_str.split("=")[1]

    try:
        if(int(flag_v)>255 or int(flag_v)<0):
            raise ValueError("Flag值域错误")
    except Exception as e:
        raise (e)