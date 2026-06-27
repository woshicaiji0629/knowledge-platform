## Query exceeded max memory size of 3GB
报错原因
当前查询和分析语句所使用的服务端内存超过3 GB。该问题通常是因为使用GROUP BY子句去重后，值太多导致的。
解决方法
优化GROUP BY子句，减少GROUP BY子句中字段的个数。
