| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.GETINDEX index_name |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定的向量索引，获取该向量索引的元数据信息。 |
| 选项 | index_name ：向量索引名称。 |
| 返回值 | 执行成功：返回该向量索引的元数据信息。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index 2 HNSW L2 auto_gc true lexical_algorithm bm25 TVS.HSET my_index key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index key2 VECTOR [5,6] creation_time 1750 命令示例（以 HNSW 算法的向量索引为例）： TVS.GETINDEX my_index 返回示例： 1) "lexical_term_count" // 全文索引分词数，Int 类型。 2) "0" 3) "lexical_record_count" // 全文索引文档数，Int 类型。 4) "0" 5) "lexical_algorithm" // 全文索引算法。 6) "bm25" 7) "auto_gc" // HNSW 算法模式下，是否开启自动回收索引空间。 8) "1" 9) "dimension" // 向量维度。 10) "2" 11) "attribute_data_size" // 属性信息内存占用（单位：字节）。 12) "3720" 13) "distance_method" // 向量距离函数。 14) "L2" 15) "data_type" // 向量数据类型。 16) "FLOAT32" 17) "algorithm" // 索引算法。 18) "HNSW" 19) "index_data_size" // 向量数据内存占用（单位：字节）。 20) "105128040" 21) "M" // HNSW 算法模式下，图索引结构中，每一层的最大出边数量。 22) "16" 23) "data_count" // 用户记录数。 24) "3" 25) "current_record_count" // 总向量数。 26) "3" 27) "ef_construct" // HNSW 算法模式下，动态列表的长度。 28) "100" 29) "inverted_index_productname" //
