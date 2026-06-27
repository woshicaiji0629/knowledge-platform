# Redis开源版小版本发布日志-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/support/apsaradb-for-redis-community-edition

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# Redis开源版小版本发布日志

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为提升用户体验，云数据库 Tair（兼容 Redis）会不定期地发布小版本，用于丰富云产品功能或修复已知缺陷。您可以参阅本文了解Redis开源版小版本的更新说明，选择在业务低峰期升级实例的小版本。

Redis开源版7.0、6.0、5.0或4.0，完全兼容对应的Redis大版本，并向下兼容。

重要

本文仅包含Redis开源版实例的小版本发布日志，关于Tair（企业版）实例的小版本发布日志（包含内存型、持久内存型和磁盘型）请参见[Tair](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)。

## 如何查询或升级实例的小版本

您可以通过控制台查看当前实例的版本，具体操作及升级版本的其注意事项，请参见[升级小版本与代理版本](products/redis/documents/user-guide/update-the-minor-version.md)。

重要

- 

系统会自动检测实例的小版本，如果小版本升级按钮不存在或处于无法单击的状态，表示该实例已经是最新的小版本。

- 

由于各地域版本发布进度可能有所差异，小版本发布情况以当前控制台显示为准。

## 更新级别说明

- 

LOW（低）：一般级别，包含日常新功能升级（例如新增某个功能）。

- 

MEDIUM（中）：推荐级别， 包含功能模块优化类的升级（例如优化了某个功能）。除此以外，还包含了LOW级别所包含的更新内容。

- 

HIGH（高）：重要级别，包含影响稳定性或安全性的重要升级（例如修复某个漏洞或缺陷）。除此以外，还包含LOW和MEDIUM级别所包含的更新内容。

说明

下述表格仅记录2025年01月01号之后的发布记录，在此之前的小版本发布记录请参见[历史版本](products/redis/documents/support/apsaradb-for-redis-community-edition.md)。

## Redis开源版标准系列

### Redis开源版7.0

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 7.0.2.12 | MEDIUM | 2026-05-11 | 安全加固 | 修复 CVE-2026-23631、CVE-2026-25243 安全漏洞。 |
| 功能优化 | 允许执行 config get cluster-require-full-coverage 配置项。 |  |  |  |
| 7.0.2.9 | MEDIUM | 2026-01-14 | 功能优化 | 支持主备无感切换。 |
| 缺陷修复 | 修复 lua 脚本内大流量命令统计错误问题。 |  |  |  |
| 7.0.2.7 | MEDIUM | 2026-01-14 | 功能优化 | 优化集群架构主备切换流程。 新增对 CONFIG 系列命令的支持。 |
| 7.0.2.6 | HIGH | 2025-11-24 | 功能优化 | 增强稳定性。 |
| 7.0.2.5 | LOW | 2025-10-31 | 功能优化 | 鉴权系统兼容 auth account:password 格式。 支持轻量集群消息，提升集群模式 pub/sub 性能。 block 类命令支持重定向。 |
| 7.0.2.4 | HIGH | 2025-10-09 | 功能优化 | 增强主备重定向的稳定性。 增强集群扩缩容的稳定性。 |
| 缺陷修复 | 修复 CVE-2025-46817 安全漏洞。 修复 CVE-2025-46818 安全漏洞。 修复 CVE-2025-46819 安全漏洞。 修复 CVE-2025-49844 安全漏洞。 |  |  |  |
| 7.0.1.19 | LOW | 2025-06-26 | 功能优化 | 增强稳定性。 |
| 7.0.1.18 | HIGH | 2025-06-23 | 功能优化 | 优化主备切换流程。 |
| 缺陷修复 | 修复 CVE-2025-27151 安全漏洞。 修复 CVE-2025-32023 安全漏洞。 修复 CVE-2025-48367 安全漏洞。 |  |  |  |
| 7.0.1.17 | HIGH | 2025-04-28 | 功能优化 | 标准架构支持-REDIRECT 重定向能力。 Sentinel 兼容模式下支持 SENTINEL masters（以及 master、slaves、replicas）命令。 新增 cmd_slowlog_count 统计。 |
| 缺陷修复 | 修复 CVE-2025-21605 安全漏洞。 修复 CVE-2024-51741 安全漏洞。 修复单个命令 QPS 统计不准确的问题。 修复在审计日志中记录 Lua 脚本内命令来源 IP 错误的问题。 |  |  |  |
| 7.0.1.16 | MEDIUM | 2025-01-16 | 安全加固 | 修复 CVE-2024-46981 安全漏洞。 |


### Redis开源版6.0

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.0.2.28 | MEDIUM | 2026-05-11 | 安全加固 | 修复 CVE-2026-23631、CVE-2026-25243 安全漏洞。 |
| 功能优化 | 允许执行 config get cluster-require-full-coverage 配置项。 |  |  |  |
| 6.0.2.27 | MEDIUM | 2026-01-14 | 功能优化 | 优化集群架构主备切换流程。 |
| 6.0.2.25 | HIGH | 2025-10-31 | 功能优化 | 鉴权系统兼容 auth acc:pwd 格式的行为。 优化流控算法。 优化 aof rewrite 方法。 |
| 6.0.2.24 | HIGH | 2025-10-09 | 缺陷修复 | 修复 CVE-2025-46817 安全漏洞。 修复 CVE-2025-46818 安全漏洞。 修复 CVE-2025-46819 安全漏洞。 修复 CVE-2025-49844 安全漏洞。 |
| 6.0.2.23 | HIGH | 2025-06-25 | 缺陷修复 | 修复 CVE-2025-32023 安全漏洞。 修复 CVE-2025-48367 安全漏洞。 |
| 6.0.2.22 | MEDIUM | 2025-06-05 | 功能优化 | 优化主备切换流程。 |
| 缺陷修复 | 修复集群扩容后大 Key 统计错误的问题。 |  |  |  |
| 6.0.2.21 | HIGH | 2025-04-28 | 功能优化 | 实例 Loading 状态时允许执行 READONLY 和 READWRITE 命令。 Sentinel 兼容模式下支持 SENTINEL masters（以及 master、slaves、replicas）命令。 |
| 缺陷修复 | 修复集群实例扩缩容期间数据访问异常的问题，影响版本 0.2.16 至 0.2.18。 修复 CVE-2025-21605 安全漏洞。 修复 Errorstats 中部分错误信息丢失的问题，主要涉及-WRONGTYPE 类型错误。 |  |  |  |
| 6.0.2.18 | HIGH | 2025-01-16 | 缺陷修复 | 修复 SRANDMEMBER 命令有概率导致实例死循环的问题。 修复 CVE-2024-46981 安全漏洞。 修复单个命令 QPS 统计不准确的问题。 |


### Redis开源版5.0

说明

