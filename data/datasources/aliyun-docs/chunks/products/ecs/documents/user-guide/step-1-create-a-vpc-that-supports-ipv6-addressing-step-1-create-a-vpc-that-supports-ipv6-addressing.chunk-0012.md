e datasource config内容前添加以下信息：
network: config: disabled
修改完成后，保存并退出。
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
Debian 8/9/10/11、Ubuntu 16
执行vi /etc/network/interfaces打开网卡配置文件，在文件中根据实际信息添加以下内容：
iface eth0 inet6 dhcp
eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
Ubuntu 18/20
禁用cloud-init修改/etc/sysconfig/network-scripts/目录下网卡文件的能力。
说明
分配IPv6地址后无需手动配置，但重启之后可能丢失，因此需要禁用cloud-init修改网卡文件的能力。
执行vi /etc/cloud/cloud.cfg打开网卡配置文件。
vi /etc/cloud/cloud.cfg
在Example datasource config内容前添加以下信息：
network: config: disabled
修改完成后，保存并退出。
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
Ubuntu 14
执行vi /etc/network/interfaces打开网卡配置文件，在文件中根据实际信息添加以下内容：
iface eth0 inet6 dhcp
eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
FreeBSD 11
执行vi /etc/rc.conf命令，打开网卡配置文件，在文件中根据实际信息添加以下内容：
ipv6_enable="YES" ipv6_ifconfig_vtnet0="<IPv6地址> <子网前缀长度>"
vtnet0：需要替换为实际网卡接口名称。修改完成后，保存并退出。
继续在文件中修改以下信息，修改完成后，保存并退出。
ip6addrctl_enable="YES" ipv6_activate_all_interfaces="YES" ipv6_network_interfaces="auto"
修改完成后，配置文件内容示例如下：
hostname="Aliyun" sshd_enable="YES" dumpdev="NO" ipv6_enable="YES" ip6addrctl_enable="YES" ip6addrctl_policy="ipv4_prefer" ipv
