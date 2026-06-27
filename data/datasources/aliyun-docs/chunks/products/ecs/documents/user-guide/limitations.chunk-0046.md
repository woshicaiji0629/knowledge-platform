## 弹性网卡

| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下能创建的弹性网卡（辅助网卡）的最大数量 | 请根据配额 ID q_elastic-network-interfaces 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 实例绑定弹性网卡的 VPC 及可用区限制 | 实例和绑定的弹性网卡，必须属于同一 VPC、同一可用区。 实例绑定的多张弹性网卡，可以属于同一 VPC、同一可用区下的不同子网（交换机）。 如果将来自同一子网的两个或多个网卡附加到一个实例，可能会遇到非对称路由等网络问题。您可以通过在一张弹性网卡（主网卡或辅助弹性网卡）上分配一个或多个辅助私网 IP 地址，实现专有网络 VPC 类型 ECS 实例的高利用率和负载故障时的流量转移。更多信息，请参见 [辅助私网](assign-secondary-private-ip-addresses.md) [IP](assign-secondary-private-ip-addresses.md) 。 | 无 |
| 单个实例可绑定的弹性网卡数量上限 | 实例可绑定的网卡数量由实例规格决定，更多信息，请参见 [实例规格族](overview-of-instance-families.md) 中的 弹性网卡 。 | 无 |

关于弹性网卡的更多内容，请参见[弹性网卡概述](eni-overview.md)。
