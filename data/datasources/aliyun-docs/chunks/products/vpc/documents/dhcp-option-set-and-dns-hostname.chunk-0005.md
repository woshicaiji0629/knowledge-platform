### 控制台
创建 DHCP 选项集
每个地域首次为 VPC 启用 DNS 主机名时，自动创建默认 DHCP 选项集并关联至 VPC。默认 DHCP 选项集不支持修改，您可以前往[专有网络控制台 - DHCP 选项集](https://vpc.console.aliyun.com/dhcp/cn-hangzhou/dhcps)，创建DHCP选项集，配置与 DNS 解析服务对应的域名和DNS 域名服务器IP。
如果 VPC 已关联其他 DHCP 选项集，VPC 启用 DNS 主机名后，将不会关联默认 DHCP 选项集，您需要自行修改关联关系。
关联专有网络
VPC 与 DHCP 选项集的关联关系，可在目标 VPC 详情页的DHCP选项集参数项、目标 DHCP 选项集的操作列或详情页，进行建立、更改或解除。
关联关系变更后，新建 ECS 会自动使用最新配置，存量 ECS 需要通过sudo dhclient -r eth0 && sudo dhclient eth0重启实例中 DHCP 进程，才能使用最新配置；解除关联关系后，阿里云会通过 DHCP 为 ECS 指定默认 DNS 服务器。确保不影响业务的前提下，您也可以通过重启实例或重启网络服务，确保存量 ECS 使用最新配置。
常见操作系统重启网络服务的命令

| 操作系统 | Version | 重启网络服务命令 |
| --- | --- | --- |
| CentOS | 6 | service network restart |
| 7 | systemctl restart network |  |
| 8 | systemctl restart NetworkManager |  |
| Debian | 8 | systemctl restart networking |
| 9 | systemctl restart networking |  |
| 10 | systemctl restart networking |  |
| Ubuntu | 14 | service networking restart |
| 16 | systemctl restart networking |  |
| 18 | systemctl restart systemd-networkd |  |
| 20 | systemctl restart systemd-networkd |  |
| Alibaba Cloud Linux 2 | 2 | systemctl restart network |
| Alibaba Cloud Linux 3 | 3 | systemctl restart NetworkManager |
