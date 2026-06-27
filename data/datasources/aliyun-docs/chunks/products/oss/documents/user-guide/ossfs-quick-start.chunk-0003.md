### Alibaba Cloud Linux
根据平台的系统架构执行相应命令，下载安装包。
x86_64架构：sudo wget https://gosspublic.alicdn.com/ossfs/ossfs2_2.0.7_linux_x86_64.rpm
aarch64架构：sudo wget https://gosspublic.alicdn.com/ossfs/ossfs2_2.0.7_linux_aarch64.rpm
根据平台的系统架构执行相应命令，安装ossfs 2.0。
x86_64架构：sudo yum install ossfs2_2.0.7_linux_x86_64.rpm -y
aarch64架构：sudo yum install ossfs2_2.0.7_linux_aarch64.rpm -y
执行以下命令，验证ossfs 2.0是否成功安装。
ossfs2 --version
说明
ossfs2的可执行文件安装在/usr/local/bin/ossfs2路径下，若您的环境变量PATH有特殊配置，可直接通过/usr/local/bin/ossfs2路径访问该程序。
