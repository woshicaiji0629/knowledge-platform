的写入能力为 5 MB/s、500 次/s，读取能力为 10 MB/s、100 次/s。 每个 EventStore 中最多创建 10 个 Shard，每个 Project 中最多创建 200 个 Shard。更多信息，请参见 [分区（Shard）](shard.md) 。 |
| 自动分裂 Shard | 打开 自动分裂 Shard 开关后，如果您写入的数据量超过已有 Shard 服务能力，日志服务会自动根据数据量增加 Shard 数量。更多信息，请参见 [管理](manage-shards.md) [Shard](manage-shards.md) 。 |
| 最大分裂数 | 打开 自动分裂 Shard 开关后，最多支持自动分裂至 256 个 readwrite 状态的 Shard。 |
| 记录外网 IP | 打开 记录外网 IP 开关后，日志服务自动把以下信息添加到日志的 Tag 字段中。 __client_ip__ ：日志来源设备的公网 IP 地址。 __receive_time__ ：日志到达服务端的时间，格式为 Unix 时间戳，表示从 1970-1-1 00:00:00 UTC 计算起的秒数。 |
