## TVS.HMGET

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HMGET index_name key attribute_key [ attribute_key ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定向量索引的 key 中对应的 attribute_key 所对应的数值。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 attribute_key ：待操作的属性 Key，支持指定多个。若需查询向量数据，需传入 VECTOR 关键字（必须大写）。若需查询全文索引中原生文本数据，需传入 TEXT 关键字（必须大写）。 |
| 返回值 | 执行成功：返回 attribute_key 对应的数值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HMGET index_name0 key0 create_time location VECTOR TEXT 返回示例： 1) "1800" 2) "[7,8]" 3) "TairVector 是 Tair 自研的向量数据库服务" |
