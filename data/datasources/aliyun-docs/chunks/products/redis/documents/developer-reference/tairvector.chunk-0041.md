| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.MINDEXKNNSEARCHFIELD index_count index_name [index_name ...] topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：index_count * O(log(N)) FLAT 算法：index_count * O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在多个向量索引中，对指定的向量（VECTOR）进行近邻查询，支持返回标签属性。 |
| 选项 | index_count ：向量索引的数量。 index_name ：向量索引名称。 topN ：查询返回的数量，取值范围为[1,10000]，默认会查询出每个向量索引的 topN 个结果，并将所有查询结果进行聚合，返回距离最近的 topN 个结果。 vector ：执行近邻查询的向量值。 field_count ：返回结果中标签属性的数量，若希望返回所有标签，可以设置 field_count 为 0。 field_name ：标签名称，数量需要与 field_count 保持一致。 filter_string ：过滤条件，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 param_key 和 param_value ：查询的运行参数，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 |
| 返回值 | 执行成功：按距离近到远的顺序返回近邻的 key 及与该目标向量的距离，以及对应的标签属性键值对。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_mk 2 HNSW L2 TVS.HSET my_index_mk key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_mk key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_mk key2 VECTOR [5,6] creation_time 1750 TVS.CREATEINDEX my_index_mx 2 HNSW L2 TVS.HSET my_index_mx key5 VECTOR [8,7] creation_time 1730 TVS.HSET my_index_mx key6 VECTOR [6,5] c
