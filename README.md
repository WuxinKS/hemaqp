 **1、安装Python 3.6** 

#CentOS系统
wget https://www.moerats.com/usr/shell/Python3/CentOS_Python3.6.sh && sh CentOS_Python3.6.sh

#Debian系统
wget https://www.moerats.com/usr/shell/Python3/Debian_Python3.6.sh && sh Debian_Python3.6.sh

#由于Ubuntu 16+自带Python3，所以只需要安装pip3就可以了
apt install python3-pip -y


 **2、安装依赖** 

git clone https://github.com/pjialin/py12306
cd py12306
pip3 install -r requirements.txt


 **3、配置程序** 

#复制配置文件
cp env.py.example env.py


 **4、测试程序** 

#开始测试
python3 main.py -t

#测试通知消息(语音, 邮件)
python3 main.py -t -n


 **5、启动程序** 

#启动命令
python3 main.py

#可用参数列表，用法见4步骤
-t 测试配置信息
-t -n 测试配置信息以及通知消息
-c 指定自定义配置文件位置

 **ps:防火墙** 

#CentOS 6
iptables -I INPUT -p tcp --dport 8008 -j ACCEPT
service iptables save
service iptables restart

#CentOS 7
firewall-cmd --zone=public --add-port=8008/tcp --permanent
firewall-cmd --reload


 **Docker安装** 

 **1、安装Docker** 

#CentOS 6
rpm -iUvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum update -y
yum -y install docker-io
service docker start
chkconfig docker on

#CentOS 7、Debian、Ubuntu
curl -sSL https://get.docker.com/ | sh
systemctl start docker
systemctl enable docker.service


 **2、配置程序** 

#新建文件夹存放配置文件
mkdir py12306 && cd py12306
wget -O env.py https://raw.githubusercontent.com/pjialin/py12306/master/env.docker.py.example
然后编辑env.py配置文件


 **3、启动容器** 

#该命令记得在步骤2建立的py12306文件夹运行，data为存放数据的文件夹
docker run -d -p 8008:8008 -v $(pwd):/config -v data:/data pjialin/py12306