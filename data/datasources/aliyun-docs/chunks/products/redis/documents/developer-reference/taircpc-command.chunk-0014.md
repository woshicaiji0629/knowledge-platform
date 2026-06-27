## CPC.ARRAY.ESTIMATE.RANGE

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.ESTIMATE.RANGE key start_time end_time |
| 时间复杂度 | O(1) |
| 命令描述 | 获取指定 TairCpc 的指定时间段内（包含指定时间点）各个时间窗口的基数估算值。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 start_time ：查询的开始时间（Unix 时间戳），单位为毫秒。 end_time ：查询的结束时间（Unix 时间戳），单位为毫秒。 |
| 返回值 | 执行成功：返回目标时间窗口的基数估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.ESTIMATE.RANGE foo 1645584510000 1645584550000 返回示例： 1) "2" 2) "0" 3) "1" 4) "0" 5) "0" |
