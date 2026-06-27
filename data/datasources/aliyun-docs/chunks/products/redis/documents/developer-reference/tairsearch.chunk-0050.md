buckets 为数组 key，数组中的 value 为对应 key 和 doc_count 统计结果。示例如下： { "aggregations": { "Per_Investor_Freq": { "buckets": [ { "doc_count": 2, "key": "Jay" }, { "doc_count": 1, "key": "Mila" } ] } } } |
| Filter Aggregation | filter 中可输入 query 语句，对 query 查询结果进行再次过滤，支持嵌套子聚合。 返回结果：符合过滤条件的文档个数（ doc_count ）。 |
