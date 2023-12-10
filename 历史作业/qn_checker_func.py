# coding=utf-8
## QN  检查，本质是 日期检查
from datetime import datetime

# 定义日期格式 年月日时分秒毫秒
format = "%Y%m%d%H%M%S%f"
qn_minLength = 17  # 未来可从packet-schema.json 读
qn_maxLength = 17  # 未来可从packet-schema.json 读


def check_qn(qn_str):
    qn_v = qn_str.split("=")[1]
    try:
        if(len(qn_v)==0):
            raise ValueError("QN无值")
        try:
            CN_date = datetime.strptime(qn_v, format)
        except:
            raise IndexError("QN不是日期")
            # print(qn_v)
        if (len(qn_v) > qn_maxLength):
           raise ValueError("QN长度多")
        elif (len(qn_v) < qn_minLength):
           raise ValueError("QN长度缺")
    except ValueError as e:   #传入无效参数
        #print(e)      #repr将对象转化为供解释器读取的形式
        raise ValueError(e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(str(e))


if __name__ == '__main__':
    qn_str_input = "201608010l5857223"
    try:
        check_qn(qn_str_input)
    except Exception as e:
        print(repr(e))
