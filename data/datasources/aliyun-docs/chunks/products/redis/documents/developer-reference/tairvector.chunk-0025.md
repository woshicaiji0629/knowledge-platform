## TVS.HPEXPIRE

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HPEXPIRE index_name key milliseconds-timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到毫秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 milliseconds-timestamp ：相对过期时间，单位为毫秒。 |
| 返回值 | key 存在且设置成功：1。 key 不存在：0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPEXPIRE index_name0 key1 1000 返回示例： (integer) 1 |
