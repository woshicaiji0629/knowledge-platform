## Tair（企业版）命令支持
Tair（企业版）实例兼容多个原生Redis版本：
Tair内存型（兼容Redis 7.0、6.0和5.0）：
Tair内存型（兼容Redis 7.0）：完全兼容Redis社区7.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair内存型（兼容Redis 6.0）：完全兼容Redis社区6.2版本及以下版本接口，额外支持Tair扩展数据结构。
Tair内存型（兼容Redis 5.0）：完全兼容Redis社区5.0版本及以下版本接口，额外支持Tair扩展数据结构。
Tair持久内存型：兼容Redis社区6.0版本及以下版本接口，部分限制请参见[Tair（企业版）持久内存型和磁盘型额外的命令限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
Tair磁盘型：兼容Redis社区6.0版本及以下版本接口，部分限制请参见[Tair（企业版）持久内存型和磁盘型额外的命令限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。
为便于浏览和内容表达，本文的表格约定使用下述注释：
✔️表示支持该命令。
❌表示不支持该命令。
数字标记①：集群架构实例在执行该命令时，需要开通直连访问并使用直连地址连接至实例，详情请参见[使用直连模式连接实例](../user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。通过Proxy节点的连接地址连接至实例时，也兼容支持该命令。
数字标记②：为兼容某些客户端框架，执行CONFIG SET命令时仅返回OK，不会真正地修改参数。如果您的业务需要对参数进行修改，可通过控制台和API进行操作，具体操作请参见[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)。
本文以最新内核小版本进行介绍，部分命令可能在指定小版本后开放支持，详情请参见[Tair](../support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](../support/apsaradb-for-redis-enhanced-edition-1.md)和[Proxy](../support/apsaradb-for-redis-proxy-nodes.md)[小版本发布日志](../support/apsaradb-for-redis-proxy-nodes.md)。
说明
各命令族中的命令，
