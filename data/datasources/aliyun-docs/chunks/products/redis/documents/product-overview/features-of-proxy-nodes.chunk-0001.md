| Proxy 能力 | 说明 |
| --- | --- |
| 集群版使用模式转换 | Proxy 能够实现架构转换，帮助您如同在使用标准架构一样地使用集群架构。Proxy 支持对 DEL 、 EXISTS 、 MGET 、 MSET 、 SDIFF 与 UNLINK 等命令进行跨 Slot 的多 Key 操作，更多信息请参见 [代理模式（Proxy）支持的命令列表](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md) 。 当标准架构无法支撑业务发展时，您无需修改代码即可将标准架构的数据迁移至带有 Proxy 的集群架构，大幅度降低业务改造成本。 |
| 负载均衡和路由转发 | Proxy 与后端的数据分片建立长连接，负责请求负载均衡和路由转发操作，关于转发规则的介绍，请参见 [Proxy](features-of-proxy-nodes.md) [的路由转发规则](features-of-proxy-nodes.md) 。 |
| 管理只读节点流量 | Proxy 会实时探测只读节点的状态，当出现下述情况时，Proxy 会执行流量管控动作： 只读节点处于异常状态：Proxy 会降低该节点的服务权重，如果多次无法连接该节点，Proxy 会停止该节点的服务（即不再将流量转发至该节点），待该异常被修复后重新启用该节点。 只读节点处于全量同步状态：Proxy 会暂时停止该节点的服务，直到该节点完成全量同步。 |
| [代理查询缓存](features-of-proxy-nodes.md) | 开启代理查询缓存功能（Proxy Query Cache）后，Proxy 会缓存热点 Key 对应的请求和返回信息，当在有效时间内收到同样的请求时直接返回结果至客户端，无需和后端的数据分片交互，可更好地改善对热点 Key 的发起大量读请求导致的访问倾斜。 说明 您可以设置 query_cache_enabled [参数](../user-guide/parameter-support.md) 开启该功能，仅 Tair 内存型、持久内存型实例支持该功能。 |
| 支持多数据库（DB） | 集群模式下，原生 Redis 和 Cluster client 均不支持多数据库（DB）功能，只使用默认的 0 号数据库，也不支持 SELECT 命令。但您可以通过 Proxy 访问集群实例，支持多数据库（DB）功能，支持使用 SELECT 命令，集群版实例默认为 256 个 DB。 说明 若您使用 StackExchange.Redis 客户端，请使用 StackExchange.Redis 2.7.20 及以上版本，否则会产生报错，更多
