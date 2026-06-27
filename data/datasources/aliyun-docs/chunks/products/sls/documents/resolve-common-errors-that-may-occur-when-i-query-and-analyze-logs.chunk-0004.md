## duplicate column conflicts[​](https://sls.aliyun.com/doc/sqlerror/duplicate_column_conflicts.html#duplicate-column-conflicts)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
您当前查询的LogStore中索引字段别名发生冲突，SQL无法确定您想要分析的具体列。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
该LogStore中某列名与某列的别名完全一样。
解决办法
检查您需要查询的目标LogStore的索引列字段，确保命名没有冲突。
