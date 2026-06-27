## TVS.HINCRBY

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HINCRBY index_name key attribute_key num |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，将指定数据记录（ key ）的 attribute_key 的值增加 num，num 为一个整数。 若指定的 attribute_key 不存在则自动新建并赋予该值，若该记录已存在则更新并覆盖原值。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 attribute_key ：待操作的属性 Key。 num ：需要为 attribute_key 的 value 增加的整数值。 |
| 返回值 | 执行成功：添加 num 后的值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HINCRBY index_name0 key0 tv01 20 返回示例： (integer) 20 |
