#coding=utf-8
import json
import sys
from datetime import datetime

# 传入参数：
# param1: 剩余未匹配到的schema_key,
# param2: jsonschema定义的必须出现的key
# 返回值 bool 通过则返回True，否则返回False
def check_required(schema_key_list_remain,required_key):
    ## 比较两个对象内所有Key是否存在交集
    #可以先将两个对象转为set类型，然后取交集
    # 如果存在交集则说明整个数据包中没有包含所有必须的key
    try:
        required_key_set=set(required_key)
        schema_key_list_remain_set=set(schema_key_list_remain)
        if(schema_key_list_remain_set&required_key_set):
           return False

        # elif(schema_key_list_remain_set.issubset(required_key_set)):
        #   return True
        else:
            return True
    except Exception as e:
        raise e



# 传入参数：
# param1:完整数段全部数据 data_section ，包含以分号间隔的各个字段
# param2:depend_dict 依赖关系字典
# 返回值 bool 通过则返回True，否则返回False
def check_depend(data_section,depend_dict):
    # 迭代depend_dict的每个kv，检查是否存在于data_section的每个数据项中
    a=[0,0]
    for i in data_section:
        if(i.find("PNO")!=-1):
            a[1]=1
        if(i.find("PNUM")!=-1):
            a[0]=1
    # 如果缺则说明依赖关系未保证，返回False
    if((a[0]==1 and a[1]==1) or(a[0]==0 and a[1]==0)):
        return True
    else:
        return False
    # 否则返回True
    pass

# 传入参数：
# param1:完整数段全部数据 data_section ，包含以分号间隔的各个字段
# param2: 格式要求中的Properties中所有字典的Key
# param3:  jsonschema 定义的是否需要检查
# 返回值 bool 通过则返回True，否则返回False

def check_addtional(data_section,schema_key_list_all,allow_addition):
    #如果 data_section中包含的Key超出schema_key_list_all中包含的key 则说明出现附加字段，返回False
    # 否则返回True
    a=[]
    for i in data_section:
        a.append(i.split("=")[0])
        a.append(i.split("=")[0].upper())
        a.append(i.split("=")[0].lower())# 【cy】目前问题所在12.6.01：00 目前能把程序运行cp链接，下一步，问老师FLAG和把相应数据写道相应框中

    if (not allow_addition["additionalProperties"]):
        #检查
        if(set(a).issubset(set(schema_key_list_all))):
            return True
            pass
        else:
            return False
    else:
        return False

