 **1����װPython 3.6** 

#CentOSϵͳ
wget https://www.moerats.com/usr/shell/Python3/CentOS_Python3.6.sh && sh CentOS_Python3.6.sh

#Debianϵͳ
wget https://www.moerats.com/usr/shell/Python3/Debian_Python3.6.sh && sh Debian_Python3.6.sh

#����Ubuntu 16+�Դ�Python3������ֻ��Ҫ��װpip3�Ϳ�����
apt install python3-pip -y


 **2����װ����** 

git clone https://github.com/pjialin/py12306
cd py12306
pip3 install -r requirements.txt


 **3�����ó���** 

#���������ļ�
cp env.py.example env.py


 **4�����Գ���** 

#��ʼ����
python3 main.py -t

#����֪ͨ��Ϣ(����, �ʼ�)
python3 main.py -t -n


 **5����������** 

#��������
python3 main.py

#���ò����б��÷���4����
-t ����������Ϣ
-t -n ����������Ϣ�Լ�֪ͨ��Ϣ
-c ָ���Զ��������ļ�λ��

 **ps:����ǽ** 

#CentOS 6
iptables -I INPUT -p tcp --dport 8008 -j ACCEPT
service iptables save
service iptables restart

#CentOS 7
firewall-cmd --zone=public --add-port=8008/tcp --permanent
firewall-cmd --reload


 **Docker��װ** 

 **1����װDocker** 

#CentOS 6
rpm -iUvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum update -y
yum -y install docker-io
service docker start
chkconfig docker on

#CentOS 7��Debian��Ubuntu
curl -sSL https://get.docker.com/ | sh
systemctl start docker
systemctl enable docker.service


 **2�����ó���** 

#�½��ļ��д�������ļ�
mkdir py12306 && cd py12306
wget -O env.py https://raw.githubusercontent.com/pjialin/py12306/master/env.docker.py.example
Ȼ��༭env.py�����ļ�


 **3����������** 

#������ǵ��ڲ���2������py12306�ļ������У�dataΪ������ݵ��ļ���
docker run -d -p 8008:8008 -v $(pwd):/config -v data:/data pjialin/py12306