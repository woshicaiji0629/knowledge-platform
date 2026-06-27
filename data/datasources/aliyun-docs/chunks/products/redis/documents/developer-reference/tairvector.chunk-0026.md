## TVS.HEXPIREAT

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HEXPIREAT index_name key timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，为指定数据记录（ key ）设置绝对过期时间，精确到秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 timestamp ：精确到秒的 UNIX 时间戳 （Unix timestamp）。若该时间早于当前时间，则该 key 会立即过期。 |
| 返回值 | key 存在且设置成功：1。 key 不存在：0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPEXPIREAT index_name0 key2 1691466981 返回示例： (integer) 1 |