def check_section(section,action):



    #print("section:",section)
    #print(type(action))
    # 提取输入数据section中 等号后面的数据部分
    try:
        section_k = section.split("=")[0]
        section_v = section.split("=")[1]
        if (section_v == ''):
            raise IndexError(section_k + "无值")
    except IndexError as e:
        raise (e)
        # raise IndexError("输入数据:", section_v, " 输入数据缺符号：=")
    try:
        if ("format" in action.keys()):
            # print(action["format"])
            # 如果当前待查字段jsonschema规则存在format 对应的要求是 date-time 则按照日期格式 检查数据

            try:
                # 定义日期格式 年月日时分秒毫秒
                format = "%Y%m%d%H%M%S%f"
                d = datetime.strptime(section_v, format)
            except:
                raise ValueError("QN不是日期")

                # 如果当前待查字段jsonschema规则存在enum 字段
    #测 ST是否在枚举范围内
        if ("enum" in action.keys()):

            if section_v not in action["enum"]:
                # print("chk_enum_range error ")
                raise ValueError(section_k+"值域错误")
            else:
                pass

            # 如果当前待查字段jsonschema规则存在minLength && maxLength字段 则检查数据section_v的长度是否符合要求
    #测长度大小
        if ("minLength" in action.keys()) and ("maxLength" in action.keys()):
            # 取当前输入数据的长度和规则中规定的比较
            if not ((len(section_v) >= action["minLength"]) and (len(section_v) <= action["maxLength"])):
                if(len(section_v)>action["maxLength"]):
                    raise ValueError(section_k+"长度多")
                elif (len(section_v) < action["minLength"]):
                    raise ValueError(section_k + "长度缺")
                # raise ValueError(section_k, " Length检查:", section_v, "数据长度范围错误")
            else:
                pass
        if (section_k == 'CP'):
                cp_v = section.split("=")
                try:
                    if (cp_v[1] == "&&&&"):
                        raise ValueError("CP正确无参数")
                    if (cp_v[1].find('&') != -1 and cp_v[1].find('&&') == -1):
                        raise ValueError("CP缺1个左&")
                    if (cp_v[1].find('&&') == -1):
                        raise ValueError("CP缺2个左&")
                    if (cp_v[4].find('&') != -1 and cp_v[4].find('&&') == -1):
                        raise ValueError("CP缺1个右&")
                    if (cp_v[4].find('&&') == -1):
                        raise ValueError("CP缺2个右&")
                except Exception as e:
                    raise (e)
            # 如果当前待查字段jsonschema规则存在type
    # 测数据大小
        if ("type" in action.keys()):
            # 如果当前待查字段jsonschema规则存在type 的值是 integer 则尝试转为整形
            if (action["type"] == "integer"):
                    num = int(section_v)
                    # 如果当前待查字段jsonschema规则存在 minimum &&  maximum 则尝试比较大小
                    if ("minimum" in action.keys()) and ("maximum" in action.keys()):
                        if not ((num > action["minimum"] - 1) and (num < action["maximum"] + 1)):
                            if(num>action["maximum"] or num<action["minimum"]):
                                raise ValueError(section_k+"值域错误")
                    else:
                                pass
    except Exception as e:
        raise e


        # 依次判断jsonschema文件中定义的所有检查动作
        # 如果当前待查字段jsonschema规则存在format 字段
#测是否日期
            # else:
            #         # 对应字段不是整形数据
            #         raise ValueError(section_k, " mum检查:", section_v, "不是整型数据")
        # else:
        #     ## 未来扩展非 integer的判断
        #     pass//

