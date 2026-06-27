### 示例1
日志内容中有request_time字段，执行字段查询语句request_time>100。
只建立全文索引，返回同时包含request_time、>（非分词符）、100这三个词的日志。
只建立double、long类型的字段索引，返回结果是request_time大于100的日志。
建立全文索引和double、long类型的字段索引，request_time的全文索引失效，返回结果是request_time大于100的日志。
