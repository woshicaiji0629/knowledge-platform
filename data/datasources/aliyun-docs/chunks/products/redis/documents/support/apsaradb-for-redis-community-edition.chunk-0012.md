4-03-14 | 功能优化 | INFO STATS 命令增加返回客户端输入、输出缓冲区超限断连的统计： client_query_buffer_limit_disconnections client_output_buffer_limit_disconnections 新增实时大 Key 统计阈值，默认为 2000。例如 String 类型的字符长度超过 2000 即判定为大 key；List、Set、Hash 等类型的元素个数超过 2000 个即判定为大 Key 等。 |
| 缺陷修复 | 修复 Stream 类型大 Key 统计错误的问题。 |  |  |  |
| 7.0.1.5 | LOW | 2024-01-09 | 功能优化 | 优化主动过期的效率。 INFO CLIENTS 命令中增加 pubsub_clients 监控项。 |
| 7.0.1.4 | HIGH | 2023-11-15 | 功能优化 | 更新至 Redis 开源社区 7.0.14 版本，更多信息请参见 [Redis 7.0.14 release note](https://github.com/redis/redis/blob/7.0.14/00-RELEASENOTES) 。 |
| 安全加固 | 修复 CVE-2023-41056 安全漏洞。 修复 CVE-2023-41053 安全漏洞。 |  |  |  |
| 7.0.1.3 | LOW | 2023-08-28 | 功能优化 | 优化实例扩缩容流程。 集群实例支持多可用区容灾部署。 |
| 7.0.1.2 | HIGH | 2023-08-01 | 新特性 | 集群架构直连模式实例支持 TLS 链路加密功能。 集群架构代理模式实例支持 IP 透传功能，您可以通过 ptod_enabled 参数进行控制。 集群架构实例的 SPUBLISH 命令支持分片内广播。 |
| 功能优化 | 更新至 Redis 开源社区 7.0.12 版本，包含多项性能优化、安全漏洞修复等，例如修复 CVE-2022-24834、CVE-2023-36824 等安全漏洞，更多信息请参见 [Redis 7.0.12 release note](https://github.com/redis/redis/blob/7.0.12/00-RELEASENOTES) 。 |  |  |  |
| 缺陷修复 | 修复热点 Key 过期时可能导致实例崩溃（Crash）的问题。 |  |  |  |
| 7.0.1.1 | LOW | 2023-07-17 | 功能优化 | 优化集群架构实例主备切换和重启的流程。 |
| 7.0.1.0 | LOW | 2023-04-20 | 新特性 | 支持售卖集群架构、读写分离架构。 支持集群架构无感扩缩容。 定
