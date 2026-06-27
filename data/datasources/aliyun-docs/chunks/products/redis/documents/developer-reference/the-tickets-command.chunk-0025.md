| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.P.RANGE Pkey fromTs toTs pkeyAggregationType pkeyTimeBucket [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] FILTER filter1 [filter2 ...] |
| 时间复杂度 | O(n)，其中 n 为目标 Datapoint 的数据块个数。 |
| 命令描述 | 在 Pkey 层级对符合过滤条件（filter）的 Datapoint 数据进行聚合，若您指定了 Skey 层级的聚合，则会优先进行 Skey 层级聚合（效果与 EXTS.S.MRANGE 命令相同），再从 Pkey 层级对第一次聚合结果进行二次聚合。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 fromTs ：查询的开始时间（Unix 时间戳），单位为毫秒。 toTs ：查询的结束时间（Unix 时间戳），单位为毫秒，支持用 * 表示系统当前的时间戳，若该值等于 fromTs 可实现单时间点查询。 pkeyAggregationType ：Pkey 的聚合类型，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 pkeyTimeBucket ：Pkey 的采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 MAXCOUNT ：指定每个 Skey 返回的 Datapoint 条数，默认为不填（Tair 的上限为 1,000,000 条）。 AGGREGATION ： aggregationType ：Skey 的聚合类型，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 timeBucket ：Skey 的采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 filter ：过滤条件，您可以根据 Skey 的标签（LABELS）过滤目标 Skey，更多信息请参见 [索引过滤语法](the-tickets-command.md) 。 说明 构建 filter 时，必须存在 EQ、CONTAINS、LIST_MATCH 逻辑中的任意一个，否则会查询失败。 |
| 返回值 | 执行成功：返回聚合结果。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.P.RANGE foo 1644451031662 * SU
