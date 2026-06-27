## EXTS.S.DEL

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.DEL Pkey Skey |
| 时间复杂度 | O(1) |
| 命令描述 | 删除指定 Pkey 中的单个 Skey，并删除目标 Skey 中所有的 Datapoint 数据。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.DEL foo temperature 返回示例： OK |
