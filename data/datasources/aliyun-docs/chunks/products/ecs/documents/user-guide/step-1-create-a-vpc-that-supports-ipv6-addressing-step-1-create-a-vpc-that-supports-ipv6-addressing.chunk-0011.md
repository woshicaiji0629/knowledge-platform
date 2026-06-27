vi /etc/sysconfig/network-scripts/ifcfg-eth0
eth0：需要替换为实际网卡接口名称。修改完成后，保存并退出。
按i键进入编辑模式，在文件中根据实际信息添加以下配置。
DHCPV6C=yes IPV6INIT=yes
修改完成后按Esc键退出编辑模式，输入:wq后按下回车键，保存并退出。
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
Alibaba Cloud Linux 4
说明
Alibaba Cloud Linux 4使用NetworkManager管理网络，网卡配置文件位于/etc/NetworkManager/system-connections/目录下，而非传统的/etc/sysconfig/network-scripts/。
执行以下命令，查看网络连接名称。
nmcli connection show
记录连接名称（通常为cloud-init eth0）。
执行以下命令，将IPv6配置为自动获取地址。
nmcli connection modify "cloud-init eth0" ipv6.method auto
cloud-init eth0：需要替换为实际的连接名称。若连接名称包含空格，请使用引号。
执行以下命令，重载网络配置并使其生效。
nmcli connection reload nmcli connection up "cloud-init eth0"
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
CentOS 8
确认网卡配置文件是否包含IPV6INIT=yes和DHCPV6C=yes两项内容。如果包含直接进行下一步操作，如果未包含需先手动添加。
vi /etc/sysconfig/network-scripts/ifcfg-eth0
eth0为网卡标识符，您需要修改成实际的标识符。修改完成后，保存并退出。
禁用cloud-init修改/etc/sysconfig/network-scripts/目录下网卡文件的能力。
说明
分配IPv6地址后无需手动配置，但重启之后可能丢失，因此需要禁用cloud-init修改网卡文件的能力。
执行vi /etc/cloud/cloud.cfg打开网卡配置文件。
vi /etc/cloud/cloud.cfg
在Example datasource config内容前添加以下信息：
network: config: disabled
修改完成后，保存并退出。
重启ECS实例使配置生效。具体操作，请参见[重启实例](restart-instances.md)。
Debian 8/9/10/11、Ubuntu 16
执行vi /etc/net
