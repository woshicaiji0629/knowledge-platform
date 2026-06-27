Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，使配置生效。
sudo sysctl -p
Ubuntu 14/16、OpenSUSE 42
执行以下命令。修改vi /etc/sysctl.conf配置文件。
vi /etc/sysctl.conf
按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。
net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0 net.ipv6.conf.lo.disable_ipv6 = 0
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，使配置生效。
sysctl -p
FreeBSD 11
执行以下命令，修改/etc/rc.conf配置文件。
vi /etc/rc.conf
按i键进入编辑模式，添加ipv6_activate_all_interfaces="YES"内容。
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，重启网络使配置生效。
/etc/netstart restart
SUSE 11/12
执行以下命令，修改/etc/modprobe.d/50-ipv6.conf配置文件。
vi /etc/modprobe.d/50-ipv6.conf
按i键进入编辑模式，删除install ipv6 /bin/true内容。
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令。修改vi /etc/sysctl.conf配置文件。
vi /etc/sysctl.conf
按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。
net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0 net.ipv6.conf.lo.disable_ipv6 = 0
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，使配置生效。
sysctl -p
如果返回inet6相关内容：表示实例已开启IPv6服务，请配置IPv6地址。
配置IPv6地址。
Alibaba Cloud Linux 2/3、CentOS 6/7、Red Hat 6/7
执行以下命令，修改网卡配置文件。
vi /etc/sysconfig/network-scripts/ifcfg-eth0
eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。
按i键进入编辑模式，在文件中根据实际信息添加以下配置。
DHCPV6C=yes IPV6INIT=yes
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，
