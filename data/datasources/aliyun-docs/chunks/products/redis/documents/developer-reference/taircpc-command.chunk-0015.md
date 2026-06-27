## CPC.ARRAY.ESTIMATE.RANGE.MERGE

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.ESTIMATE.RANGE.MERGE key timestamp range |
| 时间复杂度 | O(1) |
| 命令描述 | 获取指定 TairCpc 在指定时间点至往前 range（含当前窗口）个时间窗口内，时间窗口合并、去重后的基数估算值。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：查询的开始时间（Unix 时间戳），单位为毫秒。 range ：查询的时间窗口个数。 |
| 返回值 | 执行成功：返回目标 key 在指定时间段内去重后的基数估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.ESTIMATE.RANGE.MERGE foo 1645584510000 3 返回示例： "6" |
