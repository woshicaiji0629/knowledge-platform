## 优化SQL分析语句
计算时间较长的查询分析语句具备如下特点。
使用GROUP BY语法基于字符串列进行分组统计。
使用GROUP BY语法基于多列（大于5列）进行分组统计。
在SQL分析语句中有生成字符串的操作。
您可以通过如下方法优化分析语句。
尽量避免生成字符串的操作。
例如使用date_format函数生成格式化的时间戳，导致查询效率低。针对时间戳的计算，建议使用date_trunc或者time_series函数进行计算。示例如下：
* | select date_format(from_unixtime(__time__) , '%H_%i') as t, count(1) group by t
尽量避免对字符串列进行分组统计。
使用GROUP BY语法基于字符串列进行分组统计，会导致大量的Hash计算，这部分计算量占据整体计算量的50%以上。示例如下：
查询和分析语句（速度快）
* | select count(1) as pv , from_unixtime(__time__-__time__%3600) as time group by __time__-__time__%3600
查询和分析语句（速度慢）
* | select count(1) as pv , date_trunc('hour',__time__) as time group by time
上述两条查询分析语句都是计算每小时的日志条数。第二条语句先把时间戳转化成字符串格式（例如2021-12-12 00:00:00），然后对这个字符串列进行分组统计。第一条语句对时间整点值进行计算，并且通过分组统计后再将时间戳转化为字符串格式。
基于多列进行分组统计时，把字典大的字段放在前面。
例如字段的值有13个，uid字段的值有1亿个，则建议在GROUP BY子句中将uid字段放在前面。示例如下：
查询和分析语句（速度快）
* | select province,uid,count(1) group by uid,province
查询和分析语句（速度慢）
* | select province,uid,count(1) group by province,uid
使用估算函数。
估算函数的性能比精算函数的好。估算会损失一定的精确度，用于达到快速计算的效果。示例如下：
查询和分析语句（速度快）
* |select approx_distinct(ip)
查询和分析语句（速度慢）
* | select count(distinct(ip))
低基数场景，使用多个distinct聚合函数。
多个distinct需要拷贝复制多次原始数据网络开销大，可以开启session开关enable_opt_distinct_aggs。示例如下：
查询和分析语句（速度快）
* | select cou