if __name__ == "__main__":
    # 打印命令行参数
    # print ("sys.arg[1]:",sys.argv[1])

    # 使用分号切分数据段数据 ，赋值给变量 data_section

    with open('packet-schema-v2.1.json', 'r') as fcc_file:
        packet_schema_json = json.load(fcc_file)
        cp_flag=0
        # {'properties': {'QN': {'type': 'string', 'format': 'date-time', 'minLength': 17, 'maxLength': 17},
        #                 'ST': {'type': 'string',
        #                        'enum': ['21', '22', '23', '24', '25', '26', '27', '31', '32', '33', '34', '35', '36',
        #                                 '37', '38', '39', '41', '51', '52', '91']},
        #                 'CN': {'type': 'integer', 'minimum': 1000, 'maximum': 9999},
        #                 'PW': {'type': 'string', 'minLength': 6, 'maxLength': 6},
        #                 'MN': {'type': 'string', 'minLength': 24, 'maxLength': 24},
        #                 'Flag': {'type': 'integer', 'minimum': 0, 'maximum': 255}, 'PNUM': {'type': 'integer'},
        #                 'PNO': {'type': 'integer'}, 'CP': {'type': 'string'}},
        #  'required': ['QN', 'ST', 'CN', 'PW', 'MN', 'Flag', 'CP'], 'dependentRequired': {'PNO': ['PNUM']},
        #  'additionalProperties': False}

        # 查看当前fcc_data文件中保存到json对象
        # print(json.dumps(fcc_data, indent=4, sort_keys=True))

        # 将 当前 json文件中的properties属性中的key 保存到 schema_key_list 中
        schema_key_list = list(packet_schema_json["properties"].keys())
        schema_key_list.sort()
        # print(schema_key_list)
        # for k,v in packet_schema_json["properties"].items():
        #    print(k,v)
        # 从命令行split分号间隔的数据到 data_section中，类型为list
        # str="QN=320160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"
        # data_section=str.split((";"))
        #  对data_section中的元素进行遍历，以便检查所有出现字段是否符合格式要求

        # data_section = sys.argv[1].split(";")
        # 【cy】
        data_section="QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5".split(";")
        i=0

    for x in data_section:
        i+=1
        if(x.find('CP=')!=-1 and i<len(data_section)):
            data_section[i-1]=data_section[i-1]+data_section[i]
            data_section.remove(data_section[i])
            data_section[i-1]=data_section[i-1]+data_section[i]
            data_section.remove(data_section[i])
            break
        else:
            continue

    try:
        for item in data_section:
            # for i in range(len(schema_key_list)): #此处不能用正序循环
            # 逆序对schema_key_list保存的 json文件中的 properties属性进行遍历
            for i in reversed(range(len(schema_key_list))):
                # 通过下标访问当前key
                current_key = schema_key_list[i]
                # print("item->",item)
                # print("current_key->",current_key)
                # 判断是否第n个split 后的字符串内是否能检索到key
                if (item.find(current_key) != -1):
                    try:
                        check_section(item, packet_schema_json["properties"][current_key])
                        schema_key_list.remove(current_key)
                    except ValueError as e:
                        raise e
                    break

        ## 此时 schema_key_list 没有被 remove 的数据为 jsonschema定义中未参与检查的字段
        # print("schema_key_list remain:", schema_key_list)


        ## 接下来需要学生在实验4期间继续完成一下3个部分的检查
        # 1.比较schema_key_list中的元素是否和required存在交集，
        # 如果有则说明输入数据中缺少部分必须出现的字段
        # "required": [ "QN", "ST", "CN", "PW" ,"MN" ,"Flag" ,"CP" ],

        ## 接下来需要学生在实验4期间继续完成一下3个部分的检查
        ## 此时 schema_key_list 没有被 remove 的数据为 jsonschema定义中未参与检查的字段
        # print("schema_key_list remain:", schema_key_list)
        # 1.比较schema_key_list中的元素是否和required存在交集，
        # 如果有则说明输入数据中缺少部分必须出现的字段
        # "required": [ "QN", "ST", "CN", "PW" ,"MN" ,"Flag" ,"CP" ],
        # required = ["QN", "ST", "CN", "PW", "MN", "Flag", "CP"]




                    # 2.判断输入数据是否符合dependentRequired规则的要求
                    # "dependentRequired": {
                    # "PNO": ["PNUM"]
                    # },
        # try:        # 此处赋值应该从Json文件中读取，而不是 直接赋值可以参考 packet_schema_json["properties"].keys()的写法
            # depend_dict = {
            #     "PNO": ["PNUM"]
            # }
            # depend_dict=list(packet_schema_json["dependentRequired"].keys())
            # bRet = check_depend(data_section, depend_dict)
            # if(bRet==False):
            #     if(sys.argv[1].find("PNO")!=-1):
            #         raise ValueError("数据段缺总包号")
            #     else:
            #         raise ValueError("数据段缺包号")
        # except Exception as e:
        #     raise e
                    # 3.判断输入数据是否出现超过properties定义的属性

        #     schema_key_list_all=list(packet_schema_json["properties"].keys())
        #     allow_addition = {"additionalProperties": False}
        #     bRet = check_addtional(data_section, schema_key_list_all, allow_addition)
        #     if(bRet):
        #         raise ValueError("数据段多字段")
        # except Exception as e:
        #     raise e
        # schema_key_list_all 此处应该重新对schema_key_list_all 赋值，代码前面有
        # allow_addition 用additionalProperties的value 赋值
        # try:
        #     bRet = check_required(schema_key_list, required)
        #     if(bRet==False):
        #         raise ValueError("数据段缺数据"+set(schema_key_list)&set(required)[0])
        #     else:
        #         raise ValueError("数据段完整")
        # except Exception as e:
        #     raise e

        schema_key_list_remain=schema_key_list
        allow_addition = {"additionalProperties": False}
        schema_key_list = list(packet_schema_json["properties"].keys())
        bRet = check_addtional(data_section, schema_key_list, allow_addition)
        if (bRet == 0):

            raise ValueError("数据段多字段")
        # 2.判断输入数据是否符合dependentRequired规则的要求
        # "dependentRequired": {
        # "PNO": ["PNUM"]
        # allow_addition 用additionalProperties的value 赋值
        # },
        depend_dict=list(packet_schema_json["dependentRequired"].keys())

        # 此处赋值应该从Json文件中读取，而不是 直接赋值可以参考 packet_schema_json["properties"].keys()的写法
        # depend_dict = {
        #     "PNO": ["PNUM"]
        # }

        # 3.判断输入数据是否出现超过properties定义的属性


        # schema_key_list_all 此处应该重新对schema_key_list_all 赋值，代码前面有
    # except Exception as e:
    #     print(e)
