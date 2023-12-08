﻿echo "`r`n##check###### pkt2csv.py   ############################################### begin"
echo "`r`ncheck1-1=============>QN长度多"
python pkt2csv.py  "QN=320160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck1-2=============>QN长度缺"
python pkt2csv.py  "QN=2016080108585722;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck1-3=============>QN不是日期"
python pkt2csv.py  "QN=ABCD0801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck1-4=============>QN无值"
python pkt2csv.py  "QN=;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck2-1=============>ST值域错误"
python pkt2csv.py  "QN=20160801085857223;ST=20;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck2-2=============>ST无值"
python pkt2csv.py  "QN=20160801085857223;ST=;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck3-1=============>CN值域错误"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=999;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck3-2=============>CN无值"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck4-1=============>PW长度多"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=1000001;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck4-1=============>PW长度缺"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=10000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck5-1=============>MN长度多"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0A;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck5-2=============>MN长度缺"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck6-1=============>Flag值域错误1"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=256;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck6-2=============>Flag值域错误2"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=-1;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck7-1=============>CP缺1个左&"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck7-2=============>CP缺2个左&"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck7-3=============>CP缺1个右&"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&"
echo "`r`ncheck7-4=============>CP缺2个右&"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9"
echo "`r`ncheck7-5=============>CP正确无参数"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&&&"
echo "`r`ncheck8-1=============>数据段完整"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck8-2=============>数据段多字段"
python pkt2csv.py  "QC=123;QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck8-3=============>数据段缺ST"
python pkt2csv.py  "QN=20160801085857223;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck8-4=============>数据段缺CN"
python pkt2csv.py  "QN=20160801085857223;ST=32;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck8-5=============>数据段缺PW"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck8-6=============>数据段缺MN"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck8-7=============>数据段缺Flag"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck8-8=============>数据段缺CP"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5"
echo "`r`ncheck9=============>数据段多字段"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;QQ=123456;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck10-1=============>数据段缺包号"
python pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;PNUM=4;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck10-2=============>数据段缺总包号"
python pkt2csv.py "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;PNO=2;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck11-1=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=36;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201082857;w01001-Rtd=7.0;w01012-Rtd=10.9&&"
echo "`r`ncheck11-2=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC1;Flag=5;CP=&&DataTime=20230101084857;w01001-Rtd=7.1;w01012-Rtd=10.8&&"
echo "`r`ncheck11-3=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20230201084857;w01001-Rtd=7.2;w01012-Rtd=10.7&&"
echo "`r`ncheck11-4=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC3;Flag=5;CP=&&DataTime=20230301084857;w01001-Rtd=7.3;w01012-Rtd=10.6&&"
echo "`r`ncheck11-5=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC4;Flag=5;CP=&&DataTime=20230401084857;w01001-Rtd=7.4;w01012-Rtd=10.5&&"
echo "`r`ncheck11-6=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC5;Flag=5;CP=&&DataTime=20230501084857;w01001-Rtd=7.5;w01012-Rtd=10.4&&"
echo "`r`ncheck11-7=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC6;Flag=5;CP=&&DataTime=20230601084857;w01001-Rtd=7.6;w01012-Rtd=10.3&&"
echo "`r`ncheck11-8=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC7;Flag=5;CP=&&DataTime=20230701084857;w01001-Rtd=7.7;w01012-Rtd=10.2&&"
echo "`r`ncheck11-9=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC8;Flag=5;CP=&&DataTime=20230801084857;w01001-Rtd=7.8;w01012-Rtd=10.1&&"
echo "`r`ncheck11-10=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC9;Flag=5;CP=&&DataTime=20230901084857;w01001-Rtd=7.9;w01012-Rtd=10.0&&"
echo "`r`ncheck12-1=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC1;Flag=5;CP=&&DataTime=20221001084857;w01001-Rtd=7.0;w01012-Rtd=0&&"
echo "`r`ncheck12-2=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC1;Flag=5;CP=&&DataTime=20231001084857;w01001-Rtd=7.0;w01012-Rtd=0&&"
echo "`r`ncheck12-3=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC1;Flag=5;CP=&&DataTime=20231101084857;w01001-Rtd=0;w01012-Rtd=10.8&&"
echo "`r`ncheck12-4=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201084857;w01001-Rtd=0;w01012-Rtd=0&&"
echo "`r`ncheck12-5=============>数据段完整 "
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=31;w01012-Rtd=31&&"


