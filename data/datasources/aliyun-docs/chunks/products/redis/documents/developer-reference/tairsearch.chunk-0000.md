## TairSearch简介
TairSearch具有如下主要特点：
低延迟、高性能：依托Tair的超高性能计算能力，提供毫秒级别的写入和全文搜索能力，更多信息请参见[TairSearch](../support/performance-whitepaper-of-tairsearch.md)[性能白皮书](../support/performance-whitepaper-of-tairsearch.md)。
增量、局部更新：支持文档的增量更新与局部索引更新，包括追加字段、更新字段、删除字段以及字段自增等。
语法灵活：支持更加灵活、可读性更强的JSON查询语法，提供Bool、Match、Term、分页等查询功能，语法与Elasticsearch类似，同时支持自定义排序。
聚合查询：支持Terms、Metrics、Filter等聚合算子，更多信息请参见[Aggregations](tairsearch.md)[介绍](tairsearch.md)。
Auto-complete Suggestion：支持前缀模糊搜索、自动补全等功能。
分词定制：提供丰富、强大的分词器，内置英文（Standard、Stop等）、中文（Jieba、IK）及世界主要语言分词器，同时支持Custom自定义分词器，允许自定义用户词典和停用词等，更多信息请参见[Search](tairsearch-word-splitter.md)[分词器](tairsearch-word-splitter.md)。
索引分片查询：支持使用TFT.MSEARCH命令同时对多个索引分片（Shard index）进行查询，并自动返回已聚合的结果集。
压缩存储：支持文档级别的压缩存储（默认未开启），从而节省内存占用空间。
查询缓存：支持将最近的查询结果（可自定义）存储在缓存，从而提高热点数据的查询效率。
发布记录
内存型（兼容Redis 5.0）
2022年03月11日发布1.7.27版本，首次发布TairSearch。
2022年05月24日发布1.8.5版本，支持TairSearch Aggregations（聚合）功能。
2022年09月06日发布5.0.15版本，支持TFT.MSEARCH功能。
2023年01月13日发布5.0.25版本，全面支持分词器框架。
2023年03月15日发布5.0.28版本，支持查询缓存，支持文档压缩存储，新增TFT.ANALYZER命令。
2023年06月12日发布5.0.35版本，支持数组类型的文档，支持Okapi BM25算法。
内存型（兼容Redis 6.0）
2023年02月07日发布6.2.4.1版本，首次支持TairSearch。
该版本能力对齐内存型（兼容Redis 5.0）的5.0.25版本。
2023年03月14日发布6.2.5.0版本，支持查询缓存
