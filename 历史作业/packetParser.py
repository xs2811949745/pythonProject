# coding=gbk
# import sys
#
# #if __name__ == "__main__":
# #     print(f"Arguments count: {len(sys.argv)}")
# #     for i, arg in enumerate(sys.argv):
# #         print(f"Argument {i:>6}: {arg}")
#
# src_str = "##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
#
# ## ���Դ�ӡ�Ӱ�ͷ��������ݰ�
# print(src_str[2:])
#
# # �� ; �� ���ַ�����split �з�
# src_list = src_str.split(";")
# # �ֱ��ӡÿ��src_list�ڵ�Ԫ��
# print(src_list[0])
# print(src_list[1])
# print(src_list[2])
# print(src_list[3])
# print(src_list[4])
# print(src_list[5])
# print(src_list[6])
# # print(src_list[7])
#
# ## �����ͷ�ֱ�ȡ ���� �� QN
# tmp = src_list[0]
# left = tmp.split("=")
# print(left)
# print(left[0][2:-2])
# print(left[1])


### python
# ref:   https://realpython.com/python-command-line-arguments/

# main.py
# import sys
# # argv.py
# import sys
#
# print(f"Name of the script      : {sys.argv[0]=}")
# print(f"Arguments of the script : {sys.argv[1:]=}")
# # if __name__ == "__main__":
# #     print(f"Arguments count: {len(sys.argv)}")
# #     for i, arg in enumerate(sys.argv):
# #         print(f"Argument {i:>6}: {arg}")

'''
python main.py Python Command Line Arguments
Arguments count: 5
Argument      0: main.py
Argument      1: Python
Argument      2: Command
Argument      3: Line
Argument      4: Arguments
'''

# str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
# str1=str.split(";")
# str1=str.split("=")
# print(str)
#
# print(str1[0][0:2])
# print(str1[0][2:6])
# print(str1[1][:-3])
# print(str1[2][:-3])
# print(str1[3][:-3])
# print(str1[4][:-3])
# print(str1[5][:-5])
# print(str1[6][:-3])
# print(str1[7])




### python
# ref:   https://realpython.com/python-command-line-arguments/

# main.py
import sys

# if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
# print(f"Arguments count: {len(sys.argv)}")
# print(sys.argv)
# print(sys.argv[1])

# src_str = sys.argv[1]
# ����������v1.0�ĳ���
i=0
flag=0
src_str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
# �� ; �� ���ַ�����split �з�
src_list = src_str.split(";")
src_equal = src_str.split("=")
print(src_list)
print(src_equal)
    ## ���Դ�ӡ�Ӱ�ͷ��������ݰ�
print(f"��ӡ��ͷ���������",src_str[2:])
if src_str[0:2]!='##':
    i+=1
    print("ȱ��ͷ")
if src_equal[0][-6:-2]!="0101" and src_list[0][2:6]!="0101" and src_equal[0]!="0101":
    i+=1
    print("ȱ����")
if src_equal[0][-2:]!="QN":
    i+=1
    print("ȱ������QN")
if src_list[1][0:2]!="ST":
    i+=1
    print("ȱϵͳ����ST")
if src_list[2][0:2]!="CN":
    i+=1
    print("ȱ�������CN")
if src_list[3][0:2]!="PW":
    i+=1
    print("ȱ��������PW")
if src_list[4][0:2]!="MN":
    i+=1
    print("ȱ�豸��ʶMN")
if src_list[5][0:4]!="Flag":
    i+=1
    print("ȱ��ְ���Ӧ���ǩFlag")
if src_list[6][0:2]!="CP":
    i+=1
    print("ȱָ�����CP")
if src_equal[-1][4:9]!="1C80" and src_list[-1][-2:]!="\r\n":
    i+=1
    flag+=1
    print("ȱCRCУ��Ͱ�β")
if src_equal[-1][-2:]!="\r\n" and src_list[-1][-2:]!="\r\n"and flag==0:
    i+=1
    print("ȱ��β")
if i==0:
    print(f"��ͷ:"+src_str[0:2])  # �����ͷ
    print(f"���ݶ˳���:"+src_equal[0][2:-2])  # ������ݶ˳���
    print(f"������ QN"+src_equal[1].split(";")[0])  # ���������QN
    print(f"ϵͳ���� ST:"+src_equal[2].split(";")[0])  # ���ϵͳ����ST
    print(f"������� CN:"+src_equal[3].split(";")[0])  # ����������CN
    print(f"�������� PW:"+src_equal[4].split(";")[0])  # �������� PW
    print(f"�豸��ʶ MN:"+src_equal[5].split(";")[0])  # �豸��ʶ MN
    print(f"��ְ���Ӧ���־ Flag:"+src_equal[6].split(";")[0])  # ��ְ���Ӧ���־Flag
    print(f"ָ����� CP:"+src_equal[7].split(";")[0])  # ָ����� CP
    print(f"CRCУ��:"+src_equal[8][-6:-2])  # CRCУ��
    print("��β��" + str(hex(int(ord((src_str[-2:-1]))))) + str(hex(int(ord((src_str[-1]))))))


"""    
# �ֱ��ӡÿ��src_list�ڵ�Ԫ��
print(src_list[0])
print(src_list[1])
print(src_list[2])
print(src_list[3])
print(src_list[4])
print(src_list[5])
print(src_list[6])
    ##print(src_list[7])

    ## �����ͷ�ֱ�ȡ ���� �� QN
tmp = src_list[0]
left = tmp.split("=")
print(left)
print(left[0][2:-2])
print(left[1])
"""
'''
python main.py Python Command Line Arguments
Arguments count: 5
Argument      0: main.py
Argument      1: Python
Argument      2: Command
Argument      3: Line
Argument      4: Arguments'''







