# coding=gbk
src_str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
tem=src_str.split(";")
a=0
if src_str[0:2]!="##":
    print("ȱ��ͷ")
    a=1
elif  src_str[0:4]=="##QN":
    print("ȱ����")
    a = 1
elif src_str[6:8]!="QN":
    print("ȱ������QN")
    a = 1
elif src_str[27:29]!="ST":
    print("ȱϵͳ���� ST")
    a = 1
elif src_str[33:35]!="CN":
    print("ȱ������� CN")
    a = 1
elif src_str[41:43]!="PW":
    print("ȱ��������PW")
    a = 1
elif src_str[51:53]!="MN":
    print("ȱ�豸��ʶMN")
    a = 1
elif src_str[79:83]!="Flag":
    print("ȱ��ְ���Ӧ���־Flag")
    a = 1
elif tem[6][0:2] != 'CP':
    print("ȱָ�����")
    a = 1
elif tem[6][21:25] != '1C80':
    print("ȱCRCУ��")
    a = 1
elif  src_str[-2:]!='\r\n':
    print("ȱ��β")
    a = 1
if a==0:
    print("��ͷ��" + tem[0][0] + tem[0][1])
    print("���ݶ˳��ȣ�" + src_str.split("=")[0][-6:-2])
    print("������QN��" + src_str.split("=")[1][:-3])
    print("ϵͳ���� ST��" + tem[1][3:])
    print("������� CN��" + tem[2][3:])
    print("�������룺" + tem[3][3:])
    print("�豸��ʶMN��" + tem[4][3:])
    print("��ְ���Ӧ���־Flag��" + tem[5][5:])
    print("ָ����� CP��" + tem[6][3:-6])
    print("CRCУ�飺" + tem[6][-6:-2])
    print("��β��" + str(hex(int(ord((src_str[-2:-1]))))) + str(hex(int(ord((src_str[-1]))))))
