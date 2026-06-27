r-key.md)[Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行以下命令配置IPv6地址。
说明
在默认情况下，执行以下命令时会自动校验ecs-utils-ipv6插件是否已在本地安装，或本地版本是否为最新。若未安装或版本较旧，插件将自动下载最新版本并执行安装。
sudo acs-plugin-manager --exec --plugin=ecs-utils-ipv6
手动配置（Linux）
远程连接Linux实例。
具体操作，请参见[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行ip addr | grep inet6或者ifconfig | grep inet6命令，检查实例是否已开启IPv6服务。
如果未返回inet6相关内容：表示实例未开启IPv6服务，请开启IPv6服务。
如何开启IPv6服务？
Alibaba Cloud Linux 2/3
执行以下命令，修改/etc/sysctl.conf配置文件。
vi /etc/sysctl.conf
按i键进入编辑模式，找到如下内容，将内容末尾数值1替换为0。
net.ipv6.conf.all.disable_ipv6 = 1 net.ipv6.conf.default.disable_ipv6 = 1 net.ipv6.conf.lo.disable_ipv6 = 1
如果需要开启指定网络接口，修改信息示例如下。
net.ipv6.conf.eth0.disable_ipv6 = 0
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，验证/etc/sysctl.conf配置信息是否与initramfs中的/etc/sysctl.conf存在差异。
diff -u /etc/sysctl.conf <(lsinitrd -f /etc/sysctl.c
