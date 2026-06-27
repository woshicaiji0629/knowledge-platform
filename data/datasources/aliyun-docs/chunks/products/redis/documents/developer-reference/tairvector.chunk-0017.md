## TVS.HGETALL

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HGETALL index_name key |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定向量索引中的 key 对应的所有数据记录。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 |
| 返回值 | 执行成功：返回该 key 的所有数据记录。 若指定的向量索引或 key 不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HGETALL index_name0 key0 返回示例： 1) "VECTOR" 2) "[1,2]" 3) "location" 4) "Hangzhou" 5) "create_time" 6) "1663637425" |
