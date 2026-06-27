apsaradb-for-redis-instance.md)。通过Proxy节点的连接地址连接至实例时，也兼容支持该命令。
数字标记②：为兼容某些客户端框架，执行CONFIG SET命令时仅返回OK，不会真正地修改参数。
本文以最新内核小版本进行介绍，部分命令可能在指定小版本后开放支持，详情请参见[Redis](../support/apsaradb-for-redis-community-edition.md)[开源版小版本发布日志](../support/apsaradb-for-redis-community-edition.md)和[Proxy](../support/apsaradb-for-redis-proxy-nodes.md)[小版本发布日志](../support/apsaradb-for-redis-proxy-nodes.md)。
说明
各命令族中的命令，如无特殊备注和说明，默认支持Redis实例的所有架构，即标准架构、集群架构及读写分离架构。集群架构与读写分离架构在使用某些特定的命令时存在一些限制，更多信息请参见[集群架构与读写分离实例的命令限制](limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
