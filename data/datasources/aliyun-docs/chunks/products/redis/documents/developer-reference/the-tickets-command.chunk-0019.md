## EXTS.S.GET

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.GET Pkey Skey |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定 Skey 中最新的 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 |
| 返回值 | 执行成功：返回对应的 Datapoint 数据。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.GET foo temperature 返回示例： 1) (integer) 1644372730150 2) "32.2" |
