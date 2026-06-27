hash-max-ziplist-entries hash-max-ziplist-value | 兼容 Redis 6.0 及以下版本，默认使用 ziplist 作为 Hash 的编码方式。当 Hash 对象同时满足以下两个条件时， 使用 ziplist 编码。 Hash 的键值对数量小于 hash-max-ziplist-entries 的值。 Hash 的键和值的字符串长度都小于 hash-max-ziplist-value 。 | ❌ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| hash-max-listpack-entries hash-max-listpack-value | 兼容 Redis 7.0 版本起，默认使用 listpack 作为 Hash 的编码方式。当 Hash 对象同时满足以下两个条件时， 使用 listpack 编码。 Hash 的键值对数量小于 hash-max-listpack-entries 的值。 Hash 的键和值的字符串长度都小于 hash-max-listpack-value 。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| hz | 设置实例后台任务执行频率，例如清除过期键任务。取值范围为[1-500]，默认为 10，即每秒执行 10 次。 说明 该值越大，CPU 资源消耗越多，但在过期键较多的情况下清理频率也更高，同时实例能够更精确地处理超时。建议取值不超过 100。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ |
| latency-tracking | 是否开启命令时延监控，取值： yes （默认）：开启。 no ：不开启。 说明 仅兼容 Redis 7.0 及以上支持该参数。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ | ❌ | ❌ | ❌ |
| lazyfree-lazy-eviction | 是否开启基于 lazyfree 的驱逐功能，取值： yes ：开启。 no （默认）：不开启。 | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | 标准️️✔️ 集群✔️️️️️ 读写分离✔️ | ❌ |
| lazyfree-lazy-expire | 是否开启基于 lazyfree
