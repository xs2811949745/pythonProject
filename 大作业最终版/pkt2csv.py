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
    a = []
    for i in data_section:
        a.append(i.split("=")[0])
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
        if("type" in action.keys()) and action["type"]=='integer':
            try:
                int(section_v)
            except:
                raise IndexError(section_k+"不是整数")
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
                    if(cp_v[1].find('&') != -1 and cp_v[1].find('&&') == -1 and cp_v[-1].find('&') != -1 and cp_v[-1].find('&&') == -1):
                        raise ValueError("CP缺一个左&缺一个右&")
                    if (cp_v[1].find('&') != -1 and cp_v[1].find('&&') == -1):
                        raise ValueError("CP缺1个左&")
                    if (cp_v[1].find('&&') == -1):
                        raise ValueError("CP缺2个左&")
                    if (cp_v[-1].find('&') != -1 and cp_v[-1].find('&&') == -1):
                        raise ValueError("CP缺1个右&")
                    if (cp_v[-1].find('&&') == -1):
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
if __name__ == "__main__":
    # 打印命令行参数
    # print ("sys.arg[1]:",sys.argv[1])
    with open('packet-schema-v2.1.json', 'r') as fcc_file:
        bRet=0
        packet_schema_json = json.load(fcc_file)
        cp_flag=0
        schema_key_list = list(packet_schema_json["properties"].keys())
        schema_key_list.sort()

        # str="QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=7.5;w01012-Rtd=&&"
        # data_section=str.split((";"))
        data_section = sys.argv[1].split(";")
        # 【cy】

        # data_section="QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=7.5;w01012-Rtd=&&".split(";")
        i=0
    try:
        try:
            for x in data_section:
                i+=1
                if(x.find('CP=')!=-1 and i<len(data_section)):
                    data_section[i-1]=data_section[i-1]+data_section[i]
                    data_section.remove(data_section[i])
                    while(data_section[i-1]!=data_section[-1]):
                        data_section[i-1]=data_section[i-1]+data_section[i]
                        data_section.remove(data_section[i])
                        if(data_section[-1].count("=")>4):
                            raise ValueError("CP中多字段")
                    if(data_section[i-1].find("w01012-Rtd")==-1):
                        raise ValueError("CP缺w01012-Rtd的数据")
                    elif (data_section[i - 1].find("w01001-Rtd") == -1):
                        raise ValueError("CP缺w01001-Rtd的数据")
                    elif(data_section[i - 1].find("DataTime") == -1):
                        raise ValueError("CP日期缺DataTime")

                else:
                    continue
        except Exception as e:
            bRet = 0
            raise e
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

        schema_key_list_remain=schema_key_list
        allow_addition = {"additionalProperties": False}
        schema_key_list = list(packet_schema_json["properties"].keys())
        bRet = check_addtional(data_section, schema_key_list, allow_addition)
        if (bRet == 0):
            raise ValueError("数据段多字段")
        depend_dict=list(packet_schema_json["dependentRequired"].keys())


