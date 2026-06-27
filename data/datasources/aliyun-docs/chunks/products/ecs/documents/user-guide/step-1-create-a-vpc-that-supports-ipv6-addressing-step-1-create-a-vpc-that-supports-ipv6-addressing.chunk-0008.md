v6 = 0
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，验证/etc/sysctl.conf配置信息是否与initramfs中的/etc/sysctl.conf存在差异。
diff -u /etc/sysctl.conf <(lsinitrd -f /etc/sysctl.conf)
说明
Alibaba Cloud Linux 2配置了initramfs（initram file system）。如果initramfs中的/etc/sysctl.conf文件与IPv6的配置文件/etc/sysctl.conf存在差异，系统可能会生效新的配置，与您需求的配置混淆。
若两个配置文件存在差异，执行以下命令，重新生成initramfs。
sudo dracut -v -f
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
执行ip addr | grep inet6或者ifconfig | grep inet6命令，验证是否已成功开启IPv6。
若系统返回inet6相关内容，则表示IPv6服务已成功开启。
Alibaba Cloud Linux 4
执行以下命令，修改/etc/sysctl.conf配置文件。
vi /etc/sysctl.conf
按i键进入编辑模式，添加或修改以下内容：
net.ipv6.conf.all.disable_ipv6 = 0 net.ipv6.conf.default.disable_ipv6 = 0
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令使配置生效。
sysctl -p
执行ip -6 addr show命令，验证是否已成功开启IPv6。
若系统返回inet6相关内容，则表示IPv6服务已成功开启。
CentOS 6/7
执行以下命令，修改/etc/modprobe.d/disable_ipv6.conf配置文件。
vi /etc/modprobe.d/disable_ipv6.conf
按i键进入编辑模式，将options ipv6 disable=1修改为options ipv6 disable=0。
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
执行以下命令，修改/etc/sysconfig/network配置文件。
vi /etc/sysconfig/network
按i键进入编辑模式，将NETWORKING_IPV6=no修改为NETWORKING_IPV6=yes。
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
（可选）依次执行以下命令，重新加载IPv6模块。
说明
若您的操作系统为CentOS 6，则需要执行该步骤。否则，跳
