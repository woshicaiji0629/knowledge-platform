| 参数 | 数据类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要创建的 LogStore 名称。 |
| queryMode | string | 否 | [LogStore](manage-a-logstore.md) [规格对比](manage-a-logstore.md) 。默认值为 standard ，可选值： query ：查询型 LogStore。 standard ：标准型 LogStore。 |
| ttl | int | 否 | [数据保留天数](manage-a-logstore.md) （1~3650）默认 30，3650 表示永久。 |
| hotTtl | int | 否 | [热数据存储时间](data-tiered-storage-overview.md) （以天为单位）。默认 0，需要小于 ttl 且大于等于 7。 |
| infrequentAccessTTL | int | 否 | 目标 LogStore 的 [低频存储时间](data-tiered-storage-overview.md) （以天为单位）。默认值为 0，需要 hotTtl 存在、小于 ttl 且大于等于 30，如果 hotTtl+infrequentAccessTTL 不等于 ttl，还需要 ttl-(hotTtl+infrequentAccessTTL)>=60 。该参数需要 loongcollector-operator 组件版本号大于等于 1.0.6 有效。 |
| shardCount | int | 否 | Shard 数量。默认值为 2，取值范围为 1~100。 |
| maxSplitShard | int | 否 | 最大自动分裂 Shard 数量。默认值为 64，取值范围为 1~256。 |
| autoSplit | bool | 否 | 是否开启自动分裂 Shard。默认值为 true。 |
| telemetryType | string | 否 | 可观测数据类型。默认值为 None，可选值： None ：日志数据。 Metrics ：时序数据。 |
| appendMeta | bool | 否 | 是否记录外网 IP 地址和日志接收时间。默认值为 true。 true ：开启记录外网 IP 和日志接收时间功能，开启后日志服务自动把日志来源设备的公网 IP 地址和日志到达服务端的时间添加到日志的 Tag 字段中。 false ：不开启记录外网 IP 和日志接收时间功能。 |
| enableTracking | bool | 否 | 是否启用 WebTracking 功能。默认值为 false。 |
| encryptConf | obje
