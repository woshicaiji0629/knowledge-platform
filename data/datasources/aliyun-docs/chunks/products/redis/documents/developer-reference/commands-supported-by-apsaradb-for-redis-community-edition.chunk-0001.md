## 命令支持
云数据库 Tair（兼容 Redis）兼容多个原生Redis版本：
Tair（企业版）[内存型](../product-overview/dram-based-instances.md)（兼容Redis 7.0）：完全兼容Redis7.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[内存型](../product-overview/dram-based-instances.md)（兼容Redis 6.0）：完全兼容Redis6.2版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[内存型](../product-overview/dram-based-instances.md)（兼容Redis 5.0）：完全兼容Redis5.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair（企业版）[持久内存型](../product-overview/persistent-memory-optimized-instances-1.md)：兼容Redis6.0版本及以下版本接口，部分限制请参见[Tair（企业版）命令支持与限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Tair（企业版）[磁盘型](../product-overview/essd-based-instances-1.md)：兼容Redis6.0版本及以下版本接口，部分限制请参见[Tair（企业版）命令支持与限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Redis开源版：可选择7.0、6.0、5.0，完全兼容社区大版本并向下兼容。
为便于浏览和内容表达，本文的表格约定使用下述注释：
✔️表示支持该命令。
❌表示不支持该命令。
➖表示在原生Redis的该版本下，该命令尚未开始支持。例如原生Redis中，TOUCH命令在3.2.1及以上版本才开始支持，表格中的2.8版本下该命令即被标记为➖。
数字标记①：集群架构实例在执行该命令时，需要开通直连访问并使用直连地址连接至实例，详情请参见[使用直连模式连接实例](../user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。通过Proxy节点的连接地址连接至实例时，也兼容支持该命令。
数字标记②：为兼容某些客户端框架，执行CONFIG SET命令时仅返回OK，不会真正地修改参数。
本文以最新内核小版本进行介绍，部分命令可能在指定小版本后开放支持，详情请参见[Redis](..