echo "`r`ncheck13-1=============> w01012-Rtd数值过大"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=31;w01012-Rtd=151&&"

echo "`r`ncheck13-2=============> w01012-Rtd数值过小"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=31;w01012-Rtd=-1&&"
echo "`r`ncheck13-4=============> w01001-Rtd数值过大"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=151;w01012-Rtd=0&&"
echo "`r`ncheck13-5=============> w01001-Rtd数值过小"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=-1;w01012-Rtd=15&&"
echo "`r`ncheck13-6=============> DataTime不是日期"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=asdaubjadsasdf;w01001-Rtd=31;w01012-Rtd=1&&"
echo "`r`ncheck13-7=============> w01001-Rtd不是数字"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=a;w01012-Rtd=15&&"
echo "`r`ncheck13-8=============> w01012-Rtd不是数字"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=3;w01012-Rtd=ll&&"
echo "`r`ncheck13-9=============> CP缺w01012-Rtd的数据"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=3&&"
echo "`r`ncheck13-10=============> CP缺w01001-Rtd的数据"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01012-Rtd=15&&"
echo "`r`ncheck13-11=============> CP中缺日期DataTime"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&w01001-Rtd=7.5;w01012-Rtd=15&&"
echo "`r`ncheck13-12=============> CP中DataTime为空"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=;w01001-Rtd=7.5;w01012-Rtd=15&&"
echo "`r`ncheck13-13=============> CP中w01001-Rtd为空"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=;w01012-Rtd=15&&"
echo "`r`ncheck13-14=============> CP中w01012-Rtd为空"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=7.5;w01012-Rtd=&&"
echo "`r`ncheck13-15=============> CP中多字段"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;A=1;w01001-Rtd=7.5;w01012-Rtd=15&&"
echo "`r`ncheck13-16=============> CP中w01001-Rtd缺等号"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd7.5;w01012-Rtd=15&&"
echo "`r`ncheck13-17=============> CP中w01012-Rtd缺等号"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=20231231084857;w01001-Rtd=7.5;w01012-Rtd15&&"
echo "`r`ncheck13-18=============> CP缺DataTime的等号"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime20231231084857;w01001-Rtd=7.5;w01012-Rtd=15&&"
echo "`r`ncheck13-19=============> DataTime的长度多"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=202312310848571;w01001-Rtd=7.5;w01012-Rtd=15&&"
echo "`r`ncheck13-20=============> DataTime的长度缺"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC2;Flag=5;CP=&&DataTime=202312310848;w01001-Rtd=7.5;w01012-Rtd=15&&"
echo "`r`ncheck13-21=============>CP无值"
python pkt2csv.py "PNO=1;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP="
echo "`r`ncheck13-22=============>CP缺一个左&缺一个右&"
python pkt2csv.py "PNO=1;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&"

echo "`r`ncheck14-1=============>CN不是整数"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=a;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&&"
echo "`r`ncheck14-2=============>Flag不是整数"
python pkt2csv.py "QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=a;CP=&&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&&"
echo "`r`ncheck14-3=============>PNUM不是整数"
python pkt2csv.py "PNO=1;PNUM=a;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&&"
echo "`r`ncheck14-4=============>PNO不是整数"
python pkt2csv.py "PNO=a;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&&"
echo "`r`ncheck14-5=============>PW无值"
python pkt2csv.py "PNO=1;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=;MN=010000A8900016F000169DC0;Flag=5;CP=&&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&&"
echo "`r`ncheck14-6=============>MN无值"
python pkt2csv.py "PNO=1;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=;Flag=5;CP=&&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&&"
echo "`r`ncheck14-7=============>FLag无值"
python pkt2csv.py "PNO=1;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=;CP=&&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&&"
echo "`r`ncheck14-8=============>CP无值"
python pkt2csv.py "PNO=1;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP="
echo "`r`ncheck14-9=============>CP缺一个左&缺一个右&"
python pkt2csv.py "PNO=1;PNUM=1;QN=20160801085857223;ST=21;CN=2011;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&DataTime=20231201084857;w01001-Rtd=15;w01012-Rtd=15&"


echo "`r`ncheck12-5=============>统计"
python opPandas.py
echo "`r`n##check###### pkt2csv.py   ############################################### end"
