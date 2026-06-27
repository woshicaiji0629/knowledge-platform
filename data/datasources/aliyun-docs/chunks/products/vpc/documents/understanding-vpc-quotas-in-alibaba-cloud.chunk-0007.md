### 高可用虚拟IP使用限制与配额

| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| 无 | 支持创建高可用虚拟 IP（HaVip）的网络类型 | VPC 类型 | 无法提升 |
| 单个 ECS 实例支持同时绑定的 HaVip 数量 | 5 个 |  |  |
| 单个 HaVip 支持同时绑定的 EIP 数量 | 1 个 |  |  |
| 单个 HaVip 支持同时绑定的 ECS 实例或弹性网卡的数量 | 10 个 1、1 个 HaVip 支持同时绑定 10 个 ECS 实例或同时绑定 10 个弹性网卡，但 1 个 HaVip 不能同时绑定 ECS 实例和弹性网卡。 2、HaVip 具有子网属性，仅支持绑定到同一交换机下的 ECS 实例或弹性网卡上。 |  |  |
| HaVip 是否支持广播和组播通信 | 不支持 HaVip 只支持单播，如果您使用 Keepalived 等第三方软件实现高可用，需要修改配置文件中的通信方式为单播通信。 |  |  |
| 单个账号支持创建的 HaVip 的数量 | 50 个 |  |  |
| 单个 VPC 支持创建的 HaVip 的数量 | 50 个 |  |  |
| vpc_quota_havip_custom_route_entry | 单个路由表内，目的地址指向 HaVip 的路由条目的数量 | 5 条 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
