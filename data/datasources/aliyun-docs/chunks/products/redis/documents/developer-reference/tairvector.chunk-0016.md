## TVS.HSET

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HSET index_name key attribute_key attribute_value [ attribute_key attribute_value ] ... |
| 时间复杂度 | 若本次插入、更新数据无需创建或更新向量值，则时间复杂度为 O(1)；否则时间复杂度为 O(log(N))，N 为该向量索引中 Key 的数量。 |
| 命令描述 | 往向量索引中插入数据记录（ key ），若该记录已存在则更新并覆盖原记录。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识，该对象可通过 TVS.DEL 命令删除。 attribute_key 和 attribute_value ：该条记录的数值，为 Key-value 格式。 插入向量数据：需要将 attribute_key 设置为 VECTOR 关键字（必须大写），对应的 attribute_value 则需要为该向量索引指定维度（ dims ）的向量数据字符串，例如 VECTOR [1,2] 。一个 Key 仅支持写入一个 VECTOR 数据，若重复写入会更新并覆盖原数据。 插入文本数据：在创建索引时已制定 HybridIndex 相关参数，需要将 attribute_key 设置为 TEXT 关键字（必须大写），对应的 attribute_value 可以是文本格式（Text），例如 "TairVector 是 Tair 自研的向量数据库服务" ，也可以是向量化（Embedding）后的数据，例如 "[[2,0.221],[42,09688],...]" 。 插入其他属性：可以自定义额外属性或信息，例如 create_time 1663637425 （创建时间）、 location Hangzhou （地点）等。 |
| 返回值 | 执行成功：返回新增的数据记录数量，若更新已有的字段则返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HSET my_index key5 VECTOR [7,8] TEXT "TairVector 是 Tair 自研的向量数据库服务" create_time 1800 返回示例： (integer) 3 |
