# Redis开源版支持的参数及其说明-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/supported-parameters

# Redis开源版配置参数列表
您可以根据业务场景对云数据库 Tair（兼容 Redis）实例的参数进行调优与自定义配置，已提升实例的性能与安全性。不同的引擎版本和架构支持的参数有所区别，本文为您介绍各参数的详细说明。
## 注意事项
若设置参数时报错Parameter is not supported for current version，请升级小版本后重试，具体操作请参见[升级小版本与代理版本](update-the-minor-version.md)。
部分参数在提交修改后会自动重启实例（重启过程中实例会发生秒级闪断）。在设置参数时，您需要关注目标参数的重启生效列，更多信息，请参见[设置参数](modify-the-values-of-parameters-for-an-instance.md)。
重要
本文仅包含Redis开源版实例的参数，关于Tair（企业版）实例的参数（包含[内存型](../product-overview/dram-based-instances.md)、[持久内存型](../product-overview/persistent-memory-optimized-instances-1.md)和[磁盘型](../product-overview/essd-based-instances-1.md)）请参见[Tair](parameter-support.md)[企业版配置参数列表](parameter-support.md)。
## 支持的参数及说明
为便于阅读和内容表达，本文的表格约定使用下述注释：
✔️表示在该大版本或架构下，支持该参数。
❌表示在该大版本或架构下，不支持该参数。
说明
为最大程度保障实例的稳定运行，目前仅开放部分参数，如果某个参数未在本文中列出，即不支持设置该参数。
关于架构的详细介绍，请参见[标准架构](../product-overview/standard-master-replica-instances.md)、[集群架构](../product-overview/cluster-master-replica-instances.md)和[读写分离架构](../product-overview/read-or-write-splitting-instances-1.md)。
### 数据库内核参数
| 参数 | 说明 | 实例的大版本与架构 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 7.0 版本 | 6.0 版本 | 5.0 版本 | 4.0 版本 | 2.8 版本 |  |  |
| #no_loose_check-whitelist-always | 开启 [专有网络免密](enable-password-free-access.md) 后，是否检查客户端的 IP 在实例白名单中。取值： yes ：开启检查。在开启免密访问后，仍需将同一专有网络的客户端 IP 地址添加至实例的白名单中，才可通过该客户端连接实例。 若开启免密，但未正确设置白名单时，连接的报错示例： (error) ERR illegal address 。 no （默认）：不检查。在开启免密访问后，无需将同一专有网络的客户端 IP 地址添加至实例的白名单中，可通过该客户端连接实例。 说明 仅 经典 架构实例支持该参数。 云原生 架构无论是否开启免密，都会强制校验 IP 白名单。 | ❌ | ❌ | 标准️️✔️ 集群✔️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | ❌ |
| #no_loose_disabled-commands | 设置禁用命令，可根据业务需求禁用某些高危命令或高时间复杂度的命令，例如 FLUSHALL 、 FLUSHDB 、 KEYS 、 HGETALL 、 EVAL 、 EVALSHA 、 SCRIPT 等。 说明 命令以小写字母的形式填写，多个命令间使用英文逗号（,）分隔。 禁用 FLUSHALL 命令不会影响控制台中 清除数据 功能。 为保障实例稳定、高效率地运行，部分命令不支持被禁用，例如 CONFIG 等，具体命令请参见 [不支持禁用的命令](disable-high-risk-commands.md) 。 | 标准️️✔️ 集群✔️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ |
| #no_loose_sentinel-enabled | 在标准架构或集群架构直连模式，开启或关闭哨兵（Sentinel）兼容模式，可选值： yes ：开启。 no （默认）：关闭。 | 标准️️✔️ 集群✔️ 读写分离❌ | 标准️️✔️ 集群✔️ 读写分离❌ | 标准️️✔️ 集群✔️ 读写分离❌ | 标准️️✔️ 集群✔️ 读写分离❌ | ❌ |
| #no_loose_sentinel-password-free-access | 开启哨兵模式时，是否允许免密执行 Sentinel 相关命令，取值： yes ：开启。开启后，可以在任意连接上 免密执行 Sentinel 命令以及使用 SENTINEL 命令监听 +switch-master 通道。 no （默认）：关闭。 | 标准️️✔️ 集群✔️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | ❌ | ❌ | ❌ |
| #no_loose_sentinel-password-free-commands | 在开启哨兵模式以及 #no_loose_sentinel-password-free-access 参数后，您还可以通过本参数添加额外的免密命令列表（默认为空）。 重要 设置后，可以在任意连接上 免密执行 对应命令，请谨慎操作。 命令以小写字母的形式填写，多个命令间使用英文逗号（,）分隔。 | 标准️️✔️ 集群✔️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | ❌ | ❌ | ❌ |
| #no_loose_tls-min-version | 设置实例支持的 TLS 最低版本，取值： TLSv1 （默认）。 TLSv1.1 。 TLSv1.2 。 | 标准️️❌ 集群✔️ 读写分离✔️ | 标准️️❌ 集群✔️ 读写分离✔️ | 标准️️❌ 集群✔️ 读写分离✔️ | 标准️️❌ 集群✔️ 读写分离✔️ | 标准️️❌ 集群✔️ 读写分离✔️ |
| appendfsync | AOF（AppendOnly File）持久化功能的 fsync 频率，仅在 appendonly 参数开启时生效，默认为 everysec ，不支持修改。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| appendonly | 开启或关闭主节点的 AOF 持久化功能，取值： yes （默认）：开启 AOF 持久化。 no ：关闭 AOF 持久化。 说明 RDB（Redis database）持久化功能默认为每天一次，更多信息请参见 [自动或手动备份](automatic-or-manual-backup.md) 。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| client-output-buffer-limit pubsub client-output-buffer-limit normal | pubsub 为限制对发布订阅客户端的输出缓冲，默认为 33554432 8388608 60 。 normal 为限制对普通客户端的输出缓冲，默认为 524288000 0 0 。 参数值格式均为 <hard limit> <soft limit> <soft seconds> 。 <hard limit> ：当某客户端的输出缓冲区占用内存达到或超过 hard limit 的限制时，断开该客户端的连接。hard limit 值的单位为 Byte。 <soft limit> 和 <soft seconds> ：当某客户端的输出缓冲区占用内存达到或超过 soft limit 的限制，且该状态持续时间大于等于 soft seconds 限定的秒数，断开该客户端的连接。soft limit 值的单位为 Byte，soft seconds 值的单位为秒。 重要 仅兼容 Redis 6.0 及以上版本的实例才支持 client-output-buffer-limit normal 参数。 客户端输出缓冲区会占用运行内存，如果堆积命令过多会造成 实例数据逐出 、甚至 内存超限宕机 。调整该参数之前请仔细校验实例内存规格，谨慎操作。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| dynamic-hz | 开启或关闭动态 hz，取值： yes （默认）：开启。 no ：关闭。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | ❌ | ❌ |
| hash-max-ziplist-entries hash-max-ziplist-value | 兼容 Redis 6.0 及以下版本，默认使用 ziplist 作为 Hash 的编码方式。当 Hash 对象同时满足以下两个条件时， 使用 ziplist 编码。 Hash 的键值对数量小于 hash-max-ziplist-entries 的值。 Hash 的键和值的字符串长度都小于 hash-max-ziplist-value 。 | ❌ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| hash-max-listpack-entries hash-max-listpack-value | 兼容 Redis 7.0 版本起，默认使用 listpack 作为 Hash 的编码方式。当 Hash 对象同时满足以下两个条件时， 使用 listpack 编码。 Hash 的键值对数量小于 hash-max-listpack-entries 的值。 Hash 的键和值的字符串长度都小于 hash-max-listpack-value 。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| hz | 设置实例后台任务执行频率，例如清除过期键任务。取值范围为[1-500]，默认为 10，即每秒执行 10 次。 说明 该值越大，CPU 资源消耗越多，但在过期键较多的情况下清理频率也更高，同时实例能够更精确地处理超时。建议取值不超过 100。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| latency-tracking | 是否开启命令时延监控，取值： yes （默认）：开启。 no ：不开启。 说明 仅兼容 Redis 7.0 及以上支持该参数。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| lazyfree-lazy-eviction | 是否开启基于 lazyfree 的驱逐功能，取值： yes ：开启。 no （默认）：不开启。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ |
| lazyfree-lazy-expire | 是否开启基于 lazyfree 的过期 Key 删除功能，取值： yes （默认）：开启。 no ：不开启。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ |
| lazyfree-lazy-server-del | DEL 命令是否基于 lazyfree 异步删除数据，取值： yes （默认）：开启。 no ：不开启。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ |
| lazyfree-lazy-user-del | 执行 DEL 命令时是否基于 lazyfree 异步删除数据，取值： yes （默认）：开启。 no ：不开启。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ |
| lazyfree-lazy-user-flush | 是否将 FLUSHDB 、 FLUSHALL 、 SCRIPT FLUSH 、 FUNCTION FLUSH 命令自动转换为 Lazyfree 异步删除模式，取值： yes ：开启。 no （默认）：不开启。 说明 仅兼容 Redis 7.0 及以上支持该参数。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| list-compress-depth | 列表中两端不被压缩的节点个数，取值范围为[0-65535]。 0（默认）：表示都不压缩。 1-65535：表示 list 两端各有 1-65535 个节点不压缩，中间的节点压缩。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ |
| list-max-ziplist-entries | 仅兼容 Redis 2.8 版本支持这组参数。当 List 对象同时满足以下两个条件时， 使用 ziplist 编码。 List 对象的元素数量小于 list-max-ziplist-entries 的值。 List 对象的所有元素的字符串长度的字节数都小于 list-max-ziplist-value 的值。 | ❌ | ❌ | ❌ | ❌ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| list-max-ziplist-value |  |  |  |  |  |  |
| list-max-ziplist-size list-max-listpack-size | 兼容 Redis 6.0 及以下版本默认使用 ziplist 作为 List 的编码方式（ list-max-ziplist-size 参数），兼容 Redis 7.0 版本起默认使用 listpack 作为 List 的编码方式（ list-max-listpack-size 参数）。 取正值表示按照数据项个数来限定每个 quicklist 节点上的 ziplist（listpack）长度。例如，当该参数配置为 5 时，每个 quicklist 节点的 ziplist（listpack）最多包含 5 个数据项。 取负值表示按照占用字节数来限定每个 quicklist 节点上的 ziplist（listpack）长度，取值： -5 ：每个 quicklist 节点上的 ziplist（listpack）大小不能超过 64 Kb。 -4 ：每个 quicklist 节点上的 ziplist（listpack）大小不能超过 32 Kb。 -3 ：每个 quicklist 节点上的 ziplist（listpack）大小不能超过 16 Kb。 -2 （默认）：每个 quicklist 节点上的 ziplist（listpack）大小不能超过 8 Kb。 -1 ：每个 quicklist 节点上的 ziplist（listpack）大小不能超过 4 Kb。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ |
| maxmemory-policy | 数据逐出策略。当实例内存不足，使用量达到 Maxmemory 时，会触发数据逐出，您可以选择不同的数据逐出策略。取值如下： 说明 每个实例的 Maxmemory 为实例的规格大小，且不支持修改。例如购买的实例规格为 2 GB，则该实例的 Maxmemory 为 2 GB。 在集群架构中，当单个数据节点达到 Maxmemory 时（即使此时的总内存使用率未到达上限），该数据节点也会触发数据逐出。您需要处理数据倾斜的问题，更多信息请参见 [如何处理数据倾斜](deal-with-data-skew-issues.md) 。 LRU 表示最近最少使用的。LFU 表示最不常用的。LRU、LFU 和 volatile-ttl 都是使用近似随机算法实现的。 volatile-lru （内存型及 Redis 开源版 默认）：从已设置过期时间（Expire）的 Key 中，删除最近最少使用的 Key（LRU 算法），且不会考虑 Key 是否已经过期。 noeviction （持久内存型默认）：不删除任何 Key，当内存达到上限时，将无法写入新数据，数据库会返回错误信息。 volatile-lfu ：从已设置过期时间（Expire）的 Key 中，删除最不常用的 Key（LFU 算法）。 volatile-random ：从已设置过期时间（Expire）的 Key 中，随机删除一些 Key。 volatile-ttl ：从已设置过期时间（Expire）的 Key 中，根据存活时间（TTL）从小到大排序进行删除。 allkeys-lru ：从所有 Key 中，删除最近最少使用的 Key（LRU 算法）。 allkeys-lfu ：从所有 Key 中，删除最不常用的 Key（LFU 算法）。 allkeys-random ：从所有 Key 中，随机删除一些 Key。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| maxmemory-eviction-tenacity | 数据逐出（Eviction）因子，用于设置每次数据逐出的延时，取值为[0-100]，默认为 10。 若降低该值，可能会降低延时，但会影响数据逐出的有效性。 当写入流量特别大时，可增加该值，但延时会增大。100 表示忽略延时，不停逐出直到内存降至 maxmemory 以下或者没有可逐出 Key。 说明 仅 Redis 7.0 支持该参数。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| active-expire-effort | 删除过期 Key（Expire）因子，用于设置每次删除过期 Key 的延时，取值为[1-10]，默认为 1。数值越大删除过期 Key 越快，同时消耗的 CPU 资源也更多。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ |
| notify-keyspace-events | notify-keyspace-events 的参数值可以是以下字符的任意组合，它指定了服务器该发送哪些类型的通知。该参数将针对整个实例（所有 DB）启用通知，启用后会额外消耗 CPU，更多信息请参见 [Redis keyspace notifications](https://redis.io/docs/latest/develop/use/keyspace-notifications/) 。 K ：键空间通知，所有通知以 __keyspace@<db>__ 为前缀。 E ：键事件通知，所有通知以 __keyevent@<db>__ 为前缀。 g ： DEL 、 EXPIRE 、 RENAME 等类型无关的通用命令的通知。 $ ：字符串命令的通知，会发送关于字符串的创建、修改、删除等操作的通知。 l ：列表命令的通知。 s ：集合命令的通知。 h ：哈希命令的通知。 z ：有序集合命令的通知。 x ：过期事件，不一定在键过期时发送，而是在过期键被删除时发送。 e ：驱逐（evict）事件，每当有键因为 maxmemory 政策而被删除时发送。 A ：参数 g$lshzxe 的别名，表示监听上述所有事件，设置示例为 AKE 。 重要 输入的参数中至少包含 K 或 E ， 否则不会有任何通知被分发。 例如您希望订阅过期事件，您可以在参数设置中将该参数设置为 Ex 。设置参数后，在客户端执行对应的订阅命令： PSUBSCRIBE __keyevent@0__* ，表示订阅 DB0 的键事件通知。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| set-max-intset-entries | 当 Set 集合内的数据符合以下条件时，会使用 intset 编码。 当集合内所有数据都是字符对象。 都是基数为 10 的整数，范围为 64 位有符号整数。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| slowlog-log-slower-than | 慢日志的阈值，慢日志将记录执行时间超过该阈值的命令。单位为微秒（μs），默认为 20000（即 20 毫秒），取值范围 10000~10000000。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| slowlog-max-len | 慢日志最多保存记录条数，取值范围 100 ~ 10000 ，默认为 1024 。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| stream-node-max-bytes | Stream 中每个宏节点（Macro Node）能够占用的最大内存，取值范围： 0 ~ 999,999,999,999,999 。 说明 0 表示无限制。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | ❌ | ❌ |
| stream-node-max-entries | Stream 中每个宏节点中可存储条目的最大数量，取值范围： 0 ~ 999,999,999,999,999 。 说明 0 表示无限制。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️ 读写分离✔️ | ❌ | ❌ |
| tracking-table-max-keys | 设置 Tracking Table 中存储 Key 数量的上限，取值为[0-1000000000]，默认为 1000000。 说明 仅 Redis 7.0 支持该参数。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| timeout | 当客户端的空闲时间达到指定秒数后，实例会关闭该连接，单位为秒，取值范围为[0,100000]，默认为 0（表示不断开任何连接）。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ |
| zset-max-ziplist-entries zset-max-ziplist-value | 兼容 Redis 6.0 及以下版本默认使用 ziplist 作为 Zset 的编码方式。当 Zset 同时满足以下两个条件时， 使用 ziplist 编码。 Zset 的键值对数量小于 zset-max-ziplist-entries 的值。 Zset 的键值对的键和值的字符串长度都小于 zset-max-ziplist-value 。 | ❌ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| zset-max-listpack-entries zset-max-listpack-value | 兼容 Redis 7.0 版本起默认使用 listpack 作为 Zset 的编码方式。当 Zset 同时满足以下两个条件时， 使用 listpack 编码。 Zset 的键值对数量小于 zset-max-listpack-entries 的值。 Zset 的键值对的键和值的字符串长度都小于 zset-max-listpack-value 。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| bigkey-threshold | [Top Key](use-the-real-time-key-statistics-feature.md) [统计](use-the-real-time-key-statistics-feature.md) 中大 Key（元素数量多的 Key）的元素数量阈值。默认 2000 个，取值范围为[500-100000]。 说明 若参数设置未显示此参数，请 [升级小版本](update-the-minor-version.md) 后重试。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ |
| hotkey-threshold | [Top Key](use-the-real-time-key-statistics-feature.md) [统计](use-the-real-time-key-statistics-feature.md) 中热 Key（按 QPS）的统计阈值。默认 5000，取值范围为[100-100000]。 说明 仅小版本号 7.0.1.8、6.0.2.9、5.5.2.9 及以上支持此参数。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ |
### Proxy节点参数
代理（Proxy）节点提供的参数，仅集群架构代理模式、读写分离架构实例支持下述参数。
| 参数 | 说明 |
| --- | --- |
| cluster_compat_enable | 是否开启原生 Redis cluster 语法兼容，取值： 0 ：关闭。 1 （默认）：开启，开启后支持 READONLY、READWRITE 和 CLUSTER 类命令，具体命令请参见 [代理模式（Proxy）支持的命令列表](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md) 。 |
| hello_enabled | 是否开启通过 HELLO 命令切换协议 RESP2、RESP3 协议的开关。取值： 0 （默认）：关闭。 1 ：开启，开启后即可通过 HELLO 命令切换协议 RESP2 或 RESP3 协议。 说明 仅 Proxy 7.0.9 及以上版本支持该参数。 |
| max_session_processing | 单个连接允许堆积的最大请求个数，取值范围为[10-10000000]，默认为 1000。 代理节点转发客户端的请求给数据节点，但是未收到数据节点的回复，此时该请求即处于堆积状态。该参数主要用于限制代理节点前后端处理能力差异导致的请求堆积，避免内存上涨的问题。 |
| #no_loose_statistics-ip-enable #no_loose_statistics-cmds #no_loose_statistics-keys | 本组参数为 [可观测性能力](../product-overview/observability.md) 的一部分，设置后还需要开通 [审计日志](enable-the-new-audit-log-feature.md) 才会生效，统计周期为 5 秒/次。 #no_loose_statistics-ip-enable ：设置是否开启 IP 地址统计，即记录建连的 IP 地址，取值为 yes （开启）、 no （默认，关闭）。 #no_loose_statistics-cmds ：设置要统计的命令，统计这些命令的来源 IP 地址和频率，默认为空，即不统计。多个命令以英文逗号（,）分隔。 #no_loose_statistics-keys ：设置要统计的 Key，统计这些 Key 的来源 IP 地址和频率，默认为空，即不统计。多个 Key 以英文逗号（,）分隔。 说明 为避免影响性能， #no_loose_statistics-cmds 和 #no_loose_statistics-keys 参数中设置的值不宜设置过多，并确保仅在故障排查或运维需要时开启。 从您可以通过日志服务控制台下载审计日志（下载方法参见 [下载审计日志](download-audit-logs.md) ），然后通过关键字过滤所需信息： type 值为 7：表示 IP 地址的 QPS 统计信息。 type 值为 8：表示 IP 地址建连统计信息。 type 值为 9：表示 Key 统计信息。 type 值为 10：表示命令统计信息。 |
| ptod_enabled | 是否将客户端的 IP 地址透传到数据节点，取值： 0 ：不透传，访问数据节点的 IP 地址均为代理节点的 IP 地址。 1 （默认）：透传。 |
| readonly_lua_route_ronode_enable | 开启或关闭只读副本的 Lua 执行模式，取值： 0 （默认）：关闭 Lua 执行模式，只读副本不支持 Lua，Lua 命令会由主节点处理。 1 ：开启 Lua 执行模式，仅包含读操作的 Lua 会被转发到只读副本处理。 |
| read_request_only_ronode_whenrwsplit_enable | 开启或关闭只读账号请求定向转发，取值： 0 （默认）：关闭定向转发，只读账号的请求将按照权重分配到各节点，包括主节点。 1 ：开启定向转发，只读账号的请求将定向转发到只读副本，不会转发到主节点。 |
| rt_threshold_ms | Proxy 节点的慢日志阈值，单位为毫秒（ms），取值范围为[30-2000]，默认为 500。 如果从 Proxy 节点向数据节点发出请求后，到 Proxy 节点收到响应结束的时间超过该阈值，则会生成一条慢日志。 |
| script_check_enable | 开启或关闭代理节点对 Lua 脚本的检测，具体检查项请参见 [Proxy](../support/usage-of-lua-scripts.md) [对](../support/usage-of-lua-scripts.md) [Lua](../support/usage-of-lua-scripts.md) [的检测项](../support/usage-of-lua-scripts.md) ，取值： 0 ：不检查。若执行 Lua 的实例账号权限为只读时， 仍会开启检查。 1 （默认）：检查。 |
| sentinel_compat_enable | 在集群架构代理模式或读写分离架构，开启或关闭哨兵（Sentinel）兼容模式，可选值： 1 ：开启。 0 （默认）：关闭。 |
| transfer_subscrible_to_psubscrible_enable | 开启或关闭 SUBSCRIBE 转 PSUBSCRIBE 功能，取值： 0 （默认）：关闭，二者不转换。 1 ：开启该功能，代理节点会将 SUBSCRIBE 转换成 PSUBSCRIBE 处理。 说明 当在 Lua 中使用了 PUB 或 SUB 类命令，导致在订阅的通道无法收到通知时，可以开启该功能。 |
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
