OCNUM index | 获取索引中的文档数量。 |
| [TFT.SCANDOCID](tairsearch.md) | TFT.SCANDOCID index cursor [MATCH *value*] [COUNT count] | 获取索引中所有的 doc_id。 |
| [TFT.DELDOC](tairsearch.md) | TFT.DELDOC index doc_id [doc_id] ... | 删除索引中 doc_id 指定的文档，支持指定多个 doc_id。 |
| [TFT.DELALL](tairsearch.md) | TFT.DELALL index | 删除索引中所有文档，但不会删除 index。 |
| [TFT.ANALYZER](tairsearch.md) | TFT.ANALYZER analyzer_name text [INDEX index_name] [SHOW_TIME] | 查询分词器分词效果。 |
| [TFT.SEARCH](tairsearch.md) | TFT.SEARCH index query | 根据 query 语句搜索索引的文档，query 语法类似 [ES](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/query-dsl.html) [语法](https://www.elastic.co/guide/en/elasticsearch/reference/7.13/query-dsl.html) 。 |
| [TFT.MSEARCH](tairsearch.md) | TFT.MSEARCH index_count index [index1] ... query | 根据 query 语句搜索多个索引的文档（待查询索引的 mappings 和 settings 的配置必须相同），汇聚多个索引的查询结果，再次进行打分、排序、聚合并返回。 |
| [TFT.EXPLAINCOST](tairsearch.md) | TFT.EXPLAINCOST index query | 查询 query 语句的执行耗时，返回内容包括查询过程中涉及到的文档集合数及各阶段的耗时。 |
| [TFT.EXPLAINSCORE](tairsearch.md) | TFT.EXPLAINSCORE index query [doc_id] ... | 查询执行 query 语句的计分详情信息，您可以通过该命令了解文档分数的计算过程，并优化 Search 语句，提升文档的查询效果。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redi