Redis开源版5.0实例支持云原生和经典两种部署模式，下方列表中小版本号列括号中内容为经典实例的小版本号。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 5.5.2.28(5.2.28) | MEDIUM | 2026-05-11 | 安全加固 | 修复 CVE-2026-23631、CVE-2026-25243 安全漏洞。 |
| 功能优化 | 允许执行 config get cluster-require-full-coverage 配置项。 |  |  |  |
| 5.5.2.27(5.2.27) | MEDIUM | 2026-01-14 | 功能优化 | 优化集群架构主备切换流程。 |
| 5.5.2.25(5.2.25) | HIGH | 2025-10-31 | 功能优化 | 鉴权系统兼容 auth acc:pwd 格式的行为。 优化流控算法。 优化 aof rewrite 方法。 |
| 5.5.2.24(5.2.24) | HIGH | 2025-10-09 | 缺陷修复 | 修复 CVE-2025-46817 安全漏洞。 修复 CVE-2025-46818 安全漏洞。 修复 CVE-2025-46819 安全漏洞。 修复 CVE-2025-49844 安全漏洞。 |
| 5.5.2.23(5.2.23) | HIGH | 2025-06-25 | 缺陷修复 | 修复 CVE-2025-32023 安全漏洞。 修复 CVE-2025-48367 安全漏洞。 |
| 5.5.2.22(5.2.22) | MEDIUM | 2025-06-05 | 功能优化 | 优化主备切换流程。 |
| 缺陷修复 | 修复集群扩容后大 Key 统计错误的问题。 |  |  |  |
| 5.5.2.21(5.2.21) | HIGH | 2025-04-28 | 功能优化 | 实例 Loading 状态时允许执行 READONLY 和 READWRITE 命令。 Sentinel 兼容模式下支持 SENTINEL masters（以及 master、slaves、replicas）命令。 |
| 缺陷修复 | 修复集群实例扩缩容期间数据访问异常的问题，影响版本 5.2.17 至 5.2.18。 修复 CVE-2025-21605 安全漏洞。 修复 Errorstats 中部分错误信息丢失的问题，主要涉及-WRONGTYPE 类型错误。 |  |  |  |
| 5.5.2.18(5.2.18) | HIGH | 2025-01-16 | 缺陷修复 | 修复 SRANDMEMBER 命令有概率导致实例死循环的问题。 修复 CVE-2024-46981 安全漏洞。 修复单个命令 QPS 统计不准确的问题。 |


### Redis开源版4.0

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 1.9.20 | HIGH | 2025-10-31 | 功能优化 | 优化流控算法。 |
| 1.9.19 | HIGH | 2025-10-09 | 缺陷修复 | 修复 CVE-2025-46817 安全漏洞。 修复 CVE-2025-46818 安全漏洞。 修复 CVE-2025-46819 安全漏洞。 修复 CVE-2025-49844 安全漏洞。 |
| 1.9.18 | HIGH | 2025-01-16 | 安全加固 | 修复 CVE-2024-46981、CVE-2024-31449 安全漏洞。 |


## Redis倚天版

以下表格适用于倚天版Redis 7.0、Redis 6.0和Redis 5.0实例，其命令与特性分别兼容Redis7.0、Redis 6.0和Redis 5.0。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 26.1.6.0 | LOW | 2026-03-31 | 功能优化 | 增强稳定性。 |
| 26.1.5.0 | MEDIUM | 2026-03-30 | 新增特性 | 支持更大范围的 bigkey 数量阈值设置。 |
| 功能优化 | 增强稳定性。 |  |  |  |
| 26.1.2.0 | MEDIUM | 2026-02-25 | 缺陷修复 | 修复 hash、set、zset 等类型内部 scan 时，如果 key 不存在，返回的 cursor 非 0 的问题。 |
| 功能优化 | 增强稳定性。 |  |  |  |
| 26.1.1.0 | MEDIUM | 2026-01-30 | 功能优化 | 增强稳定性。 |
| 25.10.1.0 | HIGH | 2025-10-09 | 缺陷修复 | 修复 CVE-2025-46817 安全漏洞。 修复 CVE-2025-46818 安全漏洞。 修复 CVE-2025-46819 安全漏洞。 修复 CVE-2025-49844 安全漏洞。 修复在事务或 Lua 脚本中调用 SCAN 命令触发过期删除时可能造成死锁的问题。 |
| 25.9.1.0 | MEDIUM | 2025-09-09 | 缺陷修复 | 修复 SORT 命令可能导致备（Slave）节点发生死锁的问题。 |
| 25.8.1.0 | MEDIUM | 2025-08-15 | 功能优化 | 增强稳定性。 |
| 25.8.0.0 | MEDIUM | 2025-08-04 | 功能优化 | 客户端断开时，自动停止执行纯读取的 Lua 脚本。 |
| 25.7.2.0 | LOW | 2025-07-10 | 功能优化 | 优化 Client Output Buffer 的回收逻辑，在连接数较多时可以节省内存。 优化内存统计中 DB 的元数据占用空间。 |
| 25.7.0.0 | MEDIUM | 2025-07-01 | 功能优化 | 增强稳定性。 |
| 缺陷修复 | 修复 SCAN 命令在未匹配到相关 Pattern 时，扫描的 Key 数量相较于社区版有所增加，从而导致延迟增大的问题。 修复 XLEN 命令在 Key 不存在时返回协议格式不正确的问题。 |  |  |  |
| 25.6.1.0 | LOW | 2025-06-19 | 功能优化 | 增强稳定性。 |
| 25.6.0.0 | HIGH | 2025-06-12 | 功能优化 | 支持按每个数据类型统计大 Key（元素数量多的 Key）。 优化 SCAN 的迭代限制，以防止执行时间过长。 优化 ZSET 在进行编码转换时可能出现的内存膨胀问题。 |
| 缺陷修复 | 修复 CVE-2025-32023 安全漏洞。 修复 CVE-2025-48367 安全漏洞。 |  |  |  |
| 25.5.0.1 | LOW | 2025-05-19 | 功能优化 | 兼容 Redis 社区版 LATENCY 族的所有命令。 MONITOR 命令的返回结果对齐 Redis 社区版格式。 |
| 25.5.0.0 | HIGH | 2025-05-08 | 缺陷修复 | 修复 BITFIELD 命令对 offset 的长度限制比 Redis 社区版小的问题。 |
| 25.4.0.0 | HIGH | 2025-04-28 | 缺陷修复 | 修复 CVE-2025-21605 安全漏洞。 修复 SRANDMEMBER 有极小概率导致节点崩溃（Crash）的问题。 |
| 25.3.2.0 | LOW | 2025-03-14 | 缺陷修复 | 增强稳定性。 |
| 25.3.1.0 | LOW | 2025-03-13 | 功能优化 | 修复后台生成备份数据时，遇到特殊数据有可能导致备份失败的问题。 |
| 25.3.0.0 | LOW | 2025-03-12 | 功能优化 | 增强稳定性。 |
| 25.2.0.0 | LOW | 2025-02-12 | 功能优化 | 增强稳定性。 |
| 25.1.0.0 | HIGH | 2025-01-16 | 功能优化 | 优化半同步逻辑。 优化热 Key 逐出逻辑。 |
| 缺陷修复 | 修复 SRANDMEMBER 命令有概率导致实例死循环的问题。 修复 CVE-2024-46981 安全漏洞。 修复 EVAL 命令首次并发调用时可能存在的 Lua VM 污染的问题（脚本返回 NiL）。 |  |  |  |


