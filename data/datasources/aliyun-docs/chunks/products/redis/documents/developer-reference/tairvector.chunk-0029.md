## TVS.HTTL

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HTTL index_name key |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，查看指定数据记录（ key ）的剩余过期时间，精确到秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 |
| 返回值 | key 存在且设置了过期时间：剩余过期时间，单位为秒。 key 存在但未设置过期时间：-1。 key 或 index_name 不存在：-2。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HTTL index_name0 key2 返回示例： (integer) 58 |
