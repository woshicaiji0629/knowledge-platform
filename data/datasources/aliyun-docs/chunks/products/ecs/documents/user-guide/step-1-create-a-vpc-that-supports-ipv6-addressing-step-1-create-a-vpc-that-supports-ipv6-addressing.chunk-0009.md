nfig/network
按i键进入编辑模式，将NETWORKING_IPV6=no修改为NETWORKING_IPV6=yes。
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
（可选）依次执行以下命令，重新加载IPv6模块。
说明
若您的操作系统为CentOS 6，则需要执行该步骤。否则，跳过该步骤。
modprobe ipv6 -r modprobe ipv6 lsmod | grep ipv6
若系统返回以下内容，表明IPv6模块已经成功加载。
ipv6 xxxxx 8
说明
返回内容第三列参数值不能为 0，否则您需要重新设置IPv6服务。
执行以下命令，修改/etc/sysctl.conf配置文件。
vi /etc/sysctl.conf
按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。
net.ipv6.conf.all.disable_ipv6 = 1 net.ipv6.conf.default.disable_ipv6 = 1 net.ipv6.conf.lo.disable_ipv6 = 1
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，使配置生效。
sudo sysctl -p
Debian 8/9
执行以下命令，修改/etc/default/grub配置文件。
vi /etc/default/grub
按i键进入编辑模式，删除ipv6.disable=1内容。
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，修改/boot/grub/grub.cfg配置文件。
vi /boot/grub/grub.cfg
按i键进入编辑模式，删除ipv6.disable=1内容。
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
重启Linux实例。具体操作，请参见[重启实例](restart-instances.md)。
执行以下命令，修改/etc/sysctl.conf配置文件。
vi /etc/sysctl.conf
按i键进入编辑模式，找到如下内容，替换内容末尾数值1为0。
net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0 net.ipv6.conf.lo.disable_ipv6 = 0
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，使配置生效。
sudo sysctl -p
Ubuntu 14/16、OpenSUSE 42
执行以下命令。修改vi /etc/sysctl.conf配置文件。
vi /etc/sysctl.conf
按i键进入编辑模式，找到如下内容，替换内容末
