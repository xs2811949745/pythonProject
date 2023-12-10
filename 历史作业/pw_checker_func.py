# coding=utf-8
# 6-6
#string
maxlen=6
minlen=6
def check_pw(pw_str):
    pw_v=pw_str.split("=")[1]
    try:
        if(len(pw_v)>maxlen):
            raise ValueError("PW长度多")
        if(len(pw_v) < minlen):
            raise ValueError("PW长度缺")
    except Exception as e:
        raise (e)
