## EXTS.S.RANGE

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.RANGE Pkey Skey fromTs toTs [MAXCOUNT count] [AGGREGATION aggregationType timeBucket] |
| 时间复杂度 | O(n)，其中 n 为目标 Datapoint 的数据块个数。 |
| 命令描述 | 在 Skey 中查询指定时间内（包含指定时间点）的 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 fromTs ：查询的开始时间（Unix 时间戳），单位为毫秒。 toTs ：查询的结束时间（Unix 时间戳），单位为毫秒，支持用 * 表示系统当前的时间戳，若该值等于 fromTs 可实现单时间点查询。 MAXCOUNT ：指定返回的 Datapoint 条数，默认为不填（Tair 的上限为 1,000,000 条）。 AGGREGATION ： aggregationType ：聚合类型，例如 MAX （最大值）、 AVG （平均值）、 SUM （求和）等，更多信息请参见 [聚合功能语法](the-tickets-command.md) 。 timeBucket ：采样间隔，单位为毫秒，最小值为 1,000 毫秒。 Tair 会将该时间范围内的数据进行聚合并返回一个结果，返回的时间点为采样间隔的开始时间。 例如 AGGREGATION AVG 5000 将返回每 5,000ms 的平均数。 |
| 返回值 | 执行成功：返回对应的 Datapoint 数据，若命令中指定了聚合，则返回聚合结果。 说明 返回结果中会额外返回一个 token 值，0 表示已全部显示，1 表示还有符合条件的 Datapoint 数据未显示。您可以根据该值，同时将已返回结果中最后一个 Datapoint 的时间戳作为开始时间继续遍历获取，轻松实现分批聚合。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.RANGE foo test 1644459031662 * AGGREGATION AVG 10000 MAXCOUNT 2 // 求指定时间点内每 10,000ms 的平均数，同时指定返回 2 条数据。 返回示例： 1) 1) 1) (integer) 1644459730000 2) "20.6" 2) 1) (integer) 1644459790000 2) "21.2" 2) (integer) 1 // 1 表示还有符合条件的 Datapoint 数据未显示，0 表示已全部显示。 |
