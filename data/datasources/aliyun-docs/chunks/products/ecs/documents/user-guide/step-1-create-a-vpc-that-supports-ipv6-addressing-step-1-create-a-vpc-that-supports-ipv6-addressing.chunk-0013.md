terfaces="auto"
修改完成后，配置文件内容示例如下：
hostname="Aliyun" sshd_enable="YES" dumpdev="NO" ipv6_enable="YES" ip6addrctl_enable="YES" ip6addrctl_policy="ipv4_prefer" ipv6_activate_all_interfaces="YES" ipv6_network_interfaces="auto" ifconfig_lo0="inet 127.0.0.1 netmask 255.0.0.0" ifconfig_vtnet0="inet 192.168.XX.XX netmask 255.255.255.0" ipv6_ifconfig_vtnet0="2001:XXXX:4:4:4:4:4:4 prefixlen 64" defaultrouter="192.168.XX.XX" hostname="freebsd"
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
Anolis OS 7.9/8.4、CentOS Stream、Fedora
确认网卡配置文件是否包含IPV6INIT=yes和DHCPV6C=yes两项内容。如果包含无需再做任何操作，如果未包含需先手动添加。
vi /etc/sysconfig/network-scripts/ifcfg-eth0
eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
手动配置（Windows）
远程连接Windows实例。
具体操作，请参见[使用](connect-to-a-windows-instance-through-workbench.md)[Workbench](connect-to-a-windows-instance-through-workbench.md)[登录](connect-to-a-windows-instance-through-workbench.md)[Windows](connect-to-a-windows-instance-through-workbench.md)[实例](connect-to-a-windows-instance-through-workbench.md)。
打开命令行工具，执行ipconfig命令，检查实例是否已开启IPv6服务。
如果未返回inet6相关内容：表示实例未开启IPv6服务，请开启IPv6服务。
如何开启IPv6服务？
选择控制面板>网络和共享中心>网络连接。
单击当前网络连接名，打开状态界面，再单击属性。
选中Internet 协
