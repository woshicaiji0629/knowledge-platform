### VPC和交换机使用限制与配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_instances_num vpc_quota_instances_num_${RegionId}优先级高于 vpc_quota_instances_num | 单个地域支持创建的 VPC 的数量 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_instances_num_${RegionId} ${RegionId}为地域的变量，表示不同地域的配额名称不同。 | 指定地域支持创建的 VPC 的数量 | 10 个 |  |
| vpc_quota_vswitches_num | 单个 VPC 支持创建的交换机的数量 | 150 个 |  |
| vpc_quota_secondary_cidr_num | 单个 VPC 支持创建的附加 IPv4 网段的数量 | 5 个 |  |
| 无 | 单个 VPC 支持创建的附加 IPv6 网段的数量 | 5 个 | 无法提升 |
| 单个 VPC 支持创建的 IPv4 预留网段的数量 | 100 个 |  |  |
| 单个 VPC 支持创建的 IPv6 预留网段的数量 | 100 个 |  |  |
| 单个 VPC 支持创建的用户网段的数量 | 3 个 |  |  |
| 单个 VPC 支持云资源使用的私网网络地址数量 | 300,000 个 1、如果 ECS 实例仅有一个私网 IP，则该 ECS 实例仅使用一个网络地址。 2、如果 ECS 实例绑定了多个网卡或网卡配置了多个 IP，则该 ECS 实例使用的网络地址数为与 ECS 实例绑定的网卡上分配的 IP 地址数量之和。 |  |  |
| 单个 VPC 支持绑定的标签数量 | 20 个 |  |  |
| 单个交换机支持绑定的标签数量 | 20 个 |  |  |
