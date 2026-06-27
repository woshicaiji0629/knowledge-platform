## EXTS.S.QUERYINDEX

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.QUERYINDEX Pkey filter1 [filter2 ...] |
| 时间复杂度 | O(n)，其中 n 为过滤条件中的最大集合数。 |
| 命令描述 | 在 Pkey 中自定义过滤条件（filter），查询目标 Skey。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 filter ：过滤条件，您可以根据 Skey 的标签（LABELS）过滤目标 Skey，更多信息请参见 [索引过滤语法](the-tickets-command.md) 。 说明 构建 filter 时，必须存在 EQ、CONTAINS、LIST_MATCH 逻辑中的任意一个，否则会查询失败。 |
| 返回值 | 执行成功：返回符合过滤条件的 Skey。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.QUERYINDEX foo sensor_id=1 返回示例： 1) "temperature" |
