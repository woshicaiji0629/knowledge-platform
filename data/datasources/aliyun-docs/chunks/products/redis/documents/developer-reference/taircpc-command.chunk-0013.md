## CPC.ARRAY.ESTIMATE

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.ESTIMATE key timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 获取指定 TairCpc 中目标 timestamp 所在时间窗口的基数估算值。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：指定的 Unix 时间戳，单位为毫秒。 |
| 返回值 | 执行成功：返回对应时间窗口的基数估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.ESTIMATE foo 1645584532000 返回示例： "2" |
