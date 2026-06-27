stemctl restart systemd-networkd |  |
| Alibaba Cloud Linux 2 | 2 | systemctl restart network |
| Alibaba Cloud Linux 3 | 3 | systemctl restart NetworkManager |

如果 DHCP 选项集关联的 VPC 开启了[共享](vpc-sharing.md)[VPC](vpc-sharing.md)功能，则 DHCP 选项集也会对共享 VPC 内的 ECS 生效。
修改 DHCP 选项集
默认 DHCP 选项集不支持修改，自定义 DHCP 选项集指定的域名和 DNS 服务器 IP 可修改。
修改 DHCP 选项集后，关联 VPC 内的新建 ECS 会自动使用最新配置，存量 ECS 需要通过重启实例中 DHCP 进程，才能使用最新配置。确保不影响业务的前提下，您也可以通过重启实例或重启网络服务，确保存量 ECS 使用最新配置。
删除 DHCP 选项集
需先确保已解除与 VPC 的关联，在目标 DHCP 选项集的操作列或详情页，单击删除。
