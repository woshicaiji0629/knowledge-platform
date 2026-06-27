### 选择容灾方案
云数据库 Tair（兼容 Redis）提供了单可用区、同城、跨地域三种容灾方式，可根据您的业务要求进行选择。

| 灾备方案 | 说明 | 操作指引 |
| --- | --- | --- |
| [单可用区高可用方案](disaster-recovery.md) | 主备节点部署在同一可用区中的不同机器上，提供机器级别故障恢复能力。 | 在售卖页 可用区类型 选择 单可用区 。 |
| [同城容灾（多可用区）方案](disaster-recovery.md) | 主备节点部署在同一地域下的不同可用区（机房）中，提供机房级别故障恢复能力。 | 在售卖页 可用区类型 选择 双可用区 。 |
| [跨地域容灾方案](disaster-recovery.md) | 由多个子实例部署在不同地域构成全球分布式实例，提供地域级别（自然灾害）故障恢复能力。更多介绍，请参见 [全球多活](../user-guide/overview-of-global-distributed-cache-for-tair.md) 。 | 具体操作，请参见 [创建分布式实例](../user-guide/create-a-distributed-instance.md) 。 |
