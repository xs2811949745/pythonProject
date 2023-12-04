#coding=utf-8
echo "`r`ncheck1-1=============>QN长度多"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=320160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck1-2=============>QN长度缺"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=2016080108585722;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck1-3=============>QN不是日期"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=ABCD0801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck1-4=============>QN无值"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck2-1=============>ST值域错误"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=20;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck2-2=============>ST无值"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck3-1=============>CN值域错误"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=999;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck3-2=============>CN无值"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck4-1=============>PW长度多"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=1000001;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck4-1=============>PW长度缺"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=10000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck5-1=============>MN长度多"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0A;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck5-2=============>MN长度缺"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck6-1=============>Flag值域错误1"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=256;CP=&&RtdInterval=30&&"

echo "`r`ncheck6-2=============>Flag值域错误2"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=-1;CP=&&RtdInterval=30&&"

echo "`r`ncheck7-1=============>CP缺1个左&"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&RtdInterval=30&&"

echo "`r`ncheck7-2=============>CP缺2个左&"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=RtdInterval=30&&"

echo "`r`ncheck7-3=============>CP缺1个右&"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&"

echo "`r`ncheck7-4=============>CP缺2个右&"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30"

echo "`r`ncheck7-5=============>CP正确无参数"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&&&"

echo "`r`ncheck8-1=============>数据段完整"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck8-2=============>数据段多字段"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QC=123;QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck8-3=============>数据段缺ST"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck8-4=============>数据段缺CN"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck8-5=============>数据段缺PW"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck8-6=============>数据段缺MN"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;Flag=5;CP=&&RtdInterval=30&&"

echo "`r`ncheck8-7=============>数据段缺Flag"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;CP=&&RtdInterval=30&&"

echo "`r`ncheck8-8=============>数据段缺CP"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=20160801085857223;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5"

echo "`r`ncheck9=============>数据段多字段"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=32016080108585722;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;QQ=123456;CP=&&RtdInterval=30&&"

echo "`r`ncheck10-1=============>数据段缺包号"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=32016080108585722;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;PNUM=4;CP=&&RtdInterval=30&&"

echo "`r`ncheck10-2=============>数据段缺总包号"
python D:\Pycharm\pythonProject1\pkt2csv.py  "QN=32016080108585722;ST=32;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;PNO=2;CP=&&RtdInterval=30&&"


