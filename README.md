```bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

minikube config set cpus 8
minikube config set memory 8196
minikube config set kubernetes-version 1.23.12
https://xzz2wi11.mirror.aliyuncs.com

git config --global user.email "zengfan1992@hotmail.com"
git config --global user.name "zengfan1992"
git config --global http.proxy "http://192.168.43.1:1080"

ssh debian sudo date -s $(date +%FT%T)

sudo mkdir shared
sudo mount -t vboxsf share /home/debian/shared -o uid=debian -o gid=debian
sudo vmhgfs-fuse -o allow_other .host:/shared shared

sudo timedatectl set-timezone Pacific/Galapagos
sudo timedatectl set-timezone America/Mexico_City

eval "$('/home/zengfan/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
```
```bash
sudo apt-get install snmpd snmp snmp-mibs-downloader snmptrapd
sudo systemctl disable snmptrapd.socket
sudo systemctl disable snmptrapd.service
sudo snmptrapd -fd -Lo | grep SNMP
sudo snmptrap -v 2c -c public localhost "" .1.3.6.1.4.1.2021.251.1 sysLocation.0 s "this is test"
snmpset -v2c -c public -On localhost system.sysName.0 s linux

authCommunity execute,log,net public
traphandle default /etc/snmp/traphandle.sh
 #!/bin/sh
 read host
 read ip
 vars=
 
 while read oid val
 do
   if [ "$vars" = "" ]
   then
     vars="$oid = $val"
   else
     vars="$vars, $oid = $val"
   fi
 done
 
 echo trap: $1 $host $ip $vars
```
```bash
sudo apt-get install build-essential
sudo apt-get install xorg-dev
sudo apt-get install libgtk2.0-dev
./configure --enable-x86-64 --enable-debugger
```
```py
import os
 
# 输入要重命名的目录
path = input('请输入要重命名的目录：')
# 获取目录下的所有文件
files = os.listdir(path)
# 去掉x-前缀并覆盖原文件
for file in files:
    file
    new_file = file[file.index('_')+1:-13] + '.pdf'
    os.rename(path + '/' + file, path + '/' + new_file)
    print('重命名成功：', file, '-->', new_file)
# 按任意键结束
input('按任意键结束')
```
```bash
docker run -d -p 9092:9092 -e LISTENERS=PLAINTEXT://0.0.0.0:9092 apache/kafka
```
