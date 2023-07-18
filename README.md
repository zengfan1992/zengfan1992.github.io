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
authcommunity execute,log,net public
traphandle .1.3.6.1.4.1.2021.251.1 /home/debian/test.pl

#!/usr/bin/perl
use strict;
my $file="test.log";
open(HANDOUT,">>/home/debian/$file");
while(<STDIN>)
{
    print HANDOUT "$_";
}

sudo snmptrap -v 2c -c public localhost "hostname" .1.3.6.1.4.1.2021.251.1 sysLocation.0 s "this is test"
