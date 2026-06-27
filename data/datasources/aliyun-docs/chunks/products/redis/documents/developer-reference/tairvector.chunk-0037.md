## TVS.GETDISTANCE

| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.GETDISTANCE index_name vector key_count key [ key , ...] [TOPN topN ] [FILTER filter_string ] [MAX_DIST max_distance] |
| 时间复杂度 | HNSW 算法：O(log(N)) FLAT 算法：O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，针对指定 Key 列表，进行向量（VECTOR）近邻查询。 |
| 选项 | index_name ：向量索引名称。 vector ：执行近邻查询的向量值。 key_count ：候选 Key 的数量。 key ：Key 名称，Key 的数量需要与 key_count 一致。 TOPN ：查询返回的数量，默认为 key_count ，取值范围为[1, key_count ]。 FILTER ：过滤条件。 支持 +-*/<>!=()&&|| 等操作符，暂不支持比较字符串之间的大小。如需输入字符串，请输入转义字符（\），例如 create_time > 1663637425 && location == \"Hangzhou\" 。 操作符两侧必须用空格隔开，例如 "creation_time > 1735" 。 不支持 flag == true 类型的比较，即不支持 true、false 布尔类型，可以替换为 flag == \"true\" ，当成字符串传递即可。 MAX_DIST ：最大距离限制，若某 Key 与待查询向量的距离大于该值，则会过滤，不会返回。 |
| 返回值 | 执行成功：默认按 Key 的顺序返回对应距离，若指定了 TOPN ，则按距离近到远的顺序返回近邻 Key 与对应距离。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_k 2 HNSW L2 TVS.HSET my_index_k key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_k key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_k key2 VECTOR [5,6] creation_time 1750 命令示例： TVS.GETDISTANCE my_index_k [1,1] 2 key1 key2 返回示例： 1) "key1" 2) "13" 3) "key2" 4) "41" |
