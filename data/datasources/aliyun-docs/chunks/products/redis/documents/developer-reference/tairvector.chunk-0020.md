## TVS.HDEL

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HDEL index_name key attribute_key [ attribute_key ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 在向量索引的数据记录（ key ）中，删除指定的 attribute_key 与其数值。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识，支持指定多个。 attribute_key ：待操作的属性 Key，支持指定多个。若需删除向量数据，需传入 VECTOR 关键字（必须大写）。若需删除全量索引数据，需传入 TEXT 关键字（必须大写）。 |
| 返回值 | 执行成功：删除指定数据，并返回删除 attribute_key 的数量。 若指定索引不存在，返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HDEL index_name0 keyc VECTOR 返回示例： (integer) 1 |
