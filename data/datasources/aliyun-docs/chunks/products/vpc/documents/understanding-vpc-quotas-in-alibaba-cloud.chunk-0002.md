### 路由器和路由表使用限制与配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_route_tables_num | 单个 VPC 支持创建的自定义路由表的数量 | 9 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_route_entrys_num | 单个路由表支持创建的自定义路由条目的数量（不包括 [动态传播路由条目](vpc-route-table.md) ） | 200 条 |  |
| vpc_quota_dynamic_route_entrys_num | 单个路由表来自动态传播的路由条目数量 | 200 条 |  |
| vpc_quota_havip_custom_route_entry | 指向一个 HaVip 实例的自定义路由上限 | 5 个 |  |
| vpc_quota_vpn_custom_route_entry | 单个 VPC 内指向 VPN 的自定义路由上限 | 50 个 |  |
| 无 | 单个路由表支持绑定的标签数量 | 20 个 | 无法提升 |
| 单个 VPC 支持创建的路由器的数量 | 1 个 |  |  |
| 单个 VPC 支持指向转发路由器 TR 连接的最大路由条目数量 | 600 条 |  |  |
