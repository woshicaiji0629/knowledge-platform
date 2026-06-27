## 常见问题
Tair集群架构与开源Redis Cluster有什么区别？
相比开源Redis Cluster，云数据库 Tair（兼容 Redis）集群架构在安全性、内核性能、负载均衡和扩缩容等方面具有如下优势：
内核性能提升：Tair集群架构实例在内核性能方面进行大量优化，包含但不限如下。
容灾速度更快，不会产生Gossip广播风暴问题。
在集群实例扩缩容时，支持自动重新平衡分片数据，且在数据重新平衡时对业务请求几乎无影响。
轻松支持大量短连接场景。
便捷运维管理：相比自购服务器搭建Redis数据库，Tair集群架构实例支持多维度访问控制，支持灵活弹性扩缩容，提供丰富的监控指标以及多种高可用容灾方案等，更多信息请参见[与自建](comparison-between-apsaradb-for-redis-and-self-managed-redis.md)[Redis](comparison-between-apsaradb-for-redis-and-self-managed-redis.md)[的对比](comparison-between-apsaradb-for-redis-and-self-managed-redis.md)。
支持代理模式：Tair集群架构实例可选择代理模式，该模式提供代理服务器（Proxy），通过Proxy能实现架构转换，帮助您如同在使用标准架构一样地使用集群架构。同时，Proxy还支持负载均衡和路由转发、管理只读节点流量、缓存热点Key信息与支持集群架构使用多数据库（DB）等，更多信息请参见[Tair Proxy](features-of-proxy-nodes.md)[特性说明](features-of-proxy-nodes.md)。
标准架构升级至集群架构后需要修改代码吗？
若实例升级至集群架构代理模式，无需修改代码。您仍可以像使用标准架构一样地使用集群架构，因为[Proxy](features-of-proxy-nodes.md)[节点](features-of-proxy-nodes.md)能够实现架构转换。这将显著降低业务改造成本。
若实例升级至集群架构直连模式，需修改连接池代码，以更换为支持Cluster的客户端。
说明
除此之外，您还需了解并遵守集群架构执行多Key（跨Slot）命令、事务以及Lua脚本等相应的规范，更多信息请参见[集群架构命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
集群架构实例变配后，数据是否会自动均衡？
在标准架构升级至集群架构，或在集群架构中增减分片时，实例将自动分析数据的分布情况，并执行数据重平衡。您无需执行额外
