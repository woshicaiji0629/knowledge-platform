# 什么是TairVector-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/developer-reference/tairvector

# Vector
TairVector是Tair自研的扩展数据结构，提供高性能、实时，集存储、检索于一体的向量数据库服务。
## TairVector简介
TairVector采用多层Hash的数据结构，如下所示：TairVector提供了HNSW（Hierarchical Navigable Small World）和暴力搜索（Flat Search）两种索引算法：
HNSW：以图结构构建向量检索的索引，支持异步空间回收，可以在保证高查询精度的同时，均衡实时更新的性能表现。
暴力搜索：具有100%查询精度，插入数据速度快，适用于小规模数据集。
同时，TairVector支持欧式距离（Euclidean distance）、向量内积（Internal product）、余弦距离（Cosine distance）和Jaccard距离（Jaccard distance）等多种距离函数。相对于传统的向量检索服务，TairVector的优势如下：
所有数据均在内存中，支持实时更新索引，具有更短的读写时延。
优化内存数据结构，占用空间更小。
开箱即用，以云服务的方式整体申请即可使用，整体架构简单高效，没有复杂组件依赖。
支持向量检索与全文检索组合的混合检索。
支持创建标量（标签属性等）倒排索引，并提供先标量后向量的KNN检索特性。
发布记录
2022年10月13日随Tair内存型（兼容Redis 6.0）首次发布TairVector。
2022年11月22日发布6.2.2.0版本，新增支持Jaccard距离函数、TVS.GETINDEX命令支持统计每个索引的内存占用（index_data_size和attribute_data_size）。
2022年12月26日发布6.2.3.0版本，支持集群代理模式，新增FLOAT16的向量数据类型，新增TVS.MINDEXKNNSEARCH、TVS.MINDEXMKNNSEARCH命令。
2023年07月04日发布6.2.8.2版本，支持余弦距离、支持HNSW索引垃圾自动回收。
2023年08月03日发布23.8.0.0版本，支持对Index中的key级别设置TTL（新增TVS.HEXPIREAT、TVS.HPEXPIREAT等命令），支持对指定Key列表进行向量近邻查询（新增TVS.GETDISTANCE命令），支持全文检索（更新TVS.CREATEINDEX、TVS.KNNSEARCH等命令），可以实现向量检索与全文检索组合的混合检索。
2024年06月06日发布24.5.1.0版本，新增TVS.KNNSEARCHFIELD、TVS.MINDEXKNNSEARCHFIELD命令，支持在近邻查询时返回标签属性信息。
2024年07月22日发布24.7.0.0版本，支持在稀疏向量中使用HNSW索引。
## 最佳实践
[基于](../use-cases/building-enterprise-specific-chatbot-based-on-tair-and-llm.md)[Tair](../use-cases/building-enterprise-specific-chatbot-based-on-tair-and-llm.md)[向量检索与](../use-cases/building-enterprise-specific-chatbot-based-on-tair-and-llm.md)[LLM](../use-cases/building-enterprise-specific-chatbot-based-on-tair-and-llm.md)[构建企业专属](../use-cases/building-enterprise-specific-chatbot-based-on-tair-and-llm.md)[Chatbot](../use-cases/building-enterprise-specific-chatbot-based-on-tair-and-llm.md)
[TairVector](../use-cases/tairvector-hybrid-retrieval-practice.md)[实现全文+向量混合检索实践](../use-cases/tairvector-hybrid-retrieval-practice.md)
[基于](../use-cases/realization-of-multi-modal-retrieval-based-on-tair-vector.md)[TairVector](../use-cases/realization-of-multi-modal-retrieval-based-on-tair-vector.md)[实现图文多模态向量检索](../use-cases/realization-of-multi-modal-retrieval-based-on-tair-vector.md)
[基于](../use-cases/implement-approximate-query-for-molecular-geometries-by-using-tairvector.md)[TairVector](../use-cases/implement-approximate-query-for-molecular-geometries-by-using-tairvector.md)[向量引擎实现分子结构近似检索](../use-cases/implement-approximate-query-for-molecular-geometries-by-using-tairvector.md)
## 前提条件
实例的存储介质为[内存型](../product-overview/dram-based-instances.md)（兼容Redis 6.0及以上）。
说明
内存型（兼容Redis 5.0）实例暂不支持升级至内存型（兼容Redis 6.0），如需使用请新建实例。
## 注意事项
操作对象为Tair实例中的TairVector数据。
TairVector数据结构的index_name、Key等暂不支持Redis的Hashtags特性。
TairVector暂不支持MOVE等特性。
若业务场景对数据持久化要求较高，建议开启[半同步模式](../user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance.md)。
## 命令列表
表 1.TairVector命令
| 类型 | 命令 | 语法 | 说明 |
| --- | --- | --- | --- |
| 索引元数据操作 | [TVS.CREATEINDEX](tairvector.md) | TVS.CREATEINDEX index_name dims algorithm distance_method [ algo_param_key alog_param_value ] ... | 创建一个向量索引空间，同时指定构建索引和查询的具体算法，以及距离函数。该对象仅能通过 TVS.DELINDEX 命令删除。 |
| [TVS.GETINDEX](tairvector.md) | TVS.GETINDEX index_name | 查询指定的向量索引，获取该向量索引的元数据信息。 |  |
| [TVS.DELINDEX](tairvector.md) | TVS.DELINDEX index_name | 删除指定的向量索引及该索引内的所有数据。 |  |
| [TVS.SCANINDEX](tairvector.md) | TVS.SCANINDEX cursor [MATCH pattern ] [COUNT count ] | 扫描 Tair 实例中所有符合条件的向量索引。 |  |
| 向量数据操作 | [TVS.HSET](tairvector.md) | TVS.HSET index_name key attribute_key attribute_value [ attribute_key attribute_value ] ... | 往向量索引中插入数据记录（ key ），若该记录已存在则更新并覆盖原记录。 |
| [TVS.HGETALL](tairvector.md) | TVS.HGETALL index_name key | 查询指定向量索引中的 key 对应的所有数据记录。 |  |
| [TVS.HMGET](tairvector.md) | TVS.HMGET index_name key attribute_key [ attribute_key ...] | 查询指定向量索引的 key 中对应的 attribute_key 所对应的数值。 |  |
| [TVS.DEL](tairvector.md) | TVS.DEL index_name key [ key ...] | 在指定向量索引中，删除指定数据记录（ key ）。 |  |
| [TVS.HDEL](tairvector.md) | TVS.HDEL index_name key attribute_key [ attribute_key ...] | 在向量索引的数据记录（ key ）中，删除指定的 attribute_key 与其数值。 |  |
| [TVS.SCAN](tairvector.md) | TVS.SCAN index_name cursor [MATCH pattern ] [COUNT count ] [FILTER filter_string] [VECTOR vector] [MAX_DIST max_distance] | 在指定向量索引中，扫描符合条件的数据记录（ key ）。 |  |
| [TVS.HINCRBY](tairvector.md) | TVS.HINCRBY index_name key attribute_key num | 在指定向量索引中，将指定数据记录（ key ）的 attribute_key 的值增加 num，num 为一个整数。 |  |
| [TVS.HINCRBYFLOAT](tairvector.md) | TVS.HINCRBYFLOAT index_name key attribute_key num | 在指定向量索引中，将指定数据记录（ key ）的 attribute_key 的值增加 num，num 为一个浮点数。 |  |
| [TVS.HPEXPIREAT](tairvector.md) | TVS.HPEXPIREAT index_name key milliseconds-timestamp | 在指定向量索引中，为指定数据记录（ key ）设置绝对过期时间，精确到毫秒。 |  |
| [TVS.HPEXPIRE](tairvector.md) | TVS.HPEXPIRE index_name key milliseconds-timestamp | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到毫秒。 |  |
| [TVS.HEXPIREAT](tairvector.md) | TVS.HEXPIREAT index_name key timestamp | 在指定向量索引中，为指定数据记录（ key ）设置绝对过期时间，精确到秒。 |  |
| [TVS.HEXPIRE](tairvector.md) | TVS.HEXPIRE index_name key timestamp | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到秒。 |  |
| [TVS.HPTTL](tairvector.md) | TVS.HPTTL index_name key | 在指定向量索引中，查看指定数据记录（ key ）的剩余过期时间，精确到毫秒。 |  |
| [TVS.HTTL](tairvector.md) | TVS.HTTL index_name key | 在指定向量索引中，查看指定数据记录（ key ）的剩余过期时间，精确到秒。 |  |
| [TVS.HPEXPIRETIME](tairvector.md) | TVS.HPEXPIRETIME index_name key | 在指定向量索引中，查看指定数据记录（ key ）的绝对过期时间，精确到毫秒。 |  |
| [TVS.HEXPIRETIME](tairvector.md) | TVS.HEXPIRETIME index_name key | 在指定向量索引中，查看指定数据记录（ key ）的绝对过期时间，精确到秒。 |  |
| 向量近邻查询 | [TVS.KNNSEARCH](tairvector.md) | TVS.KNNSEARCH index_name topN vector [filter_string] [param_key param_value] | 在指定向量索引中，对指定的向量（VECTOR）进行近邻查询，最多可返回 topN 条。 |
| [TVS.KNNSEARCHFIELD](tairvector.md) | TVS.KNNSEARCHFIELD index_name topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] | 在指定向量索引中，对指定的向量（VECTOR）进行近邻查询，检索逻辑与 TVS.KNNSEARCH 相同，额外支持返回标签属性。 |  |
| [TVS.GETDISTANCE](tairvector.md) | TVS.GETDISTANCE index_name vector key_count key [ key , ...] [TOPN topN ] [FILTER filter_string ] [MAX_DIST max_distance] | 在指定向量索引中，针对指定 Key 列表，进行向量（VECTOR）近邻查询。 |  |
| [TVS.MKNNSEARCH](tairvector.md) | TVS.MKNNSEARCH index_name topN vector_count vector [vector ...] [filter_string] [param_key param_value] | 在指定向量索引中，批量对多条向量（VECTOR）进行近邻查询。 |  |
| [TVS.MINDEXKNNSEARCH](tairvector.md) | TVS.MINDEXKNNSEARCH index_count index_name [index_name ...] topN vector [filter_string] [param_key param_value] | 在多个向量索引中，对指定的向量（VECTOR）进行近邻查询。 |  |
| [TVS.MINDEXKNNSEARCHFIELD](tairvector.md) | TVS.MINDEXKNNSEARCHFIELD index_count index_name [index_name ...] topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] | 在多个向量索引中，对指定的向量（VECTOR）进行近邻查询，支持返回标签属性。 |  |
| [TVS.MINDEXMKNNSEARCH](tairvector.md) | TVS.MINDEXMKNNSEARCH index_count index_name [index_name ...] topN vector_count vector [vector ...] [filter_string] [param_key param_value] | 在多个向量索引中，批量对多条向量（VECTOR）进行近邻查询。 |  |
| 通用 | [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairVector 数据。 |
说明
本文的命令语法定义如下：
大写关键字：命令关键字。
斜体：变量。
[options]：可选参数，不在括号中的参数为必选。
A|B：该组参数互斥，请进行二选一或多选一。
...：前面的内容可重复。
## TVS.CREATEINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.CREATEINDEX index_name dims algorithm distance_method [ algo_param_key alog_param_value ] ... |
| 时间复杂度 | O(1) |
| 命令描述 | 创建一个向量索引空间，同时指定构建索引和查询的具体算法，以及距离函数。该对象仅能通过 TVS.DELINDEX 命令删除。 |
| 选项 | index_name ：向量索引名称。 dims ：向量维度，插入该索引的向量需具有相同的向量维度，取值范围为[1, 32768]。 algorithm ：构建、查询索引的算法，取值如下： FLAT ：不单独构建索引，采用暴力搜索的方式执行查询，适合 1 万条以下的小规模数据集。 HNSW ：采用 HNSW 图结构构建整个索引，并通过该算法进行查询，适合大规模的数据集。 distance_method ：计算向量距离函数，取值如下： L2 ：平方欧氏距离。 IP ：向量内积，距离值为 1-向量内积 。 COSINE ：余弦距离，距离值为 1-向量余弦值 。使用余弦距离会将写入的向量转化为单元向量（L2 正则化），因此查询得到的向量结果可能不是原始向量值。 JACCARD ：Jaccard 距离，距离值为 1-Jaccard 系数 ，且需指定向量数据类型（ data_type ）为 BINARY 。 algo_param_key 和 alog_param_value ： data_type ：（稠密）向量的数据类型，取值说明如下。 FLOAT32 （默认）：4 字节的单精度浮点数。 FLOAT16 ：2 字节的半精度浮点数（IEEE 754-2008 标准），可节省向量存储空间，但会损失一定的精度， FLOAT16 能表示的最大数值范围为[-65519, 65519]。 BINARY ：二进制向量，仅能包含 0 或 1，仅支持 Jaccard 距离函数。 HNSW 索引的特定参数，取值说明如下： ef_construct ：使用 HNSW 算法构建索引时，动态列表的长度。默认为 100，取值范围为[1,1000]，该值越大则 ANN 查询精度越高，同时性能开销越大。 M ：图索引结构中，每一层的最大出边数量。默认为 16，取值范围为[1,100]。该值越大则 ANN 查询精度越高，同时性能开销越大。 auto_gc ：自动回收索引空间，取值为 false （默认，表示关闭）、 true （表示开启），该功能要求实例的小版本为 6.2.8.2 及以上。HNSW 索引的向量删除采用标记删除的方式，开启该功能后，支持索引空间的自动回收，可有效降低内存占用，但该功能会影响该索引近邻查询的性能，推荐对内存占用量敏感的场景使用该功能。 HybridIndex （混合索引）的特定参数，取值说明如下： 如需对指定标签字段创建倒排索引，需提前指定字段名称与对应的数据类型。 语法为 inverted_index_<field_name> int|long|float|double|string ，对 field_name 字段建立倒排索引，支持的类型为 Int、Long、Float、Double 和 String， field_name 字段和数据类型关键字需小写。 例如希望对 productname 字段（String 类型）创建倒排索引的示例为 inverted_index_productname string 。 lexical_algorithm ：全文检索算法。 bm25 ：BM25（Okapi BM25）算法，适用于全文检索 后续 TVS.HSET 写入时，attribute_key 为 TEXT 关键字（必须大写），对应的 attribute_value 会自动建全文索引。 您可传入原始文本，由 Tair 向量服务构建索引。 vector ：Vector 算法，适用于稀疏向量。 您需要对原始文本进行编码（Embedding），传入稀疏向量。数据格式为 "[[2,0.221],[42,09688],...]" ，其中 Key 为 Indices ，类型为 uint32_t ，Value 为该 Index 的词频概览，类型为 Float。 若 lexical_algorithm 设置为 bm25 ，您还可以设置如下参数。 analyzer ：分词器，当前支持 jieba （默认）、 ik_smart 。 k1 ：BM25 算法中控制词频饱和度，默认为 1.2，取值范围需大于 0。 b ：BM25 算法中控制文档长度的影响，默认为 0.75，取值范围为[0,1]。 若 lexical_algorithm 设置为 vector ，您还可以设置如下参数。 lexical_use_hnsw ：稀疏向量是否使用 HNSW 索引，取值：1（使用 HNSW 索引）、0（默认，使用倒排索引）。 lexical_hnsw_m ：当 lexical_use_hnsw 为 1 时，该参数为 HNSW 索引的 M 参数，作用与说明请参见 HNSW 索引的特定参数 。 lexical_hnsw_ef_construct ：当 lexical_use_hnsw 为 1 时，该参数为 HNSW 索引的 ef_construct 参数，作用与说明请参见 HNSW 索引的特定参数 。 hybrid_ratio ：该索引在查询时向量检索的默认权重，默认为 0.5，取值范围为[0,1]，Float 类型，全文检索的权重为 1-hybrid_ratio 。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： # 创建向量存储结构：向量维度为 2、索引类型为 HNSW、距离函数为 Jaccard、向量数据类型为 BINARY。 TVS.CREATEINDEX index_name0 2 HNSW JACCARD data_type BINARY # 创建向量存储结构：向量维度为 2、索引类型为 HNSW、距离函数为 L2、向量数据类型为 FLOAT32。 TVS.CREATEINDEX index_name1 2 HNSW L2 # 创建向量存储结构：向量维度为 2、索引类型为 FLAT、距离函数为 IP、向量数据类型为 FLOAT32。 TVS.CREATEINDEX index_name2 2 FLAT IP # 创建向量存储结构：向量维度为 2、索引类型为 FLAT、距离函数为 Jaccard、向量数据类型为 BINARY。 TVS.CREATEINDEX index_name3 2 FLAT JACCARD data_type BINARY # 创建向量存储结构：向量维度为 2、索引类型为 HNSW、距离函数为 IP、向量数据类型为 FLOAT32、全文检索算法为 BM25，指定 productname 字段（String 类型）为倒排索引。 TVS.CREATEINDEX index_name4 2 HNSW IP lexical_algorithm bm25 inverted_index_productname string # 创建稀疏向量存储结构：向量维度为 2、距离函数为 IP、使用 HNSW 索引。 TVS.CREATEINDEX index_name5 2 HNSW IP lexical_algorithm vector lexical_use_hnsw 1 lexical_hnsw_m 8 lexical_hnsw_ef_construct 100 返回示例均为如下： OK |
## TVS.GETINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.GETINDEX index_name |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定的向量索引，获取该向量索引的元数据信息。 |
| 选项 | index_name ：向量索引名称。 |
| 返回值 | 执行成功：返回该向量索引的元数据信息。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index 2 HNSW L2 auto_gc true lexical_algorithm bm25 TVS.HSET my_index key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index key2 VECTOR [5,6] creation_time 1750 命令示例（以 HNSW 算法的向量索引为例）： TVS.GETINDEX my_index 返回示例： 1) "lexical_term_count" // 全文索引分词数，Int 类型。 2) "0" 3) "lexical_record_count" // 全文索引文档数，Int 类型。 4) "0" 5) "lexical_algorithm" // 全文索引算法。 6) "bm25" 7) "auto_gc" // HNSW 算法模式下，是否开启自动回收索引空间。 8) "1" 9) "dimension" // 向量维度。 10) "2" 11) "attribute_data_size" // 属性信息内存占用（单位：字节）。 12) "3720" 13) "distance_method" // 向量距离函数。 14) "L2" 15) "data_type" // 向量数据类型。 16) "FLOAT32" 17) "algorithm" // 索引算法。 18) "HNSW" 19) "index_data_size" // 向量数据内存占用（单位：字节）。 20) "105128040" 21) "M" // HNSW 算法模式下，图索引结构中，每一层的最大出边数量。 22) "16" 23) "data_count" // 用户记录数。 24) "3" 25) "current_record_count" // 总向量数。 26) "3" 27) "ef_construct" // HNSW 算法模式下，动态列表的长度。 28) "100" 29) "inverted_index_productname" // 倒排索引信息：字段名称、数据类型、数量。 30) "field: productname, type: string, size: 1" 31) "delete_record_count" // 待回收的向量数。 32) "0" |
## TVS.DELINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.DELINDEX index_name |
| 时间复杂度 | O(N)，N 为该向量索引中 Key 的数量。 |
| 命令描述 | 删除指定的向量索引及该索引内的所有数据。 |
| 选项 | index_name ：向量索引名称。 |
| 返回值 | 执行成功：删除向量索引，并返回 1。 若指定索引不存在，返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.DELINDEX index_name0 返回示例： (integer) 1 |
## TVS.SCANINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.SCANINDEX cursor [MATCH pattern ] [COUNT count ] |
| 时间复杂度 | O(N)，N 为 Tair 实例中向量索引数量。 |
| 命令描述 | 扫描 Tair 实例中所有符合条件的向量索引。 |
| 选项 | cursor ：指定本次扫描的游标，从 0 开始。 pattern ：模式匹配。 count ：指定本次扫描的数量，默认为 10，但无法保证每次迭代都返回精准的元素数量。 |
| 返回值 | 执行成功，返回一个数组： 第一个元素：下次查询的游标，若已扫描完成，则返回 0。 第二个元素：本次查询的向量索引（ index_name ）名称。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.SCANINDEX 0 返回示例： 1) "0" 2) 1) "index_name1" 2) "index_name0" 3) "index_name2" 4) "index_name3" 带 Pattern 的查询示例： TVS.SCANINDEX 0 MATCH **name[0|1] 返回示例： 1) "0" 2) 1) "index_name1" 2) "index_name0" |
## TVS.HSET
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HSET index_name key attribute_key attribute_value [ attribute_key attribute_value ] ... |
| 时间复杂度 | 若本次插入、更新数据无需创建或更新向量值，则时间复杂度为 O(1)；否则时间复杂度为 O(log(N))，N 为该向量索引中 Key 的数量。 |
| 命令描述 | 往向量索引中插入数据记录（ key ），若该记录已存在则更新并覆盖原记录。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识，该对象可通过 TVS.DEL 命令删除。 attribute_key 和 attribute_value ：该条记录的数值，为 Key-value 格式。 插入向量数据：需要将 attribute_key 设置为 VECTOR 关键字（必须大写），对应的 attribute_value 则需要为该向量索引指定维度（ dims ）的向量数据字符串，例如 VECTOR [1,2] 。一个 Key 仅支持写入一个 VECTOR 数据，若重复写入会更新并覆盖原数据。 插入文本数据：在创建索引时已制定 HybridIndex 相关参数，需要将 attribute_key 设置为 TEXT 关键字（必须大写），对应的 attribute_value 可以是文本格式（Text），例如 "TairVector 是 Tair 自研的向量数据库服务" ，也可以是向量化（Embedding）后的数据，例如 "[[2,0.221],[42,09688],...]" 。 插入其他属性：可以自定义额外属性或信息，例如 create_time 1663637425 （创建时间）、 location Hangzhou （地点）等。 |
| 返回值 | 执行成功：返回新增的数据记录数量，若更新已有的字段则返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HSET my_index key5 VECTOR [7,8] TEXT "TairVector 是 Tair 自研的向量数据库服务" create_time 1800 返回示例： (integer) 3 |
## TVS.HGETALL
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HGETALL index_name key |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定向量索引中的 key 对应的所有数据记录。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 |
| 返回值 | 执行成功：返回该 key 的所有数据记录。 若指定的向量索引或 key 不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HGETALL index_name0 key0 返回示例： 1) "VECTOR" 2) "[1,2]" 3) "location" 4) "Hangzhou" 5) "create_time" 6) "1663637425" |
## TVS.HMGET
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HMGET index_name key attribute_key [ attribute_key ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 查询指定向量索引的 key 中对应的 attribute_key 所对应的数值。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 attribute_key ：待操作的属性 Key，支持指定多个。若需查询向量数据，需传入 VECTOR 关键字（必须大写）。若需查询全文索引中原生文本数据，需传入 TEXT 关键字（必须大写）。 |
| 返回值 | 执行成功：返回 attribute_key 对应的数值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HMGET index_name0 key0 create_time location VECTOR TEXT 返回示例： 1) "1800" 2) "[7,8]" 3) "TairVector 是 Tair 自研的向量数据库服务" |
## TVS.DEL
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.DEL index_name key [ key ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，删除指定数据记录（ key ）。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识，支持指定多个。 |
| 返回值 | 执行成功：删除指定数据记录（ key ），并返回删除 key 的数量。 若指定索引不存在，返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.DEL index_name0 keyV 返回示例： (integer) 1 |
## TVS.HDEL
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HDEL index_name key attribute_key [ attribute_key ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 在向量索引的数据记录（ key ）中，删除指定的 attribute_key 与其数值。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识，支持指定多个。 attribute_key ：待操作的属性 Key，支持指定多个。若需删除向量数据，需传入 VECTOR 关键字（必须大写）。若需删除全量索引数据，需传入 TEXT 关键字（必须大写）。 |
| 返回值 | 执行成功：删除指定数据，并返回删除 attribute_key 的数量。 若指定索引不存在，返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HDEL index_name0 keyc VECTOR 返回示例： (integer) 1 |
## TVS.SCAN
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.SCAN index_name cursor [MATCH pattern ] [COUNT count ] [FILTER filter_string] [VECTOR vector] [MAX_DIST max_distance] |
| 时间复杂度 | O(N)，N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，扫描符合条件的数据记录（ key ）。 |
| 选项 | index_name ：向量索引名称。 cursor ：指定本次扫描的游标，从 0 开始。 pattern ：模式匹配。 count ：指定本次扫描的数量，默认为 10，但无法保证每次迭代都返回精准的元素数量。 filter_string ：过滤条件。 支持+-*/<>!=()&&||等操作符，暂不支持比较字符串之间的大小。如需输入字符串，请输入转义字符（\），例如 create_time > 1663637425 && location == \"Hangzhou\"。 操作符两侧必须用空格隔开，例如"creation_time > 1735"。 不支持 flag == true 类型的比较，即不支持 true、false 布尔类型，可以替换为 flag == \"true\" ，当成字符串传递即可。 vector ：查询向量，需要配合 max_distance 参数使用。 max_distance ：最大距离限制，必须配合 vector 参数使用。填写这两个参数后，返回结果与 vector 参数的距离将小于 max_distance 参数。 |
| 返回值 | 执行成功，返回一个数组： 第一个元素：下次查询的游标，若已扫描完成，则返回 0。 第二个元素：本次查询的数据记录（ key ）名称。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.SCAN index_name0 0 返回示例： 1) "0" 2) 1) "key0" 2) "keyV" |
## TVS.HINCRBY
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HINCRBY index_name key attribute_key num |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，将指定数据记录（ key ）的 attribute_key 的值增加 num，num 为一个整数。 若指定的 attribute_key 不存在则自动新建并赋予该值，若该记录已存在则更新并覆盖原值。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 attribute_key ：待操作的属性 Key。 num ：需要为 attribute_key 的 value 增加的整数值。 |
| 返回值 | 执行成功：添加 num 后的值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HINCRBY index_name0 key0 tv01 20 返回示例： (integer) 20 |
## TVS.HINCRBYFLOAT
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HINCRBYFLOAT index_name key attribute_key num |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，将指定数据记录（ key ）的 attribute_key 的值增加 num，num 为一个浮点数。 若指定的 attribute_key 不存在则自动新建并赋予该值，若该记录已存在则更新并覆盖原值。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 attribute_key ：待操作的属性 Key。 num ：需要为 attribute_key 的 value 增加的值，类型为 Float。 |
| 返回值 | 执行成功：添加 num 后的值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HINCRBYFLOAT index_name0 key0 tv02 9.34 返回示例： "9.34" |
## TVS.HPEXPIREAT
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HPEXPIREAT index_name key milliseconds-timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，为指定数据记录（ key ）设置绝对过期时间，精确到毫秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 milliseconds-timestamp ：精确到毫秒的 UNIX 时间戳 （Unix timestamp）。若该时间早于当前时间，则该 key 会立即过期。 |
| 返回值 | key 存在且设置成功：1。 key 不存在：0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPEXPIREAT index_name0 key1 16914619090000 返回示例： (integer) 1 |
## TVS.HPEXPIRE
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HPEXPIRE index_name key milliseconds-timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到毫秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 milliseconds-timestamp ：相对过期时间，单位为毫秒。 |
| 返回值 | key 存在且设置成功：1。 key 不存在：0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPEXPIRE index_name0 key1 1000 返回示例： (integer) 1 |
## TVS.HEXPIREAT
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HEXPIREAT index_name key timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，为指定数据记录（ key ）设置绝对过期时间，精确到秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 timestamp ：精确到秒的 UNIX 时间戳 （Unix timestamp）。若该时间早于当前时间，则该 key 会立即过期。 |
| 返回值 | key 存在且设置成功：1。 key 不存在：0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPEXPIREAT index_name0 key2 1691466981 返回示例： (integer) 1 |
## TVS.HEXPIRE
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HEXPIRE index_name key timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，为指定数据记录（ key ）设置相对过期时间，精确到秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 timestamp ：相对过期时间，单位为秒。 |
| 返回值 | key 存在且设置成功：1。 key 不存在：0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPEXPIREAT index_name0 key2 100 返回示例： (integer) 1 |
## TVS.HPTTL
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HPTTL index_name key |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，查看指定数据记录（ key ）的剩余过期时间，精确到毫秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 |
| 返回值 | key 存在且设置了过期时间：剩余过期时间，单位为毫秒。 key 存在但未设置过期时间：-1。 key 或 index_name 不存在：-2。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPTTL index_name0 key2 返回示例： (integer) 65417 |
## TVS.HTTL
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HTTL index_name key |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，查看指定数据记录（ key ）的剩余过期时间，精确到秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 |
| 返回值 | key 存在且设置了过期时间：剩余过期时间，单位为秒。 key 存在但未设置过期时间：-1。 key 或 index_name 不存在：-2。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HTTL index_name0 key2 返回示例： (integer) 58 |
## TVS.HPEXPIRETIME
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HPEXPIRETIME index_name key |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，查看指定数据记录（ key ）的绝对过期时间，精确到毫秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 |
| 返回值 | key 存在且设置了过期时间：绝对过期时间（Unix timestamp），单位为毫秒。 key 存在但未设置过期时间：-1。 key 或 index_name 不存在：-2。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HPEXPIRETIME index_name0 key2 返回示例： (integer) 1691473985764 |
## TVS.HEXPIRETIME
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.HEXPIRETIME index_name key |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定向量索引中，查看指定数据记录（ key ）的绝对过期时间，精确到秒。 |
| 选项 | index_name ：向量索引名称。 key ：该记录的主键标识。 |
| 返回值 | key 存在且设置了过期时间：绝对过期时间（Unix timestamp），单位为秒。 key 存在但未设置过期时间：-1。 key 或 index_name 不存在：-2。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TVS.HEXPIRETIME index_name0 key2 返回示例： (integer) 1691473985 |
## TVS.KNNSEARCH
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.KNNSEARCH index_name topN vector [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：O(log(N)) FLAT 算法：O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，对指定的向量（VECTOR）进行近邻查询，最多可返回 topN 条。 |
| 选项 | index_name ：向量索引名称。 topN ：查询返回的数量，取值范围为[1,10000]。 vector ：执行近邻查询的向量值。若您仅希望执行全文检索（索引为混合索引），可在该字段传入 "" 。 filter_string ：过滤条件。 支持 +-*/<>!=()&&|| 等操作符，暂不支持比较字符串之间的大小。如需输入字符串，请输入转义字符（\），例如 "create_time > 1663637425 && location == \"Hangzhou\"" 。 操作符两侧必须用空格隔开，例如 "creation_time > 1735" 。 不支持 flag == true 类型的比较，即不支持 true、false 布尔类型，可以替换为 flag == \"true\" ，当成字符串传递即可。 param_key 和 param_value ：查询的运行参数，取值如下。 ef_search ：查询索引的时候，动态列表的长度，默认为 100，取值范围为[1,1000]，该值越大则查询精度越高，同时性能开销越大。该参数为 HNSW 算法的特定参数。 sparse_ef_search ：在创建混合索引时，如果稀疏向量使用了 HNSW 索引，则请使用 sparse_ef_search 参数为稀疏向量 HNSW 索引的 ef_search 参数。 MAX_DIST ：最大距离限制，Float 类型，若某 Key 与待查询向量的距离大于该值，则会过滤，不会返回。 TEXT ：执行查询的文本（混合检索），可传入文本类型或向量类型，若不传入该字段或在该字段传入 "" ，表示不进行全文检索，仅执行向量检索。 hybrid_ratio ：本次查询时向量检索的权重，默认为 TVS.CREATEINDEX 设置的 hybrid_ratio 值，取值范围为[0,1]，Float 类型，全量检索的权重为 1-hybrid_ratio 。 默认情况下，系统使用先执行 KNN 向量检索、再执行标量检索的后置过滤（PostFilter）策略。 vector_filter_count ：向量检索过滤的最大数量，默认为 10000。 在 PostFilter 策略中，当向量检索结果过滤超过 vector_filter_count 条记录，但仍未到达足够返回的数据量时，系统会终止向量检索遍历。 fulltext_filter_count ：全文检索过滤的最大数量，默认为 10000。 在 PostFilter 策略中，当全文检索结果过滤超过 fulltext_filter_count 条记录，但仍未到达足够返回的数据量时，系统会终止全文检索遍历。 若您希望系统先执行倒排索引的标量检索，再执行 KNN 向量检索的前置过滤（PreFilter）策略，您可以在查询中增加 search_policy scala 参数。 同时提供 ivf_filter_count 参数，即倒排索引过滤的最大数量，默认为 10000。在 PreFilter 策略中，当倒排索引过滤的结果超过 ivf_filter_count 条记录时，系统会自动退化为 PostFilter 策略。 说明 在绝大多数情况下，上述默认参数可以在确保准确性的前提下保证系统的延迟。您可以在特定请求中调整上述参数，但上述参数越大，请求延迟也可能越大。 |
| 返回值 | 执行成功：按距离近到远的顺序返回近邻的 key 及与该目标向量的距离。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_k 2 HNSW L2 inverted_index_productname string TVS.HSET my_index_k key0 VECTOR [1,2] creation_time 1730 productname "Aliyun" TVS.HSET my_index_k key1 VECTOR [3,4] creation_time 1740 productname "other" TVS.HSET my_index_k key2 VECTOR [5,6] creation_time 1750 productname "Aliyun" 命令示例 1： TVS.KNNSEARCH my_index_k 2 [3,3.1] "creation_time > 1735" 返回示例 1： 1) "key1" 2) "0.81000018119812012" 3) "key2" 4) "12.410000801086426" 命令示例 2： TVS.KNNSEARCH my_index_k 2 [3,3.1] "creation_time > 1735 && productname == \"Aliyun\"" search_policy scala ivf_filter_count 15000 返回示例 2： 1) "key2" 2) "12.410000801086426" |
## TVS.KNNSEARCHFIELD
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.KNNSEARCHFIELD index_name topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：O(log(N)) FLAT 算法：O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，对指定的向量（VECTOR）进行近邻查询，检索逻辑与 TVS.KNNSEARCH 相同，额外支持返回标签属性。 |
| 选项 | index_name ：向量索引名称。 topN ：查询返回的数量，取值范围为[1,10000]。 vector ：执行近邻查询的向量值。若您仅希望执行全文检索（索引为混合索引），可在该字段传入 "" 。 field_count ：返回结果中标签属性的数量，若希望返回所有标签，可以设置 field_count 为 0。 field_name ：标签名称，数量需要与 field_count 保持一致。 filter_string ：过滤条件，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 param_key 和 param_value ：查询的运行参数，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 |
| 返回值 | 执行成功：按距离近到远的顺序返回近邻的 key 及与该目标向量的距离，以及对应的标签属性键值对。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_k 2 HNSW L2 TVS.HSET my_index_k key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_k key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_k key2 VECTOR [5,6] creation_time 1750 命令示例： TVS.KNNSEARCHFIELD my_index_k 2 [3,3.1] 0 "creation_time > 1735" 返回示例： 1) 1) "key1" 2) "0.81000018119812012" 3) "VECTOR" 4) "[3,4]" 5) "creation_time" 6) "1740" 2) 1) "key2" 2) "12.410000801086426" 3) "VECTOR" 4) "[5,6]" 5) "creation_time" 6) "1750" |
## TVS.GETDISTANCE
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.GETDISTANCE index_name vector key_count key [ key , ...] [TOPN topN ] [FILTER filter_string ] [MAX_DIST max_distance] |
| 时间复杂度 | HNSW 算法：O(log(N)) FLAT 算法：O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，针对指定 Key 列表，进行向量（VECTOR）近邻查询。 |
| 选项 | index_name ：向量索引名称。 vector ：执行近邻查询的向量值。 key_count ：候选 Key 的数量。 key ：Key 名称，Key 的数量需要与 key_count 一致。 TOPN ：查询返回的数量，默认为 key_count ，取值范围为[1, key_count ]。 FILTER ：过滤条件。 支持 +-*/<>!=()&&|| 等操作符，暂不支持比较字符串之间的大小。如需输入字符串，请输入转义字符（\），例如 create_time > 1663637425 && location == \"Hangzhou\" 。 操作符两侧必须用空格隔开，例如 "creation_time > 1735" 。 不支持 flag == true 类型的比较，即不支持 true、false 布尔类型，可以替换为 flag == \"true\" ，当成字符串传递即可。 MAX_DIST ：最大距离限制，若某 Key 与待查询向量的距离大于该值，则会过滤，不会返回。 |
| 返回值 | 执行成功：默认按 Key 的顺序返回对应距离，若指定了 TOPN ，则按距离近到远的顺序返回近邻 Key 与对应距离。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_k 2 HNSW L2 TVS.HSET my_index_k key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_k key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_k key2 VECTOR [5,6] creation_time 1750 命令示例： TVS.GETDISTANCE my_index_k [1,1] 2 key1 key2 返回示例： 1) "key1" 2) "13" 3) "key2" 4) "41" |
## TVS.MKNNSEARCH
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.MKNNSEARCH index_name topN vector_count vector [vector ...] [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：vector_count * O(log(N)) FLAT 算法：vector_count * O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在指定向量索引中，批量对多条向量（VECTOR）进行近邻查询。 |
| 选项 | index_name ：向量索引名称。 topN ：每条向量查询返回的数量，取值范围为[1,10000]。 vector_count ：查询的向量数。 vector ：执行近邻查询的向量值。若您仅希望执行全文检索（索引为混合索引），可在该字段传入 "" 。 filter_string ：过滤条件，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 param_key 和 param_value ：查询的运行参数，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 |
| 返回值 | 执行成功：按向量查询顺序返回多个查询结果数组，每个数组中按距离近到远的顺序返回近邻的 key 及与该目标向量的距离。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_m 2 HNSW L2 TVS.HSET my_index_m key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_m key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_m key2 VECTOR [5,6] creation_time 1750 命令示例： TVS.MKNNSEARCH my_index_m 2 2 [3,4] [5,6] "creation_time > 1735" 返回示例： 1) 1) "key1" 2) "0" 3) "key2" 4) "8" 2) 1) "key2" 2) "0" 3) "key1" 4) "8" |
## TVS.MINDEXKNNSEARCH
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.MINDEXKNNSEARCH index_count index_name [index_name ...] topN vector [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：index_count * O(log(N)) FLAT 算法：index_count * O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在多个向量索引中，对指定的向量（VECTOR）进行近邻查询。 |
| 选项 | index_count ：向量索引的数量。 index_name ：向量索引名称。 topN ：查询返回的数量，取值范围为[1,10000]，默认会查询出每个向量索引的 topN 个结果，并将所有查询结果进行聚合，返回距离最近的 topN 个结果。 vector ：执行近邻查询的向量值。 filter_string ：过滤条件，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 param_key 和 param_value ：查询的运行参数，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 |
| 返回值 | 执行成功：按距离近到远的顺序返回近邻的 key 及与该目标向量的距离。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_mk 2 HNSW L2 TVS.HSET my_index_mk key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_mk key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_mk key2 VECTOR [5,6] creation_time 1750 TVS.CREATEINDEX my_index_mx 2 HNSW L2 TVS.HSET my_index_mx key5 VECTOR [8,7] creation_time 1730 TVS.HSET my_index_mx key6 VECTOR [6,5] creation_time 1740 TVS.HSET my_index_mx key7 VECTOR [4,3] creation_time 1750 命令示例： TVS.MINDEXKNNSEARCH 2 my_index_mk my_index_mx 2 [0,0] 返回示例： 1) "key0" 2) "5" 3) "key7" 4) "25" |
## TVS.MINDEXKNNSEARCHFIELD
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.MINDEXKNNSEARCHFIELD index_count index_name [index_name ...] topN vector field_count field_name [field_name ...] [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：index_count * O(log(N)) FLAT 算法：index_count * O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在多个向量索引中，对指定的向量（VECTOR）进行近邻查询，支持返回标签属性。 |
| 选项 | index_count ：向量索引的数量。 index_name ：向量索引名称。 topN ：查询返回的数量，取值范围为[1,10000]，默认会查询出每个向量索引的 topN 个结果，并将所有查询结果进行聚合，返回距离最近的 topN 个结果。 vector ：执行近邻查询的向量值。 field_count ：返回结果中标签属性的数量，若希望返回所有标签，可以设置 field_count 为 0。 field_name ：标签名称，数量需要与 field_count 保持一致。 filter_string ：过滤条件，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 param_key 和 param_value ：查询的运行参数，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 |
| 返回值 | 执行成功：按距离近到远的顺序返回近邻的 key 及与该目标向量的距离，以及对应的标签属性键值对。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_mk 2 HNSW L2 TVS.HSET my_index_mk key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_mk key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_mk key2 VECTOR [5,6] creation_time 1750 TVS.CREATEINDEX my_index_mx 2 HNSW L2 TVS.HSET my_index_mx key5 VECTOR [8,7] creation_time 1730 TVS.HSET my_index_mx key6 VECTOR [6,5] creation_time 1740 TVS.HSET my_index_mx key7 VECTOR [4,3] creation_time 1750 命令示例： TVS.MINDEXKNNSEARCHFIELD 2 my_index_mk my_index_mx 2 [0,0] 0 返回示例： 1) 1) "key0" 2) "5" 3) "my_index_mk" 4) "VECTOR" 5) "[1,2]" 6) "creation_time" 7) "1730" 2) 1) "key1" 2) "25" 3) "my_index_mk" 4) "VECTOR" 5) "[3,4]" 6) "creation_time" 7) "1740" |
## TVS.MINDEXMKNNSEARCH
| 类别 | 说明 |
| --- | --- |
| 语法 | TVS.MINDEXMKNNSEARCH index_count index_name [index_name ...] topN vector_count vector [vector ...] [filter_string] [param_key param_value] |
| 时间复杂度 | HNSW 算法：index_count * vector_count * O(log(N)) FLAT 算法：index_count * vector_count * O(N) N 为该向量索引中 Key 的数量。 |
| 命令描述 | 在多个向量索引中，批量对多条向量（VECTOR）进行近邻查询。 |
| 选项 | index_count ：向量索引的数量。 index_name ：向量索引名称。 topN ：每条向量查询返回的数量，取值范围为[1,10000]，默认会查询出每个向量索引的 topN 个结果，并将所有查询结果进行聚合，返回距离最近的 topN 个结果。 vector_count ：查询的向量数。 vector ：执行近邻查询的向量值。 filter_string ：过滤条件，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 param_key 和 param_value ：查询的运行参数，更多信息请参见 [TVS.KNNSEARCH](tairvector.md) 中的说明。 |
| 返回值 | 执行成功：按向量查询顺序返回多个查询结果数组，每个数组中按距离近到远的顺序返回近邻的 key 及与该目标向量的距离。 若指定的向量索引不存在，返回 (empty array) 。 其他情况返回相应的异常信息。 |
| 示例 | 请提前执行如下命令： TVS.CREATEINDEX my_index_mk 2 HNSW L2 TVS.HSET my_index_mk key0 VECTOR [1,2] creation_time 1730 TVS.HSET my_index_mk key1 VECTOR [3,4] creation_time 1740 TVS.HSET my_index_mk key2 VECTOR [5,6] creation_time 1750 TVS.CREATEINDEX my_index_mx 2 HNSW L2 TVS.HSET my_index_mx key5 VECTOR [8,7] creation_time 1730 TVS.HSET my_index_mx key6 VECTOR [6,5] creation_time 1740 TVS.HSET my_index_mx key7 VECTOR [4,3] creation_time 1750 命令示例： TVS.MINDEXMKNNSEARCH 2 my_index_mk my_index_mx 2 2 [0,0] [3,3] 返回示例： 1) 1) "key0" 2) "5" 3) "key7" 4) "25" 2) 1) "key1" 2) "1" 3) "key7" 4) "1" |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
