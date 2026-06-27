# Proxy小版本发布公告-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/support/apsaradb-for-redis-proxy-nodes

# Proxy小版本发布日志
为提升用户体验，云数据库 Tair（兼容 Redis）会不定期地发布Proxy（代理）节点的小版本，用于丰富云产品功能或修复已知缺陷。您可以参阅本文了解Proxy小版本的更新说明，选择在业务低峰期升级小版本。
## 如何查询或升级Proxy的小版本
您可以通过控制台查看当前的小版本，具体操作及升级小版本的其注意事项，请参见[升级小版本与代理版本](../user-guide/update-the-minor-version.md)。
图 1.查看Proxy小版本在实例的基本信息页面，您可查看代理版本字段（如6.5.8）。
说明
系统会自动检测实例的小版本，如果集群代理升级按钮不存在或处于无法单击的状态，表示小版本已经是最新。
由于各地域版本发布进度可能有所差异，小版本发布情况以当前控制台显示为准。
## Proxy介绍
在云数据库 Tair（兼容 Redis）的[集群架构](../product-overview/cluster-master-replica-instances.md)和[读写分离架构](../product-overview/read-or-write-splitting-instances-1.md)中，代理服务器（Proxy）承担着路由转发、负载均衡与故障转移等职责。通过了解Proxy的路由转发规则和特定命令的处理方式，有助于您设计更高效的业务系统。更多信息，请参见[Tair Proxy](../product-overview/features-of-proxy-nodes.md)[特性说明](../product-overview/features-of-proxy-nodes.md)。
## 更新级别说明
LOW（低）：一般级别，包含日常新功能升级（例如新增某个功能）。
MEDIUM（中）：推荐级别， 包含功能模块优化类的升级（例如优化了某个功能）。除此以外，还包含了LOW级别所包含的更新内容。
HIGH（高）：重要级别，包含影响稳定性或安全性的重要升级（例如修复某个漏洞或缺陷）。除此以外，还包含LOW和MEDIUM级别所包含的更新内容。
说明
下述表格仅记录7.0.x与6.8.x版本发布记录，在此之前的小版本发布记录请参见[历史版本](apsaradb-for-redis-proxy-nodes.md)。
## 7.0.x
重要
7.x版本仅发布云原生版。
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 7.1.6 | MEDIUM | 2026-01-24 | 功能优化 | 支持 bf.scandump 命令。 |
| 缺陷修复 | 修改向量全局索引功能在 db 节点访问失败时可能导致的异常。 |  |  |  |
| 7.1.5 | MEDIUM | 2025-12-09 | 功能优化 | 监控项支持 P95、P99 RT。 支持 wait 命令（proxy 直接返回命令中 numreplicas 参数值）。 |
| 缺陷修复 | 修复私有连接池功能开启后有小概率异常的问题。 |  |  |  |
| 7.1.3 | MEDIUM | 2025-10-27 | 功能优化 | 新增 subscribe_route_ronode_enabled 参数配置，支持订阅命令路由至只读节点。 在读写分离架构中，启用此配置后， SUBSCRIBE 、 SSUBSCRIBE 和 PSUBSCRIBE 命令可以被路由到只读节点。 开启此功能后， __keyevent@ 和 __keyspace@ 等键空间通知频道也可能被路由到只读节点。 如需将特定会话的所有请求（包括订阅）强制路由到主节点，可以使用 AUTH <user>:<password>:master 命令进行认证。 优化低 QPS 场景下审计日志的源 IP 被错误记录为 Proxy 实例地址的问题。 |
| 7.0.21 | MEDIUM | 2025-07-29 | 功能优化 | CLIENT LIST 命令新增返回以下统计项： tot-net-in ：表示该连接的总入流量。 tot-net-out ：表示该连接的总出流量。 tot-cmds ：表示该连接的总请求数。 Redis 7.0 实例的 INFO 、 IINFO 命令支持 Latencystats 模块（Section）统计信息。 |
| 缺陷修复 | 修复在使用 Vecotr 命令后，实例规格变更可能失败的问题。 Redis cluster 语法兼容模式支持 CLUSTER COUNTKEYSINSLOT 和 CLUSTER GETKEYSINSLOT 子命令。 |  |  |  |
| 7.0.20 | LOW | 2025-07-04 | 功能优化 | 支持 XSETID 命令的可选参数。 |
| 7.0.19 | MEDIUM | 2025-06-04 | 缺陷修复 | 修复部分 Vecotr 请求在客户端断连时可能导致异常的问题。 修复 XGROUP、XINFO、OBJECT HELP 等无 Key 命令导致异常的问题。 |
| 7.0.18 | MEDIUM | 2025-04-02 | 功能优化 | 修复 Tair 向量引擎全局索引在扩容 DB 后写负载不均衡的问题。 修复集群架构读写分离实例的只读节点读流量可能偏低的问题。 |
| 7.0.17 | MEDIUM | 2025-03-12 | 功能优化 | 支持 SCRIPT SHOW 命令。 支持私有连接池功能，在使用阻塞命令、Pub/Sub、WATCH 等命令的场景下能降低 DB 侧的连接数。 |
| 缺陷修复 | 修复执行向量引擎相关请求时客户端连接断开可能导致服务端异常的问题。 修复开启 timeout 参数时，可能会断开 Pub/Sub、Monitor 或正在执行请求连接的问题。 |  |  |  |
## 历史版本
7.0.x
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 7.0.16 | LOW | 2024-12-10 | 功能优化 | 在 Sentinel 免密模式下，支持通过 #no_loose_sentinel-password-free-commands 参数配置更多的免密命令。 |
| 7.0.15 | LOW | 2024-12-02 | 功能优化 | 支持 JSON.MERGE 命令。 支持 TLS 服务端 CA 证书。 优化 Proxy 到 DB 之间的连接，改为使用用户账号权限并按用户账号隔离。 |
| 7.0.14 | LOW | 2024-10-09 | 功能优化 | 支持 TOUCH 命令。 优化 Private 连接（阻塞命令、SUBSCRIBE、WATCH 等命令会使用 Private 连接）的内存使用量。 |
| 缺陷修复 | 修复 TFT.MSEARCH 命令在 DB 没有 Source 信息时异常的问题。 |  |  |  |
| 7.0.13 | LOW | 2024-08-13 | 功能优化 | 支持通过 #no_loose_sentinel-password-free-access 配置项，免密执行 SUBSCRIBE 命令订阅 +switch-master Channel（仅限该 Channel）。 |
| 7.0.12 | MEDIUM | 2024-07-24 | 功能优化 | 优化 TairVector 全局索引接口的返回值。 支持通过 #no_loose_sentinel-password-free-access 配置项，免密执行 Sentinel 相关命令。 |
| 缺陷修复 | 修复 TairVector 全局索引在部分场景下删除异常的问题。 修复 SCRIPT EXISTS 命令在 Lua 存在时也返回 0 的问题。 |  |  |  |
| 7.0.11 | LOW | 2024-07-04 | 缺陷修复 | 修复了使用 JSON.SET 或 GIS.ADD 命令之后进行变配可能失败的问题。 |
| 7.0.10 | MEDIUM | 2024-06-18 | 新特性 | 支持 TairVector 全局索引功能。 |
| 功能优化 | 优化主备同步故障的恢复时间，降低异常时的影响。 |  |  |  |
| 缺陷修复 | 修复 TFT.MSEARCH 请求结果排序异常的问题。 修复单个 Tair 、 Tair 分片在 Key 数量很多（大于 2^24）时， SCAN 命令的返回结果可能不正确的问题。 |  |  |  |
| 7.0.9 | MEDIUM | 2024-04-08 | 功能优化 | 支持 RESP2、3 协议，并通过 HELLO 命令切换协议。但在使用前，您需要先在实例的参数设置中将 hello_enabled 参数设置为 1。 INFO 命令支持返回 pubsub_clients 和 tracking_clients 字段（需要实例兼容 Redis 6.0 及以上）。 |
| 缺陷修复 | 修复在 SSL 或 TLS 连接下，当回复数据量较大、写满 Socket 缓冲区时有可能断开连接的问题。 |  |  |  |
| 7.0.8 | MEDIUM | 2024-02-09 | 缺陷修复 | 修复在事务中连续执行 SELECT 命令或事务尾部执行 SELECT 命令可能会导致异常的问题。 修复热点 Key 缓存功能（Query cache）功能有小概率异常的问题。 修复在 TLS、SSL 连接下的请求有概率超时的问题。 |
| 7.0.7 | LOW | 2023-12-15 | 功能优化 | 优化故障恢复时间，DB 故障的场景下能快速断连恢复服务。 当发生阻塞时，优化同一连接在后续立刻发起的普通请求所记录的 RT（Response Time）值 ，避免记录慢日志。 支持 TairSearch 的 TFT.EXPLAINSCORE 命令。 |
| 7.0.6 | LOW | 2023-09-01 | 功能优化 | 降低日志记录线程的 CPU 消耗。 |
| 7.0.5 | MEDIUM | 2023-08-29 | 缺陷修复 | 修复在读写分离实例中，Tair Vector 的部分写命令可能被转发到读节点的问题。 修复 ECHO 命令被统计为写流量的问题。 |
| 7.0.4 | LOW | 2023-08-09 | 新特性 | 支持 Tair 内存型（兼容 Redis 6.0）23.8.0.0 版本新增的 Vector 模块命令。 |
| 7.0.3 | MEDIUM | 2023-07-10 | 功能优化 | 优化事务请求的连接数。在不使用 SELECT 、 WATCH 命令时，事务请求使用公共连接访问 Redis 实例。 |
| 缺陷修复 | 修复在事务请求中执行多次 SELECT 命令可能导致同一连接的后续普通请求选择的 DB 错误的问题。 |  |  |  |
| 7.0.2 | MEDIUM | 2023-05-11 | 新特性 | TR.BITOP 、 TR.BITOPCARD 命令支持跨 Slot 的 Key。 针对持久内存型， INFO 、 IINFO 命令新增返回 Persistence 信息：maxpmem（最大持久内存）、used_pmem（已使用的持久内存），单位为 B（字节）。 支持 RESP 协议嵌套超过 7 层的请求结果。 |
| 功能优化 | 优化 Proxy 模式对 Lua 语法的限制。 |  |  |  |
| 7.0.1 | MEDIUM | 2023-04-11 | 新特性 | 支持在读请求超时后，自动向其他备节点（Slave）重试。 支持 TLS 1.3 协议。 支持 TairSearch 的 TFT.ANALYZER 、 TFT.EXPLAINCOST 命令。 将命令（Command）返回结果从 Proxy 的封装结果修改为 DB 的执行结果。 优化增量订阅（Subscribe）时，Channel（频道）的计算逻辑，降低 CPU 消耗。 |
| 缺陷修复 | 修复一行审计日志的末尾多一个空格的问题。 修复当客户端协议错误时，可能会导致内存泄露的问题。 |  |  |  |
| 7.0.0 | MEDIUM | 2023-03-09 | 新特性 | 支持 Redis 6.2、Redis 7.0 命令。 支持 TairSearch 的 TFT.ANALYZER 命令。 |
6.8.x
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.8.23 | MEDIUM | 2025-02-10 | 功能优化 | 优化 Private 连接（阻塞命令、SUBSCRIBE、WATCH 等命令会使用 Private 连接）的内存使用量。 |
| 6.8.22 | MEDIUM | 2024-09-02 | 缺陷修复 | 增强稳定性。 |
| 6.8.21 | MEDIUM | 2024-07-23 | 缺陷修复 | 修复了使用 JSON.SET 或 GIS.ADD 命令之后进行变配可能失败的问题。 修复 SCRIPT EXISTS 命令在 Lua 存在时也返回 0 的问题。 |
| 6.8.20 | MEDIUM | 2024-06-24 | 新特性 | 组件间兼容性优化。 |
| 6.8.19 | MEDIUM | 2024-06-04 | 功能优化 | 优化主备同步故障的恢复时间，降低异常时的影响。 |
| 缺陷修复 | 修复 TFT.MSEARCH 请求结果排序异常的问题。 修复单个 Tair 、 Tair 分片在 Key 数量很多（大于 2^24）时， SCAN 命令的返回结果可能不正确的问题。 |  |  |  |
| 6.8.18 | MEDIUM | 2024-04-22 | 缺陷修复 | 在断开当前连接时，支持先返回已有的 Response，再断开。 |
| 6.8.17 | MEDIUM | 2024-03-28 | 缺陷修复 | 修复在 SSL 或 TLS 连接下，当回复数据量较大、写满 Socket buffer 时有可能断开连接的问题。 |
| 6.8.16 | MEDIUM | 2024-01-26 | 缺陷修复 | 修复 SSL 或 TLS 连接下的请求有可能超时的问题。 |
| 6.8.15 | MEDIUM | 2024-01-12 | 缺陷修复 | 修复在事务中连续 SELECT 或事务尾部 SELECT 会导致异常的问题。 修复 QueryCache 功能可能出现异常的问题。 |
| 6.8.14 | MEDIUM | 2023-11-16 | 功能优化 | 优化事务请求的连接数。当事务请求中没有使用 SELECT、WATCH 命令时，事务请求将通过公共连接访问数据库。 当发生阻塞时，优化同一连接在后续立刻发起的普通请求所记录的 RT（Response Time）值 ，避免记录慢日志。 支持 TairSearch 的 TFT.EXPLAINSCORE 命令。 |
| 6.8.13 | MEDIUM | 2023-07-24 | 缺陷修复 | 修复在事务中执行多次 SELECT 命令可能导致同连接中后续普通请求选择 DB 错误的问题。 |
| 6.8.12 | MEDIUM | 2023-05-17 | 新特性 | TR.BITOP 、 TR.BITOPCARD 命令支持跨 Slot 的 Key。 |
| 功能优化 | 优化 Proxy 模式对 Lua 语法的限制。 |  |  |  |
| 缺陷修复 | 修复当客户端协议错误时，可能导致的内存泄露问题。 |  |  |  |
| 6.8.11 | MEDIUM | 2023-04-04 | 新特性 | 支持 TLS 1.3 协议。 支持 TairSearch 的 TFT.ANALYZER 、 TFT.EXPLAINCOST 命令。 |
| 缺陷修复 | 修复一行审计日志的末尾多一个空格的问题。 |  |  |  |
| 6.8.10 | MEDIUM | 2023-01-06 | 新特性 | 支持 TairVector。 |
| 缺陷修复 | 修复 TairSearch 中 Filter Aggregation 聚合错误的问题。 修复开启 ptod_enabled 参数后，审计日志中客户端 IP 地址不准确的问题。 |  |  |  |
| 6.8.9 | MEDIUM | 2022-12-14 | 新特性 | INFO 命令返回值中添加 OS 字段。 支持 CLIENT KILL user 命令。 |
| 缺陷修复 | 修复 MOVED 返回数据可能不完整的问题，避免客户端协议解析失败。 |  |  |  |
| 6.8.8 | MEDIUM | 2022-11-15 | 新特性 | 支持 BF.INFO 命令。 支持 TairHash 的 EXHSCANUNORDER 命令。 单条审计日志的最大长度从 4KB 改为 2KB。 |
| 缺陷修复 | 修复 云原生 版 Proxy 实例的审计日志功能中客户端 IP 不准确的问题。 |  |  |  |
| 6.8.7 | LOW | 2022-08-22 | 功能优化 | 增强稳定性。 |
| 6.8.6 | MEDIUM | 2022-08-16 | 新特性 | 支持部分 Tairsearch。 支持 AUTH user:password 格式的鉴权方式。 |
| 功能优化 | 修复 RESP V3 协议引入的空数组嵌套解码问题。 |  |  |  |
| 6.8.4 | MEDIUM | 2022-07-20 | 新特性 | 支持 RESP V3 协议解析与转发，支持通过 resp_version 配置切换 Proxy 到 Redis 间协议。 |
| 6.8.2 | MEDIUM | 2022-06-14 | 功能优化 | 增强稳定性，修复一些 Crash 问题。 |
| 6.8.1 | LOW | 2022-04-19 | 新特性 | 支持部分 TairSearch。 支持 TairRoaring V2.2 新增的命令。 |
| 6.8.0 | MEDIUM | 2022-04-01 | 新特性 | 支持部分 TairZset。 支持部分 TairRoaring。 SSL 证书禁用 RC4 加密算法。 |
| 缺陷修复 | 修复开启 ptod_enabled 参数后，可能导致 SDIFFSTORE、SINTERSTORE、SUNIONSTORE、ZINTERSTORE、ZUNIONSTORE 命令异常的问题。 修复 SMOVE 命令可能出现 CROSSSLOT 的错误。 |  |  |  |
6.7.x
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.7.9 | MEDIUM | 2022-03-05 | 缺陷修复 | 修复 DBSIZE、KEYS 命令在部分节点异常时，返回的 Response 中结尾的 \n 被截断的问题。 |
| 6.7.8 | MEDIUM | 2022-03-03 | 缺陷修复 | 禁用 SCRIPT DEBUG 命令。 修复 ZINTERSTORE、ZUNIONSTORE 生成数据的 score 精度只有 6 位小数的问题。 |
| 6.7.7 | LOW | 2022-01-30 | 功能优化 | 增强稳定性。 |
| 6.7.6 | LOW | 2022-01-20 | 功能优化 | 增强稳定性。 |
| 6.7.5 | MEDIUM | 2022-01-10 | 功能优化 | 优化 RANDOMKEY 命令随机获取不同的 Redis 节点，避免多次 RANDOMKEY 命令落在同一个 Redis 节点。 |
| 缺陷修复 | 修复 info Commandstats 对内存型实例聚合结果错误的问题。 |  |  |  |
| 6.7.4 | MEDIUM | 2021-12-20 | 功能优化 | 增强稳定性。 |
| 6.7.3 | MEDIUM | 2021-12-15 | 缺陷修复 | 修复 SSL 连接时，首次请求存在概率不响应的问题。 |
| 6.7.2 | LOW | 2021-11-30 | 功能优化 | 增强稳定性。 |
| 6.7.1 | MEDIUM | 2021-11-23 | 功能优化 | 增强稳定性。 |
6.6.x
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.6.14 | MEDIUM | 2021-11-01 | 功能优化 | 修复 ECS 架构下（split_multi_key_cmd_as_slot 开启），ZINTERSTORE、ZUNIONSTORE 存在概率不返回的问题。 |
| 6.6.13 | MEDIUM | 2021-10-22 | 功能优化 | 修复开启 Proxy Query Cache 后，热升级存在概率失败的问题。 |
| 6.6.12 | MEDIUM | 2021-10-12 | 功能优化 | 增强稳定性。 |
| 6.6.11 | MEDIUM | 2021-10-11 | 功能优化 | 增强稳定性。 |
| 6.6.10 | MEDIUM | 2021-09-27 | 缺陷修复 | 修复 Memcache 实例在只读或只写请求下返回消息错误的问题。 |
| 6.6.9 | MEDIUM | 2021-09-06 | 缺陷修复 | 修复 CVE-2021-3711 漏洞与 CVE-2021-3712 漏洞。 |
| 6.6.8 | MEDIUM | 2021-08-30 | 功能优化 | 增强稳定性。 |
| 6.6.7 | MEDIUM | 2021-08-27 | 功能优化 | 修复开启 Statistics 功能后内存泄露的问题。 |
| 6.6.6 | LOW | 2021-08-13 | 功能优化 | 增强稳定性。 |
| 6.6.5 | LOW | 2021-08-03 | 新特性 | 支持 Memcache Gateway 模式，即可实现 Memcache 协议的支持和转发。 |
| 6.6.4 | HIGH | 2021-07-08 | 新特性 | CLIENT LIST 、 CLIENT KILL 命令支持展示和操作进程维度的连接。 |
| 缺陷修复 | 修复 TairZset 命令不支持大写的问题，更多信息，请参见 [TairZset](../tairzset-commands.md) 。 |  |  |  |
| 6.6.3 | MEDIUM | 2021-06-18 | 功能优化 | 优化多可用区容灾场景下的内部管控。 |
| 6.6.2 | LOW | 2021-06-08 | 新特性 | 增加对部分内部命令的支持。 |
| 6.6.1 | LOW | 2021-05-26 | 新特性 | 新增 TairZset 数据结构，实现任意维度的 double 类型的分值排序，提升数据处理效率，且客户端适配简易，无需任何编解码封装。更多信息，请参见 [TairZset](../tairzset-commands.md) 。 |
| 6.6.0 | LOW | 2021-04-28 | 新特性 | 新增代理查询缓存功能（Proxy Query Cache），启用后代理节点会缓存热点 Key 对应的请求和查询结果，当在有效时间内收到同样的请求时直接返回结果至客户端，无需和后端的数据分片交互，可更好地改善对热点 Key 的发起大量读请求导致的访问倾斜。 |
6.5.x
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.5.9 | HIGH | 2021-04-21 | 缺陷修复 | 修复特殊场景下，多 Key 命令死循环的问题。 |
| 6.5.8 | HIGH | 2021-04-16 | 缺陷修复 | 本版本为特殊版本，即在 6.5.5 小版本基础上，修复在选择多个 DB 的场景下，请求乱序的问题。 |
| 6.5.7 | HIGH | 2021-04-16 | 缺陷修复 | 修复在选择多个 DB 的场景下，请求乱序的问题。 |
| 6.5.6 | MEDIUM | 2021-04-09 | 新特性 | SCAN 命令支持的最大数据分片数由 256 提升为 1024。 当订阅的 Channel（频道）所在的 Slot（槽）发生迁移后，Proxy 会断开订阅的连接让客户端重连以保障数据一致性。 |
| 功能优化 | 优化 Proxy 命令处理机制： 处理 MOVED 命令时，将请求重新发给 MOVED 的地址。 发送不带 Key 的命令时，屏蔽 Slot 为空的数据分片。 |  |  |  |
| 6.5.5 | HIGH | 2021-03-05 | 缺陷修复 | 修复在 [主备切换](../user-guide/manually-switch-workloads-from-a-master-node-to-a-replica-node.md) 或 [变更配置](../user-guide/change-the-configurations-of-an-instance.md) 而触发 DHT 信息更新时，可能导致的内存泄露问题。 |
| 6.5.4 | HIGH | 2021-02-07 | 缺陷修复 | 修复客户端接收返回信息过慢可能出现的内存泄露问题。 |
| 6.5.3 | HIGH | 2021-01-21 | 新特性 | 支持在 Lua 脚本中的 KEYS 下标中使用变量。 |
| 缺陷修复 | 修复 [集群架构](../product-overview/cluster-master-replica-instances.md) 下，数据分片超过 32 个时使用 MULTI 或 BLOCK 类命令引发的内存泄露问题。 |  |  |  |
| 6.5.2 | HIGH | 2021-01-19 | 缺陷修复 | 修复 alb enat 模式下通过 Socket 获取虚拟 IP 地址（VIP）地址失败的问题。 |
| 6.5.1 | LOW | 2021-01-14 | 新特性 | 慢日志在记录多 Key 命令相关日志时，支持记录最后返回 Response 的数据分片的 IP 地址。 |
| 6.5.0 | HIGH | 2020-12-24 | 缺陷修复 | 修复执行 GIS.GETALL 命令可能导致的崩溃问题。关于该命令的详细介绍，请参见 [TairGIS](../tairgis-commands.md) 。 |
6.4.x
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.4.10 | MEDIUM | 2020-12-01 | 功能优化 | 优化密码错误场景下的提示信息，易于理解。 |
| 6.4.9 | HIGH | 2020-11-06 | 缺陷修复 | 修复多线程模式下开启 [SSL](../user-guide/configure-ssl-encryption.md) [加密](../user-guide/configure-ssl-encryption.md) 功能导致的崩溃问题。 修复执行 UNSUBSCRIBE 时，Channel（频道）中包含 0 时导致的 Response 协议错误的问题。 |
| 6.4.8 | HIGH | 2020-10-21 | 功能优化 | 运行日志对大包、ASK 回复包和 MOVED 包的二进制请求进行编码后记录，避免日志乱码问题。 |
| 缺陷修复 | 修复 max_session_processing（单个连接允许堆积的最大请求数）的配置不能被动态设置的问题。更多参数的介绍，请参见 [Redis](../user-guide/supported-parameters.md) [开源版配置参数列表](../user-guide/supported-parameters.md) 。 |  |  |  |
| 6.4.7 | MEDIUM | 2020-10-09 | 功能优化 | 优化 Proxy 节点的内部监控。 |
| 6.4.6 | HIGH | 2020-09-30 | 缺陷修复 | 修复因节点角色未初始化，导致的标准或集群架构的实例执行 SLOWLOG 命令可能超时的问题。 修复了特定规格的 [Memcache](https://help.aliyun.com/zh/memcache/product-overview/product-overview) [实例](https://help.aliyun.com/zh/memcache/product-overview/product-overview) 通过 [数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) [DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582) 连接失败的问题。 修复订阅 __keyspace@0__ 时，未指定 Key 导致的崩溃问题。 |
| 6.4.5 | LOW | 2020-09-27 | 新特性 | 增加对部分内部命令的支持。 |
| 6.4.3 | HIGH | 2020-09-25 | 功能优化 | 针对 Jedis 客户端中 pipeline 的特殊实现进行了适配，优化连接限制的释放计算，Jedis 连接示例，请参见 [客户端程序连接教程](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md) 。 |
| 缺陷修复 | 修复 BZPOPMIN 和 XREAD 命令错误记录了慢日志的问题，更多信息，请参见 [查询慢日志](../user-guide/view-slow-logs.md) 。 |  |  |  |
| 6.4.2 | HIGH | 2020-09-09 | 缺陷修复 | 修复空闲连接默认 1 分钟后被断开的问题。 |
| 6.4.1 | MEDIUM | 2020-08-25 | 新特性 | 新增 Timeout 配置，空闲的客户端连接会被自动断开。 支持统计只读节点上的慢日志信息，即 SLOWLOG 命令会发送至所有 Master 节点和只读节点。更多信息，请参见 [查询慢日志](../user-guide/view-slow-logs.md) 。 |
| 功能优化 | 优化了 Pub/Sub 和 Monitor 连接的内存使用，避免因内存碎片引起的内存快速上涨。 提升了 Proxy 节点处理新连接的能力。 |  |  |  |
| 6.4.0 | HIGH | 2020-08-18 | 缺陷修复 | 修复 ConfigServer 在完成配置前调用 stat 导致的崩溃问题。 |
6.4.x
| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.3.9 | MEDIUM | 2020-08-14 | 新特性 | 慢日志支持记录真实的客户端 IP 地址，帮助您更好地定位慢日志，更多信息，请参见 [查询慢日志](../user-guide/view-slow-logs.md) 。 |
| 功能优化 | 提升了 Proxy 节点的短连接处理能力。 |  |  |  |
| 6.3.8 | HIGH | 2020-07-24 | 缺陷修复 | 修复 Vector Clear 不释放内存导致的内存上涨的问题。 |
| 6.3.7 | HIGH | 2020-07-13 | 缺陷修复 | 修复开启 SSL 加密功能后，建立连接时可能出现的崩溃问题。 |
| 6.3.5 | HIGH | 2020-07-10 | 新特性 | 为审计日志中的二进制数据执行编码，提升日志易读性。 增加 no_loose_statistics-ip-enable 、 no_loose_statistics-keys 、 no_loose_statistics-cmds 参数，可实现对 IP、Key 和命令维度的统计，更多详细介绍请参见 [Redis](../user-guide/supported-parameters.md) [开源版配置参数列表](../user-guide/supported-parameters.md) 。 |
| 缺陷修复 | 修复连接被释放后，执行 CheckExceedLimitAndClose 可能导致的崩溃问题。 修复 SSL 加密功能开启失败的问题。 |  |  |  |
| 6.3.4 | HIGH | 2020-05-21 | 缺陷修复 | 修复 \r\n 等空包可能导致后续请求不返回的问题。 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
