# coding=gbk

import sys
if __name__ == "__main__":

    src_str = sys.argv[1]src_list = src_str.split(";")
    tmp = src_list[0] left = tmp.split("=")
    tmpstr= src_list[6].split("=")[1] +src_list[6].split("=")[2][:-6]
    if   left[0][0:2].find("##")==-1:  print("ȱ��ͷ")
    elif left[0][2:-2].find("0101")==-1:
        print("ȱ���ݶ�?��")
    elif left[1].find("20160801085857223")==-1:
        print("ȱ������")
    elif src_list[1].split("=")[1].find("32")==-1:
        print("ȱϵͳ����")
    elif src_list[2].split("=")[1].find("1062")==-1:
        print("ȱ�������")
    elif src_list[3].split("=")[1].find("100000")==-1:
        print("ȱ��������")
    elif src_list[4].split("=")[1].find("010000A8900016F000169DC0")==-1:
        print("ȱ�豸��ʶ")
    elif src_list[5].split("=")[1].find("5")==-1:
        print("ȱ��ְ���Ӧ���־")
    elif tmpstr.find("&&RtdInterval")==-1:
        print("ȱָ�����")
    elif src_list[6].split("=")[2][-6:].find("1C80")==-1:
        print("ȱCRCУ��")
    elif src_list[6].split("=")[2].find("\r\n")==-1:
        print("ȱ��β")
    else:
        print("��ͷ:"+left[0][0:2])
        print("���ݶγ���:"+left[0][2:-2])
        print("������ QN:"+left[1])
        print("ϵͳ���� ST:"+src_list[1].split("=")[1])
        print("������� CN:"+src_list[2].split("=")[1])
        print("�������� PW:"+src_list[3].split("=")[1])
        print("�豸��ʶ MN:"+src_list[4].split("=")[1])
        print("��ְ���Ӧ���־Flag:"+src_list[5].split("=")[1])
        tmpstr= src_list[6].split("=")[1] +src_list[6].split("=")[2][:-6]
        print("ָ����� CP:"+tmpstr)
        print("CRCУ��:"+src_list[6].split("=")[2][-6:])
        print("��β:"+str(hex(int(ord((src_str[-2:-1])))))+str(hex(int(ord((src_str[-1]))))))