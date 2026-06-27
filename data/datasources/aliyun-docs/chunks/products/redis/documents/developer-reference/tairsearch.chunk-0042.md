## TFT.EXPLAINSCORE

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.EXPLAINSCORE index query [doc_id] ... |
| 命令描述 | 查询执行 query 语句的计分详情信息，您可以通过该命令了解文档分数的计算过程，并优化 Search 语句，提升文档的查询效果。 该命令当前仅内存型（兼容 Redis 6.0）支持。 |
| 选项 | index ：待查询的索引名称。 query ：查询语句，语法与 TFT.SEARCH 相同。 doc_id ：指定文档 ID，若指定了该参数，返回结果只会包含 doc_id 对应的文档。 |
| 返回值 | 执行成功：返回查询到的文档信息，在 TFT.SERACH 返回结果的基础上增加每个文档的计分详情信息（ _explanation ）， _explanation 中存在如下字段。 score ：该文档的得分。 description ：score 计算使用的公式。 field ：该文档被 query 中指定的 field 所命中。 term ：该文档被 query 中指定的词项所命中。 query_boost ：该文档在本次查询中的计分权重。 details ：文档的元数据与计分过程。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.EXPLAINSCORE today_shares '{"query":{"wildcard":{"shares_name":{"value":"*BY"}}}}' 返回示例： { "hits": { "hits": [ { "_id": "17036492095306830", "_index": "today_shares", "_score": 1.0, "_source": { "shares_name": "YBY", "logictime": 14300410, "purchase_type": 1, "purchase_price": 11.1, "purchase_count": 100, "investor": "Mila" }, "_explanation": { "score": 1.0, "description": "score, computed as query_boost", "field": "shares_name", "term": "*BY", "query_boost": 1.0 } } ], "max_score": 1.0, "total": { "relation": "eq", "value": 1 } } } |
