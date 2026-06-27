## LogStore without index config[​](https://sls.aliyun.com/doc/sqlerror/logstore_without_index.html#logstore-without-index-config)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
您当前正在使用SQL语法，而LogStore并没有配置索引，使用SQL必须至少配置任一索引。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
您当前查询的目标LogStore没有配置索引。
解决方法
检查您需要查询的目标LogStore，并确定已开启索引配置（至少一列）。
