### 网络ACL使用限制与配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_nacl_ingress_entry | 单个网络 ACL 支持创建的入方向规则数量 网络 ACL 所属 VPC 开启了 IPv6 时，支持创建的 IPv4/IPv6 入方向规则，默认均为 20 条。 | 20 条 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_nacl_egress_entry | 单个网络 ACL 支持创建的出方向规则数量 网络 ACL 所属 VPC 开启了 IPv6 时，支持创建的 IPv4/IPv6 入方向规则，默认均为 20 条。 | 20 条 |  |
| nacl_quota_vpc_create_count | 单个 VPC 支持创建的网络 ACL 数量 | 20 个 |  |
