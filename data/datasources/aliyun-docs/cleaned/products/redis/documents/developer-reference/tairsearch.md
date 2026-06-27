# 全文搜索数据结构聚合查询-TairSearch-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/tairsearch

# Search
TairSearch是Tair全自研的全文搜索数据结构，采用和Elasticsearch相似（ES-LIKE）的查询语法。
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
2023年03月14日发布6.2.5.0版本，支持查询缓存，支持文档压缩存储，新增TFT.ANALYZER命令。
该版本能力对齐内存型（兼容Redis 5.0）的5.0.28版本。
2023年06月12日发布6.2.7.3版本，支持数组类型的文档，支持Okapi BM25算法。
该版本能力对齐内存型（兼容Redis 5.0）的5.0.35版本。
2023年12月21日发布23.12.1.2版本，支持TFT.EXPLAINSCORE命令。
内存型（兼容Redis 7.0）
2024年07月22日发布24.7.0.0首发版本，首次支持TairSearch。
## 最佳实践
[基于](../use-cases/accelerating-multi-column-index-federated-query-based-on-tairsearch.md)[TairSearch](../use-cases/accelerating-multi-column-index-federated-query-based-on-tairsearch.md)[加速多列索引联合查询](../use-cases/accelerating-multi-column-index-federated-query-based-on-tairsearch.md)
[基于](../use-cases/build-a-real-time-calculation-service-for-stock-k-line-based-on.md)[TairSearch](../use-cases/build-a-real-time-calculation-service-for-stock-k-line-based-on.md)[构建股票](../use-cases/build-a-real-time-calculation-service-for-stock-k-line-based-on.md)[K](../use-cases/build-a-real-time-calculation-service-for-stock-k-line-based-on.md)[线实时计算服务](../use-cases/build-a-real-time-calculation-service-for-stock-k-line-based-on.md)
[在](../use-cases/using-bool-in-tairsearch-for-combined-conditional-queries.md)[TairSearch](../use-cases/using-bool-in-tairsearch-for-combined-conditional-queries.md)[中使用](../use-cases/using-bool-in-tairsearch-for-combined-conditional-queries.md)[bool](../use-cases/using-bool-in-tairsearch-for-combined-conditional-queries.md)[进行组合条件查询](../use-cases/using-bool-in-tairsearch-for-combined-conditional-queries.md)
[在](../use-cases/using-msearch-to-implement-index-shard-search-in-tairsearch.md)[TairSearch](../use-cases/using-msearch-to-implement-index-shard-search-in-tairsearch.md)[中使用](../use-cases/using-msearch-to-implement-index-shard-search-in-tairsearch.md)[Msearch](../use-cases/using-msearch-to-implement-index-shard-search-in-tairsearch.md)[实现索引分片搜索](../use-cases/using-msearch-to-implement-index-shard-search-in-tairsearch.md)
## 前提条件
实例为Tair[内存型](../product-overview/dram-based-instances.md)，支持的版本说明：
内存型（兼容Redis 5.0）：小版本为1.7.27及以上。
内存型（兼容Redis 6.0）：小版本为6.2.4.1及以上。
内存型（兼容Redis 7.0）：所有版本。
说明
最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](../user-guide/update-the-minor-version.md)。如果您的实例为集群实例或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。
## 注意事项
操作对象为Tair实例中的TairSearch数据。
为节省内存，推荐使用如下方法：
创建索引（index）时请将文档中需要创建（反向）索引的字段设置为索引字段（将字段的index设置为true），其余字段的index设置为false。
使用_source参数中的include与exclude机制剔除源文档中不需要的字段（field），保存需要的信息。
若文档需要进行分词处理，请选择合适的分词器，避免不合适的分词器拆成出过多、无用的Token（词元），增加内存开销。
若文档较大，您可以合理使用文档压缩功能对文档进行透明压缩（自动压缩、解压）。
避免在单个索引中插入过多的文档，建议将文档存入多个不同的索引中，并控制单个索引的文档数在500万以下，从而规避（集群）实例发生数据倾斜，均衡读写流量，避免造成大Key与热key。
## 命令列表
表 1.全文检索命令
| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [TFT.CREATEINDEX](tairsearch.md) | TFT.CREATEINDEX index mappings settings | 创建索引（index）并添加映射（mappings），映射语法类似 [ES](https://www.elastic.co/guide/en/elasticsearch/reference/8.0/explicit-mapping.html) [语法](https://www.elastic.co/guide/en/elasticsearch/reference/8.0/explicit-mapping.html) 。在添加索引文档前，必须先创建索引。 |
| [TFT.UPDATEINDEX](tairsearch.md) | TFT.UPDATEINDEX index mappings settings | 向指定的索引中新增 properties 字段，或修改索引设置。 |
| [TFT.GETINDEX](tairsearch.md) | TFT.GETINDEX index | 获取索引的映射内容。 |
| [TFT.ADDDOC](tairsearch.md) | TFT.ADDDOC index document [WITH_ID doc_id] | 向索引中插入一个文档（document），可通过 WITH_ID 指定该文档在索引内的唯一 ID（doc_id），若 doc_id 已存在，则更新并覆盖原文档。若不指定 WITH_ID （默认），则自动生成 doc_id。 |
| [TFT.MADDDOC](tairsearch.md) | TFT.MADDDOC index document doc_id [document1 doc_id1] ... | 向索引中插入多个文档（document），每个文档必须指定文档 ID（doc_id）。若某个文档写入失败（例如写入的文档内容与定义的格式不符），则该命令的所有文档均不会写入。 |
| [TFT.UPDATEDOCFIELD](tairsearch.md) | TFT.UPDATEDOCFIELD index doc_id document | 更新索引中 doc_id 指定的文档，若更新的字段为 mapping 指定的索引字段时，该字段更新的内容需与 mapping 指定的类型一致；若非索引字段，支持更新任意字段类型的内容。 说明 若更新的字段已存在，则更新原文档，若字段不存在，则新增该字段。若指定的文档不存在，该命令支持自动创建文档，此时效果等同于 TFT.ADDDOC。 |
| [TFT.DELDOCFIELD](tairsearch.md) | TFT.DELDOCFIELD index doc_id field [field1 field2 ...] | 删除索引中 doc_id 指定文档的指定字段，若该字段为索引字段，会同时在索引中删除该字段的信息。 说明 若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| [TFT.INCRLONGDOCFIELD](tairsearch.md) | TFT.INCRLONGDOCFIELD index doc_id field increment | 向索引中 doc_id 指定文档的指定字段增加整数值（increment），支持指定 increment 为负数，支持指定的字段类型为 long 或 int 类型。 说明 若指定的文档不存在，该命令支持自动创建文档，初始化字段的值为 0，并增加指定的 increment。若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| [TFT.INCRFLOATDOCFIELD](tairsearch.md) | TFT.INCRFLOATDOCFIELD index doc_id field increment | 向索引中 doc_id 指定文档的指定字段增加浮点数值（increment），支持指定 increment 为负数，支持指定的字段类型为 double 类型。 说明 若指定的文档不存在，该命令支持自动创建文档，初始化字段的值为 0，并增加指定的 increment。若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| [TFT.GETDOC](tairsearch.md) | TFT.GETDOC index doc_id | 获取索引中指定 doc_id 的文档内容。 |
| [TFT.EXISTS](tairsearch.md) | TFT.EXISTS index doc_id | 查询索引中指定 doc_id 的文档是否存在。 |
| [TFT.DOCNUM](tairsearch.md) | TFT.DOCNUM index | 获取索引中的文档数量。 |
| [TFT.SCANDOCID](tairsearch.md) | TFT.SCANDOCID index cursor [MATCH *value*] [COUNT count] | 获取索引中所有的 doc_id。 |
| [TFT.DELDOC](tairsearch.md) | TFT.DELDOC index doc_id [doc_id] ... | 删除索引中 doc_id 指定的文档，支持指定多个 doc_id。 |
| [TFT.DELALL](tairsearch.md) | TFT.DELALL index | 删除索引中所有文档，但不会删除 index。 |
| [TFT.ANALYZER](tairsearch.md) | TFT.ANALYZER analyzer_name text [INDEX index_name] [SHOW_TIME] | 查询分词器分词效果。 |
| [TFT.SEARCH](tairsearch.md) | TFT.SEARCH index query | 根据 query 语句搜索索引的文档，query 语法类似 [ES](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/query-dsl.html) [语法](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/query-dsl.html) 。 |
| [TFT.MSEARCH](tairsearch.md) | TFT.MSEARCH index_count index [index1] ... query | 根据 query 语句搜索多个索引的文档（待查询索引的 mappings 和 settings 的配置必须相同），汇聚多个索引的查询结果，再次进行打分、排序、聚合并返回。 |
| [TFT.EXPLAINCOST](tairsearch.md) | TFT.EXPLAINCOST index query | 查询 query 语句的执行耗时，返回内容包括查询过程中涉及到的文档集合数及各阶段的耗时。 |
| [TFT.EXPLAINSCORE](tairsearch.md) | TFT.EXPLAINSCORE index query [doc_id] ... | 查询执行 query 语句的计分详情信息，您可以通过该命令了解文档分数的计算过程，并优化 Search 语句，提升文档的查询效果。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairSearch 数据。 |
表 2.自动补齐命令
| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [TFT.ADDSUG](tairsearch.md) | TFT.ADDSUG index text weight [text weight] ... | 在指定索引中，添加自动补全的文本及对应权重，支持添加多个文本。 |
| [TFT.DELSUG](tairsearch.md) | TFT.DELSUG index text [text] ... | 在指定索引中，删除自动补全的文本，支持删除多个文本。 |
| [TFT.SUGNUM](tairsearch.md) | TFT.SUGNUM index | 获取指定索引中自动补全文本的数量。 |
| [TFT.GETSUG](tairsearch.md) | TFT.GETSUG index prefix [MAX_COUNT count] [FUZZY] | 根据指定前缀，查询匹配的自动补全文本，将优先返回权重比较高的 text。 |
| [TFT.GETALLSUGS](tairsearch.md) | TFT.GETALLSUGS index | 获取指定索引的全量自动补全文本。 |
说明
本文的命令语法定义如下：
大写关键字：命令关键字。
斜体：变量。
[options]：可选参数，不在括号中的参数为必选。
A|B：该组参数互斥，请进行二选一或多选一。
...：前面的内容可重复。
## TFT.CREATEINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.CREATEINDEX index mappings settings |
| 命令描述 | 创建索引（index）并添加映射（mappings），映射语法类似 [ES](https://www.elastic.co/guide/en/elasticsearch/reference/8.0/explicit-mapping.html) [语法](https://www.elastic.co/guide/en/elasticsearch/reference/8.0/explicit-mapping.html) 。在添加索引文档前，必须先创建索引。 说明 为避免产生大 Key，您可以预先将大索引拆分成小索引，并设计负载规则将数据写入不同的索引中。创建该类索引时，必须使该类索引具备相同的 mappings 和 settings 配置，创建后可通过 [TFT.MSEARCH](tairsearch.md) 进行查询。 |
| 选项 | index ：待创建的索引名称。 mappings ：映射内容，支持的语法如下。 dynamic ：映射模式，支持 strict （严格映射），表示仅能写入在 properties 中已设置过的字段，无法成功写入未配置过的字段。若未指定该参数，则默认为非严格映射模式，即不会检查写入的字段是否已在 properties 中设置。 enabled ：强制检查写入文档的字段类型与 properties 中指定的类型是否一致，若不一致则写入失败，取值为 true（默认，表示会检查）和 false。该参数仅对非索引字段（ index 为 false）生效，索引字段会强制检查字段类型。 _source ：设置存储原始文档，该参数不会影响对应字段索引的创建，取值如下。 enabled ：是否存储原始文档，取值如下。 true （默认）：存储原始文档，默认存储所有字段。 可指定 excludes （不需要存储的字段）和 includes （需要存储的字段），支持配置通配符模式（WildCard）的字段。若某字段同时出现在 excludes 和 includes 时，则 excludes 的优先级大于 includes ，表示该字段最终不会存储在原始文档中，示例如下。 示例一： "_source":{"enabled":true} （默认），表示存储所有字段，等同于 "_source":{"enabled":true,"excludes":[],"includes":[]} 。 示例二： "_source":{"enabled":true,"excludes":[],"includes":["id","name"]} ，表示仅存储“id”、“name”字段。 false ：不存储原始文档。 properties ：映射的字段集合，每个字段可设置如下属性。 index ：是否将该字段设置为索引字段，取值如下： true （默认）：索引字段，查询时仅能通过索引字段查找文档。 Tair 会在内存中存储所有索引字段的原始文档，若该字段在 _source 中配置不存储原始文档，则在查询时返回的原始文档中不显示该字段。 false ：非索引字段。 boost ：该字段的计分权重，默认为 1，范围为正浮点数，Tair 将自动计算出各个字段的相对计算分。 type ：字段的数据类型，同时支持数组类型，取值如下。 说明 例如 keyword 的数组类型为 keyword[] ，其他数据类型类似。示例为： TFT.CREATEINDEX idx:pro '{"mappings":{"properties":{"f0":{"type":"keyword[]"}}}}' 。 keyword ：不可被拆分字符串。取值如下： ignore_above ：指定 keyword 的字符串长度上限，默认为 128，例如 "ignore_above":128 。 similarity ：相似度算法，取值为 classic （默认，表示使用 TF-IDF 算法）、 BM25 （Okapi BM25 算法），示例为： TFT.CREATEINDEX idx:pro '{"mappings":{"properties":{"fs0":{"type":"keyword","similarity":"BM25"}}}}' ，您也可以在 settings 中自定义 BM25 算法的参数。 text ：字符串，且可通过分词器解析，存入索引。取值如下： analyzer ：解析 text 存入索引的分词器。 您可直接选择 TairSearch 内置分词器，包含 standard （默认）、 jieba （推荐的中文分词，效果比 chinese 好）、 stop 、 IK 、 pattern 、 whitespace 、 simple 、 keyword 、 chinese 、 french 、 dutch 和 russian 等。例如 "analyzer":"jieba" ，表示使用 Jieba 中文分词器，更多信息请参见 [内置分词器](tairsearch-word-splitter.md) 。 您也可以自定义分词器，例如 "analyzer":"my_custom_analyzer" ，并在 settings 中的 analysis 参数中进行具体的分词器配置。 search_analyzer ：指定搜索时使用的分词器，支持的分词器类型与 analyzer 相同，默认为 analyzer 的设置。 similarity ：相似度算法，取值为 classic （默认，表示使用 TF-IDF 算法）、 BM25 （Okapi BM25 算法），您也可以在 settings 中自定义 BM25 算法的参数。 long ：长整型，您可以将时间点转为 Unix 时间戳，存入该数据类型中。 integer ：整型。 double ：双精度浮点型，但不支持 NaN、Inf、-Inf 等特殊的数据类型。 settings （可选）：配置索引设置，支持如下配置项。 analysis ：自定义分词器，更多信息请参见 [自定义分词器](tairsearch-word-splitter.md) 。 index ：自定义相似度算法，支持修改 Okapi BM25 算法的参数，示例如下： TFT.CREATEINDEX idx:pro15 '{"mappings":{"properties":{"fs0":{"type":"keyword","similarity":"my_similarity"}}},"settings":{"index":{"similarity":{"my_similarity":{"type":"BM25","k1": 1.0,"b": 1.0}}}}}' 。参数说明： k1 ：词项在文档中的出现频率对得分（分数）的影响，该值越大，出现频率对于得分影响越大，默认值为 1.2，取值范围需大于 0。 b ：文档长度对得分（分数）的影响，该值越大，文档长度对于得分影响越大，默认值为 0.75，取值范围为[0,1]。 queries_cache ：当您查询文档时，TairSearch 支持将查询结果存入缓存，该缓存称为查询缓存，默认最大缓存为 10000 条查询结果（内存无限制），达到上限后，将通过 LRU 算法（最近最少使用的）逐出查询结果。您可以通过配置 queries_cache ，配置查询缓存的最大内存和 TTL（Time To Live）配置，配置后，查询缓存的最大内存将以 size 为准。取值如下： size ：字符串类型，表示所有查询缓存的最大内存，当达到查询缓存最大内存后，也将通过 LRU 算法逐出查询结果。 该参数的默认单位为字节，例如 "size": "1000" 表示最多能存储 1000 字节的查询缓存，同时还支持单位："kb"、"mb"，例如 "size": "10kb" 、 "size": "1mb" 。 ttl ：整型，表示一条查询缓存的过期时间，默认为 10s，单位为秒。 示例： "settings":{"queries_cache":{"size":"100mb","ttl":3}} 。 queries_cache 配置项为节点维度的参数，在一个索引中配置后，在同进程内的其他索引也会受到影响。因此，建议所有索引都是用相同的 queries_cache 配置。 compress_doc ：配置是否启用文档透明压缩功能。开启该功能会消耗更多的 CPU，并增大读写时延，因此只建议在索引较大（如 KB 级别）且优先考虑存储成本时启用该功能。取值如下： size ：字符串类型，表示压缩的阈值，当索引达到该阈值时，才会被压缩，默认值为“10kb”。 该参数的默认单位为字节，同时还支持单位："kb"、"mb"，例如 "size": "1000" 、 "size": "10kb" 、 "size": "1mb" 。 enable ：布尔类型，表示是否启用文档压缩功能，取值为 false（默认）和 true。 示例： "settings":{"compress_doc":{"size":"1kb","enable":true}} 。 在通过 TFT.UPDATEINDEX 命令开启或关闭压缩功能后，压缩功能只对新写入或更新的文档生效，不会对已写入的文档生效。例如，通过 TFT.UPDATEINDEX 命令开启压缩功能，Tair 仅会对之后写入或更新的文档进行压缩，不会对已写入的文档进行压缩操作。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.CREATEINDEX idx:product '{"mappings":{"_source":{"enabled":true},"properties":{"product_id":{"type":"keyword","ignore_above":128},"product_name":{"type":"text"},"product_title":{"type":"text","analyzer":"jieba"}, "price":{"type":"double"}}}}' # 创建商品 ID（product_id）为 keyword 数据类型，并设置上限为 128 个字符。 # 创建商品名称（product_name）为 text 数据类型。 # 创建商品标题（product_title）为 text 数据类型，并设置分词器为中文。 # 创建价格（price）为 double 数据类型。 返回示例： OK |
## TFT.UPDATEINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.UPDATEINDEX index mappings settings |
| 命令描述 | 向指定的索引中新增 properties 字段，或修改索引设置。 |
| 选项 | index ：待操作的索引名称。 mappings ：映射内容，仅输入新增的 properties 字段（无需输入 dynamic 、 _source 等信息），且新增的 properties 字段不能与原有字段冲突，否则会新增失败。 settings ：修改索引设置。仅支持修改 queries_cache 、 compress_doc 和 index 参数，其中 index 参数仅支持修改 BM25 算法中 k1 、 b 的值。 说明 mappings 和 settings 的语法请参见 [TFT.CREATEINDEX](tairsearch.md) 。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.UPDATEINDEX idx:product '{"mappings":{"properties":{"product_group":{"type":"text","analyzer":"chinese"}}}}' 返回示例： OK |
## TFT.GETINDEX
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.GETINDEX index |
| 命令描述 | 获取索引的映射内容。 |
| 选项 | index ：待操作的索引名称。 |
| 返回值 | 执行成功：返回索引的映射内容，格式为 JSON。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.GETINDEX idx:product 返回示例： {"idx:product0310":{"mappings":{"_source":{"enabled":true,"excludes":[],"includes":["product_id"]},"dynamic":"false","properties":{"price":{"boost":1.0,"enabled":true,"ignore_above":-1,"index":true,"similarity":"classic","type":"double"},"product_id":{"boost":1.0,"enabled":true,"ignore_above":128,"index":true,"similarity":"classic","type":"keyword"},"product_name":{"boost":1.0,"enabled":true,"ignore_above":-1,"index":true,"similarity":"classic","type":"text"},"product_title":{"analyzer":"chinese","boost":1.0,"enabled":true,"ignore_above":-1,"index":true,"similarity":"classic","type":"text"}}}}} |
## TFT.ADDDOC
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.ADDDOC index document [WITH_ID doc_id] |
| 命令描述 | 向索引中插入一个文档（document），可通过 WITH_ID 指定该文档在索引内的唯一 ID（doc_id），若 doc_id 已存在，则更新并覆盖原文档。若不指定 WITH_ID （默认），则自动生成 doc_id。 |
| 选项 | index ：待操作的索引名称。 document ：插入的文档，JSON 格式，插入的值需与该字段定义的数据类型一致。 说明 若索引通过 _source 的 includes 参数配置了仅保存部分字段，则在插入或更新文档时仅保存 includes 中配置的字段。 WITH_ID doc_id ：是否指定文档 ID，如需指定文档 ID 需输入 doc_id 值，doc_id 的格式为任意字符串。 |
| 返回值 | 执行成功：返回文档 ID，格式为 JSON。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.ADDDOC idx:product '{"product_id":"product test"}' WITH_ID 00001 返回示例： {"id":"00001"} 数组的添加示例： TFT.ADDDOC idx:product '{"product_id":["an","2","3df"]}' WITH_ID 00001 |
## TFT.MADDDOC
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.MADDDOC index document doc_id [document1 doc_id1] ... |
| 命令描述 | 向索引中插入多个文档（document），每个文档必须指定文档 ID（doc_id）。若某个文档写入失败（例如写入的文档内容与定义的格式不符），则该命令的所有文档均不会写入。 |
| 选项 | index ：待操作的索引名称。 document ：插入的文档，JSON 格式，插入的值需与该字段定义的数据类型一致。 说明 若索引通过 _source 的 includes 参数配置了仅保存部分字段，则在插入或更新文档时仅保存 includes 中配置的字段。 doc_id ：指定文档 ID，doc_id 的格式为任意字符串。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.MADDDOC idx:product '{"product_id":"test1"}' 00011 '{"product_id":"test2"}' 00012 返回示例： OK |
## TFT.UPDATEDOCFIELD
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.UPDATEDOCFIELD index doc_id document |
| 命令描述 | 更新索引中 doc_id 指定的文档，若更新的字段为 mapping 指定的索引字段时，该字段更新的内容需与 mapping 指定的类型一致；若非索引字段，支持更新任意字段类型的内容。 说明 若更新的字段已存在，则更新原文档，若字段不存在，则新增该字段。若指定的文档不存在，该命令支持自动创建文档，此时效果等同于 TFT.ADDDOC。 |
| 选项 | index ：待操作的索引名称。 doc_id ：指定文档 ID。 document ：更新的文档内容，JSON 格式。 说明 若索引通过 _source 的 includes 参数配置了仅保存部分字段，则在插入或更新文档时仅保存 includes 中配置的字段。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.UPDATEDOCFIELD idx:product 00011 '{"product_id":"test8","product_group":"BOOK"}' 返回示例： OK |
## TFT.DELDOCFIELD
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.DELDOCFIELD index doc_id field [field1 field2 ...] |
| 命令描述 | 删除索引中 doc_id 指定文档的指定字段，若该字段为索引字段，会同时在索引中删除该字段的信息。 说明 若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| 选项 | index ：待操作的索引名称。 doc_id ：指定文档 ID。 field ：待删除的字段。 |
| 返回值 | 执行成功：返回成功删除的字段数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.DELDOCFIELD idx:product 00011 product_group 返回示例： (integer) 1 |
## TFT.INCRLONGDOCFIELD
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.INCRLONGDOCFIELD index doc_id field increment |
| 命令描述 | 向索引中 doc_id 指定文档的指定字段增加整数值（increment），支持指定 increment 为负数，支持指定的字段类型为 long 或 int 类型。 说明 若指定的文档不存在，该命令支持自动创建文档，初始化字段的值为 0，并增加指定的 increment。若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| 选项 | index ：待操作的索引名称。 doc_id ：指定文档 ID。 field ：待操作的字段，支持的字段类型为 long 或 int 类型，且不支持数组类型的字段。 increment ：待增加操作的值，可以指定该值为负数实现相减，数据类型为整型（int）。 |
| 返回值 | 执行成功：返回执行操作后字段的数值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.INCRLONGDOCFIELD idx:product 00011 stock 100 返回示例： (integer)100 |
## TFT.INCRFLOATDOCFIELD
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.INCRFLOATDOCFIELD index doc_id field increment |
| 命令描述 | 向索引中 doc_id 指定文档的指定字段增加浮点数值（increment），支持指定 increment 为负数，支持指定的字段类型为 double 类型。 说明 若指定的文档不存在，该命令支持自动创建文档，初始化字段的值为 0，并增加指定的 increment。若指定的字段不存在（例如被 _source 过滤的字段），则操作失败。 |
| 选项 | index ：待操作的索引名称。 doc_id ：指定文档 ID。 field ：待操作的字段，支持的字段类型 double 类型，且不支持数组类型的字段。 increment ：待增加操作的值，可以指定该值为负数实现相减，数据类型为双精度浮点型（double）。 |
| 返回值 | 执行成功：返回执行操作后字段的数值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.INCRFLOATDOCFIELD idx:product 00011 stock 299.6 返回示例： "299.6" |
## TFT.GETDOC
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.GETDOC index doc_id |
| 命令描述 | 获取索引中指定 doc_id 的文档内容。 |
| 选项 | index ：待查询的索引名称。 doc_id ：指定文档 ID。 |
| 返回值 | 执行成功：返回文档 ID 和文档内容。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.GETDOC idx:product 00011 返回示例： {"_id":"00011","_source":{"product_id":"test8"}} |
## TFT.EXISTS
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.EXISTS index doc_id |
| 命令描述 | 查询索引中指定 doc_id 的文档是否存在。 |
| 选项 | index ：待查询的索引名称。 doc_id ：指定文档 ID。 |
| 返回值 | 执行成功： 若文档存在，返回 1。 若索引或文档不存在，返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.EXISTS idx:product 00011 返回示例： (integer) 1 |
## TFT.DOCNUM
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.DOCNUM index |
| 命令描述 | 获取索引中的文档数量。 |
| 选项 | index ：待查询的索引名称。 |
| 返回值 | 执行成功：索引的文档数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.DOCNUM idx:product 返回示例： (integer) 3 |
## TFT.SCANDOCID
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.SCANDOCID index cursor [MATCH *value*] [COUNT count] |
| 命令描述 | 获取索引中所有的 doc_id。 |
| 选项 | index ：待查询的索引名称。 cursor ：指定本次扫描的游标。 MATCH *value* ：模式匹配，value 为待匹配的值，例如 MATCH *redis* 。 COUNT count ：指定本次扫描的最大数量，默认为 100。 |
| 返回值 | 执行成功：返回一个数组。 第一个元素：下次查询的 cursor ，若该 key 已扫描完成，则返回 0。 第二个元素：本次查询的 doc_id。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.SCANDOCID idx:product 0 COUNT 3 返回示例： 1) "0" 2) 1) "00001" 2) "00011" 3) "00012" |
## TFT.DELDOC
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.DELDOC index doc_id [doc_id] ... |
| 命令描述 | 删除索引中 doc_id 指定的文档，支持指定多个 doc_id。 |
| 选项 | index ：待查询的索引名称。 doc_id ：指定文档 ID。 |
| 返回值 | 执行成功：返回成功删除的文档数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.DELDOC idx:product 00011 00014 返回示例： "1" # 本示例中 ID"00014"文档不存在，故仅删除 ID"00011"文档，返回 1。 |
## TFT.DELALL
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.DELALL index |
| 命令描述 | 删除索引中所有文档，但不会删除 index。 |
| 选项 | index ：待查询的索引名称。 doc_id ：指定文档 ID。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.DELALL idx:product 返回示例： OK |
## TFT.ANALYZER
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.ANALYZER analyzer_name text [INDEX index_name] [SHOW_TIME] |
| 命令描述 | 查询分词器分词效果。 |
| 选项 | analyzer_name ：分词器名称，支持内置分词器和自定义分词器。 若指定自定义分词器或修改了内置分词器的配置（停用词或词典），您还需要指定创建该分词器的索引名称（INDEX）。 text ：待分词的文档，utf-8 格式。 INDEX （可选）：分词器的索引名称。若指定自定义分词器或修改了内置分词器的配置（停用词或词典），该参数必选。 SHOW_TIME （可选）：指定是否返回分词执行的时间，单位为微秒（us）。 该时间包含词库加载的时间，当第一次加载 JiebaAnalyzer、IKAnalyzer 等具有较大内置词库的分词器时，耗时可能会达到秒级。 |
| 返回值 | 执行成功：返回 Token 信息，JSON 格式。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.ANALYZER standard "Tair is a nosql database" 返回示例： '{ "tokens":[ { "token":"Tair", "start_offset":0, "end_offset":4, "position":0 }, { "token":"nosql", "start_offset":10, "end_offset":15, "position":3 }, { "token":"database", "start_offset":16, "end_offset":24, "position":4 } ] }' |
## TFT.SEARCH
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.SEARCH index query |
| 命令描述 | 根据 query 语句搜索索引的文档，query 语法类似 [ES](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/query-dsl.html) [语法](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/query-dsl.html) 。 |
| 选项 | index 为待查询的索引名称； query 为类似 ES 语法的 DLS 语句，支持如下字段： query ：查询子句，支持如下语法。 match ：基础的匹配查询，支持如下参数。 在不需要对文档进行分词拆分或模糊匹配的场景下，推荐使用 term 、 prefix 等命令，以提高查询效率。 query ：查询的文档内容。 说明 未开启模糊匹配（ fuzziness ）时，query 中的文档会被指定分词器（ analyzer ）拆分成多个词根，同时您可以指定 operator （不同词根之间的关系）、 minimum_should_match （至少需要匹配多少个词根）参数。 开启了模糊匹配（ fuzziness ）时，上述参数将无效，您可以指定 prefix_length 参数。 analyzer ：指定 match 查询语句的分词器，支持 standard （默认，英文分词器）、 chinese 、 arabic 、 cjk 、 czech 、 brazilian 、 german 、 greek 、 persian 、 french 、 dutch 、 russian 和 jieba （中分分词），更多信息请参见 [Search](tairsearch-word-splitter.md) [分词器](tairsearch-word-splitter.md) 。 minimum_should_match ：查询语句会通过分词器拆分成多个词根，您可以通过本参数指定至少需要匹配多少个词根。该参数在未开启模糊匹配且 operator 为 OR 时生效。 operator ：指定通过分词器拆分的词根之间的关系，取值为 AND 和 OR（默认）。例如 '{"query":{"match":{"f0":{"query":"redis cluster","operator":"OR"}}}}' ，表示待搜索的文档中包含"redis"或"cluster"即满足查询条件。 fuzziness ：是否开启模糊匹配查询，默认为关闭， "fuzziness":1 为开启模糊匹配，例如 '{"query":{"match":{"f0":{"query":"excelentl","fuzziness":1}}}}' 。 prefix_length ：设置模糊匹配保持不变的起始字符数，默认为 0，该参数仅在开启模糊匹配时生效。 term ：词根查询，不会对查询内容进行拆分，效率比 match 高，支持查询所有字段类型。同时，该查询方式支持指定 lowercase 参数，表示是否将待查询的词根预先转换为小写，取值为 true（默认）和 false。例如 '{"query":{"term":{"f0":{"value":"redis","boost": 2.0}}}}' 或 '{"query":{"term":{"f0":{"value":"redis","lowercase": false}}}}' 。 若添加文档时使用的分词器不会将文档转化为小写，建议将 lowercase 参数设置为 false，否则可能查不到结果。 terms ：多词根查询，上限为 1024 个词根。同时，该查询方式支持指定 lowercase 参数，表示是否将待查询的词根预先转换为小写，取值为 true（默认）和 false。例如 '{"query":{"terms":{"f0":["redis","excellent"]}}}' 。 若添加文档时使用的分词器不会将文档转化为小写，建议将 lowercase 参数设置为 false，否则可能查不到结果。 range ：范围查询，支持所有字段类型，取值为 lt （小于）、 gt （大于）、 lte （小于等于）和 gte （大于等于），例如 '{"query":{"range":{"f0":{"lt":"abcd","gt":"ab"}}}}' 。 wildcard ：通配符查询，格式为 "wildcard":{"待查询 field":{"value":"查询内容"}} ，只支持 * 和 ? 通配符，例如 '{"query":{"wildcard":{"f0":{"value":"*b?Se"}}}}' 。 prefix ：前缀查询，例如 '{"query":{"prefix":{"f0":"abcd"}}' ，表示查询 f0 字段以 abcd 为开头的文档。 bool ：复合查询，上限为 1024 个词根，取值如下。 must ：查询结果需匹配 must 列表中所有查询子句，例如 '{"query":{"bool":{"must":[{"match":{"DB":"redis"}},{"match":{"Architectures":"cluster"}}]}}}' ，表示查询 DB 为 Redis、架构（Architectures）为 cluster 的文档。 must_not ：查询结果需不匹配 must_not 列表中所有查询子句。 should ：查询结果需匹配 should 列表中任意一个查询子句（表示或），可指定 minimum_should_match 参数。 minimum_should_match ：该参数需搭配 should 语句使用，表示至少需匹配多少个查询子句。若 bool 语句中只有 should 语句，则该参数默认为 1； bool 语句中还有 must 或 must_not 语句，则该参数默认为 0。例如 '{"query":{"bool":{"minimum_should_match":1,"should":[{"match":{"DB":"redis"}},{"match":{"Architectures":"cluster"}}]}}}' ，表示查询 DB 为 Redis 或架构（Architectures）为 cluster 的文档。 说明 bool 查询语句中可嵌套任何类型的子查询语句，例如嵌套 bool 语句，示例为 TFT.SEARCH idx:product '{"query":{"bool":{"must":[{"term":{"product_name":"apple"}},{"bool":{"minimum_should_match":1,"should":[{"term":{"price":19.5}},{"term":{"product_id":"fruits_2"}}]}}]}}}' 。 dis_max ：最佳匹配复合查询，默认返回 queries 查询子句中单个 query 分数最高的结果在首位。 若指定了 tie_breaker 参数，将增加匹配多个查询子句的文档分数， tie_breaker 的取值范围为[0，1]，默认为 0。指定 tie_breaker 后，目标文档分数的计算规则为：query 的最高分+（（将除最高分以外的 query 分数相加） * tie_breaker ）。例如查询中有 3 个子句，tie_breaker 为 0.5，doc1 在每个子句的分数为[5,1,3]，最终 doc1 分数为 5+((1+3)*0.5)。 命令示例为 '{"query":{"dis_max":{"queries":[{"term":{"f0":"redis"}},{"term":{"f1":"database"}},{"match":{"title":"redis memory database"}}],"tie_breaker": 0.5}}}' 。 constant_score ：固定分数的复合查询，通过 filter 查询并返回任意一个符合的文档，支持设置权重（boost，double 类型，默认为 1.0），文档将以指定的 boost 返回。例如 '{"query":{"constant_score":{"filter":{"term":{"f0":"abc"}},"boost":1.2}}}' 。 match_all ：查询全部文档，支持设置权重（boost，double 类型，默认为 1.0），可以将指定的分数赋予所有返回的文档，例如 '{"query":{"match_all":{"boost":2.3}}}' 。 说明 通过 bool 、 dis_max 与 constant_score 进行复合查询时，可对 term 、 terms 、 range 、 wildcard 设置权重（boost，默认为 1），区分多个条件的权重，例如 '{"query":{"bool":{"must":[{"match":{"f0":"v0"}},"term":{"f0":{"value":"redis","boost":2}}]}}}' 。 sort ：结果排序，但不支持指定数组类型的字段，取值如下。 _score （默认）：按计分权重降序，示例为 "sort":"_score" 。 _doc ：按文档 ID 升序，示例为 "sort":"_doc" 。 指定字段：按指定字段升序，该字段必须为索引（index 为 true）字段或开启强制类型检查（enabled 为 true）的字段，同时仅支持指定字段类型为：keyword、long、integer、double。例如 "sort":"price" ，表示指定以 price 字段升序排序。 支持输入一个数组进行多条件排序，将按照数组内的顺序进行排序，可通过 order 调整默认顺序，取值为 desc （降序）和 acs （升序）。例如 '{"sort":[{"price":{"order":"desc"}},{"_doc":{"order":"desc"}}]}' ，表示优先根据 price 排序，在 price 相同时根据_doc 排序。 _source ：指定查询结果中的字段，可指定 includes （需要展示的 field）和 excludes （不需要展示的 field），支持配置通配符模式（WildCard）的 field。例如 "_source":{"includes":["f0"] ，表示查询结果仅返回 f0 字段。 aggs ：对 query 查询子句的结果进行聚合。若字段为数组类型，则仅支持 Terms Aggregation。语法与示例请参见 [Aggregations](tairsearch.md) [介绍](tairsearch.md) 。 track_total_hits ：通过 term 、 terms 、 match （不开启模糊匹配）语句查询（含复合查询）时，是否查询所有文档。取值如下： false （默认）：仅查询 score 排名前 100 的文档。 true ：查询所有文档。 警告 开启后，若命中的文档数过多会导致慢查询，请谨慎使用。 from ：指定开始返回的目标文档起点，默认为 0，表示从第一个查到的文档开始返回。 size ：返回查询的文档数量，默认为 10，取值范围为[0,10000]。size 为 0 表示结果集中不返回具体的文档， 只返回命中查询的总文档数量（total）。 说明 可通过 from 和 size 参数到达分页的效果，但分页越多越影响性能。 |
| 返回值 | 执行成功：返回查询到的文档信息。 说明 返回参数中的 relation 为查询到的文档数量，取值： eq （表示查询到的文档数量等于 value 值）、 gte （表示大于或等于 value 值），示例如下。 { "hits": { "hits": [], "max_score": null, "total": { "relation": "gte", "value": 100 } } } 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.SEARCH idx:product '{"sort":[{"price":{"order":"desc"}}]}' 返回示例： {"hits":{"hits":[{"_id":"fruits_3","_index":"idx:product","_score":1.0,"_source":{"product_id":"fruits_3","product_name":"orange","price":30.2,"stock":3000}},{"_id":"fruits_2","_index":"idx:product","_score":1.0,"_source":{"product_id":"fruits_2","product_name":"banana","price":24.0,"stock":2000}},{"_id":"fruits_1","_index":"idx:product","_score":1.0,"_source":{"product_id":"fruits_1","product_name":"apple","price":19.5,"stock":1000}}],"max_score":1.0,"total":{"relation":"eq","value":3}}} 更多示例，请参见 [TFT.Search](tairsearch.md) [查询示例](tairsearch.md) 。 |
## TFT.MSEARCH
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.MSEARCH index_count index [index1] ... query |
| 命令描述 | 根据 query 语句搜索多个索引的文档（待查询索引的 mappings 和 settings 的配置必须相同），汇聚多个索引的查询结果，再次进行打分、排序、聚合并返回。 说明 TFT.MSEARCH 命令返回的结果是对多个索引的查询结果再次进行打分、排序、聚合的结果，该结果不等同于对多个索引的数据集合直接进行打分、排序、聚合等结果。TFT.MSEARCH 的策略如下： 打分和排序：对子结果集再进行打分、排序。 聚合： Sum、max、min、avg、value_count：对子结果集再进行同等属性的聚合运算。 Sum_of_squares、variance、std_deviation：对子结果集进行取均值运算。 Terms Aggregation 和 Filter Aggregation：对子结果集再进行统计聚合运算。 |
| 选项 | index_cout ：待查询的索引数量，取值范围为[1,100]。 index ：待查询的索引名称。查询多个索引时，待查询索引的 mappings 和 settings 的配置必须相同，若各索引的 mappings 配置不一致或索引不存在均会报错。 query ：聚合查询语句，支持如下参数： query ：查询子句。 sort ：结果排序，但不支持指定数组类型的字段。 _source ：指定查询结果中的字段。 aggs ：对 query 查询子句的结果进行聚合。若字段为数组类型，则仅支持 Terms Aggregation。 track_total_hits ：通过 term、terms、match（不开启模糊匹配）语句查询（含复合查询）时，是否查询所有文档。 size ：指定查询返回的文档数量。 可通过 size 、 reply_with_keys_cursor 与 keys_cursor 参数实现分页查询。若 keys_cursor 为 0（默认情况下）， Tair 会在各索引的查询结果中，从排序最高的文档（第一位）开始，获取指定数量的文档；若 keys_cursor 不为 0，则从指定位置开始获取指定数量的文档，再将多个索引的查询结果汇聚在一起，进行打分、排序、聚合，并输出最终文档。 例如单次查询 3 个索引（key0、key1、key2），设置 size 为 10： 首次搜索，可设置 keys_cursor 为 0： Tair 会从 3 个索引中各搜索出排序靠前的 10 个文档（此时共有 30 个候选文档），然后汇聚、打分、排序、聚合等，输出整体排名靠前的 10 个文档。返回的 keys_cursor 示例为 {"keys_cursor":{"key0":2,"key1":5,"key2":3}} 。 第二次查询时，可使用同样的查询语句，并加上 {"keys_cursor":{"key0":2,"key1":5,"key2":3}} ： Tair 会在各个索引中，从指定的位置开始再获取 10 个文档（例如 key0 从第 3 位开始向后获取 10 个文档，key1 与 key2 也类似，此时仍有 30 个候选文档），再将多个索引的查询结果汇聚在一起，进行打分、排序、聚合，并输出最终文档。 reply_with_keys_cursor ：指定是否返回每个索引下一轮查询的游标信息，取值：true、false（默认）。 keys_cursor ：指定本次查询的各索引的游标，可以将上轮查询返回的 keys_cursor 作为本次查询的输入，实现分页查询。默认为 0，表示第一位。 说明 相比较 TFT.SEARCH 的 query 语句，TFT.MSEARCH 的 query 不支持 from 参数，但可以通过 size 、 reply_with_keys_cursor 与 keys_cursor 参数实现分页查询，其余参数语法均可参见 [TFT.SEARCH](tairsearch.md) 。 |
| 返回值 | 执行成功：返回查询到的文档信息，与 TFT.SEARCH 的返回结果类似，同时还会返回 aux_info 。 aux_info 字段中包含：索引 mappings 和 settings 的 CRC-64 值（业务请求可忽略该值）、 keys_cursor 值（可选，下次各索引开始查询的游标位置）、 field_type 值（字段的数据类型，仅在根据索引字段排序时返回）， aux_info 示例如下： { "aux_info":{ "index_crc64":15096806844241479487, "keys_cursor":{ "key0":2, "key1":5, "key2":3 }, "field_type":{ "f0":"long" } } } 其他情况返回相应的异常信息。 |
| 示例 | 提前执行如下命令： TFT.CREATEINDEX key0 '{"mappings":{"properties":{"f0":{"type":"long"}}}}' TFT.CREATEINDEX key1 '{"mappings":{"properties":{"f0":{"type":"long"}}}}' TFT.CREATEINDEX key2 '{"mappings":{"properties":{"f0":{"type":"long"}}}}' TFT.ADDDOC key0 '{"f0":120}' TFT.ADDDOC key0 '{"f0":130}' TFT.ADDDOC key1 '{"f0":140}' TFT.ADDDOC key1 '{"f0":150}' TFT.ADDDOC key2 '{"f0":160}' TFT.ADDDOC key2 '{"f0":170}' 命令示例： TFT.MSEARCH 3 key0 key1 key2 '{"size":2,"query":{"range":{"f0":{"gt":120,"lte":170}}},"sort":[{"f0":{"order":"desc"}}],"reply_with_keys_cursor":true}' 返回示例： {"hits":{"hits":[{"_id":"16625439765504840","_index":"key2","_score":1.0,"_source":{"f0":170}},{"_id":"16625439741096630","_index":"key2","_score":1.0,"_source":{"f0":160}}],"max_score":1.0,"total":{"relation":"eq","value":5}},"aux_info":{"index_crc64":10084399559244916810,"keys_cursor":{"key0":0,"key1":0,"key2":2}}} 第二页查询命令示例： TFT.MSEARCH 3 key0 key1 key2 '{"size":2,"query":{"range":{"f0":{"gt":120,"lte":170}}},"sort":[{"f0":{"order":"desc"}}],"reply_with_keys_cursor":true,"keys_cursor":{"key0":0,"key1":0,"key2":2}}' # 查询语句与第一次查询相同，但需要增加上轮查询返回的 keys_cursor 信息。 返回示例： {"hits":{"hits":[{"_id":"16625439652681160","_index":"key1","_score":1.0,"_source":{"f0":150}},{"_id":"16625439624704580","_index":"key1","_score":1.0,"_source":{"f0":140}}],"max_score":1.0,"total":{"relation":"eq","value":5}},"aux_info":{"index_crc64":10084399559244916810,"keys_cursor":{"key0":0,"key1":2,"key2":2}}} |
## TFT.EXPLAINCOST
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.EXPLAINCOST index query |
| 命令描述 | 查询 query 语句的执行耗时，返回内容包括查询过程中涉及到的文档集合数及各阶段的耗时。 |
| 选项 | index ：待查询的索引名称。 query ：查询语句，语法与 TFT.SEARCH 相同。 |
| 返回值 | 执行成功：返回查询耗时信息，JSON 格式，整体耗时由如下三部分组成。 QUERY_COST ：query 查询耗时，单位为微秒（time_cost_us）。同时还包含查询视图信息（query）和 query 对应的文档集合数（doc_num）。若涉及 bool 查询方法会展示 bool 查询过程的步骤耗时（steps）。 AGGS_COST ：查询过程中聚合（Aggregations）的耗时，单位为微秒（time_cost_us），若查询语句中没有指定聚合查询，则无该耗时。 COLLECTOR_COST ：查询结果采集、排序的耗时，单位为微秒（time_cost_us），同时还包含排序类型（collector_type），返回值为 sort 排序（ScoreCollector）和分数排序（CustomSortCollector）。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.EXPLAINCOST idx:product '{"sort":[{"price":{"order":"desc"}}]}' 返回示例： { "QUERY_COST": { "query": "MATCHALL_QUERY", "doc_num": 1, "time_cost_us": 2 }, "COLLECTOR_COST": { "collector_type": "CustomSortCollector", "time_cost_us": 20 } } |
## TFT.EXPLAINSCORE
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.EXPLAINSCORE index query [doc_id] ... |
| 命令描述 | 查询执行 query 语句的计分详情信息，您可以通过该命令了解文档分数的计算过程，并优化 Search 语句，提升文档的查询效果。 该命令当前仅内存型（兼容 Redis 6.0）支持。 |
| 选项 | index ：待查询的索引名称。 query ：查询语句，语法与 TFT.SEARCH 相同。 doc_id ：指定文档 ID，若指定了该参数，返回结果只会包含 doc_id 对应的文档。 |
| 返回值 | 执行成功：返回查询到的文档信息，在 TFT.SERACH 返回结果的基础上增加每个文档的计分详情信息（ _explanation ）， _explanation 中存在如下字段。 score ：该文档的得分。 description ：score 计算使用的公式。 field ：该文档被 query 中指定的 field 所命中。 term ：该文档被 query 中指定的词项所命中。 query_boost ：该文档在本次查询中的计分权重。 details ：文档的元数据与计分过程。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.EXPLAINSCORE today_shares '{"query":{"wildcard":{"shares_name":{"value":"*BY"}}}}' 返回示例： { "hits": { "hits": [ { "_id": "17036492095306830", "_index": "today_shares", "_score": 1.0, "_source": { "shares_name": "YBY", "logictime": 14300410, "purchase_type": 1, "purchase_price": 11.1, "purchase_count": 100, "investor": "Mila" }, "_explanation": { "score": 1.0, "description": "score, computed as query_boost", "field": "shares_name", "term": "*BY", "query_boost": 1.0 } } ], "max_score": 1.0, "total": { "relation": "eq", "value": 1 } } } |
## TFT.ADDSUG
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.ADDSUG index text weight [text weight] ... |
| 命令描述 | 在指定索引中，添加自动补全的文本及对应权重，支持添加多个文本。 |
| 选项 | index ：待操作的索引名称。 text ：自动补全文本。 weight ：对应文本的计分权重，范围为正整数。 |
| 返回值 | 执行成功：返回成功添加的文档数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.ADDSUG idx:redis 'redis is a memory database' 3 'redis cluster' 10 返回示例： (integer) 2 |
## TFT.DELSUG
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.DELSUG index text [text] ... |
| 命令描述 | 在指定索引中，删除自动补全的文本，支持删除多个文本。 |
| 选项 | index ：待查询的索引名称。 text ：待删除的文本，需指定完整、正确的文本。 |
| 返回值 | 执行成功：返回成功删除的文本数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.DELSUG idx:redis 'redis is a memory database' 'redis cluster' 返回示例： (integer) 2 |
## TFT.SUGNUM
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.SUGNUM index |
| 命令描述 | 获取指定索引中自动补全文本的数量。 |
| 选项 | index ：待查询的索引名称。 |
| 返回值 | 执行成功：返回索引中的文本数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.SUGNUM idx:redis 返回示例： (integer) 3 |
## TFT.GETSUG
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.GETSUG index prefix [MAX_COUNT count] [FUZZY] |
| 命令描述 | 根据指定前缀，查询匹配的自动补全文本，将优先返回权重比较高的 text。 |
| 选项 | index ：待查询的索引名称。 prefix ：指定的查询前缀。 MAX_COUNT count ：配置返回文本的最大数量，count 的取值范围为[0,255]。 FUZZY ：是否启用模糊匹配。 |
| 返回值 | 执行成功：返回自动补全文本的列表。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.GETSUG idx:redis res MAX_COUNT 2 FUZZY 返回示例： 1) "redis cluster" 2) "redis lock" |
## TFT.GETALLSUGS
| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.GETALLSUGS index |
| 命令描述 | 获取指定索引的全量自动补全文本。 |
| 选项 | index ：待查询的索引名称。 |
| 返回值 | 执行成功：返回自动补全文本的列表。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.GETALLSUGS idx:redis 返回示例： 1) "redis cluster" 2) "redis lock" 3) "redis is a memory database" |
## Aggregations介绍
您可以在[TFT.SEARCH](tairsearch.md)请求中添加aggs（或aggregations）子句，对query查询子句的结果进行聚合。
### 用法
通常情况下，在aggs子句中，您需要自定义聚合名称，并指定聚合类型与聚合字段（field），仅支持聚合数值类型与keyword类型的字段，例如：
TFT.SEARCH shares '{"query":{"term":{"investor":"Jay"}},"aggs":{"Jay_Sum":{"sum":{"field":"purchase_price"}}}}' # 自定义聚合名称为Jay_Sum、聚合类型为sum（求和）、聚合字段为purchase_price。
返回结果包含query的查询结果和aggs的聚合结果：
{"hits":{"hits":[{"_id":"16581351808123930","_index":"today_shares0718","_score":1.0,"_source":{"shares_name":"XAX","logictime":14300210,"purchase_type":1,"purchase_price":101.1,"purchase_count":100,"investor":"Jay"}},{"_id":"16581351809626430","_index":"today_shares0718","_score":1.0,"_source":{"shares_name":"XAX","logictime":14300310,"purchase_type":1,"purchase_price":111.1,"purchase_count":100,"investor":"Jay"}}],"max_score":1.0,"total":{"relation":"eq","value":2}},"aggregations":{"Jay_Sum":{"value":212.2}}}
说明
您可以在查询语句中加上"size":0，将仅返回aggs的结果。
### aggs聚合类型
aggs支持Metric Aggregation、Terms Aggregation、Filter Aggregation功能。
| 类别 | 说明 |
| --- | --- |
| Metric（指标） Aggregation | 一般是对数值类型（例如 integer、double 等）字段进行数值计算或统计，不支持嵌套子聚合。支持如下指标： sum ：求和。 max ：最大值。 min ：最小值。 avg ：平均值。 sum_of_squares ：平方和。 variance ：方差。 std_deviation ：标准差。 value_count ：统计 value 个数，不进行去重，支持数值类型与 keyword 类型字段。 extended_stats ：进行上述所有指标的计算，一次性返回各类结果。 说明 除 value_count 外，其余指标均只支持数值类型字段。 返回结果：指定字段进行计算后的值，类型均为 double。 |
| Terms Aggregation | 统计 value 的去重个数，仅支持 keyword 类型字段，支持嵌套子聚合，参数说明如下： terms field ：聚合字段，仅支持 keyword 类型字段。 size ：返回查询结果的数量，默认为 10，取值范围为[1,65536)。 order ：返回 object 的排序规则，取值如下： _count （默认）：按结果数量排序，取值为 desc （降序，默认）和 asc （升序），示例为 "order":{"_count":"desc"} 。 _key ：按目标字段的字符排序，取值为 desc （降序）和 asc （升序），示例为 "order":{"_key":"desc"} 。 min_doc_count ：最小文档数，默认为 1，查询结果的文档数若小于该数量将不显示。 include ：指定 value 需包含或匹配的字符串，当目标字段为 String 类型时，支持正则匹配；当目标字段为数组时，需完全匹配字符串。 exclude ：指定 value 不能包含或匹配的字符串，目标字段的类型要求与 include 相同，若同时存在 include 和 exclude ，将先检查 include 再检查 exclude 。 部分请求示例： { "aggs": { "Per_Investor_Freq":{ "terms": { "field": "investor" } } } } 返回结果：聚合名称为 key，类型为 Object 的 JSON 内容。Object 中以 buckets 为数组 key，数组中的 value 为对应 key 和 doc_count 统计结果。示例如下： { "aggregations": { "Per_Investor_Freq": { "buckets": [ { "doc_count": 2, "key": "Jay" }, { "doc_count": 1, "key": "Mila" } ] } } } |
| Filter Aggregation | filter 中可输入 query 语句，对 query 查询结果进行再次过滤，支持嵌套子聚合。 返回结果：符合过滤条件的文档个数（ doc_count ）。 |
### Aggregations查询示例
创建索引。
TFT.CREATEINDEX today_shares '{"mappings":{"properties":{"shares_name":{"type":"keyword"},"logictime":{"type":"long"},"purchase_type":{"type":"integer"},"purchase_price":{"type":"double"},"purchase_count":{"type":"long"},"investor":{"type":"keyword"}}}}' # 创建今日股票交易量索引 # shares_name：股票名称 # logictime：成交时间点 # purchase_type：购买类型 # purchase_price：成交价格 # purchase_count：成交数 # investor：投资者ID
预计输出：
OK
添加文档数据。
依次执行如下命令。
TFT.ADDDOC today_shares '{"shares_name":"XAX","logictime":14300210, "purchase_type":1,"purchase_price":101.1, "purchase_count":100,"investor":"Jay"}' TFT.ADDDOC today_shares '{"shares_name":"XAX","logictime":14300310, "purchase_type":1,"purchase_price":111.1, "purchase_count":100,"investor":"Jay"}' TFT.ADDDOC today_shares '{"shares_name":"YBY","logictime":14300410, "purchase_type":1,"purchase_price":11.1, "purchase_count":100,"investor":"Mila"}'
预计输出：
OK
进行查询。
查询示例如下：
## sum
# 查询Jay购买股票的总金额。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"investor":"Jay"}},"aggs":{"Jay_Sum":{"sum":{"field":"purchase_price"}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":2}},"aggregations":{"Jay_Sum":{"value":212.2}}}
## max
# 查询Jay购买单只股票的最大金额。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"investor":"Jay"}},"aggs":{"Jay_Max":{"max":{"field":"purchase_price"}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":2}},"aggregations":{"Jay_Max":{"value":111.1}}}
## avg
# 查询Jay购买不同股票的平均金额。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"investor":"Jay"}},"aggs":{"Jay_Avg":{"avg":{"field":"purchase_price"}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":2}},"aggregations":{"Jay_Avg":{"value":106.1}}}
## std_deviation
# 查询Jay购买股票金额的标准差。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"investor":"Jay"}},"aggs":{"Jay_Std_Deviation":{"std_deviation":{"field":"purchase_price"}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":2}},"aggregations":{"Jay_Std_Deviation":{"value":5.0}}}
## extended_stats
# 查询Jay购买股票的整体行情（各指标值）。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"investor":"Jay"}},"aggs":{"Jay_Extended_Stats":{"extended_stats":{"field":"purchase_price"}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":2}},"aggregations":{"Jay_Extended_Stats":{"count":2,"sum":212.2,"max":111.1,"min":101.1,"avg":106.1,"sum_of_squares":10221.21,"variance":25.0,"std_deviation":5.0}}}
## terms
# 统计交易2笔以上的投资者。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"purchase_type":1}},"aggs":{"Per_Investor_Freq":{"terms":{"field":"investor","min_doc_count":2,"order": {"_key":"desc"}}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":3}},"aggregations":{"Per_Investor_Freq":{"buckets":[{"key":"Jay","doc_count":2}]}}}
## terms嵌套
# 统计各股票的交易记录总数以及每种股票的平均成交额，但不包含“XAX”股票。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"purchase_type":1}},"aggs":{"Per_Investor_Freq":{"terms":{"field":"shares_name","include":"[A-Z]+","exclude":["XAX"]},"aggs":{"Price_Avg":{"avg":{"field":"purchase_price"}}}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":3}},"aggregations":{"Per_Investor_Freq":{"buckets":[{"key":"YBY","doc_count":1,"Price_Avg":{"value":11.1}}]}}}
## filter嵌套
# 统计Jay购买股票的数量与整体行情（各指标值）。 TFT.SEARCH today_shares '{"size":0,"query":{"term":{"purchase_type":1}}, "aggs":{"Jay_BuyIn_Filter": {"filter": {"term":{"investor": "Jay"}},"aggs":{"Jay_BuyIn_Quatation":{"extended_stats":{"field":"purchase_price"}}}}}}' # 预期输出： {"hits":{"hits":[],"max_score":null,"total":{"relation":"eq","value":3}},"aggregations":{"Jay_BuyIn_Filter":{"doc_count":2,"Jay_BuyIn_Quatation":{"count":2,"sum":212.2,"max":111.1,"min":101.1,"avg":106.1,"sum_of_squares":10221.21,"variance":25.0,"std_deviation":5.0}}}}
## TFT.Search查询示例
创建水果商品索引。
TFT.CREATEINDEX idx:product '{"mappings":{"_source":{"enabled":true},"properties":{"product_id":{"type":"keyword","ignore_above":128},"product_name":{"type":"text"},"product_title":{"type":"text","analyzer":"jieba"},"product_group":{"type":"text","analyzer":"jieba"},"price":{"type":"double"},"stock":{"type":"integer"}}}}'
预期输出：
OK
添加文档数据。
TFT.MADDDOC idx:product '{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}' fruits_1 '{"product_id":"fruits_002","product_name":"banana","product_title":"新鲜野生超甜香蕉。","product_group":"菲律宾","price":24.0,"stock":2000}' fruits_2 '{"product_id":"fruits_003","product_name":"orange","product_title":"网红橘子、新鲜柑橘。","product_group":"中国重庆","price":30.2,"stock":3000}' fruits_3
预期输出：
OK
进行查询。
查询示例如下：
## match_all
# 查询全部文档，设置返回的分数为1.2。 TFT.SEARCH idx:product '{"query":{"match_all":{"boost":1.2}}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":1.2,"_source":{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}},{"_id":"fruits_2","_index":"idx:product","_score":1.2,"_source":{"product_id":"fruits_002","product_name":"banana","product_title":"新鲜野生超甜香蕉。","product_group":"菲律宾","price":24.0,"stock":2000}},{"_id":"fruits_3","_index":"idx:product","_score":1.2,"_source":{"product_id":"fruits_003","product_name":"orange","product_title":"网红橘子、新鲜柑橘。","product_group":"中国重庆","price":30.2,"stock":3000}}],"max_score":1.2,"total":{"relation":"eq","value":3}}}
## match
# 查询product_group为华东地区山东省的文档，设置仅返回product_name、price、stock字段。 TFT.SEARCH idx:product '{"query":{"match":{"product_group":"华东地区山东省"}},"_source":{"includes":["product_name","price","stock"]}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product_fruits","_score":0.278921,"_source":{"product_name":"apple","price":19.5,"stock":1000}}],"max_score":0.278921,"total":{"relation":"eq","value":1}}} # 模糊搜索product_name为aple fruit的文档，并指定通过分词器拆分的词根之间的关系为或。 TFT.SEARCH idx:product '{"query":{"match":{"product_name":{"query":"aple fruit","fuzziness":1,"operator":"OR"}}}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":1.405465,"_source":{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}}],"max_score":1.405465,"total":{"relation":"eq","value":1}}}
## term
# 查询product_name为apple的文档，设置仅返回product_name、price、stock字段。 TFT.SEARCH idx:product '{"query":{"term":{"product_name":{"value":"apple"}}},"_source":{"includes":["product_name","price","stock"]}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":1.405465,"_source":{"product_name":"apple","price":19.5,"stock":1000}}],"max_score":1.405465,"total":{"relation":"eq","value":1}}}
## terms
# 查询product_name为apple和banana的文档，设置仅返回product_name、price、stock字段。 TFT.SEARCH idx:product '{"query":{"terms":{"product_name":["apple","banana"]}},"_source":{"includes":["product_name","price","stock"]}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":0.496907,"_source":{"product_name":"apple","price":19.5,"stock":1000}},{"_id":"fruits_2","_index":"idx:product","_score":0.496907,"_source":{"product_name":"banana","price":24.0,"stock":2000}}],"max_score":0.496907,"total":{"relation":"eq","value":2}}}
## wildcard
# 查询product_name为*pp?e的文档。 TFT.SEARCH idx:product '{"query":{"wildcard":{"product_name":{"value":"*pp?e"}}}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":1.0,"_source":{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}}],"max_score":1.0,"total":{"relation":"eq","value":1}}}
## prefix
# 查询product_name前缀为ap的文档。 TFT.SEARCH idx:product '{"query":{"prefix":{"product_name":{"value":"ap"}}}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":1.0,"_source":{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}}],"max_score":1.0,"total":{"relation":"eq","value":1}}}
## range与sort
# 查询price大于15且小于等于30的文档，设置返回结果以price降序排序，同时设置仅返回product_name、price、stock字段。 TFT.SEARCH idx:product '{"query":{"range":{"price":{"gt":15,"lte":30}}},"sort":[{"price":{"order":"desc"}}],"_source":{"includes":["product_name","price","stock"]}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_2","_index":"idx:product","_score":1.0,"_source":{"product_name":"banana","price":24.0,"stock":2000}},{"_id":"fruits_1","_index":"idx:product","_score":1.0,"_source":{"product_name":"apple","price":19.5,"stock":1000}}],"max_score":1.0,"total":{"relation":"eq","value":2}}}
## bool
# 查询product_name为apple且product_group为中国的文档。 TFT.SEARCH idx:product '{"query":{"bool":{"must":[{"term":{"product_name":{"value":"apple"}}},{"match":{"product_group":"中国"}}]}}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":1.575668,"_source":{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}}],"max_score":1.575668,"total":{"relation":"eq","value":1}}}
## dis_max
# 输入product_group为中国、product_title为超甜以及product_title为香蕉，进行字段最佳匹配查询。 TFT.SEARCH idx:product '{"query":{"dis_max":{"queries":[{"term":{"product_group":"中国"}},{"term":{"product_title":"超甜"}},{"match":{"product_title":"香蕉"}}]}}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_2","_index":"idx:product","_score":0.614891,"_source":{"product_id":"fruits_002","product_name":"banana","product_title":"新鲜野生超甜香蕉。","product_group":"菲律宾","price":24.0,"stock":2000}},{"_id":"fruits_1","_index":"idx:product","_score":0.444693,"_source":{"product_id":"fruits_001","product_name":"apple","product_title":"新鲜农家有机红苹果。","product_group":"中国山东","price":19.5,"stock":1000}},{"_id":"fruits_3","_index":"idx:product","_score":0.444693,"_source":{"product_id":"fruits_003","product_name":"orange","product_title":"网红橘子、新鲜柑橘。","product_group":"中国重庆","price":30.2,"stock":3000}}],"max_score":0.614891,"total":{"relation":"eq","value":3}}}
## constant_score
# 查询product_group为中国的文档，设置返回的分数为1.2，同时设置仅返回product_name、price、stock字段。 TFT.SEARCH idx:product '{"query":{"constant_score":{"filter":{"term":{"product_group":"中国"}},"boost":1.2}},"_source":{"includes":["product_name","price","stock"]}}' # 预期输出： {"hits":{"hits":[{"_id":"fruits_1","_index":"idx:product","_score":1.2,"_source":{"product_name":"apple","price":19.5,"stock":1000}},{"_id":"fruits_3","_index":"idx:product","_score":1.2,"_source":{"product_name":"orange","price":30.2,"stock":3000}}],"max_score":1.2,"total":{"relation":"eq","value":2}}}
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
