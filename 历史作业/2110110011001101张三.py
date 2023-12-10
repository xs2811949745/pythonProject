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
    pass



# 传入参数：
# param1:完整数段全部数据 data_section ，包含以分号间隔的各个字段 
# param2:depend_dict 依赖关系字典
# 返回值 bool 通过则返回True，否则返回False
def check_depend(data_section,depend_dict):
    # 迭代depend_dict的每个kv，检查是否存在于data_section的每个数据项中
    # 如果缺则说明依赖关系未保证，返回False
    # 否则返回True
    pass

# 传入参数：
#  param1:完整数段全部数据 data_section ，包含以分号间隔的各个字段 
# param2: 格式要求中的Properties中所有字典的Key
# param2:  jsonschema 定义的是否需要检查
# 返回值 bool 通过则返回True，否则返回False

def check_addtional(data_section,schema_key_list_all,allow_addition):
    #如果 data_section中包含的Key超出schema_key_list_all中包含的key 则说明出现附加字段，返回False
    # 否则返回True
    if (not allow_addition):
        #检查
        pass
    else:
        return True




def check_section(section,action):
    #print("section:",section)
    #print(type(action))
    # 提取输入数据section中 等号后面的数据部分
    try:
        section_k=section.split("=")[0]
        section_v=section.split("=")[1]
    except IndexError as e :
        print(repr(e))
        raise IndexError("输入数据:",section_v," 输入数据缺符号：=")
    
    #依次判断jsonschema文件中定义的所有检查动作    
    # 如果当前待查字段jsonschema规则存在format 字段
    if ("format" in action.keys()):
        #print(action["format"])
        # 如果当前待查字段jsonschema规则存在format 对应的要求是 date-time 则按照日期格式 检查数据
        try:
            # 定义日期格式 年月日时分秒毫秒
            format = "%Y%m%d%H%M%S%f"
            d=datetime.strptime(section_v, format)
            print("datetime found:",d)
        except ValueError as e:
            print(repr(e))
            raise ValueError(section_k," format检查:",section_v,"不是日期类型数据") 

    # 如果当前待查字段jsonschema规则存在enum 字段
    if ("enum" in action.keys()):
        #print("action:enum")       
        if section_v  not in action["enum"]: 
            #print("chk_enum_range error ")
            raise ValueError(section_k," enum检查:",section_v,"枚举范围错误") 
        else:
            print(section_v,"chk_enum_range succ ")
            pass
    
    # 如果当前待查字段jsonschema规则存在minLength && maxLength字段 则检查数据section_v的长度是否符合要求
    if ("minLength" in action.keys()) and ("maxLength" in action.keys()):
        # 取当前输入数据的长度和规则中规定的比较
        if not ((len(section_v) >= action["minLength"]) and (len(section_v) <= action["maxLength"])):
            raise ValueError(section_k," Length检查:",section_v,"数据长度范围错误") 
        else:
            print(section_v,"chk_string_len succ") 
            pass
    
    # 如果当前待查字段jsonschema规则存在type
    if ("type" in action.keys()):
        # 如果当前待查字段jsonschema规则存在type 的值是 integer 则尝试转为整形
        if action["type"]=="integer":
            if section_v.isdigit():
                num= int(section_v)
                # 如果当前待查字段jsonschema规则存在 minimum &&  maximum 则尝试比较大小
                if ("minimum" in action.keys()) and ("maximum" in action.keys()):
                    if not (( num > action["minimum"]-1) and (num < action["maximum"]+1)):
                        raise ValueError(section_k," mum检查:",num,"整型数据范围错误") 
                    else:
                        print(section_v,"chk_integer_range succ ")
                        
                else:
                    print(section_v,"do not need check maximum or minimum ")
                    pass
            else:
                # 对应字段不是整形数据
                raise ValueError(section_k," mum检查:",section_v,"不是整型数据")
        else:
            ## 未来扩展非 integer的判断
            pass 
        

if __name__ == "__main__":
    # 打印命令行参数
    #print ("sys.arg[1]:",sys.argv[1])

    #使用分号切分数据段数据 ，赋值给变量 data_section

    with open('packet-schema-v2.1.json', 'r') as fcc_file:
        packet_schema_json = json.load(fcc_file)
        
        # 查看当前fcc_data文件中保存到json对象
        #print(json.dumps(fcc_data, indent=4, sort_keys=True))
        
        # 将 当前 json文件中的properties属性中的key 保存到 schema_key_list 中
        schema_key_list=list(packet_schema_json["properties"].keys())
        schema_key_list.sort()
        #print(schema_key_list)

        #for k,v in packet_schema_json["properties"].items():
        #    print(k,v)

        #从命令行split分号间隔的数据到 data_section中，类型为list 
        data_section=sys.argv[1].split(";")
        # 对data_section中的元素进行遍历，以便检查所有出现字段是否符合格式要求
        for item in data_section:   
            # for i in range(len(schema_key_list)): #此处不能用正序循环
            # 逆序对schema_key_list保存的 json文件中的 properties属性进行遍历
            for i in reversed(range(len(schema_key_list))):
                # 通过下标访问当前key 
                current_key = schema_key_list[i]
                #print("item->",item)
                #print("current_key->",current_key)
                # 判断是否第n个split 后的字符串内是否能检索到key 
                if (item.find(current_key)!= -1):        
                    try:
                        check_section(item,packet_schema_json["properties"][current_key])
                    except Exception as e:
                        print(repr(e))    
                    schema_key_list.remove(current_key)
                    break
        ## 此时 schema_key_list 没有被 remove 的数据为 jsonschema定义中未参与检查的字段
        print("schema_key_list remain:",schema_key_list)
        
        ## 接下来需要学生在实验4期间继续完成一下3个部分的检查
        # 1.比较schema_key_list中的元素是否和required存在交集，
        # 如果有则说明输入数据中缺少部分必须出现的字段
        #"required": [ "QN", "ST", "CN", "PW" ,"MN" ,"Flag" ,"CP" ],
        
        required= [ "QN", "ST", "CN", "PW" ,"MN" ,"Flag" ,"CP" ]
        
        bRet= check_required(schema_key_list,required)
        
        
        # 2.判断输入数据是否符合dependentRequired规则的要求
        #"dependentRequired": {
        #"PNO": ["PNUM"]
        #},
        # 此处赋值应该从Json文件中读取，而不是 直接赋值可以参考 packet_schema_json["properties"].keys()的写法
        depend_dict= {
        "PNO": ["PNUM"]
        }
        bRet=check_depend(data_section,depend_dict)
        
       
        # 3.判断输入数据是否出现超过properties定义的属性
        allow_addition={"additionalProperties": False}
        
        #schema_key_list_all 此处应该重新对schema_key_list_all 赋值，代码前面有
        # allow_addition 用additionalProperties的value 赋值
        bRet=check_addtional(data_section,schema_key_list,allow_addition)
        
        

