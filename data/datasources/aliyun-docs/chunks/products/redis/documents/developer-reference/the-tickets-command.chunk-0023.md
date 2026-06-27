| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.MRANGE Pkey fromTs toTs [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] [WITHLABELS] FILTER filter1 [filter2 ...] |
| 时间复杂度 | O(n)，其中 n 为目标 Datapoint 的数据块个数。 |
| 命令描述 | 在 Skey 中自定义过滤条件（filter）与查询时间点（包含指定时间点），查询目标 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 fromTs ：查询的开始时间（Unix 时间戳），单位为毫秒。 toTs ：查询的结束时间（Unix 时间戳），单位为毫秒，支持用 * 表示系统当前的时间戳，若该值等于 fromTs 可实现单时间点查询。 MAXCOUNT ：指定每个 Skey 返回的 Datapoint 条数，默认为不填（Tair 的上限为 1,000,000 条）。 AGGREGATION ： aggregationType ：聚合类型，例如 MAX （最大值）、 AVG （平均值）、 SUM （求和）等，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 timeBucket ：采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 WITHLABELS ：设置返回结果中是否包含标签信息，默认为不填（不显示标签信息）。 filter ：过滤条件，您可以根据 Skey 的标签（LABELS）过滤目标 Skey，更多信息请参见 [索引过滤语法](the-tickets-command.md) 。 说明 构建 filter 时，必须存在 EQ、CONTAINS、LIST_MATCH 逻辑中的任意一个，否则会查询失败。 |
| 返回值 | 执行成功：返回符合过滤条件的 Skey 组信息。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.MRANGE foo 1644451031662 * AGGREGATION MAX 10000 WITHLABELS FILTER sensor_id=1 返回示例： 1) 1) "temperature" 2) 1) 1) "sensor_id" 2) "1" 3) 1) 1) (integer) 1644481000000 2) "30" 4) (integer) 0 2) 1) "test" 2) 1)
