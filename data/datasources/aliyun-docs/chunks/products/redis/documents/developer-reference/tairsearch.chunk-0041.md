## TFT.EXPLAINCOST

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.EXPLAINCOST index query |
| 命令描述 | 查询 query 语句的执行耗时，返回内容包括查询过程中涉及到的文档集合数及各阶段的耗时。 |
| 选项 | index ：待查询的索引名称。 query ：查询语句，语法与 TFT.SEARCH 相同。 |
| 返回值 | 执行成功：返回查询耗时信息，JSON 格式，整体耗时由如下三部分组成。 QUERY_COST ：query 查询耗时，单位为微秒（time_cost_us）。同时还包含查询视图信息（query）和 query 对应的文档集合数（doc_num）。若涉及 bool 查询方法会展示 bool 查询过程的步骤耗时（steps）。 AGGS_COST ：查询过程中聚合（Aggregations）的耗时，单位为微秒（time_cost_us），若查询语句中没有指定聚合查询，则无该耗时。 COLLECTOR_COST ：查询结果采集、排序的耗时，单位为微秒（time_cost_us），同时还包含排序类型（collector_type），返回值为 sort 排序（ScoreCollector）和分数排序（CustomSortCollector）。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.EXPLAINCOST idx:product '{"sort":[{"price":{"order":"desc"}}]}' 返回示例： { "QUERY_COST": { "query": "MATCHALL_QUERY", "doc_num": 1, "time_cost_us": 2 }, "COLLECTOR_COST": { "collector_type": "CustomSortCollector", "time_cost_us": 20 } } |
