## User-Data脚本
简介
User-Data脚本传入Linux实例后直接作为Shell脚本执行，且仅在实例首次启动时运行一次。
运行频率
启动实例：仅在实例首次启动时运行一次，重启实例不会再自动运行。
更换操作系统：自动运行。
重新初始化系统盘：自动运行。
重要
以下情况不会自动运行脚本：
如果更换操作系统使用的是自定义镜像且来源于原实例，更换操作系统时会判断实例不是初次启动，因此不会自动运行脚本。
如果创建使用的是自定义镜像，则创建实例时系统盘就有数据，初始化系统盘时会判断实例不是首次启动，因此不会自动运行脚本。
格式
首行均以#!开头。
User-Data脚本示例
运行自定义脚本
#!/bin/sh echo "Hello World. The time is now $(date -R)!" | tee /root/userdata_test.txt
示例User-Data脚本的效果是在实例首次启动时，向userdata_test.txt文件写入系统时间。
自定义实例软件源、DNS解析配置及时间同步服务
在创建实例时，您可以通过User-Data脚本自定义实例的软件源、DNS解析配置及时间同步服务。以下示例以CentOS Stream 9为例，实际使用中请根据您的操作系统进行相应配置替换。
重要
系统会在实例启动时自动配置默认的yum源、NTP服务和DNS服务，您可以使用实例自定义数据更改默认的yum源、NTP服务和DNS服务，但请注意：
如果您自定义了yum源，阿里云官方不再提供yum源相关支持。
如果您自定义了NTP服务，阿里云官方不再提供相关时间同步服务。
#!/bin/sh # Modify DNS echo "nameserver 114.114.114.114" | tee /etc/resolv.conf # Modify yum repo and update cp /etc/yum.repos.d/centos.repo /etc/yum.repos.d/centos.repo.bak cp /etc/yum.repos.d/centos-addons.repo /etc/yum.repos.d/centos-addons.repo.bak sed -i "s@http://mirrors.cloud.aliyuncs.com/centos-stream/@https://mirror.stream.centos.org/@g" /etc/yum.repos.d/centos.repo sed -i "s@http://mirrors.cloud.aliyuncs.com/centos-stream/@https://mirror.stream.centos.org/@g" /etc/yum.repos.d/centos-a
