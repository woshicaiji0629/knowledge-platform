| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.4.10 | MEDIUM | 2020-12-01 | 功能优化 | 优化密码错误场景下的提示信息，易于理解。 |
| 6.4.9 | HIGH | 2020-11-06 | 缺陷修复 | 修复多线程模式下开启 [SSL](../user-guide/configure-ssl-encryption.md) [加密](../user-guide/configure-ssl-encryption.md) 功能导致的崩溃问题。 修复执行 UNSUBSCRIBE 时，Channel（频道）中包含 0 时导致的 Response 协议错误的问题。 |
| 6.4.8 | HIGH | 2020-10-21 | 功能优化 | 运行日志对大包、ASK 回复包和 MOVED 包的二进制请求进行编码后记录，避免日志乱码问题。 |
| 缺陷修复 | 修复 max_session_processing（单个连接允许堆积的最大请求数）的配置不能被动态设置的问题。更多参数的介绍，请参见 [Redis](../user-guide/supported-parameters.md) [开源版配置参数列表](../user-guide/supported-parameters.md) 。 |  |  |  |
| 6.4.7 | MEDIUM | 2020-10-09 | 功能优化 | 优化 Proxy 节点的内部监控。 |
| 6.4.6 | HIGH | 2020-09-30 | 缺陷修复 | 修复因节点角色未初始化，导致的标准或集群架构的实例执行 SLOWLOG 命令可能超时的问题。 修复了特定规格的 [Memcache](https://help.aliyun.com/zh/memcache/product-overview/product-overview) [实例](https://help.aliyun.com/zh/memcache/product-overview/product-overview) 通过 [数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) [DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) 连接失败的问题。 修复订阅 __keyspace@0__ 时，未指定 Key 导致的崩溃问题。 |
| 6.4.5 | LOW | 2020-09-27 | 新特性 | 增加对部分内部命令的支持。 |
| 6.4.