## 历史版本

历史（2025年01月01号之前）小版本发布记录可通过下方表格进行回溯查阅。

Redis开源版7.0版本历史发布记录

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 7.0.1.15 | LOW | 2024-12-10 | 功能优化 | 在 Sentinel 免密模式下，支持通过 #no_loose_sentinel-password-free-commands 参数配置更多的免密命令。 优化客户端新增累计流量、命令统计信息。 |
| 缺陷修复 | 修复集群实例在扩、缩容时大 Key 统计阈值失效的问题。 增强集群实例扩、缩容的稳定性。 |  |  |  |
| 7.0.1.13 | HIGH | 2024-10-08 | 安全加固 | 修复 CVE-2024-31228 安全漏洞。 修复 CVE-2024-31227 安全漏洞。 修复 CVE-2024-31449 安全漏洞。 增强稳定性。 |
| 7.0.1.12 | LOW | 2024-08-12 | 功能优化 | 支持 Sentinel 免密配置。 |
| 7.0.1.10 | LOW | 2024-07-23 | 功能优化 | 支持 EventBus 事件记录。 |
| 7.0.1.9 | LOW | 2024-06-25 | 功能优化 | 优化 Pub/Sub 类命令的执行效率，避免大量连接同时停止订阅时造成卡顿。 优化客户端轮询检查策略，避免长连接无法及时进行内存统计和回收。 |
| 7.0.1.8 | LOW | 2024-05-28 | 功能优化 | 增加对处于 WATCH 或 BLOCK 状态的连接监控。 增加对 Rehash 的相关监控项。 实时统计热 Key（Hotkey）功能升级，允许调整热 Key 统计阈值，并支持展示精确 QPS、在同一时间支持最多统计 50 个热点 Key 等。 |
| 缺陷修复 | 修复由于使用共享对象造成 QPS 统计错误的问题，当开启实时统计热 Key 功能后将不在使用共享对象。 |  |  |  |
| 7.0.1.7 | LOW | 2024-04-24 | 功能优化 | 更新至 Redis 开源社区 7.0.15 版本，更多信息请参见 [Redis 7.0.15 release note](https://github.com/redis/redis/blob/7.0.15/00-RELEASENOTES) 。 |
| 7.0.1.6 | MEDIUM | 2024-03-14 | 功能优化 | INFO STATS 命令增加返回客户端输入、输出缓冲区超限断连的统计： client_query_buffer_limit_disconnections client_output_buffer_limit_disconnections 新增实时大 Key 统计阈值，默认为 2000。例如 String 类型的字符长度超过 2000 即判定为大 key；List、Set、Hash 等类型的元素个数超过 2000 个即判定为大 Key 等。 |
| 缺陷修复 | 修复 Stream 类型大 Key 统计错误的问题。 |  |  |  |
| 7.0.1.5 | LOW | 2024-01-09 | 功能优化 | 优化主动过期的效率。 INFO CLIENTS 命令中增加 pubsub_clients 监控项。 |
| 7.0.1.4 | HIGH | 2023-11-15 | 功能优化 | 更新至 Redis 开源社区 7.0.14 版本，更多信息请参见 [Redis 7.0.14 release note](https://github.com/redis/redis/blob/7.0.14/00-RELEASENOTES) 。 |
| 安全加固 | 修复 CVE-2023-41056 安全漏洞。 修复 CVE-2023-41053 安全漏洞。 |  |  |  |
| 7.0.1.3 | LOW | 2023-08-28 | 功能优化 | 优化实例扩缩容流程。 集群实例支持多可用区容灾部署。 |
| 7.0.1.2 | HIGH | 2023-08-01 | 新特性 | 集群架构直连模式实例支持 TLS 链路加密功能。 集群架构代理模式实例支持 IP 透传功能，您可以通过 ptod_enabled 参数进行控制。 集群架构实例的 SPUBLISH 命令支持分片内广播。 |
| 功能优化 | 更新至 Redis 开源社区 7.0.12 版本，包含多项性能优化、安全漏洞修复等，例如修复 CVE-2022-24834、CVE-2023-36824 等安全漏洞，更多信息请参见 [Redis 7.0.12 release note](https://github.com/redis/redis/blob/7.0.12/00-RELEASENOTES) 。 |  |  |  |
| 缺陷修复 | 修复热点 Key 过期时可能导致实例崩溃（Crash）的问题。 |  |  |  |
| 7.0.1.1 | LOW | 2023-07-17 | 功能优化 | 优化集群架构实例主备切换和重启的流程。 |
| 7.0.1.0 | LOW | 2023-04-20 | 新特性 | 支持售卖集群架构、读写分离架构。 支持集群架构无感扩缩容。 定期将热 Key（Hotkey）信息打印到审计日志中以便于排查。 |
| 7.0.0.6 | LOW | 2023-01-31 | 新特性 | 支持 审计日志 。 支持 Top Key 统计 。 支持 时延洞察 。 |
| 7.0.0.5 | LOW | 2022-07-21 | 功能优化 | 更新至 Redis 开源社区 7.0.4 版本。 |
| 7.0.0.4 | LOW | 2022-06-20 | 功能优化 | 更新至 Redis 开源社区 7.0.2 版本。 |
| 7.0.0.3 | LOW | 2022-05-27 | 首次发布 | 首次发布 Redis 开源版 云盘版实例的 7.0 版本，更多信息请参见 [Redis 7.0 release notes](https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES) 。 |


Redis开源版6.0版本历史发布记录

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 6.0.2.17 | LOW | 2024-12-10 | 功能优化 | 在 Sentinel 免密模式下，支持通过 #no_loose_sentinel-password-free-commands 参数配置更多的免密命令。 优化客户端新增累计流量、命令统计信息。 |
| 缺陷修复 | 修复集群实例在扩、缩容时大 Key 统计阈值失效的问题。 增强集群实例扩、缩容的稳定性。 |  |  |  |
| 6.0.2.15 | HIGH | 2024-10-08 | 安全加固 | 修复 CVE-2024-31228 安全漏洞。 修复 CVE-2024-31449 安全漏洞。 |
| 6.0.2.14 | LOW | 2024-08-12 | 功能优化 | 支持 Sentinel 免密配置。 |
| 6.0.2.12 | LOW | 2024-07-23 | 功能优化 | 优化同时开启 VPC 免密功能和 #no_loose_check-whitelist-always 参数时的白名单检查逻辑。 时延洞察功能支持 Pipeline 的监控。 |
| 缺陷修复 | 修复 Lua、MULTI 内命令执行耗时统计错误的问题，影响范围为 6.0.2.8~6.0.2.11 版本。 |  |  |  |
| 6.0.2.11 | LOW | 2024-06-25 | 功能优化 | 优化 Pub/Sub 类命令的执行效率，避免大量连接同时停止订阅时造成卡顿。 优化客户端轮询检查策略，避免长连接无法及时进行内存统计和回收。 优化子进程生成 RDB 和 AOF 文件的落盘方法。 |
| 6.0.2.10 | LOW | 2024-05-28 | 安全加固 | 增强稳定性。 |
| 6.0.2.9 | LOW | 2024-05-28 | 功能优化 | 增加对处于 WATCH 或 BLOCK 状态的连接监控。 增加对 Rehash 的相关监控项。 实时统计热 Key（Hotkey）功能升级，允许调整热 Key 统计阈值，并支持展示精确 QPS、在同一时间支持最多统计 50 个热点 Key 等。 |
| 缺陷修复 | 修复由于使用共享对象造成 QPS 统计错误的问题，当开启实时统计热 Key 功能后将不在使用共享对象。 |  |  |  |
| 6.0.2.8 | LOW | 2024-04-24 | 功能优化 | 更新至 Redis 开源社区 6.0.20 版本，更多信息请参见 [Redis 6.0.20 release note](https://github.com/redis/redis/blob/6.0.20/00-RELEASENOTES) 。 |
| 6.0.2.7 | LOW | 2024-03-14 | 功能优化 | INFO STATS 命令增加返回客户端输入、输出缓冲区超限断连的统计： client_query_buffer_limit_disconnections client_output_buffer_limit_disconnections 新增实时大 Key 统计阈值，默认为 2000。例如 String 类型的字符长度超过 2000 即判定为大 key；List、Set、Hash 等类型的元素个数超过 2000 个即判定为大 Key 等。 |
| 6.0.2.6 | LOW | 2024-01-09 | 功能优化 | 优化主动过期的效率。 INFO CLIENTS 命令中增加 pubsub_clients 监控项。 优化 CLUSTER NODES、CLUSTER SLOTS 命令的执行效率。 |
| 6.0.2.5 | LOW | 2023-08-28 | 功能优化 | 增加主备复制流量统计，将在 INFO STATS 中单独显示。 |
| 6.0.2.4 | HIGH | 2023-08-21 | 功能优化 | 集群架构直连模式实例支持 TLS 链路加密功能。 |
| 安全加固 | 修复 CVE-2022-24834 安全漏洞。 |  |  |  |
| 6.0.2.3 | MEDIUM | 2023-07-17 | 安全加固 | 优化集群架构实例主备切换和重启的流程。 |
| 6.0.2.1 | MEDIUM | 2023-06-30 | 安全加固 | 增强集群架构的稳定性。 |
| 6.0.2.0 | HIGH | 2023-04-24 | 功能优化 | 定期将热 Key（Hotkey）信息打印到审计日志中以便于排查。 ptod_enabled 参数的开关覆盖了性能监控与慢日志查询功能。 |
| 安全加固 | 修复在极端场景下，集群架构扩缩容时的若干缺陷。 |  |  |  |
| 6.0.1.24 | LOW | 2022-11-14 | 安全加固 | 增强稳定性。 |
| 6.0.1.23 | LOW | 2022-09-20 | 功能优化 | 审计日志新增记录过期删除事件。 审计日志不再记录 PING、AUTH、SELECT 等非写命令。 |
| 6.0.1.22 | LOW | 2022-09-13 | 功能优化 | 优化集群架构实例连接数耗尽后的处理方式。 |
| 6.0.1.21 | LOW | 2022-08-30 | 功能优化 | 优化集群架构实例的启动流程。 |
| 6.0.1.20 | LOW | 2022-06-28 | 功能优化 | 修复 ZUNIONSTORE 和 ZINTERSTORE 等命令在集群代理模式下报错的问题。 |
| 6.0.1.19 | LOW | 2022-06-22 | 功能优化 | 优化延迟统计直方图，详情请参见 [时延洞察](products/redis/documents/user-guide/latency-insights.md) 。 |
| 安全加固 | 升级、优化集群架构增、删节点流程，详情请参见 [调整集群分片数](products/redis/documents/user-guide/adjust-the-number-of-cluster-shards.md) 。 |  |  |  |
| 6.0.1.18 | LOW | 2022-05-17 | 功能优化 | 删除 INFO 命令返回的 Errorstats - Selected 字段。 |
| 6.0.1.17 | LOW | 2022-05-10 | 功能优化 | 集群架构支持 MOVE 命令。 |
| 6.0.1.16 | MEDIUM | 2022-04-25 | 安全加固 | 优化升级集群架构增、删节点流程，增强稳定性。 |
| 6.0.1.15 | LOW | 2022-03-24 | 新特性 | 支持延时统计直方图（Latency），详情请参见 [时延洞察](products/redis/documents/user-guide/latency-insights.md) 。 支持 INFO 命令返回 Errorstats（Redis 错误统计）信息。 |
| 6.0.1.14 | LOW | 2022-02-21 | 功能优化 | 支持 READONLY、READWRITE 命令，详情请参见 [Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) [开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) 。 |
| 6.0.1.13 | LOW | 2022-01-14 | 功能优化 | 增加 DB 元数据监控项：占用内存。 优化实时 Top Key 统计功能。 |
| 6.0.1.12 | HIGH | 2021-10-26 | 安全加固 | 修复集群变配过程中慢日志过多的问题，增强稳定性。 |
| 6.0.1.11 | HIGH | 2021-10-13 | 功能优化 | 增强了集群变配时槽（slot）无感迁移的自治能力。 优化 CLUSTER NODES 等命令的性能。 优化白名单功能。 |
| 6.0.1.10 | HIGH | 2021-09-06 | 功能优化 | 增强稳定性。 |
| 6.0.1.9 | MEDIUM | 2021-08-16 | 功能优化 | 增强了槽（slot）的无感迁移可靠性，增强稳定性。 |
| 6.0.1.8 | MEDIUM | 2021-08-06 | 功能优化 | 增强稳定性。 |
| 6.0.1.7 | MEDIUM | 2021-08-06 | 功能优化 | 增强稳定性。 |
| 6.0.1.6 | MEDIUM | 2021-07-19 | 新特性 | 合并社区 6.0.14 版本的更新内容，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 |
| 功能优化 | 优化 Slot（槽）迁移数据完成后删除源端 Slot 数据的流程，增强数据可靠性。 简化 Slot 迁移数据的增量数据同步流程。 |  |  |  |
| 6.0.1.5 | MEDIUM | 2021-06-04 | 功能优化 | 增强稳定性。 |
| 6.0.1.4 | MEDIUM | 2021-05-27 | 功能优化 | 增强稳定性。 |
| 6.0.1.3 | LOW | 2021-05-18 | 新特性 | 支持大 Key（big key）实时统计。 |
| 6.0.1.2 | MEDIUM | 2021-05-07 | 功能优化 | 增强稳定性。 |
| 6.0.1.1 | MEDIUM | 2020-11-28 | 新特性 | 合并社区 6.0.9 版本的更新内容，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 支持槽（slot）的无感迁移能力。 支持通过公网获取虚拟 IP（VIP）地址，为使用 [直连模式](products/redis/documents/user-guide/enable-the-direct-connection-mode.md) 客户端提供更好的支持。 |
| 功能优化 | 优化实例健康检查能力，提升在磁盘抖动场景下的主备切换速度。 |  |  |  |
| 6.0.0.5 | HIGH | 2020-08-21 | 缺陷修复 | 修复热点 Key 统计不准确的问题。 |
| 6.0.0.4 | HIGH | 2020-07-20 | 缺陷修复 | 修复部分参数的配置在重启后失效的问题。 修复慢日志对链路中备库标志错误的问题。 |
| 6.0.0.3 | LOW | 2020-06-11 | 新特性 | 合并社区 6.0.5 版本的更新内容，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 INFO 命令返回值中， Replication 部分支持展示 role 信息（例如 role:master ），可兼容 Redisson 客户端在部分场景下对该信息的调用。 支持对读写命令 QPS 的统计，更多信息，请参见 [查看性能监控](products/redis/documents/user-guide/view-monitoring-data.md) 。 |
| 6.0.0.2 | LOW | 2020-06-02 | 新特性 | 合并社区 6.0.4 版本的更新内容，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 |
| 6.0.0.1 | LOW | 2020-05-06 | 首次发布 | 首次发布的小版本，基于社区 6.0.1 版本，更多信息，请参见 [Redis 6.0 release notes](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES) 。 |


Redis开源版5.0版本历史发布记录

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 5.5.2.17(5.2.17) | LOW | 2024-12-10 | 功能优化 | 优化客户端新增累计流量、命令统计信息。 |
| 缺陷修复 | 修复集群实例在扩、缩容时大 Key 统计阈值失效的问题。 增强集群实例扩、缩容的稳定性。 |  |  |  |
| 5.5.2.15(5.2.15) | HIGH | 2024-10-08 | 安全加固 | 修复 CVE-2024-31228 安全漏洞。 修复 CVE-2024-31449 安全漏洞。 |
| 5.5.2.13(5.2.13) | LOW | 2024-08-21 | 功能优化 | 兼容开启 VPC 免密功能后使用错误密码鉴权的情况。 |
| 5.5.2.12(5.2.12) | LOW | 2024-07-23 | 功能优化 | 优化同时开启 VPC 免密功能和 #no_loose_check-whitelist-always 参数时的白名单检查逻辑。 时延洞察功能支持 Pipeline 的监控。 兼容至 Redis 开源社区 5.0.14 版本。 |
| 缺陷修复 | 修复 Lua、MULTI 内命令执行耗时统计错误的问题，影响范围为 5.2.8~5.2.11 版本。 |  |  |  |
| 5.5.2.11(5.2.11) | LOW | 2024-06-25 | 功能优化 | 优化 Pub/Sub 类命令的执行效率，避免大量连接同时停止订阅时造成卡顿。 优化客户端轮询检查策略，避免长连接无法及时进行内存统计和回收。 优化子进程生成 RDB 和 AOF 文件的落盘方法。 |
| 5.5.2.10(5.2.10) | LOW | 2024-05-28 | 安全加固 | 增强稳定性。 |
| 5.5.2.9(5.2.9) | LOW | 2024-05-28 | 功能优化 | 增加对处于 WATCH 或 BLOCK 状态的连接监控。 增加对 Rehash 的相关监控项。 实时统计热 Key（Hotkey）功能升级，允许调整热 Key 统计阈值，并支持展示精确 QPS、在同一时间支持最多统计 50 个热点 Key 等。 |
| 缺陷修复 | 修复由于使用共享对象造成 QPS 统计错误的问题，当开启实时统计热 Key 功能后将不在使用共享对象。 |  |  |  |
| 5.5.2.8(5.2.8) | LOW | 2024-04-24 | 安全加固 | 增强稳定性。 |
| 5.5.2.7(5.2.7) | LOW | 2024-03-14 | 功能优化 | INFO STATS 命令增加返回客户端输入、输出缓冲区超限断连的统计： client_query_buffer_limit_disconnections client_output_buffer_limit_disconnections 新增实时大 Key 统计阈值，默认为 2000。例如 String 类型的字符长度超过 2000 即判定为大 key；List、Set、Hash 等类型的元素个数超过 2000 个即判定为大 Key 等。 |
| 5.5.2.6(5.2.6) | LOW | 2024-01-09 | 功能优化 | 优化主动过期的效率。 INFO CLIENTS 命令中增加 pubsub_clients 监控项。 优化 CLUSTER NODES 、 CLUSTER SLOTS 命令的执行效率。 |
| 5.0.5.20(0.5.20) | HIGH | 2025-01-16 | 安全加固 | 修复 CVE-2024-46981 安全漏洞。 |
| 5.2.5 | LOW | 2023-08-28 | 功能优化 | 增加主备复制流量统计，将在 INFO STATS 中单独显示。 |
| 5.2.4 | HIGH | 2023-08-21 | 功能优化 | 集群架构直连模式实例支持 TLS 链路加密功能。 |
| 安全加固 | 修复 CVE-2022-24834 安全漏洞。 |  |  |  |
| 5.2.2 | MEDIUM | 2023-07-17 | 安全加固 | 优化集群架构实例主备切换和重启的流程。 |
| 5.2.1 | MEDIUM | 2023-06-30 | 安全加固 | 增强集群架构的稳定性。 |
| 5.2.0 | HIGH | 2023-04-24 | 功能优化 | 定期将热 Key（Hotkey）信息打印到审计日志中以便于排查。 ptod_enabled 参数的开关覆盖了性能监控与慢日志查询功能。 |
| 安全加固 | 修复在极端场景下，集群架构扩缩容时的若干缺陷。 |  |  |  |
| 5.1.13 | LOW | 2022-11-14 | 安全加固 | 增强稳定性。 |
| 5.1.12 | LOW | 2022-09-20 | 功能优化 | 审计日志新增记录过期删除事件。 审计日志不再记录 PING、AUTH、SELECT 等非写命令。 |
| 5.1.11 | LOW | 2022-09-06 | 功能优化 | 优化集群架构实例连接数耗尽后的处理方式。 |
| 5.1.10 | LOW | 2022-08-23 | 功能优化 | 优化集群架构实例的启动流程。 优化延迟统计直方图。 |
| 5.1.9 | LOW | 2022-06-22 | 功能优化 | 优化延迟统计直方图，详情请参见 [时延洞察](products/redis/documents/user-guide/latency-insights.md) 。 |
| 安全加固 | 升级、优化集群架构增、删节点流程，详情请参见 [调整集群分片数](products/redis/documents/user-guide/adjust-the-number-of-cluster-shards.md) 。 |  |  |  |
| 5.1.8 | LOW | 2022-05-17 | 功能优化 | 删除 INFO 命令返回的 Errorstats - Selected 字段。 |
| 5.1.7 | LOW | 2022-05-06 | 功能优化 | 集群架构支持 MOVE 命令。 |
| 5.1.6 | MEDIUM | 2022-04-25 | 功能优化 | 优化升级集群架构增、删节点流程，增强稳定性。 |
| 5.1.5 | LOW | 2022-04-13 | 功能优化 | 增强稳定性。 |
| 5.1.4 | LOW | 2022-03-24 | 新特性 | 支持延时统计直方图（Latency），详情请参见 [时延洞察](products/redis/documents/user-guide/latency-insights.md) 。 支持 INFO 命令返回 Errorstats（Redis 错误统计）信息。 |
| 5.1.3 | LOW | 2022-02-21 | 功能优化 | 支持 READONLY、READWRITE 命令，详情请参见 [Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) [开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md) 。 |
| 5.1.1 | LOW | 2022-01-04 | 功能优化 | 增加 DB 元数据监控项：占用内存。 |
| 5.0.9 | LOW | 2021-12-22 | 功能优化 | 优化实时 Top Key 统计功能。 |
| 5.0.8 | LOW | 2021-11-15 | 功能优化 | 支持集群版无感扩、缩容。 账号名称大小写敏感。 |
| 0.5.19 | HIGH | 2023-08-15 | 安全加固 | 修复 CVE-2022-24834 安全漏洞。 |
| 0.5.18 | LOW | 2022-08-23 | 功能优化 | 优化集群架构实例的启动流程。 |
| 0.5.17 | HIGH | 2022-06-07 | 安全加固 | 增强稳定性。 |
| 0.5.16 | HIGH | 2022-05-23 | 安全加固 | 提升集群架构实例开通直连访问后，变配的稳定性。 |
| 0.5.15 | HIGH | 2022-04-25 | 安全加固 | 修复集群架构实例开通直连访问后，变配过程中迁移大 Key 概率性失败的问题。 |
| 0.5.14 | LOW | 2022-01-04 | 功能优化 | 增加 DB 元数据监控项：占用内存。 |
| 0.5.12 | LOW | 2021-11-29 | 功能优化 | 修复异常情况下集群实例重启失败的问题。 |
| 0.5.11 | LOW | 2021-11-24 | 功能优化 | 修复实时 Key 分析功能遗漏统计 Spop 命令的问题。 |
| 0.5.10 | HIGH | 2021-10-26 | 安全加固 | 修复集群变配过程中慢日志过多的问题，增强稳定性。 |
| 0.5.9 | HIGH | 2021-10-15 | 安全加固 | 增强稳定性。 |
| 0.5.8 | MEDIUM | 2021-10-13 | 功能更新 | 增强了集群变配时槽（slot）无感迁移的自治能力。 |
| 0.5.7 | LOW | 2021-08-26 | 新特性 | 细分 QPS（Queries Per Second）统计，当前支持统计读、写与其他，共计三类 QPS。 |
| 0.5.6 | HIGH | 2021-08-16 | 缺陷修复 | 增强了槽（slot）的无感迁移可靠性，增强稳定性。 |
| 0.5.5 | HIGH | 2021-08-05 | 缺陷修复 | 修复集群实例开通直连的场景下，变配存在概率失败的问题。 |
| 0.5.4 | MEDIUM | 2021-07-27 | 功能更新 | 增强稳定性。 |
| 0.5.3 | MEDIUM | 2021-07-21 | 功能更新 | 优化数据迁移完成后删除源端数据的流程，增强数据可靠性。 简化数据迁移的增量数据同步流程。 |
| 0.5.2 | HIGH | 2021-04-26 | 安全加固 | 主要解决社区 Lua JIT 的安全性漏洞。 |
| 新特性 | 优化槽（slot）的迁移能力，云盘版实例可基于此实现无损扩缩容。 支持大 Key（big key）实时统计。 支持通过公网获取虚拟 IP（VIP）地址，为使用直连地址用户提供更好的支持。 |  |  |  |
| 0.5.0 | MEDIUM | 2021-03-25 | 新特性 | 支持槽（slot）的无感迁移能力。 |
| 功能优化 | 增强在处理大量异步客户端请求场景下的稳定性。 |  |  |  |
| 0.4.0 | MEDIUM | 2021-03-09 | 新特性 | 支持大 Key（big key）实时统计。 支持 CONFIG RESETSTAT 命令。 当返回 illegal address 错误消息时，Redis 会将当前客户端的 IP 地址包含在错误消息中。您可以根据提示，为 Redis 实例设置正确的 IP 白名单。 图 1. IP 地址提示 r-bp xxx .redis.rds.aliyuncs.com:6379> auth (error) ERR illegal address: 172.16.xxx:39136 |
| 功能优化 | 优化实例健康检查能力，提升在磁盘抖动场景下的主备切换速度。 |  |  |  |
| 0.3.10 | HIGH | 2020-09-25 | 缺陷修复 | 修复 CLUSTER NODES 命令返回值与开源协议不一致的问题，即槽（slot）间以空格分隔，避免客户端解析错误。 |
| 0.3.9 | LOW | 2020-07-20 | 新特性 | 支持 ECS 安全组功能，通过为 Redis 实例绑定 ECS 所属安全组的方式实现快速授权（无需手动填写 ECS 的 IP 地址），可提升运维的便捷性。更多信息，请参见 [通过](products/redis/documents/getting-started/step-2-configure-whitelists.md) [ECS](products/redis/documents/getting-started/step-2-configure-whitelists.md) [安全组设置白名单](products/redis/documents/getting-started/step-2-configure-whitelists.md) 。 |
| 0.3.8 | HIGH | 2020-07-14 | 功能优化 | 开放 CLIENT UNBLOCK 子命令。 |
| 缺陷修复 | 修复在迁移 slot（槽）时解析 expire（过期时间）不正确的问题。 订正审计日志中的 latency 标记位，避免其在主备审计日志中混淆。 |  |  |  |
| 0.3.7 | HIGH | 2020-06-17 | 缺陷修复 | 修复直连模式下返回 IP 地址不可达的问题。 |
| 0.3.6 | LOW | 2020-06-09 | 新特性 | INFO 命令返回值中， Replication 部分支持展示 role 信息（例如 role:master ），可兼容 Redisson 客户端在部分场景下对该信息的调用。 |
| 0.3.5 | LOW | 2020-06-05 | 新特性 | 支持对读写命令 QPS 的统计，更多信息，请参见 [查看性能监控](products/redis/documents/user-guide/view-monitoring-data.md) 。 |
| 0.3.4 | HIGH | 2020-04-08 | 缺陷修复 | 修复热点 Key 在被执行逐出时可能出现的崩溃问题。 修复关闭审计日志时因 UAF（Use-After-Free）导致的崩溃问题。 |
| 0.3.1 | HIGH | 2020-02-20 | 新特性 | 支持审计日志功能，为您提供日志的查询、在线分析、导出等功能，更多信息，请参见 [审计日志](products/redis/documents/user-guide/enable-the-new-audit-log-feature.md) 。 支持直连模式，客户端通过直连地址可绕过代理，连接方式类似连接原生 Redis 集群，可降低链路开销，进一步提升 Redis 服务的响应速度。更多信息，请参见 [开通直连访问](products/redis/documents/user-guide/enable-the-direct-connection-mode.md) 。 支持在 [专有网络](products/redis/documents/user-guide/enable-password-free-access.md) [VPC](products/redis/documents/user-guide/enable-password-free-access.md) [免密访问](products/redis/documents/user-guide/enable-password-free-access.md) 的场景下，申请公网连接地址。 增加 INFO 命令中关于 oom_err_count 的统计场景：即 maxmemory 数据量超过设定值时会被计入。 |
| 缺陷修复 | 修复当 RPOPLPUSH 命令的 source 和 destination 相同时，在执行过程中因触发了过期机制导致的崩溃问题。 修复专有网络 VPC 免密模式下权限验证错误的问题。 |  |  |  |
| 0.2.0 | LOW | 2020-01-17 | 新特性 | 支持实时热点 Key 统计，帮助您快速发现实例中的热点 Key，更多信息，请参见 [Top Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [统计](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) 。 |
| 0.1.2 | LOW | 2019-11-26 | 新特性 | 支持在 [读写分离](products/redis/documents/product-overview/read-or-write-splitting-instances-1.md) 实例的只读节点中执行只读的 lua 脚本。 |
| 0.1.2 之前 | 不涉及 | 不涉及 | 不涉及 | 5.0 版本下的早期小版本，建议升级至最新的小版本。 |


Redis开源版4.0版本历史发布记录

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 1.9.17 | LOW | 2023-11-25 | 安全加固 | 增强稳定性。 |
| 1.9.16 | LOW | 2023-08-15 | 安全加固 | 增强稳定性。 |
| 1.9.15 | LOW | 2023-05-17 | 功能优化 | 集群架构实例支持在云监控控制台查看代理节点到数据节点的连接数。 |
| 1.9.14 | LOW | 2022-11-14 | 功能优化 | 优化统计信息。 |
| 1.9.13 | LOW | 2022-08-23 | 功能优化 | 优化集群架构实例的启动流程。 |
| 1.9.12 | HIGH | 2022-06-07 | 安全加固 | 增强稳定性。 |
| 1.9.10 | HIGH | 2022-05-23 | 安全加固 | 提升集群架构实例开通直连访问后，变配的稳定性。 |
| 1.9.9 | HIGH | 2022-04-25 | 安全加固 | 增强稳定性。 |
| 1.9.8 | HIGH | 2022-04-25 | 安全加固 | 修复集群架构实例开通直连访问后，变配过程中迁移大 Key 概率性失败的问题。 |
| 1.9.6 | HIGH | 2021-10-15 | 安全加固 | 增强稳定性。 |
| 1.9.5 | LOW | 2021-09-13 | 新特性 | 细分 QPS（Queries Per Second）统计，当前支持统计读、写与其他，共计三类 QPS。 |
| 1.9.4 | HIGH | 2021-08-05 | 缺陷修复 | 修复集群实例开通直连的场景下，变配存在概率失败的问题。 |
| 1.9.3 | MEDIUM | 2021-07-20 | 功能更新 | 增强稳定性。 |
| 1.9.2 | HIGH | 2021-04-19 | 安全加固 | 主要解决社区 Lua JIT 的安全性漏洞。 |
| 新特性 | 支持通过公网获取虚拟 IP（VIP）地址，为使用直连地址用户提供更好的支持。 |  |  |  |
| 1.9.1 | MEDIUM | 2021-03-08 | 功能优化 | 优化实例健康检查能力，提升在磁盘抖动场景下的主备切换速度。 优化大内存实例通过 fork 执行 BGSAVE 和 REWRITE 的能力，避免可能出现的长时间停顿问题。 |
| 1.9.0 | LOW | 2021-02-22 | 新特性 | 当返回 illegal address 错误消息时，Redis 会将当前客户端的 IP 地址包含在错误消息中。您可以根据提示，为 Redis 实例设置正确的 IP 白名单。 |
| 1.8.8 | HIGH | 2020-09-25 | 缺陷修复 | 修复 CLUSTER NODES 命令返回值与开源协议不一致的问题，即槽（slot）间以空格分隔，避免客户端解析错误。 |
| 1.8.7 | LOW | 2020-07-20 | 新特性 | 支持 ECS 安全组功能，通过为 Redis 实例绑定 ECS 所属安全组的方式实现快速授权（无需手动填写 ECS 的 IP 地址），可提升运维的便捷性。更多信息，请参见 [通过](products/redis/documents/getting-started/step-2-configure-whitelists.md) [ECS](products/redis/documents/getting-started/step-2-configure-whitelists.md) [安全组设置白名单](products/redis/documents/getting-started/step-2-configure-whitelists.md) 。 |
| 1.8.6 | HIGH | 2020-07-14 | 缺陷修复 | 订正审计日志中的 latency 标记位，避免其在主备审计日志中混淆。 |
| 1.8.5 | LOW | 2020-06-09 | 新特性 | INFO 命令返回值中， Replication 部分支持展示 role 信息（例如 role:master ），可兼容 Redisson 客户端在部分场景下对该信息的调用。 |
| 1.8.4 | LOW | 2020-06-05 | 新特性 | 支持对读写命令 QPS 的统计，更多信息，请参见 [查看性能监控](products/redis/documents/user-guide/view-monitoring-data.md) 。 |
| 1.8.3 | HIGH | 2020-04-08 | 缺陷修复 | 修复热点 Key 在被执行逐出时可能出现的崩溃问题。 修复关闭审计日志时因 UAF（Use-After-Free）导致的崩溃问题。 |
| 1.8.1 | LOW | 2020-02-20 | 新特性 | 支持在已开启 [专有网络](products/redis/documents/user-guide/enable-password-free-access.md) [VPC](products/redis/documents/user-guide/enable-password-free-access.md) [免密访问](products/redis/documents/user-guide/enable-password-free-access.md) 的场景下，申请公网连接地址的操作。 |
| 1.8.0 | HIGH | 2020-01-16 | 新特性 | 支持实时热点 Key 统计，帮助您快速发现实例中的热点 Key，更多信息，请参见 [Top Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) [统计](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md) 。 |
| 缺陷修复 | 修复在 [直连访问](products/redis/documents/user-guide/enable-the-direct-connection-mode.md) 场景下， INFO 命令的返回信息可包含 cluster_enabled 信息，使某些 SDK 能够正确地自协商至集群模式。 |  |  |  |
| 1.7.1 | MEDIUM | 2019-11-20 | 新特性 | 支持在读写分离实例的只读节点中执行只读的 lua 脚本。 支持直连模式，客户端通过直连地址可绕过代理，像连接原生 Redis 集群一样连接阿里云 Redis 集群，可降低链路开销，进一步提升 Redis 服务的响应速度。更多信息，请参见 [开通直连访问](products/redis/documents/user-guide/enable-the-direct-connection-mode.md) 。 INFO 命令的返回信息中， Memory 部分中增加对 lua 脚本内存量的统计。 |
| 功能优化 | 优化审计日志的对内存使用。 |  |  |  |
| 1.5.8 | HIGH | 2019-09-23 | 缺陷修复 | 修复旧版全球多活链路中，双向同步时 SETEX 的原子性被破坏的问题。 |
| 1.5.6 | HIGH | 2019-08-28 | 新特性 | 审计日志支持记录 latency 事件。 |
| 缺陷修复 | 修复客户端发起的 KEYS 、 FLUSHALL 、 FLUSHDB 等命令引发的慢请求可能引起主备切换的问题。 |  |  |  |
| 1.5.4 | LOW | 2019-07-08 | 新特性 | 支持审计日志功能，为您提供日志的查询、在线分析、导出等功能，更多信息，请参见 [审计日志](products/redis/documents/user-guide/enable-the-new-audit-log-feature.md) 。 支持对整个事件循环的 latency 记录，帮助您了解引擎的状态。 |
| 1.5.2 | HIGH | 2019-07-04 | 缺陷修复 | 修复当 RPOPLPUSH 命令的 source 和 destination 相同时，在执行过程中因触发了过期机制导致的崩溃问题。 |
| 1.4.0 | HIGH | 2019-05-15 | 缺陷修复 | 修复实例重启后，进入加载 RDB 或 AOF 的状态会触发主备切换的问题。 |
| 1.4.0 之前 | 不涉及 | 不涉及 | 不涉及 | 4.0 版本下的早期小版本，建议升级至最新的小版本。 |


Redis倚天版历史发布记录

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 24.12.1.0 | LOW | 2024-12-18 | 功能优化 | 增强稳定性。 |
| 24.12.0.0 | LOW | 2024-12-06 | 功能优化 | 在 Sentinel 免密模式下，支持通过 #no_loose_sentinel-password-free-commands 参数配置更多的免密命令。 增强稳定性。 |
| 24.11.0.0 | LOW | 2024-11-20 | 功能优化 | INFO 命令中返回了节点的 run_id 字段。 优化升级和变配迁移的稳定性。 |
| 24.10.0.0 | MEDIUM | 2024-10-16 | 功能优化 | 写性能提升约 5% ~ 10%左右。 |
| 缺陷修复 | 修复 CVE-2024-31228 安全漏洞。 修复 CVE-2024-31227 安全漏洞。 修复 CVE-2024-31449 安全漏洞。 增强稳定性。 |  |  |  |
| 24.8.2.0 | LOW | 2024-08-28 | 缺陷修复 | 增强稳定性。 |
| 24.8.1.0 | LOW | 2024-08-22 | 功能优化 | 针对兼容 Redis 7.0 版本，允许 SET 命令的 GET 参数同时和 NX/XX 参数使用。 |
| 24.8.0.0 | LOW | 2024-08-15 | 功能优化 | 基本命令的处理速度提升 5%。 |
| 24.7.0.0 | LOW | 2024-07-22 | 功能优化 | 增强稳定性。 |
| 24.6.0.0 | LOW | 2024-07-02 | 功能优化 | 优化在突发大流量场景下主备节点同步的稳定性。 |
| 24.5.1.0 | LOW | 2024-06-06 | 功能优化 | 取消 COMMAND GETKEYS 命令的使用限制。 |
| 24.5.0.0 | MEDIUM | 2024-05-22 | 功能优化 | 优化主备模式下跨 Slot 命令的同步能力。 优化了大实例的后台 BGREWRITE 的速度。 INFO 命令中返回了 Per command 的 CPU、QPS、流量信息。 |
| 缺陷修复 | 增强稳定性。 |  |  |  |
| 24.4.1.0 | MEDIUM | 2024-04-22 | 功能优化 | 支持 DTS 任务重启后同步点位任意回退，若实例需要长期配置 DTS 任务，建议升级到该版本。 |
| 24.4.0.0 | MEDIUM | 2024-04-16 | 功能优化 | 优化基础数据结构的内存占用，在少量复杂结构元素时降低内存占用。 |
| 缺陷修复 | 增强稳定性。 |  |  |  |
| 24.3.2.2 | MEDIUM | 2024-03-21 | 功能优化 | 优化标准架构（主备）实例的引擎元数据占用。 |
| 缺陷修复 | 增强稳定性。 |  |  |  |
| 24.3.2.1 | MEDIUM | 2024-03-18 | 缺陷修复 | 修复 XINFO 命令返回格式多了一层缩进的问题。 修复 SCAN 命令返回的结果数量有概率远大于 Count 参数值的问题。 |
| 24.3.1.0 | LOW | 2024-03-11 | 功能优化 | 延迟创建 DB（多数据库）的元数据，不在执行 SELECT 命令时立即创建，而是当向 DB 中读、写数据时创建 DB 及其元数据。以避免某些 Redis 管控工具遍历所有 DB 造成元数据膨胀。 优化存在多个 DB 时的过期检查效率，公平地根据携带过期数据的数量下发过期任务。 |
| 24.3.0.0 | MEDIUM | 2024-03-07 | 功能优化 | 支持在平滑扩缩容迁移变配失败时进行秒级回滚，避免因变配失败导致实例不可用。 说明 但在使用较多逻辑 DB 的情况下会导致元数据占用内存较大，如果遇到此类问题请升级至 24.3.2.2 及以上版本，已优化该问题。 允许集群架构下执行多 DB 命令：SWAPDB、COPY、MOVE。 |
| 缺陷修复 | 修复 ZRANGEBYSCORE 命令设置 LIMIT 过大时可能导致 DB 预分配内存 OOM 的问题。 |  |  |  |
| 24.1.0.0 | MEDIUM | 2024-01-23 | 缺陷修复 | 修复 GETDEL 命令异常情况下可能会导致实例崩溃的问题。 修复 XINFO STREAM 命令返回的结果中 last-entry 信息错误的问题。 |
| 23.12.2.0 | LOW | 2023-12-26 | 功能优化 | 增强稳定性。 |
| 23.12.1.2 | MEDIUM | 2023-12-21 | 功能优化 | 优化部分场景下的写性能，推荐升级。 |
| 缺陷修复 | 合并 Redis 社区中有关 Lua 脚本的多个 CVE 修复。 优化若干个稳定性问题，推荐升级。 |  |  |  |
| 23.8.1.3 | MEDIUM | 2023-09-25 | 缺陷修复 | 修复 ZSet 结构在内存编码转换的时候，有极低概率导致崩溃的问题。 修复遇到错误的 Redis 协议时，有低概率导致服务端异常 HA 的问题。 |
| 23.8.1.2 | MEDIUM | 2023-08-22 | 功能优化 | 降低实例空闲时的 CPU 使用率，提升实例基础性能。 标准化 CloudDBA 中的 CPU 使用率指标。 主备复制流量将在 INFO STATS 中单独显示。 |
| 23.8.0.0 | LOW | 2023-08-03 | 首次发布 | 首次发布的小版本。 |


## 相关文档

- 

Proxy节点的版本发布记录请参见[Proxy](products/redis/documents/support/apsaradb-for-redis-proxy-nodes.md)[小版本发布日志](products/redis/documents/support/apsaradb-for-redis-proxy-nodes.md)。

- 

Tair（企业版）的版本发布记录请参见[Tair](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)。

[上一篇：Tair小版本发布日志](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)[下一篇：Proxy小版本发布日志](products/redis/documents/support/apsaradb-for-redis-proxy-nodes.md)

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
