using a blocksize of 4096.
解决方案：安装高版本的e2fsprogs，例如1.42.8。
检查e2fsprogs当前的版本。
sudo rpm -qa | grep e2fsprogs
下载1.42.8版本的e2fsprogs。
也可以在[e2fsprogs](https://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v1.42.8/?spm=a2c4g.11186623.2.14.Pb5baW)查看最新的软件包。sudo wget https://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v1.42.8/e2fsprogs-1.42.8.tar.gz --no-check-certificate
编译高版本的工具。
解压软件包。
sudo tar xvzf e2fsprogs-1.42.8.tar.gz
进入软件包目录。
cd e2fsprogs-1.42.8
生成Makefile文件。
sudo ./configure
编译e2fsprogs。
sudo make
安装e2fsprogs。
sudo make install
检查是否成功更新版本。
sudo rpm -qa | grep e2fsprogs
- 如何通过API接口初始化数据盘？
调用[RunCommand](../developer-reference/api-ecs-2014-05-26-runcommand.md)接口向目标实例发送初始化指令，搭配调用[DescribeInvocations](../developer-reference/api-ecs-2014-05-26-describeinvocations.md)接口查询命令回执实现初始化并挂载文件系统操作。
- 安装初始化工具时，提示“404 Not Found”怎么解决？
CentOS 6、Debian 9/10/11操作系统已结束生命周期，需要先[切换](options-for-dealing-with-centos-linux-end-of-life.md)[Centos](options-for-dealing-with-centos-linux-end-of-life.md)[源地址](options-for-dealing-with-centos-linux-end-of-life.md)或[Debian 9/10/11](other-operating-systems.md)[源地址](other-operating-systems.md)后再进行工具安装
该文章对您有帮助吗？
反馈
