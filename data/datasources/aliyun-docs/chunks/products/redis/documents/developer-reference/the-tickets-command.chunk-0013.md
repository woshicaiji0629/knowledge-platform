## EXTS.S.ALTER

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.ALTER Pkey Skey [DATA_ET time] |
| 时间复杂度 | O(1) |
| 命令描述 | 修改指定 Skey 的元数据信息，当前仅支持修改过期时间（DATA_ET）。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.ALTER foo temperature DATA_ET 100000 返回示例： OK |
