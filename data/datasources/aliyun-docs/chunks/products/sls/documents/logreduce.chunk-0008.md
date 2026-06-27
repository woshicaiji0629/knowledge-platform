## SQL示例
日志服务还支持通过执行查询分析语句获取日志聚类结果。
获取日志聚类结果
查询分析语句
* | select a.pattern, a.count,a.signature, a.origin_signatures from (select log_reduce(3) as a from log) limit 1000
说明
查看聚类结果时，您可以单击复制查询语句获取日志聚类结果所对应的查询分析语句。
修改参数
修改查询分析语句中的log_reduce(precision)，precision代表聚类精度，取值范围1~16，数字越小，聚类精度越高，生成的模式格式越多，默认为3。
返回字段
在统计图表页签中返回日志聚类详细信息。

| 参数 | 说明 |
| --- | --- |
| pattern | 某类日志的具体模式。 |
| count | 当前指定的查询时间段内，某模式对应的日志条数。 |
| signature | 某模式的签名。 |
| origin_signatures | 某模式的二级签名，可以通过二级签名，反查原始数据。 |

对比不同时间段日志聚类结果
查询分析语句
* | select v.pattern, v.signature, v.count, v.count_compare, v.diff from (select compare_log_reduce(3, 86400) as v from log) order by v.diff desc limit 1000
说明
Log Compare对比不同时间段日志聚类结果后，您可以单击复制查询语句获取对应的查询分析语句。
修改参数
修改查询分析语句中的compare_log_reduce(precision, compare_interval)。
precision代表聚类精度，取值范围1~16，数字越小，聚类精度越高，生成的模式格式越多，默认为3。
compare_interval表示对比N秒之前某一时间段的日志，正整数。
返回字段

| 参数 | 说明 |
| --- | --- |
| pattern | 某类日志的具体模式。 |
| count_compare | 在前一时间段内，某模式对应的日志数量。 |
| count | 当前指定的查询时间段内，某模式对应的日志条数。 |
| diff | count 和 count_compare 的差值。 |
| signature | 某模式的签名。 |
