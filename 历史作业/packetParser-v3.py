# coding=gbk
src_str="##0101QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&1C80\r\n"
tem=src_str.split(";")
if src_str[-2:]!='\r\n':
    print("��ȱ��β")
else:
    print("��ͷ��" + tem[0][0] + tem[0][1])
    print("���ݶ˳��ȣ�" + src_str.split("=")[0][-6:-2])
    print("������QN��" + src_str.split("=")[1][:-3])
    print("ϵͳ���� ST��" + tem[1][3:])
    print("������� CN��" + tem[2][3:])
    print("�������룺" + tem[3][3:])
    print("�豸��ʶMN��" + tem[4][3:])
    print("��ְ���Ӧ���־Flag��" + tem[5][5:])
    print("ָ����� CP��" + tem[6].split("=")[1][0:] + tem[6].split("=")[2][:-6])
    print("CRCУ�飺" + tem[6].split("=")[2][4:-1])
    print("��β��" + str(hex(int(ord((src_str[-2:-1]))))) + str(hex(int(ord((src_str[-1]))))))