# print("数据段正常")


# 以上为作业六



        # 3.判断输入数据是否出现超过properties定义的属性
        # "additionalProperties": false
        # 4.当以上检查都通过则说明本数据包无问题，继续执行以下代码
        # 获取CP=字符串的index

        # print(d_main_struct.keys())
        # print(d_main_struct.items())
        # print(d_main_struct.values())

        # 获取 字符串CP= 之后的 命令参数串
        required = ["QN", "ST", "CN", "PW", "MN", "Flag", "CP"]
        bRet = check_depend(data_section, depend_dict)
        if(bRet==0):
            if (sys.argv[1].find("PNO") != -1):
                raise IndexError("数据段缺总包号")
            else:
                raise IndexError("数据段缺包号")

        bRet = check_required(schema_key_list_remain, required)
        a=list(set(schema_key_list_remain)&set(required))
        if(a==['CP']):
            cp_flag=1#cp_flag=1代表cp缺少,否则代表他不缺少
        if(bRet==0):
            raise IndexError("数据段缺"+a[0])
        elif(bRet==1):
            print("数据段完整")
    except Exception as e:
        print(e)



    # 【cy】
    data_section1="QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5"

    if(cp_flag==1):
        data_section1=data_section1+"CP="
        # sys.argv[1]=sys.argv[1]+'CP='
    # cp_index= sys.argv[1].index('CP=')
    cp_index = data_section1.index('CP=')#不缺cp的情况下


    # 获取 字符串CP= 之前的主结构串，并转换为字典结构

    # 【cy】
    d_main_struct = dict(x.split("=") for x in data_section1[:cp_index - 1].split(";"))
    # d_main_struct = dict(x.split("=") for x in sys.argv[1][:cp_index - 1].split(";"))
    # 【cy】
    cp_str=sys.argv[1][cp_index:]
    # cp_str = data_section1[cp_index:]
    #print(cp_str)
    # 去掉CP= 后面的前后 && 符号
    cp_str_value=cp_str[3:].strip("&&")
    #print(cp_str_value)

    # 将 命令参数串 转换为字典
    if(cp_str_value==''):
        d_command_param =''
    else:
        d_command_param= dict(x.split("=") for x in cp_str_value.split(";"))

    # 合并 d_main_struct 和  d_command_param 两个字典到 d_merge


    d_merge={}
    d_merge=d_main_struct.copy()
    d_merge.update(d_command_param)
    # print (d_merge.keys())
    # print(d_merge.items())
    # print(d_merge.values())

    # 准备将 d_merge 字典输出到csv文件
    import os
    # 判断文件是否存在，如果存在则不重复输出表头（字典的key）
    csv_exist_flag = os.path.exists('2000123456张三.csv')

    import csv
    with open('2000123456张三.csv', 'a') as file:
        writer = csv.writer(file)
        # 判断csv_exist_flag 不要重复输出csv的表头
        if not csv_exist_flag:
            writer.writerow(d_merge.keys())
        writer.writerow(d_merge.values())

