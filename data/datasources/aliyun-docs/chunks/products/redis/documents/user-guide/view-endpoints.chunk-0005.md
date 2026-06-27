## 专有网络与公网
云数据库 Tair（兼容 Redis）支持的网络类型：
专有网络
专有网络VPC（Virtual Private Cloud）是私有网络环境，通过底层网络协议，在网络二层完成网络隔离，具备安全可靠、灵活可控、简单易用的特性和较强的可扩展性。更多信息请参见[什么是专有网络](../../../vpc/documents/what-is-vpc.md)[VPC](../../../vpc/documents/what-is-vpc.md)。
应用场景：[ECS](../../../ecs/documents/user-guide/what-is-ecs.md)[实例](../../../ecs/documents/user-guide/what-is-ecs.md)与实例属于同一专有网络，并通过专有网络连接至实例，可获得更高的安全性和更低的网络延迟。
公网（Internet）
公网即互联网，更多信息请参见[申请公网连接地址](apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md)。
通过公网连接实例不会产生阿里云流量费用，但存在一定的安全风险，推荐通过专有网络连接以获取更高的安全性。
应用场景：本地设备、不同专有网络的ECS实例和第三方云产商可通过公网连接实例。