# 以上为作业六
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

        # CP = & & DataTime = 20231201082857;
        # w01001 - Rtd = 7.0;
        # w01012 - Rtd = 10.9&&
        #下面对CP中的相关数据进行合法性检查
        # 【cy】
        try:
            cp_index=sys.argv[1].index('CP=')
        except :
            raise ValueError("数据段缺CP")
        cp_str=sys.argv[1][cp_index:]
        # data_section1="QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=7.5;w01012-Rtd=&&"
        # cp_index=data_section1.index('CP=')#缺cp怎么办?
        # cp_str = data_section1[cp_index:]
        #确定cp标准
        cp_standard={
            "w01001-Rtd":
                {
                    "type":1.0,
                    "min":0,
                    "max":150
                },
            "w01012-Rtd":
                {
                    "type": 1.0,
                    "min": 0,
                    "max": 150
                },
            "DataTime":
                {
                    "type":"string",
                    "maxlength":14,
                    "minlength":14
                }
        }
        # 【cy】
        try:
            if(sys.argv[1].find("DataTime=")==-1):
                raise ValueError("CP缺DataTime的等号")
            if (sys.argv[1].find("w01012-Rtd=") == -1):
                raise ValueError("CP中w01012-Rtd缺等号")
            if (sys.argv[1].find("w01001-Rtd=") == -1):
                raise ValueError("CP中w01001-Rtd缺等号")
        except Exception as e:
            raise e
        string=cp_str
        # 去掉字符串开头和结尾的 "CP=&&" 和 "&&"
        string = string.strip("CP=&&").strip("&&")

        # 分割字符串，得到键值对列表
        pairs = string.split(";")

        # 创建一个空字典
        data_dict = {}
        pairs+=''
        # 遍历键值对列表
        for pair in pairs:
            # 分割键值对，得到键和值
            # 将键值对添加到字典中
            try:
                key, value = pair.split("=")
                data_dict[key] = value
            except:
                raise IndexError("w01012-Rtd的值为空")
        for x in data_dict.keys():
            if (x == "DataTime"):
                if (data_dict[x] == ''):
                    raise ValueError("DataTime值为空")
            if(x=="DataTime"):
                try:

                     if len(data_dict[x])>cp_standard[x]["maxlength"]:
                         bRet = 0
                         raise ValueError("CP中DataTime长度多")
                     if len(data_dict[x])<cp_standard[x]["minlength"]:
                         bRet = 0
                         raise ValueError("CP中DataTime长度缺")
                except Exception as e:
                    bRet = 0
                    raise e
                try:
                     datetime.strptime(data_dict[x], "%Y%m%d%H%M%S")
                except Exception as e:
                     raise ValueError("DataTime不是日期")
                except Exception as e:
                    bRet = 0
                    raise e
            if(x=="w01001-Rtd"):
                try:
                     float(data_dict[x])
                except:
                    bRet = 0
                    if data_dict[x] != '':
                        raise IndexError("w01001-Rtd的值不是数字")
                    else:
                        raise IndexError("w01001-Rtd的值为空")
                try:
                    if (data_dict[x] == ''):
                        raise ValueError("w01001-Rtd值为空")
                    if float(data_dict[x])>cp_standard[x]["max"]:
                        bRet = 0
                        raise ValueError("w01001-Rtd的值过大")
                    if float(data_dict[x])<cp_standard[x]["min"]:
                        bRet = 0
                        raise ValueError("w01001-Rtd的值过小")
                except Exception as e:
                    bRet = 0
                    raise e
            if (x == "w01012-Rtd"):
                try:
                     float(data_dict[x])
                except:
                    bRet = 0
                    raise IndexError("w01012-Rtd的值不是数字")
                try:
                    if float(data_dict[x])>cp_standard[x]["max"]:
                        bRet = 0
                        raise ValueError("w01012-Rtd的值过大")
                    if float(data_dict[x])<cp_standard[x]["min"]:
                        bRet = 0
                        raise ValueError("w01012-Rtd的值过小")
                except Exception as e:
                    bRet = 0
                    raise e
        if(bRet==1):
            print("数据段完整")
    except Exception as e:
        bRet = 0
        print(e)



    # 【cy】
    # data_section1="QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=7.5;w01012-Rtd=&&"
    if(bRet==1):
        if(cp_flag==1):
            # data_section1=data_section1+"CP="
            sys.argv[1]=sys.argv[1]+'CP='
        cp_index= sys.argv[1].index('CP=')
        # cp_index = data_section1.index('CP=')#不缺cp的情况下


        # 获取 字符串CP= 之前的主结构串，并转换为字典结构

        # 【cy】
        # d_main_struct = dict(x.split("=") for x in data_section1[:cp_index - 1].split(";"))
        d_main_struct = dict(x.split("=") for x in sys.argv[1][:cp_index - 1].split(";"))
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
        d_merge={}
        d_merge=d_main_struct.copy()
        d_merge.update(d_command_param)
        import os

        csv_exist_flag = os.path.exists('221040100213胡焮铭.csv')

        import csv
        with open('221040100213胡焮铭.csv', 'a') as file:
            writer = csv.writer(file)
            # 判断csv_exist_flag 不要重复输出csv的表头
            if not csv_exist_flag:
                writer.writerow(d_merge.keys())
            writer.writerow(d_merge.values())

