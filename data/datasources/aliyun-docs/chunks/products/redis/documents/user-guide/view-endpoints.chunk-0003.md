## 代理模式与直连模式
云数据库 Tair（兼容 Redis）支持的连接模式：
代理模式
客户端通过代理服务器（Proxy Server）连接实例。
Proxy为阿里云完全自研，承担着路由转发、负载均衡、模式转换与故障转移等职责，同时支持执行[阿里云自研的](https://help.aliyun.com/zh/tair/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode#concept-2353538)[Proxy](https://help.aliyun.com/zh/tair/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode#concept-2353538)[命令](https://help.aliyun.com/zh/tair/developer-reference/in-house-commands-for-tair-instances-in-proxy-mode#concept-2353538)，具有聚合连接、增强读性能、简单易用等优势，有助于您设计更高效的业务系统，更多信息请参见[Tair Proxy](https://help.aliyun.com/zh/tair/product-overview/features-of-proxy-nodes#concept-2334147)[特性说明](https://help.aliyun.com/zh/tair/product-overview/features-of-proxy-nodes#concept-2334147)。
直连模式
若实例为标准架构，客户端将直接连接主节点（Master）。
若实例为集群架构，客户端将直接连接实例，由原生Redis Cluster进行负载均衡等，与原生Redis Cluster连接模式完全一致。
各架构的网络、连接功能矩阵
为便于阅读，约定✔️表示支持该功能，❌表示不支持该功能。
