# coding=utf-8
#coding=utf-8
import sys
from datetime import datetime
import re

# QN检查
qn_minLength = 17
qn_maxLength = 17
format = "%Y%m%d%H%M%S%f"

def check_qn(qn_str):
    try:
        qn_v = qn_str.split("=")[1]
        if qn_minLength <= len(qn_v) <= qn_maxLength:
            CN_date = datetime.strptime(qn_v, format)
            # print(CN_date)
        else:
            raise ValueError("QN长度不合法")
    except Exception as e:
        # print(e)
        raise (e)

# ST检查
st_target_list = ["21","22","23","24","25","26","27","31","32","33","34","35","36","37","38","39","41","51","52","91"]

def check_st(st_str):
    try:
        st_v = st_str.split("=")[1]
        # print(st_v)
        if st_v not in st_target_list:
            raise ValueError("ST值域范围不合法")
    except (ValueError, IndexError) as e:
        raise e

# CN检查
def check_cn(cn_str):
    cn_v = cn_str.split("=")[1]
    try:
        if len(cn_v) == 0:
            raise ValueError("CN无值")
        if not 1000 <= int(cn_v) <= 9999:
            raise ValueError("CN值域错误")
    except ValueError as e:
        raise e

# PW检查
maxlen = 6
minlen = 6

def check_pw(pw_str):
    pw_v = pw_str.split("=")[1]
    try:
        if len(pw_v) > maxlen:
            raise ValueError("PW字符过多")
        if len(pw_v) < minlen:
            raise ValueError("PW长度缺失")
    except ValueError as e:
        raise e

# MN检查
size = 24

def check_mn(mn_str):
    mn_v = mn_str.split("=")[1]
    try:
        if len(mn_v) > size:
            raise ValueError("MN长度过多")
        if len(mn_v) < size:
            raise ValueError("MN长度缺失")
    except ValueError as e:
        raise e

# CP检查
def check_cp(cp_str):
    cp_v = cp_str.split("=")[1].split("&")
    try:
        for item in cp_v:
            if not re.match(r'^&{2,4}$', item):
                raise ValueError("CP格式不正确")
    except Exception as e:
        raise e


# Flag检查
def check_flag(flag_str):
    flag_v = flag_str.split("=")[1]

    try:
        if not 0 <= int(flag_v) <= 255:
            raise ValueError("Flag值域错误")
    except ValueError as e:
        raise e

if __name__ == "__main__":
    # 打印命令行参数
    # print("sys.arg[1]:", sys.argv[1])
    # 使用分号切分数据段数据 ，赋值给变量 data_section
    data_section = sys.argv[1].split(";")
    # 循环遍历data_section 的元素
    try:
        for item in data_section:
            # print("item:", item)
            # 如果元素内包含QN 则调用QN的检查函数check_qn
            if "QN" in item:
                # print("QN:", item)
                check_qn(item)
            # 如果元素内包含ST则调用ST的检查函数check_st
            elif "ST" in item:
                # print("ST:", item)
                check_st(item)
            # 如果... 则调用 ... 检查函数 ...
            elif "CN" in item:
                check_cn(item)
            elif "PW" in item:
                check_pw(item)
            elif "MN" in item:
                check_mn(item)
            elif "Flag" in item:
                check_flag(item)
            elif "CP" in item:
                check_cp(item)
    except Exception as e:
        raise (e)
