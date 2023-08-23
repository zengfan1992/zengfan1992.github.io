```bash
minikube start --insecure-registry 192.168.56.1:8181 --registry-mirror http://192.168.56.1:8181 \n
--image-mirror-country cn
minikube config set kubernetes-version 1.23.12
minikube config set cpus 4
minikube config set memory 8196
minikube config set driver qemu2
https://xzz2wi11.mirror.aliyuncs.com
git config --global user.email "zengfan1992@hotmail.com"
git config --global user.name "zengfan1992"
/usr/lib/virtualbox/VBoxManage startvm ubuntu --type headless
"C:\Program Files\Oracle\VirtualBox\VboxManage" startvm ubuntu --type headless
ssh ubuntu sudo date -s $(date +%FT%T)
sed -i "s@http://repo.openeuler.org@http://repo.huaweicloud.com/openeuler@g" /etc/apt/sources.list
qemu-img convert -p -f vmdk -O qcow2 centos6.9.vmdk centos6.9.qcow2
qemu-img resize bionic-server-cloudimg-amd64.img 50G
growpart /dev/vda 1
resize2fs /dev/vda1
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
