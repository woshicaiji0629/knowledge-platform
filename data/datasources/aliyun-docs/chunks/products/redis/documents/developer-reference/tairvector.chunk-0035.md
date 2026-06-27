| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.KNNSEARCHFIELD index_name topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：O(log(N)) FLAT 算法：O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，对指定的向量（VECTOR）进行近邻查询，检索逻辑与 TVS.KNNSEARCH 相同，额外支持返回标签属性。 |
| 选项 | index_name ：向量索引名称。 topN ：查询返回的数量，取值范围为[1,10000]。 vector ：执行近邻查询的向量值。若您仅希望执行全文检索（索引为混合索引），可在该字段传入 "" 。 field_count ：返回结果中标签属性的数量，若希望返回所有标签，可以设置 field_count 为 0。 field_name ：标签名称，数量需要与 field_count 保持一致。 filter_string ：过滤条件，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 param_key 和 param_value ：查询的运行参数，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 |
| 返回值 | 执行成功：按距离近到远的顺序返回近邻的 key 及与该目标向量的距离，以及对应的标签属性键值对。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_k 2 HNSW L2 TVS.HSET my_index_k key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_k key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_k key2 VECTOR [5,6] creation_time 1750 命令示例： TVS.KNNSEARCHFIELD my_index_k 2 [3,3.1] 0 "creation_time > 1735" 返回示例： 1) 1) "key1" 2) "0.81000018119812012" 3) "VECTOR" 4) "[3,4]" 5) "creation_time" 6) "1740" 2) 1) "key2" 2) "12.410000801086426" 3) "VECTOR" 4) "
