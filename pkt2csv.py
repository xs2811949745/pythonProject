# coding=utf-8
import json
import sys
from jsonschema import validate
from jsonschema.exceptions import *
def check_section(section, action):
    try:
        # 提取输入数据section中 等号前部分
        section_k = section.split("=")[0]
        # 提取输入数据section中 等号后部分
        section_v = section.split("=")[1]
    except IndexError as e:
        print(repr(e))
        raise IndexError("输入数据:", section_v, " 输入数据缺符号：=")

    #  类型定义为整型则按整型转换后按jsonschema校验
    if action["type"] == "integer":
        if section_v.isdigit():
            try:
                validate(int(section_v), action)
            except ValidationError as ee:
                print(repr(ee))
                raise ValidationError(section_k,ee)
        else:
            raise ValueError(section_k, " mum检查:", section_v, "不是整型数据")
    #  类型定义为非整型则按jsonschema校验
    else:
        try:
            validate(section_v, action)
        except ValidationError as ee:
            print(repr(ee))
            raise ValidationError(section_k,ee)


if __name__ == "__main__":
    # 打印命令行参数
    # print ("sys.arg[1]:",sys.argv[1])

    # 使用分号切分数据段数据 ，赋值给变量 data_section

    with open('packet-schema-v2.1.json', 'r') as fcc_file:
        packet_schema_json = json.load(fcc_file)

        # 查看当前fcc_data文件中保存到json对象
        # print(json.dumps(fcc_data, indent=4, sort_keys=True))

        # 将 当前 json文件中的properties属性中的key 保存到 schema_key_list 中
        schema_key_list = list(packet_schema_json["properties"].keys())
        schema_key_list.sort()
        # print(schema_key_list)

        # for k,v in packet_schema_json["properties"].items():
        #    print(k,v)
        # 从命令行split分号间隔的数据到 data_section中，类型为list
        # 对data_section中的元素进行遍历，以便检查所有出现字段是否符合格式要求

        # data_section = sys.argv[1].split(";")【cy】

        data_section="QN=32016080108585722;ST=36;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20160801085857;LA1-Rtd=50.1;LA2-Rtd=150.1&&"
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
                    except Exception as e:
                        print(repr(e))
                    schema_key_list.remove(current_key)
                    break
        ## 此时 schema_key_list 没有被 remove 的数据为 jsonschema定义中未参与检查的字段
        print("schema_key_list remain:", schema_key_list)

        ## 接下来需要学生在实验4期间继续完成一下3个部分的检查
        # 1.比较schema_key_list中的元素是否和required存在交集，
        # 如果有则说明输入数据中缺少部分必须出现的字段
        # "required": [ "QN", "ST", "CN", "PW" ,"MN" ,"Flag" ,"CP" ],

        # 2.判断输入数据是否符合dependentRequired规则的要求
        # "dependentRequired": {
        # "PNO": ["PNUM"]
        # },

        # 3.判断输入数据是否出现超过properties定义的属性
        # "additionalProperties": false

        # 4.当以上检查都通过则说明本数据包无问题，继续执行以下代码

        # 获取CP=字符串的index
        # cp_index= sys.argv[1].index('CP=')【cy】
        cp_index = data_section.index('CP=')
        # 获取 字符串CP= 之前的主结构串，并转换为字典结构
        # d_main_struct = dict(x.split("=") for x in sys.argv[1][:cp_index - 1].split(";"))【cy】
        d_main_struct = dict(x.split("=") for x in data_section[:cp_index - 1].split(";"))
        #print(d_main_struct.keys())
        #print(d_main_struct.items())
        #print(d_main_struct.values())

        # 获取 字符串CP= 之后的 命令参数串
        # cp_str=sys.argv[1][cp_index:]【cy】
        cp_str = data_section[cp_index:]
        #print(cp_str)
        # 去掉CP= 后面的前后 && 符号
        cp_str_value=cp_str[3:].strip("&&")
        #print(cp_str_value)

        # 将 命令参数串 转换为字典
        d_command_param= dict(x.split("=") for x in cp_str_value.split(";"))

        # 合并 d_main_struct 和  d_command_param 两个字典到 d_merge
        d_merge={}
        d_merge=d_main_struct.copy()
        d_merge.update(d_command_param)
        print (d_merge.keys())
        print(d_merge.items())
        print(d_merge.values())

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
